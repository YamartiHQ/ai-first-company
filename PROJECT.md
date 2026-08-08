# AI-First Company Project

## Purpose

This repository defines a vendor-neutral organizational model for organizations in which humans and AI systems operate within one coherent organizational system.

It connects a conceptual Architecture to one Reference Design and to the Technical Requirements needed to realize that design.

The repository concerns organizational design and its required technical capabilities. It does not prescribe particular products, vendors, models, runtimes, programming languages, or infrastructure.

This document governs repository purpose, document roles, authority, and evolution. It does not redefine the organizational meaning established by the Architecture.

## Document authority

Authority follows document role, not file order, level of detail, or implementation convenience.

| Document or artifact | Role and authority |
|---|---|
| `PROJECT.md` | Governs repository purpose, document roles, authority, and evolution. |
| [`01-architecture/ARCHITECTURE.md`](01-architecture/ARCHITECTURE.md) | Authoritative source for the organizational Architecture: its concepts, responsibilities, boundaries, and relationships. |
| [`01-architecture/ARCHITECTURE_KNOWLEDGE_GRAPH.md`](01-architecture/ARCHITECTURE_KNOWLEDGE_GRAPH.md) | Derived semantic representation of the Architecture. It must remain traceable to and consistent with the authoritative Architecture. |
| [`01-architecture/ARCHITECTURE_GLOSSARY.md`](01-architecture/ARCHITECTURE_GLOSSARY.md) | Derived terminology representation of the Architecture. It clarifies defined terms but does not create architectural meaning. |
| [`01-architecture/ARCHITECTURE_VALIDATION.md`](01-architecture/ARCHITECTURE_VALIDATION.md) | Derived validation framework for the Architecture. It defines validation types, scenario structure, result classifications, quality requirements, and traceability without extending Architecture meaning. |
| [`02-reference-design/REFERENCE_DESIGN.md`](02-reference-design/REFERENCE_DESIGN.md) | One coherent organizational design derived from the Architecture. It is authoritative for this Reference Design, but not for the Architecture itself. |
| `02-reference-design/diagrams/` | Non-authoritative visual representations derived from the Reference Design. A diagram cannot override its source text. |
| [`03-technical-requirements/TECHNICAL_REQUIREMENTS.md`](03-technical-requirements/TECHNICAL_REQUIREMENTS.md) | Technical requirements derived from the Reference Design. It is authoritative for the required technical capabilities, but cannot silently add organizational responsibilities. |
| [`README.md`](README.md), [`00-introduction/THE-CORE-IDEA.md`](00-introduction/THE-CORE-IDEA.md), [`00-introduction/ORIGIN_AND_RELATED_WORK.md`](00-introduction/ORIGIN_AND_RELATED_WORK.md), and [`00-introduction/USING_THE_FOUNDATION_WITH_AN_LLM.md`](00-introduction/USING_THE_FOUNDATION_WITH_AN_LLM.md) | Explanatory entry, context, and application documents. Where they summarize or apply authoritative material, the corresponding authoritative document prevails. |
| `01-architecture/diagrams/` | Non-authoritative visual derived representations. A diagram cannot override its source text. |

If documents conflict, resolve the conflict according to these roles:

- repository governance follows `PROJECT.md`;
- organizational meaning follows the Architecture;
- Reference Design responsibilities must remain consistent with and traceable to the Architecture;
- Technical Requirements must remain derived from the Reference Design; and
- explanatory, application, and visual material must be corrected to follow the source it represents.

## Layer relationship

The substantive model has three layers:

```text
Architecture
      ↓
Reference Design
      ↓
Technical Requirements
```

The Architecture explains what an AI-First Company is.

The Reference Design translates the Architecture into an organizational design.

The Technical Requirements define the technology required to realize that design.

Each layer answers a different question and must stay within its boundary. Greater detail in a downstream layer does not give that layer authority over an upstream one.

## Change routing

Route a proposed change to the document whose responsibility changes:

- A new or changed organizational concept, responsibility, boundary, or relationship belongs first in the Architecture.
- A different composition of existing architectural responsibilities belongs in the Reference Design.
- A requirement on the technical realization of a Reference responsibility belongs in the Technical Requirements.
- A new technology, product, model, or implementation pattern does not automatically change the Architecture or Reference Design.
- Explanatory material, orientation, application guidance and prompts, and visualizations follow their authoritative sources and must not redefine them.

When a proposal appears to span layers, identify the upstream meaning first. Downstream consequences are synchronized only after that meaning is accepted in its authoritative layer.

## Traceability and completeness

Every Reference responsibility must remain traceable to the Architecture. A responsibility that cannot be explained through the Architecture is not added silently. It is reviewed as a misplaced technical concern, an unnecessary responsibility, or a possible architectural gap.

The relationship between the Reference Design and Technical Requirements is bidirectional for coverage:

> Every technically relevant Reference responsibility must be covered by at least one Technical Requirement.

> Every Technical Requirement must exist because at least one Reference responsibility requires it.

This no-orphan rule prevents both unidentified technical dependencies and technology-driven requirements without an organizational reason.

Traceability records composition and derivation. It does not make a downstream artifact authoritative over its source.

## Synchronization rules

When Architecture meaning changes, inspect every affected derived representation and synchronize it where necessary:

- `01-architecture/ARCHITECTURE_KNOWLEDGE_GRAPH.md` for concepts, relationships, boundaries, and source links;
- `01-architecture/ARCHITECTURE_GLOSSARY.md` for terminology and definitions;
- `01-architecture/ARCHITECTURE_VALIDATION.md` for validation types, scenario structure, result classifications, quality requirements, and traceability; and
- `01-architecture/diagrams/` for labels, elements, relationships, and captions.

Also inspect downstream consequences in the Reference Design and Technical Requirements. A change to the Architecture does not imply that every downstream document must change, but every affected dependency must be reviewed.

When the Reference Design changes, inspect its Architecture traceability, synchronize `02-reference-design/diagrams/`, and synchronize affected Technical Requirements. When Technical Requirements change, verify that their Reference basis and coverage remain explicit.

When authoritative content changes, review `README.md`, `00-introduction/THE-CORE-IDEA.md`, `00-introduction/ORIGIN_AND_RELATED_WORK.md`, and `00-introduction/USING_THE_FOUNDATION_WITH_AN_LLM.md` for stale explanations or application guidance. Derived, explanatory, and application artifacts must never become a competing source of organizational meaning.

## Change process

For a material change:

1. Identify the layer that owns the changed meaning.
2. Update and review the authoritative document for that layer.
3. Verify its upstream traceability, where applicable.
4. Inspect and synchronize affected derived, downstream, explanatory, and visual artifacts.
5. Validate links, terminology, layer boundaries, and end-to-end coverage.

The repository may evolve when evidence reveals a genuine gap or changed organizational need. Available technology alone is not sufficient reason to expand the organizational model.
