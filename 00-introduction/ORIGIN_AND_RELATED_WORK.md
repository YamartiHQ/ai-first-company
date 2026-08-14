# Origin, Related Work, and Contribution

## Document Role

This document explains why AI-First Company was developed, how it relates to established fields of work, and what contribution this repository intends to make.

This document is historical and explanatory. It does not define or extend the Architecture. Where it summarizes the model, the authoritative repository document prevails.

## Why This Project Exists

This project began with the practical intention to build an AI-first company from the ground up, initially around one founder. **This describes the origin of the project, not an Architecture requirement or preferred organizational form.**

The work required more than selecting AI tools or automating tasks. It raised organizational questions about shared intelligence, stable capabilities, Context, responsibility, Authority, Accountability, controlled execution, Organizational Learning, Continuous Assurance, Controlled Autonomy, and continuity.

Existing work addresses many of these questions individually, but the project did not identify one sufficiently complete model connecting them across organizational Architecture, Reference Design, and Technical Requirements for this purpose.

The model generalized beyond its initial founder-led realization into a performer-neutral organizational architecture applicable to Human Performers, AI Performers, mixed organizations, small and large organizations, and hierarchical or non-hierarchical coordination.

The historical origin remains useful because it demanded a model coherent enough for real operation without requiring unnecessary organizational size or one technical system for every responsibility.

## Development Process

AI-First Company emerged through iterative exploration, modeling, critique, and validation rather than adoption of one pre-existing framework.

The work brought together questions and practices from organizational design, enterprise architecture, knowledge management, AI governance, identity and authorization, controlled systems, and agent-oriented computing. Concepts were repeatedly renamed, separated, combined, or rejected to preserve clear responsibilities and boundaries.

Many concepts emerged through the project's internal modeling process before specific external work was reviewed. Later comparisons with standards, research, protocols, and implementation approaches served as validation, challenge, and discovery inputs. They confirmed some independently developed ideas, exposed missing boundaries and risks, and occasionally introduced relevant considerations that had not yet been represented. Those findings informed subsequent refinement, but external work was not adopted wholesale and does not become authoritative for the Architecture.

The references below identify representative comparison points, not a complete provenance record for every concept or revision.

Later refinement increasingly separated:

- Performer from Organization;
- Experience from Organizational Learning;
- Capability Qualification from Authority;
- Performer Memory from Company Brain;
- Decision from Execution, External Effect, and Outcome; and
- a central assistant concept from the governed, role-aware Executive Agent that presents organizational understanding and supports interaction without becoming a second Company Brain or mandatory path for all operation.

The resulting Architecture was translated into one Reference Design and traceable Technical Requirements. This translation tests whether organizational meaning can remain explicit on the path toward implementation without becoming tied to products or vendors.

## From Initial Realization to General Organizational Architecture

Validation exposed assumptions specific to the initial founder-led realization. Refinement generalized them:

- a universal human-accountability default became performer-neutral Authority and Accountability;
- Founder Continuity became Organizational Continuity;
- Company Memory as the central intelligence idea became Company Brain with differentiated State, Memory, Knowledge, Practice, and Provenance;
- one Operating Cycle became distinct Operating, Learning, and Assurance loops;
- AI assistance framing became Human, AI, and Group Performers;
- a central AI assistance interface became a governed, role-aware Executive Agent for organizational understanding, interaction, coordination, monitoring, review, and authorized action without becoming a second Company Brain, universal System of Record, or mandatory route for all operation; and
- upward management escalation became capability- and governance-aware Attention routing.

This evolution reflects refinement of the model, not deletion of its historical origin. Historical terms in this section describe how the model changed; they are not active Architecture concepts.

## Relationship to Existing Work

AI-First Company exists within established and rapidly evolving fields. The areas below provide relevant context and overlap with parts of the model.

These relationships do not imply that every Architecture concept derives from one source. Some sources informed the problem space, while other similarities reflect established practice or independent convergence. This document does not reconstruct source-level provenance for every design decision.

### Enterprise Architecture and Capability Modeling

