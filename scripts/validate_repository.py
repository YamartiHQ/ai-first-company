#!/usr/bin/env python3
"""Validate repository structure, links, semantic catalogs, traceability, prompts, and diagram pairs."""

from __future__ import annotations

import html
import re
import sys
import textwrap
import urllib.parse
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def section(text: str, start: str, end: str | None = None) -> str:
    try:
        result = text.split(start, 1)[1]
    except IndexError:
        fail(f"Missing section marker: {start}")
        return ""
    if end:
        result = result.split(end, 1)[0]
    return result


def markdown_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def fenced_text_containing(text: str, needle: str) -> str | None:
    for block in re.findall(r"```text\n(.*?)\n\s*```", text, re.S):
        normalized = textwrap.dedent(block).strip()
        if needle in normalized:
            return normalized
    return None


def github_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: Counter[str] = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        explicit = re.search(r'<a\s+(?:name|id)=["\']([^"\']+)', line, re.I)
        if explicit:
            anchors.add(explicit.group(1))
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = match.group(1)
        heading = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", heading)
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = html.unescape(heading).replace("`", "").lower()
        slug = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE).replace(" ", "-")
        occurrence = counts[slug]
        counts[slug] += 1
        anchors.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return anchors


def validate_markdown() -> None:
    markdown_files = sorted(ROOT.rglob("*.md"))
    anchor_cache = {path: github_anchors(path) for path in markdown_files}
    link_pattern = re.compile(r"!?\[[^]]*]\(([^)]+)\)")
    image_pattern = re.compile(r"<img\b([^>]*)>", re.I | re.S)
    attribute_pattern = re.compile(r"([:\w-]+)\s*=\s*([\"'])(.*?)\2", re.S)
    local_html_images = 0

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        fences = [line for line in text.splitlines() if re.match(r"^\s*(```|~~~)", line)]
        if len(fences) % 2:
            fail(f"Unbalanced Markdown fence: {path.relative_to(ROOT)}")

        for link_match in link_pattern.finditer(text):
            raw_target = link_match.group(1)
            target = raw_target.strip().strip("<>")
            if not target or re.match(r"^(?:https?://|mailto:|chatgpt-conversation:)", target):
                continue
            target = target.split()[0]
            file_part, separator, anchor = target.partition("#")
            decoded = urllib.parse.unquote(file_part)
            resolved = (path.parent / decoded).resolve() if decoded else path.resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"Link escapes repository: {path.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                fail(f"Missing local target: {path.relative_to(ROOT)} -> {target}")
                continue
            if link_match.group(0).startswith("!") and resolved.suffix.lower() == ".png":
                fail(f"Local PNG must use an HTML img element with intrinsic dimensions: {path.relative_to(ROOT)} -> {target}")
            if separator and anchor and resolved.suffix.lower() == ".md":
                if resolved not in anchor_cache:
                    anchor_cache[resolved] = github_anchors(resolved)
                decoded_anchor = urllib.parse.unquote(anchor)
                if decoded_anchor not in anchor_cache[resolved]:
                    fail(f"Missing anchor: {path.relative_to(ROOT)} -> {target}")

        for image_match in image_pattern.finditer(text):
            attributes = {
                name.lower(): value.strip()
                for name, _quote, value in attribute_pattern.findall(image_match.group(1))
            }
            source = attributes.get("src", "")
            if not source:
                fail(f"HTML image without src: {path.relative_to(ROOT)}")
                continue
            if re.match(r"^(?:https?://|data:)", source):
                continue

            decoded = urllib.parse.unquote(source.split("#", 1)[0].split("?", 1)[0])
            resolved = (path.parent / decoded).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"HTML image escapes repository: {path.relative_to(ROOT)} -> {source}")
                continue
            if not resolved.exists():
                fail(f"Missing local HTML image: {path.relative_to(ROOT)} -> {source}")
                continue

            local_html_images += 1
            if not attributes.get("alt", "").strip():
                fail(f"Local HTML image without alt text: {path.relative_to(ROOT)} -> {source}")

            width = attributes.get("width", "")
            height = attributes.get("height", "")
            if not width.isdigit() or int(width) <= 0 or not height.isdigit() or int(height) <= 0:
                fail(f"Local HTML image requires positive numeric width and height: {path.relative_to(ROOT)} -> {source}")
                continue

            if resolved.suffix.lower() == ".png":
                header = resolved.read_bytes()[:24]
                if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
                    fail(f"Invalid PNG header: {resolved.relative_to(ROOT)}")
                    continue
                actual_width = int.from_bytes(header[16:20], "big")
                actual_height = int.from_bytes(header[20:24], "big")
                if (int(width), int(height)) != (actual_width, actual_height):
                    fail(
                        f"HTML image dimensions differ from PNG: {path.relative_to(ROOT)} -> {source} "
                        f"({width}x{height} declared, {actual_width}x{actual_height} actual)"
                    )

    if local_html_images != 19:
        fail(f"Local HTML content images: expected 19, found {local_html_images}")


