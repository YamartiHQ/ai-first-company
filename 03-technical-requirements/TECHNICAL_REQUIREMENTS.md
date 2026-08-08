# AI-First Company — Technical Requirements

## Contents

1. [Purpose](#1-purpose)
2. [From Reference Design to Technology](#2-from-reference-design-to-technology)
3. [Technical Principles](#3-technical-principles)
4. [Technical Component Inventory](#4-technical-component-inventory)
5. [Reference Composition × Technology Matrix](#5-reference-composition--technology-matrix)
6. [Implementation Map](#6-implementation-map)
7. [Technology Requirements](#7-technology-requirements)
8. [Cross-Technology Requirements](#8-cross-technology-requirements)
9. [Completeness and Traceability](#9-completeness-and-traceability)
10. [Minimum Technical Realization](#10-minimum-technical-realization)

## 1. Purpose

> **The Technical Requirements define the technology required to realize the AI-First Company Reference Design.**

The Architecture explains what an AI-First Company is.

The [Reference Design](../02-reference-design/REFERENCE_DESIGN.md) translates the Architecture into an organizational design.

The Technical Requirements define the technology required to realize that design.

They do not prescribe a particular vendor, product, programming language, cloud platform, model provider, database product, agent framework, or deployment environment.

Instead, they define:

- which technical components are required by the Reference Design;
- which Reference responsibilities create those requirements;
- what each technical component must be capable of doing;
- where multiple requirements may share one concrete implementation; and
- how a concrete technology can be evaluated against the requirements.

The result is intended to provide a practical basis for implementation.

### 1.1 Requirement Language

When used to express an obligation in this document, **must** and **must not** define mandatory conformance conditions, **should** and **should not** define expected conditions from which a concrete implementation may deviate only with an explicit justification, and **may** defines an optional choice.

`Must Support` identifies the complete capability set against which a concrete implementation of a Technical Component is evaluated. Every applicable capability in that field is mandatory, whether it is supplied directly or through an explicitly identified Shared Implementation.

A developer should be able to move from:

```text
Reference Composition
        ↓
Required Technology
        ↓
Technical Requirements
        ↓
Concrete Technology Selection
```

without having to infer missing parts of the technical architecture.

---

## 2. From Reference Design to Technology

The Technical Requirements are derived from the Reference Design rather than from available technology.

For every technically relevant Reference responsibility, the analysis follows the same path:

```text
Reference Composition
        ↓
Reference Responsibility
        ↓
Required Technical Function
        ↓
Technical Component
        ↓
Technical Requirements
        ↓
Implementation Choice
```

A technical component exists in this document because at least one Reference responsibility requires it.

Likewise, every technically relevant Reference responsibility must be covered by one or more technical components.

This creates two complementary rules:

> **No Reference responsibility may depend on an unidentified technical capability.**

> **No technical component should be introduced merely because a technology exists.**

The Technical Requirements therefore realize the Reference Design without silently extending it.

A relationship may be conditional for either of two reasons:

- the Reference Design use case itself may not require the function; or
- an already selected shared implementation may or may not provide the complete required function.

In both cases, the condition must remain explicit. A conditional component is mandatory whenever its stated condition is true.

---

## 3. Technical Principles

### 3.1 Technology Independence

Technology classes are defined independently of individual products and vendors.

A requirement may therefore be realized by a commercial product, hosted service, open-source system, custom implementation, or a combination of these.

### 3.2 Shared Implementation

Separate Technical Requirements do not necessarily require separate products or services.

A single technical system may satisfy multiple requirements if it fulfills the complete requirement set of each.

For example:

```text
Relational Database
Full-Text Search
Vector Search
        ↓
may be provided by
one concrete system
```

The requirements remain distinct even when their implementation is shared.

### 3.3 Deterministic Control

AI may interpret information, reason, generate content, recommend actions, and perform organizational capabilities.

Identity, authorization, authority boundaries, durable execution state, external effects, and other hard organizational boundaries must remain technically enforceable independently of an AI model deciding to respect them.

### 3.4 Durable Organizational State

Material organizational state must survive the execution lifetime of individual agents, models, or application processes.

An agent crash, model replacement, or process restart must not silently destroy organizational execution state.

### 3.5 Controlled External Effects

External actions pass through controlled technical boundaries.

Technical credentials do not create organizational permission.

Uncertainty about an external action must remain visible rather than being converted into assumed success or failure.

### 3.6 Environment Separation

Sandbox and Production represent different organizational realities.

Their mutable state, execution, credentials, configuration, traces, and external-effect boundaries remain appropriately separated.

### 3.7 Versioned Change

Material implementations and configurations remain identifiable across change.

This includes, where relevant:

- Capability Agent implementations;
- model configurations;
- Execution Graphs;
- connectors;
- policies;
- context strategies; and
- evaluation candidates.

### 3.8 Observable Failure

Failure remains observable and bounded.

Technical failure may reduce available capability, but it must not silently expand authority or weaken governance.

### 3.9 Evidence-Based Qualification

Evaluation produces evidence.

Qualification states what that evidence demonstrates for a defined organizational scope.

Neither evaluation nor qualification automatically creates Production authority or activates a candidate in Production.

### 3.10 Adversarial Content

Retrieved content, external messages, documents, media, tool results, model output, and other processed information may be incorrect, manipulated, or adversarial.

Technical implementation must preserve the distinction between information and organizational instruction. Content alone must not create Intent, authority, policy, tool permission, or a change to technical enforcement.

### 3.11 Bounded Delegation and Composition

Delegation between agents, services, tools, and workflows remains attributable to the originating execution and bounded by its identity, Company Capability, action, information, resource, environment, and authorization scope.

Combining individually permitted identities, information access, tools, or actions must not produce a consequential Outcome outside the originating authorization boundary.

### 3.12 Security Integrity and Containment

Versioning alone does not establish integrity. Material models, agent configurations, prompts, skills, connectors, policies, dependencies, deployment artifacts, and evaluation assets must remain identifiable and verifiable according to organizational consequence.

Production execution remains contained by applicable process, file, network, credential, tool, destination, data-flow, and resource boundaries. Detection, revocation, isolation, and recovery must not depend on the affected model or agent cooperating.

### 3.13 Defense in Depth

Agent-specific controls supplement rather than replace an appropriate cybersecurity baseline.

No model, prompt, evaluation result, agent framework, policy engine, or internal network location is a sufficient security boundary by itself. Concrete implementations protect confidentiality, integrity, availability, and recoverability through layered controls proportionate to organizational consequence.

---

## 4. Technical Component Inventory

The Technical Requirements evaluate the following technical component types.

Some are broadly required across the Reference Design. Others become required only when a clearly stated condition applies.

Multiple component requirements may be satisfied by the same concrete system through **Shared Implementation**.

- Backend Application / Service Framework
- Relational Database Management System
- Object / File Storage System
- Full-Text Search Engine
- Vector Search Engine
- Embedding Model / Service
- Large Language Model / Inference Service
- AI Agent Framework / Runtime
- Workflow Orchestration Engine
- Identity and Access Management System
- Authorization / Policy Enforcement System
- Secrets Management System
- Integration / Connector Framework
- Versioned Configuration Repository
- Application UI Framework
- Logging, Monitoring & Tracing Platform
- Backup & Recovery Tooling
- Environment Isolation Mechanism
- Deployment & Provisioning Tooling
- Automated Testing & Evaluation Framework
- Message Broker / Event Bus
- Service Virtualization / Mocking Framework
- Data Transformation / Anonymization Tooling
- Document Parsing / Text Extraction
- Schema / Data Validation Library

This inventory describes **technical requirements, not product count**.

---

## 5. Reference Composition × Technology Matrix

A **✓** means that the Composition itself creates the technical requirement.

A written condition means that the component becomes required when that explicitly stated situation applies.

Conditions based on organizational use distinguish use cases that genuinely need a function. Conditions based on Shared Implementation distinguish whether an additional component is necessary after a selected system has been evaluated against the complete requirement. Neither kind of condition makes the underlying requirement optional when the condition applies.

An empty cell means that the Composition does not itself create that requirement.

Technologies belonging to another contained Composition are not duplicated.

### 5.1 Application, Data & Search

| Reference Composition | Backend Application / Service Framework | Relational Database Management System | Object / File Storage System | Full-Text Search Engine | Vector Search Engine | Embedding Model / Service |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Executive Agent** | ✓ |  |  |  |  |  |
| **Company Brain** | ✓ | ✓ | If files, documents or artifacts are stored rather than only referenced | If text must be retrieved by words, phrases or exact terms | If knowledge must be retrieved by semantic similarity | If Vector Search is used |
| **Capability Agent** |  |  | If the capability directly reads, creates or retains files or large artifacts |  |  |  |
| **Execution Graph Layer** |  |  |  |  |  |  |
| **Company Interface Layer** |  |  | If external interactions transfer files or attachments that must be retained or buffered |  |  |  |
| **Sandbox Organization** |  |  |  |  |  |  |
| **Production Organization** |  |  |  |  |  |  |
| **Evaluation & Qualification** | ✓ | ✓ | If evaluation uses files, large datasets, replay artifacts or other unstructured/binary evidence |  |  |  |

### 5.2 AI & Execution

| Reference Composition | Large Language Model / Inference Service | AI Agent Framework / Runtime | Workflow Orchestration Engine | Message Broker / Event Bus | Schema / Data Validation Library |
|---|:---:|:---:|:---:|:---:|:---:|
| **Executive Agent** | ✓ | ✓ |  |  | ✓ |
| **Company Brain** |  |  |  |  | ✓ |
| **Capability Agent** | ✓ | ✓ |  |  | ✓ |
| **Execution Graph Layer** |  |  | ✓ | If Workflow and Integration systems cannot provide the required asynchronous signals and event delivery | ✓ |
| **Company Interface Layer** |  |  |  | If Connector and Workflow systems cannot provide the required event-delivery guarantees | ✓ |
| **Sandbox Organization** |  |  |  |  |  |
| **Production Organization** |  |  |  |  |  |
| **Evaluation & Qualification** | If semantic or model-based evaluation is used |  |  |  | ✓ |

### 5.3 Identity, Authority & Integration

| Reference Composition | Identity and Access Management System | Authorization / Policy Enforcement System | Secrets Management System | Integration / Connector Framework | Versioned Configuration Repository |
|---|:---:|:---:|:---:|:---:|:---:|
| **Executive Agent** | ✓ | ✓ | If model or tool access uses organization-managed credentials |  | ✓ |
| **Company Brain** | ✓ | ✓ | If access to underlying Systems of Record requires managed credentials |  |  |
| **Capability Agent** | ✓ | ✓ | If model or tool access uses managed credentials |  | ✓ |
| **Execution Graph Layer** | ✓ | ✓ |  |  | ✓ |
| **Company Interface Layer** | ✓ | ✓ | If a connector requires managed credentials | ✓ | ✓ |
| **Sandbox Organization** | ✓ | ✓ | If Sandbox components or simulated/external systems use managed credentials |  | ✓ |
| **Production Organization** | ✓ | ✓ | If Production models, services or external systems use managed credentials |  | ✓ |
| **Evaluation & Qualification** | ✓ | ✓ | If evaluation accesses protected models, data or systems using managed credentials |  |  |

### 5.4 Human Interaction & Operations

| Reference Composition | Application UI Framework | Logging, Monitoring & Tracing Platform | Backup & Recovery Tooling | Deployment & Provisioning Tooling |
|---|:---:|:---:|:---:|:---:|
| **Executive Agent** | ✓ | ✓ |  |  |
| **Company Brain** |  | ✓ |  |  |
| **Capability Agent** | If humans interact directly with the Capability Agent | ✓ |  |  |
| **Execution Graph Layer** | If executions include human approval or decision steps | ✓ |  |  |
| **Company Interface Layer** |  | ✓ |  |  |
| **Sandbox Organization** |  | ✓ |  | ✓ |
| **Production Organization** |  | ✓ | ✓ | ✓ |
| **Evaluation & Qualification** | If evaluation or qualification includes human review |  |  |  |

### 5.5 Sandbox & Evaluation-specific Technology

| Reference Composition | Environment Isolation Mechanism | Automated Testing & Evaluation Framework | Service Virtualization / Mocking Framework | Data Transformation / Anonymization Tooling | Document Parsing / Text Extraction |
|---|:---:|:---:|:---:|:---:|:---:|
| **Executive Agent** |  |  |  |  |  |
| **Company Brain** |  |  |  |  | If stored documents must become searchable or semantically retrievable |
| **Capability Agent** |  |  |  |  | If the capability must interpret document formats rather than already extracted content |
| **Execution Graph Layer** |  |  |  |  |  |
| **Company Interface Layer** |  |  |  |  |  |
| **Sandbox Organization** | ✓ |  | If evaluation requires external systems to be simulated | If sensitive Production-derived data is transferred into Sandbox |  |
| **Production Organization** | ✓ |  |  |  |  |
| **Evaluation & Qualification** |  | ✓ |  |  | If evaluation scenarios contain documents whose content must be extracted |

---

## 6. Implementation Map

The Implementation Map explains each technology relationship from the matrix through its Reference basis.

A Reference basis is either a named responsibility from the Reference Design or an explicit implementation condition derived from that responsibility. Supporting labels such as `Operation`, `Configuration`, or `Protected Access` group technical consequences; they do not create additional Reference Design responsibilities.

It answers:

> **Why does this Composition require this technology?**

It does not redefine the technology itself.

### 6.1 Executive Agent

| Reference Basis | Required Technology | Used for |
|---|---|---|
| Organization Understanding | Backend Application / Service Framework | Coordinate deterministic processing and access to organizational information |
| Organization Understanding | Large Language Model / Inference Service | Interpret relevant organizational state, knowledge, activity, uncertainty and attention |
| Organization Understanding | AI Agent Framework / Runtime | Run the Executive Agent with model access, bounded context and controlled tools |
| Context Builder | Backend Application / Service Framework | Assemble bounded Working Context |
| Context Builder | Schema / Data Validation Library | Produce structured and validatable Working Context |
| Capability Coordination | Identity and Access Management System | Preserve participant and workload identity |
| Capability Coordination | Authorization / Policy Enforcement System | Preserve authority, information and execution boundaries |
| Organizational Interaction | Application UI Framework | Provide conversation, dashboards, reports, notifications and decisions |
| Configuration | Versioned Configuration Repository | Preserve identifiable Executive Agent and context-strategy configuration |
| Operation | Logging, Monitoring & Tracing Platform | Observe relevant interactions, failures and technical execution |
| Protected Access | Secrets Management System | Required when model or tool access uses managed credentials |

### 6.2 Company Brain

| Reference Basis | Required Technology | Used for |
|---|---|---|
| Shared Organizational Understanding | Backend Application / Service Framework | Provide a coherent access layer across organizational representations |
| Memory, State and Context | Relational Database Management System | Store structured state, relationships, decisions and metadata |
| Memory, State and Context | Schema / Data Validation Library | Maintain explicit structured organizational representations |
| Knowledge Access | Full-Text Search Engine | Required when text must be retrieved by exact terms, phrases or lexical relevance |
| Knowledge Access | Vector Search Engine | Required when knowledge must be retrieved by semantic similarity |
| Knowledge Access | Embedding Model / Service | Required when Vector Search is used; generate its semantic representations |
| Curation and Artifacts | Object / File Storage System | Required when files, documents or artifacts are stored rather than only referenced |
| Curation and Artifacts | Document Parsing / Text Extraction | Required when stored document content must become searchable or semantically retrievable |
| Sources and Authority | Relational Database Management System | Maintain the source registry, System-of-Record mapping and authority metadata |
| Sources and Authority | Identity and Access Management System | Identify humans, agents and services accessing organizational information |
| Sources and Authority | Authorization / Policy Enforcement System | Enforce governed Knowledge Access and information boundaries |
| Sources and Authority | Secrets Management System | Required when authoritative systems require managed credentials |
| Operation | Logging, Monitoring & Tracing Platform | Observe retrieval, access and relevant information-flow failures |

### 6.3 Capability Agent

| Reference Basis | Required Technology | Used for |
|---|---|---|
| Capability Alignment | AI Agent Framework / Runtime | Realize a Company Capability as an executable agent implementation |
| Capability Alignment | Large Language Model / Inference Service | Perform AI-based reasoning, interpretation or generation |
| Capability Alignment | Versioned Configuration Repository | Identify model, instructions, tools and other material implementation characteristics |
| Performer Replaceability | AI Agent Framework / Runtime | Allow models, tools and agent implementations to be replaced without redefining the Company Capability |
| Performer Replaceability | Versioned Configuration Repository | Preserve the identifiable implementation characteristics required to compare, replace and re-evaluate performers |
| Working Context | Schema / Data Validation Library | Consume and produce bounded structured organizational data |
| Working Context | Authorization / Policy Enforcement System | Keep information and tool access within organizational boundaries |
| Working Context | Identity and Access Management System | Give the Capability Agent an attributable technical identity |
| Protected Access | Secrets Management System | Required when model or tool access uses managed credentials |
| Files and Artifacts | Object / File Storage System | Required when the capability reads, creates or retains files or large artifacts |
| Document Handling | Document Parsing / Text Extraction | Required when document formats themselves must be interpreted |
| Direct Human Interaction | Application UI Framework | Required where humans interact directly with the Capability Agent |
| Operation | Logging, Monitoring & Tracing Platform | Trace implementation, relevant activity, failure and outcome |

### 6.4 Execution Graph Layer

| Reference Basis | Required Technology | Used for |
|---|---|---|
| Organizational Execution | Workflow Orchestration Engine | Execute long-running, stateful organizational processes |
| Organizational Execution | Schema / Data Validation Library | Define structured graph inputs, outputs and states |
| Capability before Performer | Identity and Access Management System | Preserve attributable participant and performer identities |
| Capability before Performer | Authorization / Policy Enforcement System | Verify permitted performer and action scope |
| Waiting and Decisions | Workflow Orchestration Engine | Persist waits, timers, approvals and resume conditions |
| Waiting and Decisions | Application UI Framework | Required where graphs contain human approvals or decisions |
| Events and Signals | Message Broker / Event Bus | Required when Workflow and Integration systems cannot provide the required asynchronous signals and event delivery |
| Observable Execution | Logging, Monitoring & Tracing Platform | Preserve execution/version, state transitions, failures and outcomes |
| Reproducibility and Evolution | Versioned Configuration Repository | Preserve identifiable Execution Graph definitions and versions |

### 6.5 Company Interface Layer

| Reference Basis | Required Technology | Used for |
|---|---|---|
| Inbound Information | Integration / Connector Framework | Receive and normalize external information |
| Inbound Information | Schema / Data Validation Library | Validate external payloads before organizational processing |
| Inbound Information | Object / File Storage System | Required when incoming files or attachments must be retained or buffered |
| Inbound Events | Message Broker / Event Bus | Required when Connector and Workflow systems cannot provide the required event-delivery guarantees |
| Outbound Action | Integration / Connector Framework | Execute controlled reads, writes, commands and external effects |
| Outbound Action | Authorization / Policy Enforcement System | Verify organizational permission before external action |
| Connectors | Versioned Configuration Repository | Preserve connector implementations and configuration versions |
| Connectors | Secrets Management System | Required if a connector requires managed credentials |
| Systems of Record | Integration / Connector Framework | Access authoritative systems without coupling Company Capabilities to providers |
| Identity and Provenance | Identity and Access Management System | Relate organizational participants to technical identities |
| Identity and Provenance | Logging, Monitoring & Tracing Platform | Preserve execution, external system and outcome attribution |
| Failure | Integration / Connector Framework | Surface timeout, availability, rate-limit and unresolved-result conditions |

### 6.6 Sandbox Organization

| Reference Basis | Required Technology | Used for |
|---|---|---|
| Organizational Environment | Environment Isolation Mechanism | Prevent Sandbox state, credentials, execution and effects from becoming Production reality |
| Organizational Environment | Deployment & Provisioning Tooling | Create reproducible evaluation environments |
| Isolation | Identity and Access Management System | Distinguish Sandbox identities from Production |
| Isolation | Authorization / Policy Enforcement System | Enforce Sandbox-specific authority and information boundaries |
| Isolation | Secrets Management System | Required if Sandbox components or simulated/external systems use managed credentials |
| Isolation | Versioned Configuration Repository | Preserve the exact environment and candidate configuration |
| Isolation | Logging, Monitoring & Tracing Platform | Keep Sandbox execution distinguishable and observable |
| External-System Simulation | Service Virtualization / Mocking Framework | Required when evaluation requires external systems without real external consequences |
| Production-derived Evaluation Data | Data Transformation / Anonymization Tooling | Required when sensitive Production-derived data enters Sandbox |

**Replay does not create an additional Sandbox-specific technology requirement.**  
The Sandbox provides the isolated organizational environment and relevant evaluation state. Repeatable scenario execution and comparison are provided by the Automated Testing & Evaluation Framework of Evaluation & Qualification.

### 6.7 Production Organization

**Production includes its own operational Company Brain.**  
The technologies required to realize that Company Brain remain defined by the Company Brain Composition and are therefore not duplicated as Production-specific requirements in this map.

| Reference Basis | Required Technology | Used for |
|---|---|---|
| Operational Reality | Environment Isolation Mechanism | Keep Production reality distinct from Sandbox |
| Authorized Execution | Identity and Access Management System | Maintain attributable Production identities |
| Authorized Execution | Authorization / Policy Enforcement System | Ensure technical Production access does not itself create authority |
| Authorized Execution | Secrets Management System | Required if Production models, services or external systems use managed credentials |
| Change | Versioned Configuration Repository | Identify active Production configuration and versions |
| Change | Deployment & Provisioning Tooling | Apply accepted Production changes reproducibly |
| Continuity | Backup & Recovery Tooling | Restore relevant Production state and configuration |
| Failure | Logging, Monitoring & Tracing Platform | Detect failures, degraded capability and dependency problems |
| Failure and Recovery | Deployment & Provisioning Tooling | Restore or replace failed components without bypassing governance |

### 6.8 Evaluation & Qualification

| Reference Basis | Required Technology | Used for |
|---|---|---|
| Evaluation | Automated Testing & Evaluation Framework | Execute Candidates against scenarios, historical cases, replay and failure conditions |
| Capability-Based Evaluation | Automated Testing & Evaluation Framework | Evaluate Candidates against defined Company Capabilities under specified organizational conditions |
| Evaluation | Backend Application / Service Framework | Coordinate evaluation runs, evidence and qualification workflows |
| Evaluation | Relational Database Management System | Store candidates, scenarios, runs, metrics and qualification metadata |
| Operational Confidence | Relational Database Management System | Maintain contextual and revisable Operational Confidence records linked to the relevant Candidate, Capability, conditions and supporting evidence |
| Evaluation Evidence | Object / File Storage System | Required when evaluation uses files, large datasets, replay artifacts or other unstructured/binary evidence |
| Evaluation Evidence | Schema / Data Validation Library | Maintain structured and comparable evaluation records |
| Evaluation Evidence | Document Parsing / Text Extraction | Required when evaluation scenarios contain documents whose content must be extracted |
| Model-based Evaluation | Large Language Model / Inference Service | Required where semantic/model-based assessment is used |
| Qualification | Identity and Access Management System | Attribute Candidates, reviewers and qualification decisions |
| Qualification | Authorization / Policy Enforcement System | Preserve qualification scope and separation from authority |
| Protected Evaluation Resources | Secrets Management System | Required when protected models, data or systems are accessed |
| Human Judgment | Application UI Framework | Required where evaluation or qualification includes human review |

---

## 7. Technology Requirements

The `Must Support` column is also the selection test for a concrete implementation.

A concrete implementation satisfies a Technology Requirement when all applicable `Must Support` capabilities are provided either directly or through an explicitly identified **Shared Implementation**.

| Requirement ID | Technology | Must Support | Shared Implementation |
|---|---|---|---|
| **TR-APP** | **Backend Application / Service Framework** | Deterministic application logic; internal APIs/services; integration with data, AI, identity, workflow and connector components; structured errors; testability; modular service logic | AI Agent Framework / Runtime; Integration / Connector Framework; Automated Testing & Evaluation Framework |
| **TR-RDB** | **Relational Database Management System** | Durable persistence; relational schemas; primary/foreign keys; referential integrity; transactions; constraints; concurrent reads/writes; concurrency-safe updates; indexes; schema evolution; programmatic access; backup/restore integration | Full-Text Search Engine; Vector Search Engine; Versioned Configuration Repository |
| **TR-OFS** | **Object / File Storage System** | Durable object/file storage; stable identifiers; metadata; integrity verification; access-control integration; large-object support; reliable retrieval; retention/versioning where required | — |
| **TR-FTS** | **Full-Text Search Engine** | Text indexing; exact and phrase search; relevance ranking; metadata filtering; incremental index updates; deletion/update support; source traceability; access-boundary-compatible filtering | Relational Database Management System; Vector Search Engine |
| **TR-VSS** | **Vector Search Engine** | Vector indexing; similarity/top-k search; metadata filtering; insertion/update/deletion; environment separation; source references; embedding-version awareness | Relational Database Management System; Full-Text Search Engine |
| **TR-EMB** | **Embedding Model / Service** | Text-to-vector generation; query and batch embedding; identifiable model/version; stable output dimensions within a version; programmatic access; re-embedding after model changes | Large Language Model / Inference Service |
| **TR-LLM** | **Large Language Model / Inference Service** | Programmatic inference; reasoning/interpretation; generation; sufficient context; structured output; tool/function interaction or equivalent; identifiable model/configuration; explicit errors/timeouts/rate limits; usage metadata | Embedding Model / Service |
| **TR-AGT** | **AI Agent Framework / Runtime** | Model invocation; Working Context injection; versioned agent configuration; controlled and allowlisted tools; structured I/O; workload identity; bounded and attributable subagent delegation; separation of source content from organizational instruction; external authorization enforcement; process, file, network and resource-containment integration; execution and iteration limits; error handling; cancellation; tracing hooks; replaceable models and tools | Backend Application / Service Framework; Workflow Orchestration Engine |
| **TR-WFL** | **Workflow Orchestration Engine** | Durable long-running execution; persistent state; wait states; timers; external signals/events; retries/backoff; human approval gates; parallel branches; recovery after restart; failure paths; versioning; correlation; idempotency support; reconstructable execution; bounded delegation; execution budgets; circuit breakers; termination of runaway or recursively expanding work | AI Agent Framework / Runtime; Message Broker / Event Bus |
| **TR-IAM** | **Identity and Access Management System** | Human identities; workload/agent identities; authentication; identity lifecycle; machine-readable principals/claims; application integration; environment separation; attributable identity; short-lived or task-scoped identity where required; preserved delegation chain; prompt revocation and containment support | Authorization / Policy Enforcement System |
| **TR-AUT** | **Authorization / Policy Enforcement System** | Decisions based on identity/resource/action/context; capability and mandate boundaries; information restrictions; risk/environment rules; approval conditions; default or explicit deny; versioned rules; auditable decisions; per-action programmatic enforcement; tool, destination and data-flow boundaries; bounded delegation and onward delegation; prevention of unauthorized privilege composition; information-egress enforcement | Identity and Access Management System; Backend Application / Service Framework |
| **TR-SEC** | **Secrets Management System** | Encrypted secret storage; programmatic retrieval; fine-grained access control; environment separation; audit; versioning/rotation; API keys/tokens/certificates/service credentials; protection from prompt/context/log leakage | IAM or deployment platforms where they satisfy the full requirement |
| **TR-CON** | **Integration / Connector Framework** | Replaceable connectors; explicitly bounded and allowlisted read/write/query/command/event operations, resources and destinations; authentication integration; schema translation/validation; inbound-content trust metadata; outbound information-policy enforcement; timeouts; retries; rate limits; idempotency; explicit errors; unresolved-result representation; provenance; connector versioning | Backend Application / Service Framework; Message Broker / Event Bus |
| **TR-CFG** | **Versioned Configuration Repository** | Identifiable versions; change history; diff/review; restoration; environment-specific configuration; access control; execution/evaluation references; versioning of agents, graphs, connectors, policies and context strategies; integrity verification; attributable approval and controlled activation of material versions | Relational Database Management System; Deployment & Provisioning Tooling |
| **TR-UIF** | **Application UI Framework** | Authenticated organizational views; structured presentation; forms/decisions; human approvals/reviews; dashboards/reports; optional conversation; IAM/backend integration; attributable consequential actions | One UI framework may serve several Compositions |
| **TR-OBS** | **Logging, Monitoring & Tracing Platform** | Structured logs; metrics; health and security monitoring; alerts; correlation IDs; execution/distributed tracing; delegation-chain and authorization-decision visibility; search; retention; environment separation; dependency health; organizational execution correlation; sensitive-data protection; append-only or tamper-evident records where required by consequence; detection of anomalous access, tool use, egress, resource consumption and boundary violations | One observability platform may provide all three functions |
| **TR-BKP** | **Backup & Recovery Tooling** | Relevant state/configuration backup; encryption; retention; tested restore; recovery according to organizational consequence; coordination with execution recovery | Native RDBMS/Object Storage backup; Deployment & Provisioning Tooling |
| **TR-ISO** | **Environment Isolation Mechanism** | Separation of mutable state, execution state, credentials, configuration, traces and external effects; explicit environment and workload identity; prevention of Sandbox→Production impact; adjustable isolation strength; process, file-system, network, credential and tool isolation; destination and egress restriction; CPU, memory, storage, time and process limits; containment and termination independent of agent cooperation | Deployment & Provisioning Tooling |
| **TR-DEP** | **Deployment & Provisioning Tooling** | Reproducible environments; versioned deployment configuration; controlled activation; environment-specific secrets/configuration; technical rollback; health verification; attributable change history; drift detection; Sandbox reset/disposal; verifiable deployment artifacts and dependencies; integrity and provenance checks; controlled promotion; rapid isolation or rollback after a security incident | Environment Isolation Mechanism; Versioned Configuration Repository |
| **TR-EVL** | **Automated Testing & Evaluation Framework** | Versioned candidates/scenarios; synthetic/historical/replay/failure/adversarial cases; repeatable and batch/regression runs; deterministic evaluators; optional model-based evaluators; expected/observed comparison; authority, information, delegation, tool, egress, resource and containment boundary tests; instruction-injection, manipulated-tool-output, poisoning, compromised-dependency, privilege-composition, exfiltration, observability-bypass and runaway-execution cases where applicable; metrics; evidence capture; trace and human-review integration | Backend Application / Service Framework; Service Virtualization / Mocking Framework |
| **TR-EVT** | **Message Broker / Event Bus** | When separately required: durable asynchronous delivery; queue/pub-sub; authenticated participants; correlation; retry; dead-letter handling; backpressure; deduplication/idempotency; ordering where required; environment separation; monitoring | Workflow Orchestration Engine; Integration / Connector Framework |
| **TR-MCK** | **Service Virtualization / Mocking Framework** | Simulated external APIs/services/events; controlled responses; latency/timeouts/rate limits; defined failures; duplicates; unresolved outcomes; repeatable behavior; no real Production effects | Automated Testing & Evaluation Framework; Integration / Connector Framework |
| **TR-ANM** | **Data Transformation / Anonymization Tooling** | Purpose-specific selection; minimization; masking; pseudonymization/anonymization where required; repeatable transformations; provenance preservation; validation; auditability | Backend Application / Service Framework; Integration / Connector Framework |
| **TR-DOC** | **Document Parsing / Text Extraction** | Supported-format parsing; text/metadata extraction; source references; explicit failures; programmatic/batch processing; attachment handling where needed; optional OCR; reprocessing after parser changes; preservation of source-content boundaries; extracted instruction-like content remains data rather than executable organizational instruction | Backend Application / Service Framework |
| **TR-SCH** | **Schema / Data Validation Library** | Structured schemas; required/optional fields; types; enums; constraints; nested structures; runtime validation; machine-readable errors; schema evolution; validation for API, LLM, Working Context, workflow, connector, tool-call, external-action and evaluation records; rejection of undeclared operations, resources, destinations and fields | Backend Application / Service Framework; AI Agent Framework / Runtime; Integration / Connector Framework; Automated Testing & Evaluation Framework |

Object or file storage may be supplied by a deployment platform as the concrete implementation of **TR-OFS** when it satisfies that requirement completely. The platform is not thereby introduced as a separate Technical Component or listed as a Shared Implementation.

---

## 8. Cross-Technology Requirements

Some requirements cannot be satisfied meaningfully by one component alone.

### 8.1 End-to-End Attribution

**Requirement ID:** XTR-ATR

Consequential organizational activity remains attributable across the technical chain:

```text
Participant
    ↓
Company Capability
    ↓
Execution
    ↓
Technical Identity
    ↓
Tool / Connector
    ↓
External Outcome
```

Shared infrastructure must not erase organizational accountability.

### 8.2 End-to-End Version Traceability

**Requirement ID:** XTR-VTR

Material execution and evaluation must be able to identify the relevant versions of the technical elements that influenced behavior.

Where applicable, this includes:

- agent implementation;
- model configuration;
- Execution Graph;
- policy;
- connector;
- context strategy; and
- environment configuration.

### 8.3 Provenance Preservation

**Requirement ID:** XTR-PRV

Source and provenance information remain connected to organizational information as it is retrieved, transformed, summarized, indexed, or processed by AI.

AI-generated summaries or interpretations must not silently replace authoritative source identity.

### 8.4 Source Authority vs. Retrieval Relevance

**Requirement ID:** XTR-SAR

> **Retrieval relevance must not determine organizational authority.**

Full-Text Search, Vector Search, or AI-assisted retrieval may identify information as relevant.

Whether a source is authoritative is determined by the organizational source and System-of-Record model, not by search rank, semantic similarity, or model preference.

### 8.5 Knowledge Lifecycle Preservation

**Requirement ID:** XTR-KLP

> **Retrieved, transformed, summarized, or AI-generated information must not silently become durable Company Memory.**

Technical processing may create Evidence, Working Knowledge, summaries, indexes, or other derived representations.

Movement into durable organizational knowledge remains governed by the applicable knowledge lifecycle.

### 8.6 Environment Separation

**Requirement ID:** XTR-ENV

Production and Sandbox separation remains effective across:

- state;
- execution;
- identity;
- credentials;
- configuration;
- traces;
- external interactions; and
- generated information.

### 8.7 Safe Failure

**Requirement ID:** XTR-SAF

Failure and uncertainty may cause the organization to:

```text
wait
restrict
retry
gather evidence
escalate
or stop
```

but never silently expand authority.

### 8.8 External Consequence

**Requirement ID:** XTR-EXT

Technical rollback does not imply reversal of real-world organizational consequences.

Where external effects require correction, the implementation must support explicit recovery or compensating organizational action where possible.

### 8.9 Adversarial Content and Instruction Separation

**Requirement ID:** XTR-ACI

External messages, documents, retrieved material, media, tool results, model output, and derived representations remain data within their applicable source and trust boundaries.

The technical implementation must not allow instruction-like content alone to:

- create or modify Intent;
- grant identity, authority, credentials, information access, or tool permission;
- modify policy, configuration, evaluation criteria, or enforcement;
- select an unapproved tool, operation, resource, destination, or external recipient; or
- bypass an approval, decision, or Work Admission boundary.

Controls may include structured interfaces, instruction/data separation, schema validation, trust metadata, tool and operation allowlists, content isolation, and independent authorization at the point of consequential action. Model-level refusal or prompt wording alone is not a sufficient hard boundary.

### 8.10 Delegation and Authorization Composition

**Requirement ID:** XTR-DEL

Every material delegation between agents, services, workflows, or tools preserves the originating execution, Company Capability, delegating identity, delegated identity, permitted action, information scope, resource scope, environment, expiry, and onward-delegation boundary where applicable.

A delegated participant receives no broader authority than the originating execution. The union of separately permitted identities, tools, information access, or actions must not create an unauthorized consequential Outcome.

Authorization is re-evaluated at material action boundaries rather than inferred from possession of context, a credential, a prior tool result, or another agent's request.

### 8.11 Runtime, Tool, and Network Containment

**Requirement ID:** XTR-CON

Agent and model execution must remain contained according to organizational consequence. Applicable boundaries include:

- process and child-process creation;
- file-system paths and operations;
- network protocols, endpoints, and destinations;
- tools, connectors, commands, and parameters;
- credentials and secret retrieval;
- data stores and information classes;
- external side effects; and
- CPU, memory, storage, time, iteration, concurrency, and financial consumption.

Containment, cancellation, isolation, and revocation must remain enforceable outside the affected agent or model. Production placement does not imply unrestricted Production access.

### 8.12 Information Egress

**Requirement ID:** XTR-EGR

Information Classification applies to generated, transformed, summarized, aggregated, and outbound information as well as to source access.

Before material external transmission, the implementation verifies the initiating execution, Company Capability, information class, intended recipient or destination, permitted purpose, action, and authorization. Access to information and access to an outbound channel do not by themselves authorize their combination.

Logs, prompts, traces, model-provider requests, tool calls, error reports, and evaluation artifacts are also potential egress paths and remain subject to applicable information and secret boundaries.

### 8.13 Component and Supply-Chain Integrity

**Requirement ID:** XTR-SCI

Material models, prompts, skills, agent configurations, connectors, tools, policies, dependencies, containers, deployment artifacts, datasets, evaluators, and context strategies remain identifiable by version and verifiable according to consequence.

The implementation must support attributable source and approval, integrity verification, controlled activation, dependency and configuration change review, drift detection, restoration or rollback, and revocation or isolation of a compromised component where applicable.

Third-party or dynamically discovered components receive no implicit organizational trust, information access, credentials, or authority merely because they are technically compatible.

### 8.14 Security Observation and Incident Containment

**Requirement ID:** XTR-INC

Security-relevant execution remains observable across identity, delegation, authorization decisions, Working Context references, tool and connector use, external destinations, information egress, resource consumption, configuration, and resulting Outcomes.

Where consequence requires it, records must make unauthorized modification or deletion detectable. Monitoring must support timely restriction, credential rotation or revocation, workload isolation, execution termination, preservation of relevant Evidence, recovery, and accountable incident review.

Incident containment does not depend on the affected agent, model, connector, or runtime voluntarily stopping or accurately reporting its own behavior.

### 8.15 Agentic Security Evaluation

**Requirement ID:** XTR-ASE

The Automated Testing & Evaluation Framework must support the adversarial and boundary scenarios selected by Evaluation & Qualification for a Company Capability with material information, tool, code, financial, legal, or external-effect access.

The applicable scenario set covers, where relevant:

- direct and indirect instruction injection;
- manipulated messages, documents, retrieved content, media, and tool output;
- Working Context, Working Knowledge, Company State, or Company Memory poisoning attempts;
- compromised or substituted models, skills, tools, connectors, dependencies, or evaluators;
- identity misuse, delegation expansion, and unauthorized privilege composition;
- secret or classified-information disclosure and exfiltration;
- unauthorized code, process, file, network, tool, or external action;
- runaway loops, recursive delegation, resource exhaustion, and cost escalation;
- observability, attribution, and audit bypass or tampering; and
- revocation, containment, safe failure, and recovery after detected compromise.

Evaluation preserves the candidate, environment, policy, scenario, expected boundary, observed behavior, trace, and result. Passing functional tests alone is insufficient evidence for a consequential Production authorization.

### 8.16 Baseline Cybersecurity Integration

**Requirement ID:** XTR-BCI

Agentic security controls operate within an appropriate organizational cybersecurity baseline. According to information class, exposure, and consequence, the concrete implementation supports:

- authenticated and encrypted communications;
- encryption of sensitive stored information and backups;
- hardened configuration and minimization of exposed services;
- secure identity, credential, key, certificate, and secret lifecycles;
- vulnerability, dependency, update, and patch management;
- integrity and provenance review for deployed artifacts and dependencies;
- network, workload, endpoint, storage, and administrative-access protection;
- security monitoring, alerting, incident response, containment, recovery, and post-incident review; and
- periodic testing of restore, revocation, isolation, and other material security controls.

These Technical Requirements do not prescribe one security standard or product. Implementers remain responsible for applicable legal, regulatory, contractual, sector-specific, and risk-based security requirements beyond this minimum integration boundary.

---

## 9. Completeness and Traceability

The Technical Requirements use four complementary consistency checks.

### 9.1 Inventory ↔ Matrix

Every component listed in the Technical Component Inventory appears in the Reference Composition × Technology Matrix.

Every technology appearing in the Matrix is defined in the Inventory.

### 9.2 Matrix ↔ Implementation Map

Every technology relationship shown in the Matrix is explained by at least one corresponding Reference basis in the Implementation Map.

Conditional relationships remain conditional for the same explicit reason.

### 9.3 Implementation Map ↔ Technology Requirements

Every technical component referenced by the Implementation Map has a complete `Must Support` definition in the Technology Requirements.

### 9.4 Cross-Technology Requirements ↔ Concrete Implementation

Every applicable Cross-Technology Requirement must be mapped to one or more concrete components, interfaces, or enforcement boundaries and verified at the complete-system level.

Component coverage under Section 7 alone is not sufficient for conformance. A concrete implementation must also demonstrate every applicable Section 8 requirement by its stable `XTR-*` identifier.

This produces the end-to-end relationship:

```text
Reference Design
      ↓
Technical Component Inventory
      ↓
Composition × Technology Matrix
      ↓
Implementation Map
      ↓
Technology Requirements
      ↓
Applicable Cross-Technology Requirements
      ↓
Concrete Technology Selection and System-Level Verification
```

The resulting completeness rule is:

> **Every technically relevant Reference Design responsibility is covered by at least one Technical Requirement.**

And conversely:

> **Every Technical Requirement exists because it supports at least one Reference Design responsibility.**

And at realization time:

> **Every applicable Cross-Technology Requirement is assigned to and verified across concrete components or enforcement boundaries.**

---

## 10. Minimum Technical Realization

The Technical Requirements define required capabilities, not a minimum number of products.

A compact implementation may satisfy several requirements through the same concrete system.

This applies equally to a solo founder, a small organization, and a larger organization. Organizational scale does not determine how many products or independently deployed services are required. The concrete realization should remain proportionate to risk, consequence, operating conditions, and required assurance while preserving the specified technical boundaries and complete requirement coverage.

For example:

```text
One database system
may provide:

Relational Database Management
Full-Text Search
Vector Search
parts of Configuration Storage
```

A workflow system may provide:

```text
Durable Execution
Wait States
Timers
Retries
Signals / Events
Scheduling
```

An identity platform may provide:

```text
Human Identity
Workload Identity
Authentication
Authorization
```

An observability platform may provide:

```text
Logging
Metrics
Monitoring
Tracing
```

Likewise, Environment Isolation may be realized through different technical approaches depending on the organizational risk:

```text
logical isolation
container
virtual machine
separate cloud account
separate host
physical computer
```

The Technical Requirements do not prefer one of these approaches solely because it is more complex.

> **The minimum technical realization is not defined by the number of products used. It is defined by complete coverage of the Technical Requirements.**

A progressive implementation may establish this coverage capability by capability. Existing systems may continue to serve as Systems of Record or provide required technical functions during transition. They should be replaced or retired only after the successor realization preserves required data, provenance, authority, operational state, controls, and recoverability.

---

## Scope Status

The Technical Requirements provide a continuous implementation path:

```text
Architecture
      ↓
Reference Design
      ↓
Technical Requirements
      ↓
Concrete Technology Selection
```

The content is complete for the defined Reference Design scope. Future changes should be introduced only when a Reference Design change, implementation evidence, or a verified coverage gap requires them.