Enterprise-architecture practices separate organizational capabilities from particular processes, structures, applications, and technologies. Capability-based planning and layered architectural descriptions therefore provide important context for the distinction between a Company Capability and its replaceable Capability Implementations and Performers.

Relevant bodies of work include [the TOGAF Standard and its Series Guides](https://www.opengroup.org/togaf/series-guides) and [the ArchiMate modeling language](https://www.opengroup.org/archimate-forum/archimate-overview). AI-First Company does not adopt their complete methods or metamodels. It applies a focused ontology to Human and AI operation, organizational intelligence, coordination, Authority, Accountability, execution, learning, assurance, and continuity.

### Knowledge Management and Provenance

Knowledge-management disciplines address how organizations create, maintain, share, review, and improve organizational knowledge. Provenance standards address how origin, attribution, derivation, and transformation remain represented across systems and contexts.

[ISO 30401](https://www.iso.org/standard/68683.html) provides requirements for organizational knowledge-management systems, while the [W3C PROV family of specifications](https://www.w3.org/TR/prov-overview/) provides interoperable models for Provenance.

These fields relate to the Architecture's Company Brain, Company Memory, Source Claims, Evidence, Provenance, Context Construction, and Organizational Learning. AI-First Company does not impose a universal linear promotion pipeline and is not an implementation of either standard.

### AI Governance and Risk Management

AI-governance and risk-management frameworks establish expectations for Accountability, transparency, traceability, evaluation, risk treatment, and lifecycle governance.

Relevant examples include the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), [ISO/IEC 42001](https://www.iso.org/standard/42001), and the [OECD AI Principles](https://oecd.ai/en/ai-principles).

AI-First Company shares these concerns but serves a different purpose. It defines a broader organizational architecture for coordinated Human and AI operation. Continuous Assurance, bounded and reversible autonomy, evaluation, traceability, and governed Authority complement rather than replace applicable governance, legal, regulatory, or sector-specific frameworks.

### Identity, Authorization, and Controlled Access

Security and identity practices provide established foundations for authentication, authorization, least privilege, policy enforcement, and auditable use of resources. [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final), is one relevant example.

Work on AI-agent identity, authorization, security, and interoperability is also developing rapidly, including the [NIST AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative).

This work overlaps with the Architecture's bounded Authority and controlled execution. The Architecture additionally addresses the Organizational Control Plane, scoped credentials, External Effects, Trajectory Integrity, and the distinction between Capability Qualification, Operational Confidence, and authorized governance decisions.

### Multi-Agent Systems, Agent Infrastructure, and Human Interaction

Research and standards for multi-agent systems have long addressed agent identity, communication, discovery, coordination, platform services, and lifecycle management. The [FIPA specifications](https://www.fipa.org/specifications/) are an established example.

More recent work explores conversational multi-agent orchestration, specialized and replaceable agents, long-running task coordination, tool and data integration, agent interoperability, and human-facing control surfaces. Representative comparison points include [AutoGen](https://arxiv.org/abs/2308.08155), Microsoft Research's [Magentic-UI](https://www.microsoft.com/en-us/research/publication/magentic-ui-report/), and Google's overview of current [agent protocols](https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols/).

These approaches provided useful validation and discovery inputs for Capability Agents, the Executive Agent, Human-AI interaction, bounded tool use, coordination, and replaceable implementations. AI-First Company treats agent frameworks, protocols, and interface technologies as possible implementation approaches. Agent topology, orchestration, memory, or interface centrality does not by itself create organizational Responsibility, Authority, Accountability, shared organizational intelligence, or mandatory hierarchy.

AI-First Company is not a multi-agent platform specification. Its unit of design is the organization, including Human and AI Performers, Company Capabilities, organization-owned intelligence, coordination, Authority, Accountability, Information Governance, learning, execution, assurance, and continuity.

### Agent State, Memory, and AI Evaluation

Modern agent implementations increasingly distinguish conversation history, session State, longer-term memory, external artifacts, and shared task State. Google's [Agent Development Kit memory guidance](https://codelabs.developers.google.com/codelabs/agent-memory/instructions?hl=en) and Microsoft's [agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) provide representative implementation-level comparison points.

Work on AI evaluation also emphasizes continuous, documented evaluation and the value of independent review. The [NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) provides one governance reference. Research on [LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) also identifies position, verbosity, self-enhancement, and reasoning limitations that can affect model-based evaluation.

These developments provided important validation, challenge, and discovery inputs for the separation of Working Memory, Performer Memory, Working Context, Company Brain, Organizational Learning, Evidence, and Continuous Assurance. AI-First Company extends implementation distinctions into organizational boundaries: retained agent State does not automatically become organizational truth or learning, and agreement among correlated evaluators does not automatically become independent Evidence or Authority.

### AI-First Organizational and Operating-Model Work

Strategy, organizational-design, and industry work increasingly describes AI as part of the operating model rather than an additional tool. Common themes include redesigning work around outcomes, coordinating Human and AI capabilities across judgment, execution, learning, and governance, making organizational intelligence usable, and governing increasing autonomy.

This body of work helps establish the broader problem space but varies widely in purpose and depth. AI-First Company does not depend on one industry definition. It provides a technology-neutral architecture intended to make organizational responsibilities, relationships, and implementation requirements explicit.

## Contribution of AI-First Company

AI-First Company does not claim novelty for each constituent idea. Its contribution lies in integrating them into one coherent organizational model and preserving meaning across three traceable layers:

```text
Architecture
      ↓
Reference Design
      ↓
Technical Requirements
```

Within that model, AI-First Company:

- provides one organizational architecture for Human and AI Performers;
- separates stable Company Capabilities from Capability Implementations and Performers;
- separates Responsibility, Authority, and Accountability;
- defines Company Brain as organization-owned intelligence;
- keeps Performer Memory distinct from Company Brain;
- constructs Working Context under information and Authority boundaries;
- connects Experience and Organizational Reflection to governed Organizational Learning;
- separates Capability Qualification, Operational Confidence, and Authority;
- supports Controlled Autonomy through bounded Authority, controls, and Continuous Assurance;
- preserves Decision ≠ Execution ≠ External Effect ≠ Outcome;
- routes Attention without requiring hierarchy;
- applies Information Governance across Memory, Context, Learning, and External Research; and
- supports Organizational Continuity across Human, AI, implementation, provider, and other dependency change.

The intended result is not a product, software stack, universal operating procedure, or claim of unique invention. It is a stable model from which organizational designs and technical implementations can be derived and evaluated.

## Claims Not Made

This repository does not claim:

- invention or first use of every concept in AI-First Company;
- an exhaustive review of all related academic, standards, regulatory, or industry work;
- proof that no comparable synthesis exists elsewhere;
- replacement of applicable law, regulation, professional judgment, or sector-specific governance;
- that AI-first implies removing humans;
- that AI-first requires autonomous Agents everywhere;
- that AI-First Company requires a non-hierarchical organization;
- that one Reference Design is the only valid Architecture realization; or
- that every responsibility requires a separate person, team, component, or system.

The absence of a source or framework does not imply irrelevance. This overview positions AI-First Company honestly rather than establishing a universal priority claim.

## Human–AI Collaboration

This repository was developed by **Andreas Nöthen** through sustained Human–AI collaboration. AI assistance supported exploration, synthesis, drafting, critique, structural analysis, and consistency validation.

Andreas Nöthen initiated and directed the work, evaluated and accepted its conceptual decisions, and remains responsible for the published result. AI-generated proposals were review inputs, not authoritative sources.

Because the work evolved through iterative conversations, comparison, discovery, and revision, this document does not attribute individual sentences or concepts to particular AI outputs or external sources. Its references identify representative fields, standards, research, protocols, and implementation approaches used during development. They are not a complete provenance record for every concept or revision.

## Research Scope and Temporal Limitations

This overview reflects work identified and reviewed during development of AI-First Company through its current release.

The field is evolving rapidly, particularly around agent memory, Organizational Learning, Continuous Assurance, autonomous execution, AI-agent security, identity, interoperability, multi-agent coordination, and Human–AI operating models.

This is a bounded landscape assessment rather than a systematic literature review. It should not be treated as exhaustive or permanently current. Later releases may revise the positioning as standards mature, terminology stabilizes, or materially relevant work becomes available.