def validate_model_counts() -> None:
    glossary = (ROOT / "01-architecture/ARCHITECTURE_GLOSSARY.md").read_text(encoding="utf-8")
    graph = (ROOT / "01-architecture/ARCHITECTURE_KNOWLEDGE_GRAPH.md").read_text(encoding="utf-8")
    reference = (ROOT / "02-reference-design/REFERENCE_DESIGN.md").read_text(encoding="utf-8")
    requirements = (ROOT / "03-technical-requirements/TECHNICAL_REQUIREMENTS.md").read_text(encoding="utf-8")

    glossary_part = section(glossary, "## Part 1", "## Part 2")
    glossary_entries = re.findall(r"^####\s+(.+)$", glossary_part, re.M)
    if len(glossary_entries) != 82 or len(set(glossary_entries)) != 82:
        fail(f"Glossary entries: expected 82 unique, found {len(glossary_entries)} / {len(set(glossary_entries))} unique")

    concept_catalog = section(graph, "## Concept Catalog", "## Relationship Vocabulary")
    catalog_concepts = re.findall(r"^\| ([^|]+?) \|.*?\[Source]", concept_catalog, re.M)
    if len(catalog_concepts) != 82 or len(set(catalog_concepts)) != 82:
        fail(f"Knowledge Graph concepts: expected 82 unique, found {len(catalog_concepts)} / {len(set(catalog_concepts))} unique")
    if set(glossary_entries) != set(catalog_concepts):
        fail("Glossary and Knowledge Graph concept sets differ")

    vocabulary = section(graph, "## Relationship Vocabulary", "## Relationship Catalog")
    relation_types = []
    for line in vocabulary.splitlines():
        match = re.match(r"^\| ([^|]+?) \|", line)
        if match and match.group(1) not in {"Relationship", "---"}:
            relation_types.append(match.group(1))
    if len(relation_types) != 42 or len(set(relation_types)) != 42:
        fail(f"Relationship types: expected 42 unique, found {len(relation_types)} / {len(set(relation_types))} unique")

    relationship_catalog = section(graph, "## Relationship Catalog", "## Validated Attributes")
    catalog_rows = re.findall(
        r"^\| (R\d{3}) \| (.+?) `([^`]+)` (.+?) \| (Explicit|Derived) \|.*?\[Source\]\(([^)]+)\) \|$",
        relationship_catalog,
        re.M,
    )
    catalog_ids = [item[0] for item in catalog_rows]
    statuses = Counter(item[4] for item in catalog_rows)
    if len(catalog_ids) != 135 or len(set(catalog_ids)) != 135:
        fail(f"Relationship catalog IDs: expected 135 unique, found {len(catalog_ids)} / {len(set(catalog_ids))} unique")
    if statuses != Counter({"Explicit": 130, "Derived": 5}):
        fail(f"Relationship status counts differ: {dict(statuses)}")

    yaml = section(graph, "```yaml", "```")
    concept_yaml, relationship_yaml = yaml.split("  relationships:", 1)
    yaml_concepts = re.findall(
        r'^\s+- \{ id: ([a-z0-9_]+), label: "([^"]+)", trace: "([^"]+)" \}$',
        concept_yaml,
        re.M,
    )
    yaml_concept_ids = [item[0] for item in yaml_concepts]
    yaml_labels = [item[1] for item in yaml_concepts]
    yaml_relationships = re.findall(
        r'^\s+- \{ id: (R\d{3}), source: ([a-z0-9_]+), relation: "([^"]+)", target: ([a-z0-9_]+), status: (explicit|derived), trace: "([^"]+)" \}$',
        relationship_yaml,
        re.M,
    )
    yaml_relationship_ids = [item[0] for item in yaml_relationships]
    yaml_statuses = Counter(item[4] for item in yaml_relationships)
    if len(yaml_concept_ids) != 82 or len(set(yaml_concept_ids)) != 82:
        fail(f"YAML concepts: expected 82 unique, found {len(yaml_concept_ids)} / {len(set(yaml_concept_ids))} unique")
    if set(yaml_labels) != set(catalog_concepts):
        fail("Knowledge Graph Markdown and YAML concept labels differ")
    if yaml_relationship_ids != catalog_ids:
        fail("Knowledge Graph Markdown and YAML relationship ID sequences differ")
    if yaml_statuses != Counter({"explicit": 130, "derived": 5}):
        fail(f"YAML relationship status counts differ: {dict(yaml_statuses)}")

    concept_label_by_id = {identifier: label for identifier, label, _ in yaml_concepts}
    unresolved_endpoints = sorted({
        endpoint
        for _, source, _, target, _, _ in yaml_relationships
        for endpoint in (source, target)
        if endpoint not in concept_label_by_id
    })
    if unresolved_endpoints:
        fail(f"Knowledge Graph relationships use unknown endpoints: {', '.join(unresolved_endpoints)}")

    markdown_edges = {
        identifier: (source, relation, target, status.lower(), trace)
        for identifier, source, relation, target, status, trace in catalog_rows
    }
    yaml_edges = {
        identifier: (
            concept_label_by_id.get(source, source), relation,
            concept_label_by_id.get(target, target), status, trace,
        )
        for identifier, source, relation, target, status, trace in yaml_relationships
    }
    if markdown_edges != yaml_edges:
        differing = sorted(set(markdown_edges) | set(yaml_edges), key=lambda item: int(item[1:]))
        differing = [identifier for identifier in differing if markdown_edges.get(identifier) != yaml_edges.get(identifier)]
        fail(f"Knowledge Graph Markdown/YAML relationship details differ: {', '.join(differing)}")

    architecture_path = ROOT / "01-architecture/ARCHITECTURE.md"
    architecture_anchors = github_anchors(architecture_path)
    yaml_traces = [trace for _, _, trace in yaml_concepts]
    yaml_traces.extend(trace for _, _, _, _, _, trace in yaml_relationships)
    invalid_traces = sorted({trace for trace in yaml_traces if not trace.startswith("ARCHITECTURE.md#") or trace.split("#", 1)[1] not in architecture_anchors})
    if invalid_traces:
        fail(f"Knowledge Graph YAML traces do not resolve: {', '.join(invalid_traces)}")

    composition_block = section(reference, "The Reference Design contains ten top-level Compositions:", "## 6. The Operational Organization")
    compositions = [
        "Executive Agent", "Execution Graph Layer", "Company Brain", "Organizational Learning",
        "Capability Agent", "Organizational Control Plane", "Company Interface Layer",
        "Sandbox Organization", "Production Organization", "Evaluation & Assurance",
    ]
    for composition in compositions:
        if composition_block.count(composition) != 1:
            fail(f"Reference Composition inventory must contain {composition!r} exactly once")

    inventory = section(requirements, "The Reference Design requires the following 25 technical component types.", "The two additional v2 Compositions")
    component_types = re.findall(r"^- (.+)$", inventory, re.M)
    if len(component_types) != 25 or len(set(component_types)) != 25:
        fail(f"Technical component types: expected 25 unique, found {len(component_types)} / {len(set(component_types))} unique")

    tr_ids = re.findall(r"^\| \*\*(TR-[A-Z0-9]+)\*\* \|", requirements, re.M)
    tr_anchors = re.findall(r'<a name="(tr-[a-z0-9]+)"></a>', requirements)
    xtr_ids = re.findall(r"^\*\*Requirement ID:\*\* (XTR-[A-Z0-9]+)$", requirements, re.M)
    if len(tr_ids) != 25 or len(set(tr_ids)) != 25:
        fail(f"TR IDs: expected 25 unique, found {len(tr_ids)} / {len(set(tr_ids))} unique")
    expected_tr_anchors = {identifier.lower() for identifier in tr_ids}
    if len(tr_anchors) != 25 or set(tr_anchors) != expected_tr_anchors:
        fail("Every stable TR ID must have one matching custom Markdown anchor")
    if len(xtr_ids) != 21 or len(set(xtr_ids)) != 21:
        fail(f"XTR IDs: expected 21 unique, found {len(xtr_ids)} / {len(set(xtr_ids))} unique")
    tr_suffixes = {identifier.removeprefix("TR-") for identifier in tr_ids}
    xtr_suffixes = {identifier.removeprefix("XTR-") for identifier in xtr_ids}
    collisions = sorted(tr_suffixes & xtr_suffixes)
    if collisions:
        fail(f"TR/XTR suffix collisions: {', '.join(collisions)}")

    matrix = section(requirements, "## 5. Reference Composition × Technology Matrix", "## 6. Implementation Map")
    matrix_components: set[str] = set()
    matrix_pairs: set[tuple[str, str]] = set()
    headers: list[str] = []
    for line in matrix.splitlines():
        cells = markdown_cells(line) if line.startswith("|") else []
        if cells and cells[0] == "Reference Composition":
            headers = cells[1:]
            matrix_components.update(headers)
        elif headers and cells and cells[0].startswith("**") and not cells[0].startswith("**---"):
            composition = cells[0].strip("*")
            for technology, value in zip(headers, cells[1:]):
                if value:
                    matrix_pairs.add((composition, technology))
    if matrix_components != set(component_types):
        fail("Technical component inventory and Matrix columns differ")

    tr_rows = re.findall(
        r'^\| \*\*(TR-[A-Z0-9]+)\*\* \| (?:<a name="tr-[a-z0-9]+"></a>)?\*\*(.+?)\*\* \|',
        requirements,
        re.M,
    )
    tr_technology_by_id = dict(tr_rows)
    if set(tr_technology_by_id.values()) != set(component_types):
        fail("Technical component inventory and TR technology names differ")

    implementation = section(requirements, "## 6. Implementation Map", "## 7. Technology Requirements")
    implementation_pairs: set[tuple[str, str]] = set()
    current_composition: str | None = None
    for line in implementation.splitlines():
        heading = re.match(r"^### 6\.\d+ (.+)$", line)
        if heading:
            current_composition = heading.group(1)
            continue
        cells = markdown_cells(line) if line.startswith("|") else []
        if current_composition and len(cells) == 3 and cells[0] not in {"Reference Basis", "---"}:
            for technology in (item.strip() for item in cells[1].split(";")):
                if technology:
                    implementation_pairs.add((current_composition, technology))
    missing_bases = sorted(matrix_pairs - implementation_pairs)
    unexpected_bases = sorted(implementation_pairs - matrix_pairs)
    if missing_bases:
        fail(f"Matrix relationships without Implementation Map basis: {missing_bases}")
    if unexpected_bases:
        fail(f"Implementation Map relationships absent from Matrix: {unexpected_bases}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    usage = (ROOT / "00-introduction/USING_AI_FIRST_COMPANY_WITH_AN_LLM.md").read_text(encoding="utf-8")
    prompt_needle = "Help me understand or apply AI-First Company:"
    readme_prompt = fenced_text_containing(readme, prompt_needle)
    usage_prompt = fenced_text_containing(usage, prompt_needle)
    if not readme_prompt or not usage_prompt:
        fail("Short Start Prompt is missing from README or LLM usage guidance")
    elif readme_prompt != usage_prompt:
        fail("README and LLM usage Short Start Prompts differ")


def validate_structure_and_diagrams() -> None:
    required = [
        "README.md", "PROJECT.md", "LICENSE", "CITATION.cff", "CONTRIBUTING.md",
        "SECURITY.md", "CODE_OF_CONDUCT.md", ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/ISSUE_TEMPLATE/config.yml",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            fail(f"Missing required repository artifact: {relative}")

    diagram_roots = [
        ROOT / "00-introduction/diagrams",
        ROOT / "01-architecture/diagrams",
        ROOT / "02-reference-design/diagrams",
        ROOT / "03-technical-requirements/diagrams",
    ]
    for diagram_root in diagram_roots:
        svg_stems = {path.stem for path in diagram_root.glob("*.svg")}
        png_stems = {path.stem for path in diagram_root.glob("*.png")}
        missing_png = svg_stems - png_stems
        if missing_png:
            fail(f"SVG files without PNG renders in {diagram_root.relative_to(ROOT)}: {sorted(missing_png)}")
        for svg in diagram_root.glob("*.svg"):
            try:
                root = ET.parse(svg).getroot()
            except ET.ParseError as exc:
                fail(f"Invalid SVG XML: {svg.relative_to(ROOT)}: {exc}")
                continue
            local_names = [element.tag.rsplit("}", 1)[-1] for element in root.iter()]
            for required_name in ("title", "desc", "metadata"):
                if local_names.count(required_name) != 1:
                    fail(f"{svg.relative_to(ROOT)} must contain exactly one <{required_name}>")


def main() -> int:
    validate_structure_and_diagrams()
    validate_markdown()
    validate_model_counts()
    if ERRORS:
        print("Repository validation failed:")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print("Repository validation passed.")
    print("Validated structure, links, semantic catalogs, technical traceability, prompt synchronization, stable IDs, and SVG/PNG pairs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
