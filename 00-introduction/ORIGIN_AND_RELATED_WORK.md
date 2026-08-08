# Origin, Related Work, and Contribution

## Document Role

This document explains why the AI-First Company Foundation was developed, how it relates to established fields of work, and what contribution this repository intends to make.

In this repository, the **Foundation** means the complete vendor-neutral body of work formed by the Architecture, Reference Design, and Technical Requirements. It is not an additional architectural layer or a reference to an earlier project name.

It is an explanatory document. It does not define or extend the Architecture. Where it summarizes a Foundation concept, the corresponding authoritative document prevails.

## Why This Project Exists

This project began with the practical intention to build an AI-first company from the ground up, initially around one founder.

The work required more than selecting AI tools or automating existing tasks. It raised organizational questions about shared knowledge, stable responsibilities, authority, controlled execution, evidence, accountability, and change. Existing work addresses many of these questions individually, but the project did not identify a single, sufficiently complete model that connected them across organizational Architecture, Reference Design, and Technical Requirements for this purpose.

The Foundation was developed to provide that connection. Its scope later expanded to include established organizations that may move toward an AI-first target architecture progressively, while preserving existing authority, accountability, and organizational truth throughout the transition.

This origin remains important to the design: the model must be coherent enough to guide a real organization, but it must not require unnecessary organizational size or a separate technical system for every architectural responsibility.

## Development Process

The Foundation emerged through iterative exploration, modeling, critique, and validation rather than through the adoption of one pre-existing framework.

The work brought together questions and practices found across organizational design, enterprise architecture, knowledge management, AI governance, identity and authorization, controlled systems, and agent-oriented computing. Concepts were repeatedly renamed, separated, combined, or rejected to preserve clear responsibilities and decision boundaries within one coherent organizational model.

The resulting Architecture was then translated into one Reference Design and into traceable Technical Requirements. This translation is part of the contribution: it tests whether organizational meaning can remain explicit as the model moves toward implementation without becoming tied to particular products or vendors.

## Relationship to Existing Work

The Foundation exists within an established and rapidly evolving field. The areas below provide relevant context and contain concepts, practices, or concerns that overlap with parts of the model.

These relationships do not imply that every Foundation concept was derived from a particular source. Some sources informed the wider problem space, while other similarities represent established practice or independent convergence. This document does not attempt to reconstruct a source-level provenance history for every design decision.

### Enterprise Architecture and Capability Modeling

Enterprise-architecture practices provide established ways to separate organizational capabilities from particular processes, structures, applications, and technologies. Capability-based planning and layered architectural descriptions are therefore important context for the Foundation's distinction between a Company Capability and its replaceable implementations.

