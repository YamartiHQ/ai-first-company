# AI-First Company

AI-First Company is a vendor-neutral organizational model for organizations in which humans and AI systems operate within one coherent organizational system.

It addresses a problem that tools alone cannot solve: how knowledge, responsibility, authority, execution, and learning can remain coherent when both human and AI contributors participate in the organization.

The project is about organizational design, not a product or software stack. Models, agents, tools, providers, and runtimes are replaceable implementation choices within the boundaries of the organization.

In this repository, the **Foundation** means the complete vendor-neutral body of work formed by the Architecture, Reference Design, and Technical Requirements. It is the basis from which application guidance, examples, and implementations may be derived, not an additional architectural layer or a reference to an earlier project name.

## Reading path

Start with the conceptual introduction, then follow the three substantive layers:

1. [The Core Idea](00-introduction/THE-CORE-IDEA.md)
2. [Architecture](01-architecture/ARCHITECTURE.md)
3. [Reference Design](02-reference-design/REFERENCE_DESIGN.md)
4. [Technical Requirements](03-technical-requirements/TECHNICAL_REQUIREMENTS.md)

The Architecture explains what an AI-First Company is.

The Reference Design translates the Architecture into an organizational design.

The Technical Requirements define the technology required to realize that design.

Repository governance and document authority are defined in [PROJECT.md](PROJECT.md).

## Author and contact

The AI-First Company Foundation was created and is maintained by **Andreas Nöthen**.

For public questions, corrections, and proposed improvements, use the [GitHub Issues](https://github.com/YamartiHQ/ai-first-company/issues) page. For private or security-sensitive communication, email [contact@yamarti.com](mailto:contact@yamarti.com) rather than opening a public issue.

## Context and positioning

[Origin, Related Work, and Contribution](00-introduction/ORIGIN_AND_RELATED_WORK.md) explains why the Foundation was developed, how it relates to established fields of work, what contribution it intends to make, and how human–AI collaboration supported its development. It is optional context rather than part of the authoritative three-layer model.

## Use the Foundation with an LLM

[Using the Foundation with an LLM](00-introduction/USING_THE_FOUNDATION_WITH_AN_LLM.md) provides a short conversational Start Prompt, a transparent full prompt, a later-session Resume Prompt, repository-grounding checks, and practical starting paths for new and existing organizations.

The Foundation remains the stable knowledge and requirements basis. The LLM acts as a replaceable interpretation, interaction, and current-research layer. It can help a founder apply the model, ask for missing company context, evaluate a proposed design, or research current technology choices against the Technical Requirements without making one model authoritative.

To begin:

1. If the LLM can access public GitHub repositories, copy the [Short Start Prompt](00-introduction/USING_THE_FOUNDATION_WITH_AN_LLM.md#short-start-prompt) and optionally add the first question.
2. If it cannot access the repository, upload the [LLM usage document](00-introduction/USING_THE_FOUNDATION_WITH_AN_LLM.md) together with [`PROJECT.md`](PROJECT.md), [`ARCHITECTURE.md`](01-architecture/ARCHITECTURE.md), [`REFERENCE_DESIGN.md`](02-reference-design/REFERENCE_DESIGN.md), and [`TECHNICAL_REQUIREMENTS.md`](03-technical-requirements/TECHNICAL_REQUIREMENTS.md), then instruct it to follow the **Copyable Foundation Prompt** contained in the usage document.
3. In a repository-aware local workspace, open this repository and instruct the LLM to follow `00-introduction/USING_THE_FOUNDATION_WITH_AN_LLM.md`.
4. Continue the conversation normally. The LLM should preserve the established scope and guide the next relevant step.

## Architecture companions

The authoritative Architecture is supported by derived artifacts for different forms of use:

- [Architecture Knowledge Graph](01-architecture/ARCHITECTURE_KNOWLEDGE_GRAPH.md) — a semantic representation of concepts and relationships;
- [Architecture Glossary](01-architecture/ARCHITECTURE_GLOSSARY.md) — a terminology reference; and
- [Architecture Validation](01-architecture/ARCHITECTURE_VALIDATION.md) — the framework for validating Architecture meaning and traceability.

## Planned application work

Foundation v1 defines the framework itself. The following application artifacts are planned as subsequent work rather than requirements for Foundation v1:

- **Solo Founder Minimal Realization** — demonstrate and validate the smallest coherent realization for one founder or one primary accountable individual;
- **Day-One Reference Configuration** — a concrete initial organizational and technical configuration;
- **Existing Organization Transition Blueprint** — a governed path for establishing the target organization alongside existing structures;
- **Capability-by-Capability Adoption Path** — progressive validation, adoption, cutover, and retirement of existing capability implementations;
- **Reference Company** — one end-to-end company example that makes the framework concrete;
- **Reference Implementation** — a future programmed realization derived from the Reference Design and Technical Requirements.

The next phase applies the Foundation to the real solo-founder company whose intended creation initiated this project. That work is expected to produce operational Evidence for the planned Solo Founder Minimal Realization, Day-One Reference Configuration, and Reference Company. The current repository-grounded prompt is the provided LLM interaction method; any later packaging decision would be a separate implementation choice supported by operational Evidence rather than a missing part of Foundation v1.

Company formation procedures such as legal-form selection, naming rights, registration, taxation, banking, or notarization are not part of these artifacts unless a separate product or jurisdiction-specific guide defines them.

## Repository structure

```text
ai-first-company/
├── .gitignore
├── LICENSE
├── README.md
├── PROJECT.md
├── 00-introduction/
│   ├── THE-CORE-IDEA.md
│   ├── ORIGIN_AND_RELATED_WORK.md
│   └── USING_THE_FOUNDATION_WITH_AN_LLM.md
├── 01-architecture/
│   ├── ARCHITECTURE.md
│   ├── ARCHITECTURE_KNOWLEDGE_GRAPH.md
│   ├── ARCHITECTURE_GLOSSARY.md
│   ├── ARCHITECTURE_VALIDATION.md
│   └── diagrams/                # Architecture diagram SVG sources and PNG renders
├── 02-reference-design/
│   ├── REFERENCE_DESIGN.md
│   └── diagrams/                # Reference Design diagram SVG sources and PNG renders
└── 03-technical-requirements/
    └── TECHNICAL_REQUIREMENTS.md
```

## License

This project is licensed under the
[Creative Commons Attribution 4.0 International License](LICENSE).