Relevant established bodies of work include [the TOGAF Standard and its Series Guides](https://www.opengroup.org/togaf/series-guides) and [the ArchiMate modeling language](https://www.opengroup.org/archimate-forum/archimate-overview). The Foundation does not adopt their complete methods or metamodels. It applies its own focused ontology to the organization of human and AI contribution, authority, knowledge, execution, evidence, and evolution.

### Knowledge Management and Provenance

Knowledge-management disciplines address how organizations create, maintain, share, review, and improve organizational knowledge. Provenance standards address how the origin, derivation, attribution, and transformation of information can remain represented across systems and contexts.

[ISO 30401](https://www.iso.org/standard/68683.html) provides requirements for organizational knowledge-management systems, while the [W3C PROV family of specifications](https://www.w3.org/TR/prov-overview/) provides interoperable models for provenance. These are relevant to the Foundation's treatment of Company Artifacts, Company Memory, Evidence, and traceability. The Foundation's knowledge lifecycle and organizational boundaries remain its own architectural composition rather than an implementation of either standard.

### AI Governance and Risk Management

AI-governance and risk-management frameworks establish important expectations for accountability, transparency, traceability, evaluation, risk treatment, and lifecycle governance.

Relevant examples include the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), [ISO/IEC 42001](https://www.iso.org/standard/42001), and the [OECD AI Principles](https://oecd.ai/en/ai-principles). The Foundation shares many of these concerns but serves a different purpose. It defines a broader organizational architecture for coordinated human and AI operation and does not replace governance, regulatory, legal, or sector-specific frameworks.

### Identity, Authorization, and Controlled Access

Security and identity practices provide established foundations for explicit authentication, authorization, least-privilege access, policy enforcement, and auditable use of resources. [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final), is one relevant example.

Work on AI-agent identity, authorization, security, and interoperability is also developing rapidly, including the [NIST AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative). This work overlaps with the Foundation's concern for bounded authority and controlled execution. The Foundation additionally distinguishes technical ability, operational confidence, and organizational authorization: evidence about performance may inform an accountable decision, but it does not create authority by itself.

### Multi-Agent Systems and Agent Infrastructure

Research and standards for multi-agent systems have long addressed agent identity, communication, discovery, coordination, platform services, and lifecycle management. The [FIPA specifications](https://www.fipa.org/specifications/) are an established example of work in this area.

The Foundation is not a multi-agent platform specification. Its unit of design is the company, including human accountability, organizational capabilities, shared knowledge, governance, evidence, and deliberate evolution. Agents and agent platforms are possible implementations within that organization rather than the organizing center of the model.

### AI-First Organizational and Operating-Model Work

Strategy, organizational-design, and industry work increasingly describes AI as part of the operating model rather than as an additional tool. Common themes include redesigning work around outcomes, combining human judgment with AI-supported execution, making organizational knowledge accessible, and governing increasing levels of autonomy.

This body of work helps establish the broader problem space, but it varies widely in purpose and depth. The Foundation does not depend on any single industry definition of an AI-first organization. It provides a technology-neutral architectural model intended to make the underlying responsibilities, boundaries, and implementation requirements explicit.

## Contribution of This Foundation

The Foundation does not claim novelty for each of its constituent ideas. Its contribution lies in integrating them into one coherent organizational model and preserving their meaning across three traceable layers:

```text
Architecture
      ↓
Reference Design
      ↓
Technical Requirements
```

Within that model, the Foundation:

- treats humans and AI systems as contributors within one organizational system rather than as separate organizational worlds;
- separates stable Company Capabilities from replaceable human and technical implementations;
- separates technical ability, evidence-based Operational Confidence, and organizational authorization;
- keeps consequential authority and accountability explicitly governed;
- treats organizational memory as curated knowledge with context, provenance, evidence, and review conditions rather than as shared storage alone;
- connects controlled execution to attributable outcomes and reusable Evidence;
- allows continuous learning while requiring deliberate, authorized change; and
- is designed to support both a compact realization for a solo founder and progressive capability-by-capability transition for an established organization.

The intended result is not a product, software stack, or universal operating procedure. It is a stable foundation from which different organizational designs and technical implementations can be derived and evaluated.

## Operational Validation as the Next Phase

Foundation v1 establishes the conceptual, organizational, and technical basis. The next phase applies that basis to the real solo-founder company whose intended creation initiated this project.

Beginning with a compact realization and one capability at a time, operational use is expected to produce Evidence about practicality, proportionality, missing guidance, unnecessary burden, and the behavior of the defined boundaries under real conditions.

That Evidence is intended to support subsequent application artifacts, including the Solo Founder Minimal Realization, Day-One Reference Configuration, and Reference Company. It may lead to corrections or clarifications in downstream artifacts and, where a genuine architectural contradiction or gap is demonstrated, inform a separately governed future Foundation change.

This next phase does not make the operating company a demonstration constructed only to confirm the Foundation. The company remains a real organization pursuing real outcomes. Its operation provides an opportunity to challenge the Foundation rather than assuming it is correct.

The [LLM usage document](USING_THE_FOUNDATION_WITH_AN_LLM.md) provides an immediately usable repository-grounded prompt for beginning that application through a replaceable general-purpose LLM without making one model authoritative.

## Claims Not Made

This repository does not claim:

- invention or first use of every concept that appears in the Foundation;
- an exhaustive review of all related academic, standards, regulatory, or industry work;
- proof that no comparable synthesis exists elsewhere;
- replacement of applicable law, regulation, professional judgment, or sector-specific governance;
- that one Reference Design is the only valid realization of the Architecture; or
- that every architectural responsibility requires a separate person, team, component, or technical system.

The absence of a source or framework from this document does not imply that it is irrelevant. The related-work overview is intended to position the Foundation honestly, not to establish a universal claim of priority.

## Human–AI Collaboration

This repository was developed by **Andreas Nöthen** through sustained human–AI collaboration. AI assistance was used for exploration, synthesis, drafting, critique, structural analysis, and consistency validation.

Andreas Nöthen initiated and directed the work, evaluated and accepted its conceptual decisions, and remains responsible for the published result. AI-generated proposals were treated as inputs for review, not as authoritative sources.

Because the work evolved through iterative conversations and repeated revision, this document does not attribute individual sentences or concepts to particular AI outputs. Its references identify relevant established fields and frameworks; they are not presented as a complete provenance record of the development process.

## Research Scope and Temporal Limitations

This overview reflects work identified and reviewed during the development of Foundation v1. The field is evolving rapidly, particularly around AI-agent governance, identity, interoperability, organizational memory, and human–AI operating models.

The overview is therefore a bounded landscape assessment, not a systematic literature review. It should not be treated as exhaustive or permanently current. Later releases may revise this positioning as standards mature, terminology stabilizes, or materially relevant work becomes available.
