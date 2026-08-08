# AI-First Company Reference Design

## Contents

1. [Purpose](#1-purpose)
2. [From Architecture to Reference](#2-from-architecture-to-reference)
3. [A Living Organization](#3-a-living-organization)
4. [Reference Principles](#4-reference-principles)
5. [Composition Overview](#5-composition-overview)
6. [The Operational Organization](#6-the-operational-organization)
7. [Executive Agent](#7-executive-agent)
8. [Company Brain](#8-company-brain)
9. [Capability Agent](#9-capability-agent)
10. [Execution Graph Layer](#10-execution-graph-layer)
11. [Company Interface Layer](#11-company-interface-layer)
12. [Sandbox Organization](#12-sandbox-organization)
13. [Production Organization](#13-production-organization)
14. [Evaluation & Qualification](#14-evaluation--qualification)
15. [Composition Relationships](#15-composition-relationships)
16. [Operational Flows](#16-operational-flows)
17. [Organizational Evolution](#17-organizational-evolution)
18. [Architecture Traceability](#18-architecture-traceability)
19. [Failure Modes](#19-failure-modes)
20. [Future Evolution](#20-future-evolution)

## 1. Purpose

> **The Reference Design translates the Architecture into an organizational design.**

The AI-First Company Reference Design presents one practical composition of the [AI-First Company Architecture](../01-architecture/ARCHITECTURE.md).

It shows how architectural concepts can work together as an operational organization while remaining independent of specific technologies, products, providers, and runtimes.

The Reference Design is intentionally opinionated. It presents one design, not the only possible design. Other designs may realize the same Architecture differently.

This document composes existing Architecture concepts and responsibilities; it does not add, redefine, or override organizational meaning established by the Architecture.

---

## 2. From Architecture to Reference

The AI-First Company is described through three layers:

> **The Architecture explains what an AI-First Company is.**  
> **The Reference Design translates the Architecture into an organizational design.**  
> **The [Technical Requirements](../03-technical-requirements/TECHNICAL_REQUIREMENTS.md) define the technology required to realize that design.**

```text
Architecture
     │
     ▼
Reference Design
     │
     ▼
Technical Requirements
```

Each layer answers a different question:

| Layer | Question |
|---|---|
| **Architecture** | What is an AI-First Company? |
| **Reference Design** | How can the Architecture be composed into an organizational design? |
| **Technical Requirements** | What technology is required to realize that design? |

The Reference Design therefore remains organizational rather than technological.

Concrete databases, models, runtimes, protocols, frameworks, and infrastructure belong to the Technical Requirements.

---

## 3. A Living Organization

An AI-First Company can be understood, for a moment, through the analogy of a living system.

A living system perceives its environment, maintains an understanding of its current condition, remembers relevant experience, coordinates capabilities, acts, observes the results, and learns.

An AI-First Company requires many of the same organizational functions:

```text
Perceive
   ↓
Understand
   ↓
Remember
   ↓
Coordinate
   ↓
Act
   ↓
Observe
   ↓
Learn
```

Information moves through the organization somewhat like signals through a nervous system: observations enter, context and intent move between organizational functions, actions reach the outside world, and outcomes return as new information.

The analogy is intentionally limited.

The Reference Design does not attempt to reproduce human biology or model an organization as a human being. It uses the comparison only to make one characteristic intuitive:

> **An AI-First Company is a connected organizational system whose parts continuously exchange information, context, intent, and outcomes.**

From this point forward, the Reference uses organizational rather than biological terminology.

---

## 4. Reference Principles

The Reference Design follows a small set of principles.

### Architecture Grounded

Every organizational responsibility in the Reference Design remains traceable to the Architecture.

### One Reference Design

The Reference presents one complete organizational design rather than a catalogue of alternatives.

### Proportional Realization

Completeness of organizational responsibility does not require a separate person, team, process, or system for every Composition. A solo founder or small organization may realize several Compositions through shared people, artifacts, and implementations while preserving their distinct responsibilities and boundaries.

### Capability before Implementation

Organizational capabilities remain stable while their performers and implementations may change.

### Human Leadership

AI may understand, prepare, coordinate, recommend, and execute within organizational boundaries. Human accountability and applicable decision authority remain intact.

### Shared Organizational Understanding

Humans and AI should operate from compatible organizational knowledge and current state rather than isolated conversations or private representations.

### Replaceability

Agents, models, providers, runtimes, interfaces, and other implementation choices remain replaceable without redefining the organization.

### Observable Execution

Organizational work remains understandable, attributable, reviewable, and recoverable where required.

### Evidence-Based Trust

Operational trust is earned through evidence and remains specific to the capability and conditions for which it was established.

### Deliberate Evolution

> **The organization may learn continuously while changing deliberately.**

---

## 5. Composition Overview

The Architecture is built from **Concepts**.

The Reference Design is built from **Compositions**.

A Composition combines Architecture Concepts into a distinct operational responsibility.

The Reference Design contains eight top-level Compositions:

```text
AI-FIRST COMPANY REFERENCE DESIGN

Core
├── Executive Agent
├── Company Brain
├── Capability Agent
└── Execution Graph Layer

Boundary
└── Company Interface Layer

Environments
├── Sandbox Organization
└── Production Organization

Assurance
└── Evaluation & Qualification
```

![The eight Reference Design Compositions grouped as Core, Boundary, Environments, and Assurance.](diagrams/reference-design-composition.png)

*The Compositions define distinct organizational responsibilities rather than required products, teams, or technical services.*

No Composition represents a particular technology.

The term **Agent** in a Composition describes a logical implementation responsibility. It does not require a single model, runtime, process, or agent instance and may be realized through a coordinated multi-agent system.

These Compositions define distinct organizational responsibilities, not a required organization chart or minimum number of implementations. One implementation may support several Compositions where it preserves their boundaries and satisfies their complete requirements.

The complete Reference Design may also be realized progressively. A new organization may begin with a compact realization, while an existing organization may establish Compositions capability by capability alongside current structures. This Reference Design defines the target composition rather than a transition procedure. Until an explicit, validated transition occurs, existing sources, authority, and accountability retain their established status and boundaries.

Together, they form the organizational design that the Technical Requirements will later make technically realizable.

---

## 6. The Operational Organization

The central relationships of the operational organization can be represented as:

```text
                   Human Leadership
                          ⇅
                   Executive Agent
                          ⇅
                    Company Brain
                          ⇅
               Execution Graph Layer
                          ⇅
                  Capability Agents
                          ⇅
               Company Interface Layer
                          ⇅
                    External World
```

This is not a hierarchy.

It is not a mandatory sequence of technical calls.

It represents the principal organizational relationships through which understanding, context, intent, execution, evidence, and outcomes move.

The Executive Agent provides human leadership with the primary operational interface to the organization.

The Company Brain provides shared organizational understanding.

Execution Graphs structure organizational work.

Capability Agents provide replaceable implementations of Company Capabilities.

The Company Interface Layer provides the controlled boundary to the External World.

Information and activity may travel in either direction, and not every activity involves every Composition.

---

### Organizational Evolution

The operational organization is complemented by a separate mechanism for evaluating change:

```text
                Candidate Change
                       │
                       ▼
             Sandbox Organization
                       │
                       ▼
          Evaluation & Qualification
                       │
                       ▼
             Accountable Adoption
                       │
                       ▼
            Production Organization

Production Organization
        ┈┈┈┈┈┈┈┈┈┈► Sandbox Organization
        optional controlled
        Production-derived information
```

Production exists to operate the organization.

Sandbox exists to evaluate change.

Evaluation & Qualification determines what the resulting evidence demonstrates.

The accountable organizational mechanisms determine whether a qualified change is adopted.

> **What moves from Sandbox to Production is a qualified change—not the Sandbox state.**

---

## 7. Executive Agent

> **The Executive Agent is the primary operational interface to an AI-First Company.**

The Executive Agent enables human leadership to understand, operate, and evolve the organization through one coherent organizational interface.

It provides a perspective across the organization as a whole without becoming the owner of organizational knowledge, state, capabilities, or authority.

Its responsibility consists of four closely related functions.

### 7.1 Organization Understanding

The Executive Agent uses the Company Brain to establish an operational understanding of the organization.

It interprets relevant Company State, Company Memory, ongoing work, pending decisions, available capabilities, material events, uncertainty, and matters requiring attention.

Its central question is not:

> *What information exists?*

It is:

> **What does the current organizational situation mean?**

Organization Understanding is interpretive. The underlying organizational information remains owned and governed by its respective Architecture Concepts and authoritative sources.

### 7.2 Context Builder

The Context Builder obtains the Working Context required for the current activity by orchestrating governed Knowledge Access through the Company Brain.

It is the Executive Agent's use of the Architecture's Knowledge Access capability, not a separate context-preparation capability or competing information path. Knowledge Access remains responsible for selecting, retrieving, synthesizing, and delivering the smallest sufficient Working Context.

Its objective is not to maximize available context.

It assembles the:

> **smallest sufficient organizational context.**

A customer activity, for example, may require recent communication, contractual commitments, relevant decisions, current state, unresolved work, and applicable policies without requiring the customer's entire history.

Material uncertainty, conflicting authoritative information, and missing information remain visible rather than being resolved implicitly.

The Context Builder therefore turns broad organizational understanding into bounded, purpose-specific Working Context.

### 7.3 Capability Coordination

The Executive Agent coordinates organizational capabilities rather than attempting to perform all organizational work itself.

Its primary question is:

> **Which Company Capability is required?**

The current performer of that capability is a separate and replaceable concern.

Capability Coordination identifies and relates the Company Capabilities required for the organizational objective. It does not select a performer merely from technical availability. When an Execution Graph is used, the Execution Graph Layer resolves each capability step to a performer that is qualified and authorized for that step. Work that does not require an Execution Graph remains subject to the equivalent Controlled Execution, qualification, and authorization boundaries.

The Executive Agent may coordinate one or several capabilities depending on the organizational objective. Their execution remains subject to the authority, information, and execution boundaries defined by the Architecture.

### 7.4 Organizational Interaction

The Executive Agent presents the organization through interaction modes appropriate to the activity and participant.

These may include:

- conversation;
- dashboards;
- notifications;
- reports;
- visual exploration; and
- voice or other interaction modes.

No individual interaction mode defines the Executive Agent.

A routine organizational state may require only a concise status view. A consequential decision may require an interactive explanation of evidence, alternatives, uncertainty, and expected consequences.

Interaction follows organizational need rather than forcing every activity into a conversation.

### 7.5 Boundary

The Executive Agent is the **primary**, not exclusive, operational interface.

Humans may interact directly with Capability Agents or other authorized organizational views where appropriate.

Its unique responsibility is to make the organization as a whole operationally accessible to human leadership.

---

## 8. Company Brain

> **The Company Brain is the shared organizational working representation of an AI-First Company.**

The Company Brain enables humans and AI to work from a shared organizational understanding.

It brings relevant organizational representations together while preserving their distinct meaning, authority, lifecycle, and source.

These may include:

- Company Memory;
- Company State;
- Working Context;
- organizational relationships;
- capability information;
- decisions and mandates; and
- governed Knowledge Access.

> **The Company Brain unifies access to organizational understanding while preserving the distinct meaning and authority of its underlying Architecture Concepts.**

### 8.1 Shared Organizational Understanding

The purpose of the Company Brain is not shared storage.

It is **shared organizational understanding**.

Humans and Capability Agents do not require identical interfaces or representations. They do, however, need to operate from compatible organizational facts, decisions, state, relationships, and boundaries.

This allows different participants to interact with the same organization without creating parallel organizational realities.

### 8.2 Memory, State, and Context

Three distinctions are particularly important:

**Company Memory** preserves what the company has intentionally decided to remember.

**Company State** represents what is currently true.

**Working Context** contains what is required for a particular activity.

The Company Brain makes these representations usable together without treating them as interchangeable.

### 8.3 Sources and Authority

The Company Brain does not need to become the authoritative source for every piece of organizational information.

Different information classes may remain authoritative in different Systems of Record.

The Company Brain can make relevant information available for organizational understanding while preserving its source, authority, and provenance.

Known source and provenance do not by themselves establish that information is reliable or benign. Material integrity, trust, and uncertainty conditions remain visible, and instruction-like content within organizational information remains information rather than becoming Intent, authority, or policy.

This distinction allows the organization to gain a unified working representation without creating a second competing operational truth.

### 8.4 Curation rather than Accumulation

The Company Brain is not an unlimited accumulation of every message, document, transcript, observation, and execution trace.

Raw information may remain in appropriate Systems of Record, evidence stores, archives, or evaluation datasets.

Only information that passes the applicable knowledge lifecycle becomes durable organizational knowledge.

This allows extensive source material to remain available without forcing every retained item into active Company Memory.

> **The Company Brain exists to create shared organizational understanding, not shared storage.**

---

## 9. Capability Agent

> **A Capability Agent is a replaceable agent-based implementation of one or more Company Capabilities.**

A Capability Agent performs organizational work within defined Company Capabilities and the organizational boundaries applicable to that work.

The Company Capability remains stable while its current operational implementation may evolve.

### 9.1 Capability Alignment

A Capability Agent derives its organizational responsibility from the Company Capability it implements, not from everything its underlying model or runtime is technically capable of doing.

The relevant question is:

> **Which Company Capability is this agent implementing?**

not:

> *What can this agent technically do?*

This keeps organizational responsibility stable while AI capabilities continue to change.

### 9.2 Working Context

A Capability Agent receives the Working Context required for its current activity.

It does not require unrestricted access to the Company Brain or every information source available to the organization.

Information access remains purpose-specific and subject to the applicable organizational boundaries.

The Capability Agent treats retrieved content, messages, documents, and tool results as information within Working Context. Content contained in those sources cannot grant additional tools, information access, delegation, or authority.

### 9.3 Performer Replaceability

A Company Capability is not inherently tied to a particular AI agent.

Depending on the capability and context, organizational work may be performed by:

- a Capability Agent;
- a human;
- another software system; or
- a combination of participants.

This allows the organizational capability to survive changes in people, agents, models, runtimes, and technology.

> **The capability belongs to the organization. Its current performer does not.**

### 9.4 Qualification

A replacement Capability Agent does not automatically inherit the trust established by its predecessor.

Changes to the underlying model, instructions, runtime, tools, context strategy, or other material implementation characteristics may change operational behavior.

A new implementation can therefore be evaluated against the same Company Capability and relevant organizational scenarios before receiving equivalent operational scope.

> **Company Capabilities remain stable while their operational implementations can evolve.**

### 9.5 Delegated and Adversarial Operation

A Capability Agent may be implemented through multiple coordinated agents or other delegated technical participants. Each delegation remains attributable to the originating execution and must preserve its Company Capability, Working Context, information, action, resource, and authorization boundaries.

Combining the individually permitted access or actions of several participants must not create a broader consequential capability or Outcome than the originating execution is authorized to produce. Onward delegation requires an explicit boundary and cannot expand authority.

Capability Agents may encounter manipulated inputs, compromised dependencies, adversarial instructions, or misleading tool results. Their implementation must therefore rely on externally enforceable organizational boundaries rather than model compliance alone.

---

## 10. Execution Graph Layer

> **The Execution Graph Layer translates Intent into reproducible, observable, and controlled execution.**

Execution Graphs make organizational work explicit.

They describe how an objective progresses through capabilities, decisions, waiting states, interactions, and outcomes without permanently binding the organizational process to individual performers or technologies.

### 10.1 Organizational Execution

An Execution Graph may contain:

- Company Capabilities;
- human activities;
- Capability Agent activities;
- decision points;
- approval gates;
- waiting states;
- external interactions;
- parallel work;
- recovery paths; and
- outcomes.

It describes the organizational execution path, not the private reasoning process of an individual participant.

### 10.2 Capability before Performer

Execution Graphs depend primarily on Company Capabilities rather than named performers.

```text
Intent
        ↓
Execution Graph
        ↓
Required Company Capability
        ↓
Qualified and Authorized Performer
        ↓
Outcome
```

The performer may be a Capability Agent, a human, another system, or an appropriate combination.

The Executive Agent may identify the required Company Capability. The Execution Graph Layer resolves the performer for a graph step from the implementations that remain qualified and authorized within the applicable context. This keeps capability coordination separate from performer resolution.

This allows the graph to remain stable when the implementation of a capability changes.

### 10.3 Waiting and Decisions

Not all organizational work should execute continuously from beginning to end.

An Execution Graph may intentionally wait for:

- human approval;
- additional evidence;
- an external response;
- completion of another activity;
- resolution of uncertainty;
- fulfillment of a precondition; or
- a defined point in time.

Waiting is therefore a valid organizational state rather than an execution failure.

The graph represents where a decision is required. It does not create the authority to make that decision.

### 10.4 Observable Execution

Execution preserves sufficient information to understand how an organizational outcome was reached.

Depending on the activity, this may include:

- originating intent;
- graph and graph version;
- participating capabilities and performers;
- Working Context references;
- decisions and approvals;
- external interactions;
- significant state transitions;
- failures and recovery actions; and
- resulting outcomes.

This makes organizational work reviewable and provides evidence for later evaluation.

### 10.5 Reproducibility

Reproducibility does not require every execution to produce an identical result.

Humans, AI systems, external systems, and changing organizational conditions may introduce legitimate variation.

Instead, reproducibility means that the organization can reconstruct the relevant execution structure, conditions, context, participants, decisions, and resulting outcome.

### 10.6 Evolution

Execution Graphs may evolve as organizational processes improve.

Material changes can be exercised in the Sandbox Organization and evaluated before adoption in Production.

The organizational execution model therefore remains stable enough to understand while remaining capable of deliberate evolution.

> **Execution Graphs preserve organizational execution while the performers and technologies beneath them remain replaceable.**

---

## 11. Company Interface Layer

> **The Company Interface Layer is the controlled organizational boundary between an AI-First Company and the External World.**

The Company Interface Layer enables the organization to receive information from and perform authorized actions in external systems without coupling organizational capabilities directly to individual providers, products, or interfaces.

It separates **what the organization intends to do** from **how an external system makes that interaction technically possible**.

### 11.1 Inbound Information

External information enters the organization through controlled interfaces.

```text
External World
      ↓
Company Interface Layer
      ↓
Attributable Input
      ↓
Organizational Processing
```

Incoming information should preserve sufficient source, identity, timestamp, representation, metadata, and provenance for its intended organizational use.

Arrival alone does not make external information accepted organizational knowledge or Company Memory.

External content is treated as potentially incorrect, manipulated, or adversarial according to its source and consequence. Instructions embedded in messages, documents, retrieved content, media, or tool results remain inbound information; they do not create Intent, authorization, policy, or permission to invoke another tool.

### 11.2 Outbound Action

The same boundary applies to actions leaving the organization.

```text
Intent
      ↓
Controlled Execution
      ↓
Company Interface Layer
      ↓
External System
```

The Company Interface Layer enables an authorized external action.

It does not create the authority for that action.

Before a material external effect, the applicable identity, Company Capability, action, destination, Information Classification, and authorization boundary remain technically verifiable. Separately permitted access and actions must not be combined into an unauthorized external Outcome.

### 11.3 Connectors

Connectors provide replaceable technical relationships with individual external systems.

A connector may support reading, writing, querying, events, commands, synchronization, or combinations of these functions.

Each connector exposes only the operations, resources, destinations, and data flows required for its authorized organizational use. Possession of a broad provider credential must not turn every technically available provider operation into an available organizational action.

The organizational capability remains independent of the connector and provider through which it currently operates.

For example:

```text
Customer Communication
        ↓
Company Interface Layer
        ↓
Email Connector
        ↓
Email Provider
```

Changing the connector or provider should not redefine the Customer Communication Capability.

### 11.4 Systems of Record

The Company Interface Layer preserves authoritative source boundaries.

Where a system acts as the System of Record for a particular information class, the Company Brain may make relevant information from that system organizationally usable without becoming a competing authoritative source.

This allows unified organizational understanding without creating duplicate organizational truth.

### 11.5 Identity and Provenance

Material external interaction remains attributable.

Where relevant, the organization should be able to relate an interaction to:

- the initiating participant;
- the Company Capability;
- the relevant execution;
- the technical identity used;
- any material delegation chain;
- the external system; and
- the resulting outcome.

Shared technical infrastructure must not erase organizational accountability.

### 11.6 Failure

External systems may become unavailable, delayed, inconsistent, rate-limited, or uncertain.

They may also return manipulated content or behave as a compromised dependency. Their output remains subject to the same source, integrity, authorization, and execution boundaries as other inbound information.

The Company Interface Layer exposes these conditions to organizational execution rather than hiding them.

The appropriate organizational response—wait, retry, use an alternative, escalate, or stop—belongs to controlled execution.

> **External systems are replaceable. The organizational boundary through which the company interacts with them remains controlled.**

---

## 12. Sandbox Organization

> **The Sandbox Organization is an isolated realization of the AI-First Company used to evaluate organizational change without affecting Production.**

The Sandbox provides an environment in which candidate changes can be exercised under controlled conditions before they are permitted to affect operational reality.

Its purpose extends beyond software testing.

The Sandbox can evaluate changes to agents, models, execution, context strategies, interfaces, policies, and other material organizational behavior.

### 12.1 Organizational Environment

The Sandbox reproduces the parts of the AI-First Company necessary for the evaluation being performed.

Depending on scope, this may include:

- Company Brain representations;
- Capability Agents;
- Execution Graphs;
- Company Interfaces;
- organizational state;
- applicable policies and authority boundaries;
- external-system simulations; and
- relevant technical runtime behavior.

Not every evaluation requires a complete replica of Production.

It requires sufficient organizational realism for the question being evaluated.

### 12.2 Isolation

Sandbox activity remains distinguishable from Production activity.

This includes:

- organizational state;
- Company Memory;
- credentials;
- external actions;
- execution traces;
- decisions;
- generated information; and
- evaluation outcomes.

Experimental or synthetic information must not silently become Production state or knowledge.

### 12.3 Evaluation Data

The Sandbox may operate with:

- synthetic data;
- predefined scenarios;
- historical cases;
- replay data;
- controlled Production snapshots;
- anonymized Production-derived data;
- pseudonymized Production-derived data; or
- appropriate combinations.

The origin and status of evaluation information remain explicit.

Where Production-derived information is required, its transfer is controlled and purpose-specific.

### 12.4 Candidate Change

The Sandbox may evaluate changes such as:

- a Capability Agent;
- an AI model;
- agent instructions;
- an Execution Graph;
- a connector;
- a context strategy;
- an organizational policy;
- a runtime; or
- combinations of these elements.

The Sandbox exercises the candidate.

It does not determine whether the candidate is suitable for Production.

That responsibility belongs to Evaluation & Qualification.

### 12.5 Replay

Where sufficient historical information exists, previous organizational situations may be replayed.

Replay asks:

> **How would this candidate have handled the same organizational situation?**

This enables meaningful comparison between current and candidate implementations without requiring Production to become the experiment.

### 12.6 Production Adoption

Sandbox state is not promoted wholesale into Production.

> **What moves from Sandbox to Production is a qualified change—not the Sandbox state.**

Synthetic information, experimental Company State, Sandbox Company Memory, and unrelated Sandbox activity remain outside Production.

> **The Sandbox allows the organization to change without requiring Production to become the experiment.**

---

## 13. Production Organization

> **The Production Organization is the operational realization of the AI-First Company in which authorized organizational work produces real-world outcomes.**

Production represents the organization's current operational reality.

Its activities may affect customers, people, systems, products, finances, commitments, and the External World.

### 13.1 Operational Reality

Production contains the current forms of:

- Company State;
- organizational work;
- Capability implementations;
- Execution Graphs;
- applicable decisions and mandates;
- authorized external interactions; and
- operational outcomes.

The defining difference between Production and Sandbox is therefore not necessarily technology.

It is **organizational consequence**.

### 13.2 Production Company Brain

Production maintains its own operational Company Brain.

Sandbox does not share that Company Brain as a common mutable organizational state.

Selected information may be transferred under controlled conditions, but Production and Sandbox remain distinct organizational realities.

### 13.3 Authorized Execution

Deployment into Production does not grant authority.

Neither a human nor a Capability Agent gains additional organizational permission merely because it is technically able to perform an action in the Production environment.

```text
Technical ability
        ≠
Organizational authority
```

Production preserves the authority, information, and execution boundaries defined by the Architecture.

Production identity, network, process, file, tool, credential, and resource access remain no broader than required for the authorized capability implementation. The combined privileges of coordinated agents or services must not silently exceed the originating authorization boundary.

### 13.4 Continuity

Availability and recovery requirements follow organizational need.

Different Company Capabilities may therefore have different continuity requirements.

An AI-First Company does not require every agent, model, or technical component to operate continuously simply because it exists in Production.

Continuity also applies when the primary accountable individual or organizational role becomes temporarily or permanently unavailable. The organization preserves sufficient organizational knowledge, mandate state, access state, and operational context to determine deliberately whether work may continue, continue with reduced scope, wait, pause, escalate, or transfer to another accountable participant.

Continuity of access does not create authority. Technical access and organizational authority remain distinct, and responsibility, Decision Mandates, Standing Authorization, qualification, and Operational Confidence do not transfer automatically.

Founder Continuity is organizational continuity rather than a technical disaster recovery specification.

### 13.5 Failure

Production failures may involve Capability Agents, Execution Graphs, external systems, models, identities, infrastructure, state, or other dependencies.

Failures remain observable and lead to defined recovery, fallback, waiting, escalation, restriction, or safe termination according to organizational consequence.

Failure does not justify silently bypassing authority or information boundaries.

### 13.6 Change

Production changes through deliberate organizational evolution.

Material uncertainty is evaluated outside Production where appropriate before an accepted change affects operational reality.

> **Production operates. Sandbox evaluates change.**

---

## 14. Evaluation & Qualification

> **Evaluation & Qualification transforms organizational evidence into operational trust.**

Evaluation & Qualification determines whether a candidate has demonstrated sufficient performance and reliability for a defined organizational scope.

It provides the assurance mechanism between candidate change and accountable Production adoption.

**Qualification** is a Reference Design responsibility derived from the Architecture's Initial Qualification, Requalification and Replay, Evidence, Capability History, and Operational Confidence. It is not an additional Architecture Concept and does not grant authority.

### 14.1 Evaluation

Evaluation examines candidate behavior under defined organizational conditions.

Candidates may include:

- Capability Agents;
- models;
- Execution Graphs;
- context strategies;
- connectors;
- policies;
- technical components; or
- combinations of these elements.

Evaluation may use synthetic scenarios, historical cases, replay, Production-derived cases, failure scenarios, adversarial scenarios, and purpose-designed capability tests.

Where relevant to the candidate and consequence, adversarial evaluation includes manipulated external content, instruction injection, misleading tool output, knowledge or context poisoning, compromised connectors or dependencies, unauthorized privilege composition, delegation expansion, information exfiltration, resource exhaustion, observability bypass, and attempted Production-boundary escape.

The purpose is not merely to produce a score.

It is to create evidence about operational suitability.

### 14.2 Capability-Based Evaluation

Evaluation is anchored to Company Capabilities.

The relevant question is not:

> *How good is this model?*

It is:

> **How well does this candidate perform this Company Capability under these organizational conditions?**

A candidate may therefore be qualified for one Company Capability while remaining unqualified for another.

### 14.3 Evaluation Evidence

Relevant evidence may include:

- candidate identity and version;
- Company Capability;
- scenario or dataset;
- Working Context;
- Execution Graph;
- expected outcome;
- observed outcome;
- errors and uncertainty;
- policy or boundary violations;
- human assessment; and
- execution traces.

Evaluation conclusions remain reviewable through the evidence supporting them.

### 14.4 Qualification

Qualification turns sufficient evaluation evidence into an explicit statement about operational suitability.

It answers:

> **For what organizational work, under what conditions, and within what boundaries has this candidate demonstrated sufficient capability?**

Qualification may therefore be limited by:

- Company Capability;
- information class;
- risk;
- operational context;
- required human oversight;
- permitted actions;
- Execution Graph; or
- other relevant conditions.

Qualification is scoped rather than universal.

### 14.5 Operational Confidence

Operational Confidence represents evidence-based confidence in an implementation performing a defined organizational responsibility under specified conditions.

It can increase through successful operation and additional evidence.

It can decrease through:

- failures;
- changed conditions;
- new evidence;
- regression;
- implementation changes;
- dependency changes; or
- changed organizational risk.

Operational Confidence is contextual and revisable.

### 14.6 Replacement

A replacement implementation does not automatically inherit the qualification or Operational Confidence of its predecessor.

Existing capability definitions, scenarios, known failure cases, and operational evidence provide a reusable basis for evaluating the candidate.

This allows technological replacement without discarding organizational learning.

### 14.7 Qualification and Authority

Three concepts remain distinct:

```text
Technical Capability
        ≠
Qualification
        ≠
Authorization
```

**Technical Capability** describes what a system can potentially do.

**Qualification** describes what it has demonstrated sufficient capability to do under defined conditions.

**Authorization** describes what it is permitted to do.

Increasing technical capability therefore does not silently create increasing organizational authority.

Authorization may apply to an individual action or may be granted in advance as bounded Standing Authorization for recurring actions. Standing Authorization originates in accountable organizational governance, remains attributable, and applies only to the approved capability, scope, conditions, and explicit boundaries.

Standing Authorization is reviewable and revocable and may be narrowed when conditions change. Qualification and Operational Confidence may inform it but do not create it, and a materially changed or replacement implementation does not inherit it automatically.

### 14.8 Production Evidence

Production can generate valuable evidence through successful outcomes, failures, corrections, escalations, unexpected situations, and changing operational conditions.

That evidence may improve future evaluation.

Production does not thereby become the experimental environment.

Operational experience becomes input to future controlled evaluation.

### 14.9 Human Judgment

Not every organizational outcome can be evaluated adequately through automated metrics.

Human judgment may remain necessary where evaluation involves ambiguity, strategy, communication quality, ethical considerations, legal interpretation, novel situations, or other context-sensitive consequences.

Automation can support qualification without eliminating accountability.

> **Operational trust is earned through evidence, not assumed from technical capability.**

---

## 15. Composition Relationships

The eight Compositions form one connected organizational design.

Their relationships enable organizational understanding, context, intent, execution, evidence, and outcomes to move through the company without collapsing distinct responsibilities into one system.

```text
                   Human Leadership
                          ⇅
                   Executive Agent
                          ⇅
                    Company Brain
                          ⇅
               Execution Graph Layer
                          ⇅
                  Capability Agents
                          ⇅
               Company Interface Layer
                          ⇅
                    External World
```

The diagram represents principal organizational relationships, not hierarchy or mandatory technical call paths.

All relationships remain subject to applicable Information Classification, authorization, Decision Mandates, and other architectural boundaries.

### 15.1 Primary Relationships

| Relationship | Purpose |
|---|---|
| **Executive Agent ⇄ Company Brain** | Makes shared organizational understanding operationally accessible to human leadership. |
| **Company Brain ⇄ Execution Graph Layer** | Provides relevant organizational context to execution and receives resulting state, evidence, and knowledge inputs. |
| **Execution Graph Layer ⇄ Capability Agents** | Connects organizational execution to qualified and authorized performers of required Company Capabilities. |
| **Capability Agents ⇄ Company Interface Layer** | Enables controlled interaction between organizational capabilities and external systems. |
| **Company Interface Layer ⇄ External World** | Provides the controlled boundary for inbound information and authorized external action. |
| **Sandbox ⇄ Evaluation & Qualification** | Exercises candidate change and turns resulting behavior into evaluation evidence. |
| **Evaluation & Qualification → Production** | Provides qualification results for accountable adoption decisions. |
| **Production ⇢ Sandbox** | Optionally provides controlled Production-derived information for realistic evaluation. |

The Production-to-Sandbox relationship is optional. A Sandbox may operate entirely from synthetic, historical, or purpose-built evaluation information.

### 15.2 Human Interaction

The Executive Agent is the primary operational interface for human leadership, not the exclusive human interface to the organization.

Humans may interact directly with Capability Agents, specialist interfaces, dashboards, reports, or other authorized organizational views where appropriate.

Different interaction paths do not create different organizational realities.

They remain grounded in the same organizational state, knowledge, capabilities, authority, and information boundaries.

### 15.3 Organizational Views

Dashboards, conversations, reports, notifications, explorers, and similar representations are interaction modes rather than independent top-level Compositions.

They present the relevant part of the organization in a form appropriate to the participant and activity.

This allows interaction to follow organizational need rather than forcing every activity through one universal interface.

### 15.4 Relationship Principle

A relationship does not transfer responsibility or authority between Compositions.

A Capability Agent receiving information from the Company Brain does not own that knowledge.

An Execution Graph containing a decision point does not gain authority to make that decision.

A Company Interface possessing technical credentials does not gain permission to use them arbitrarily.

An Executive Agent presenting a recommendation does not become the accountable decision-maker.

> **Composition relationships enable organizational cooperation without collapsing organizational boundaries.**

---

## 16. Operational Flows

The Production Organization is the operating AI-First Company.

Its Compositions work together to perceive relevant events, establish organizational understanding, coordinate work, perform Company Capabilities, interact with the External World, and incorporate resulting outcomes into the organization's current state and knowledge lifecycle.

There is no requirement that every activity begin with the Executive Agent.

The organization is **connected rather than centrally routed**.

Where Evidence supports an organizational proposal, prioritization follows this sequence:

```text
Evidence-supported proposal
        ↓
Proposal Evaluation
        ↓
Impact + Urgency evaluated independently
        ↓
Response Class
        ↓
Applicable Decision Mandate
```

Impact and Urgency are separate dimensions. Response Class prioritizes organizational attention; it does not create authority. Proposal Evaluation does not authorize execution, and accountable decision-making remains with the applicable Decision Mandate.

### 16.1 External Event

An external event may initiate organizational evaluation and, where applicable, Intent Generation. It does not directly authorize execution:

```text
External World
      ↓
Company Interface Layer
      ↓
Attributable Input
      ↓
Organizational Event / Evidence
      ↓
Evaluation / Intent Generation where applicable
      ↓
Intent
      ↓
Applicable authorization confirmed
      ↓
Work Admission
      ↓
Execution Graph as Controlled Execution
      ↓
Required Company Capability
      ↓
Qualified and Authorized Performer
      ↓
Outcome
```

The Working Context for that activity is assembled from the organizational information required to perform it.

The objective is not to expose everything the company knows.

It is to provide the **smallest sufficient organizational context**.

### 16.2 Human Intent

Human leadership may initiate work through the Executive Agent:

```text
Human Leadership
      ↓
Executive Agent
      ↓
Organization Understanding
      ↓
Context Builder through Knowledge Access
      ↓
Working Context
      ↓
Intent
      ↓
Applicable authorization confirmed
      ↓
Work Admission
      ↓
Execution Graph as Controlled Execution
      ↓
Required Company Capability
      ↓
Qualified and Authorized Performer
      ↓
Outcome
```

The Executive Agent translates a human request into explicit Intent without bypassing the authorization, admission, execution, and performer boundaries that apply elsewhere.

### 16.3 Proactive Activity

Organizational activity does not require a new human request.

Work may also begin through:

- schedules;
- external events;
- state changes;
- monitored conditions;
- recurring organizational processes; or
- other defined triggers.

Proactive activity may include Continuous Environmental Intelligence performed through existing organizational capabilities and the controlled external boundary. It observes relevant external change continuously and proportionately, uses the Company Interface Layer where external information enters, preserves source and attribution, and produces organizational Evidence when an observation is sufficiently significant.

Continuous Environmental Intelligence does not decide, assign authority, execute, or automatically create Intent or priority. Observation, Proposal Evaluation, accountable decision, Intent, and Controlled Execution remain distinct.

Proactive operation changes how work begins, not the authority under which it is performed.

### 16.4 Outcomes

An outcome may affect operational reality, organizational knowledge, or both.

```text
Execution Outcome
      │
      ├──→ Company State
      │
      ├──→ Evidence
      │
      ├──→ Working Knowledge
      │
      └──→ possible validation
                    ↓
              Company Artifact
                    ↓
               Company Memory
```

These paths remain distinct.

An operational outcome may change Company State immediately without becoming Company Memory.

Likewise, new information may remain Evidence without becoming accepted organizational knowledge.

### 16.5 Operational Principle

The operational organization does not behave as one large autonomous agent.

It coordinates distinct organizational responsibilities whose current performers and technologies can change while the organizational design remains stable.

> **The organization coordinates capabilities, not personalities or models.**

---

## 17. Organizational Evolution

The Production Organization operates the company.

Organizational Evolution provides the controlled path through which that organization changes.

It is not a second permanent operational loop.

Change begins when evidence, experience, external conditions, human intent, or technological development creates a meaningful candidate for improvement.

### 17.1 Candidate Change

A candidate change may involve:

- a Capability Agent;
- an AI model;
- an Execution Graph;
- a context strategy;
- a connector;
- a policy;
- a technical component;
- an organizational process; or
- a combination of these elements.

Detection of an opportunity does not automatically change the organization.

It creates a candidate for evaluation.

### 17.2 Evaluation Path

```text
Candidate Change
      ↓
Sandbox Organization
      ↓
Evaluation Evidence
      ↓
Evaluation & Qualification
      ↓
Qualification Result
      ↓
Accountable Adoption Decision
      ↓
Production Organization
```

![A candidate change is evaluated in Sandbox, qualified through Evidence, and reaches Production only after an accountable adoption decision.](diagrams/organizational-evolution.png)

*What moves to Production is a qualified change—not the Sandbox state.*

The Sandbox provides the environment in which the candidate is exercised.

Evaluation & Qualification determines what the resulting evidence demonstrates.

Applicable organizational authority determines whether the qualified change is adopted.

### 17.3 Realistic Sandbox Conditions

The Sandbox may combine different forms of evaluation information:

```text
                Synthetic Data
                      │
                      ▼
Historical ───► Sandbox Organization ◄┈┈┈ Production
 / Replay                                optional controlled
   Data                                  derived information
```

Production-derived information is optional.

Where used, it may require selection, classification, minimization, anonymization, pseudonymization, isolation, and provenance.

The goal is sufficient realism for evaluation—not unrestricted replication of Production.

### 17.4 Qualified Change

Successful evaluation does not promote the Sandbox into Production.

> **What moves from Sandbox to Production is a qualified change—not the Sandbox state.**

Qualification may still result in:

- required human approval;
- narrower authorization;
- limited rollout;
- additional observation;
- increased supervision; or
- other controls appropriate to the operational consequence.

Qualification demonstrates capability for a defined scope.

It does not create authority.

### 17.5 Continuous Learning, Deliberate Change

The organization may continuously collect operational evidence and observe relevant external conditions without continuously modifying itself.

Learning and changing are distinct organizational activities.

> **The organization may learn continuously while changing deliberately.**

---

## 18. Architecture Traceability

The Reference Design is derived from the AI-First Company Architecture.

The relationship is many-to-many.

A Reference Composition may combine several Architecture Concepts, while one Architecture Concept may influence several Compositions.

Traceability therefore represents **composition and influence**, not ownership.

| Reference Composition | Principal Architecture Concept Nodes |
|---|---|
| **Executive Agent** | Company State, Company Memory, Working Context, Knowledge Access, Company Capability, Decision Mandate, Intent, Role |
| **Company Brain** | Company Memory, Company State, Working Context, Knowledge Access, Company Artifact, Decision Record, System of Record, Evidence, Validated Knowledge |
| **Capability Agent** | Company Capability, Working Context, Information Classification, Decision Mandate, Work Admission, Controlled Execution, Operational Confidence, Standing Authorization |
| **Execution Graph Layer** | Intent, Company Capability, Work Admission, Controlled Execution, Decision Mandate, Organizational Event, Evidence, Outcome |
| **Company Interface Layer** | External World, Evidence, Information Classification, System of Record, Data Custody, Organizational Event, Controlled Execution, Outcome, Access Boundary |
| **Sandbox Organization** | Trust Domain, Company Execution Environment, Company State, Evidence, Operational Confidence, Capability History, Information Classification, Controlled Execution |
| **Production Organization** | AI-First Company, Company State, Company Memory, Decision Mandate, Company Capability, System of Record, Founder Continuity, Recoverability, Standing Authorization |
| **Evaluation & Qualification** | Evidence, Company Capability, Operational Confidence, Confidence Profile, Capability History, Capability Improvement, Standing Authorization, Validated Knowledge |

The mapping is explanatory rather than exhaustive.

### 18.1 Cross-Cutting Responsibilities and Properties

Some Architecture responsibilities and properties intentionally apply across much or all of the Reference Design. They remain traceable to the Architecture but are not represented as additional Concept Nodes by this section.

These include:

- Human Accountability;
- Decision Mandates;
- Information Classification;
- attribution;
- authority boundaries;
- reviewability;
- Knowledge Independence;
- Systems of Record;
- security and privacy;
- recoverability;
- replaceability; and
- controlled evolution.

Assigning these Concepts exclusively to one Composition would incorrectly narrow their scope.

### 18.2 Traceability Rule

A new Reference responsibility must remain explainable through the Architecture.

If it cannot be, it may:

1. belong to the Technical Requirements rather than the Reference Design;
2. be unnecessary or misplaced; or
3. reveal a genuine gap requiring separate Architecture review.

> **Every Reference responsibility remains traceable to the Architecture.**

---

## 19. Failure Modes

The Reference Design must remain useful when information, participants, execution, environments, external systems, or evaluation fail.

The objective is not to eliminate failure.

It is to make failure **observable, bounded, recoverable, and accountable**.

### 19.1 Understanding Failure

Organizational understanding may become incomplete or incorrect through:

- stale state;
- missing information;
- contradictory sources;
- incorrect summaries;
- manipulated sources, retrieved content, or tool results;
- instruction-like content being mistaken for Intent or authority;
- missing relationships; or
- unresolved uncertainty.

The organization must not hide material uncertainty merely to produce a coherent answer.

### 19.2 Execution Failure

A Capability Agent or Execution Graph may fail, become unavailable, regress, reach an unresolved state, or encounter conditions outside its qualification.

Depending on the activity, the organization may:

- wait;
- retry;
- restrict;
- substitute another qualified performer;
- gather additional evidence;
- escalate;
- request human intervention; or
- terminate safely.

Failure never expands authority.

### 19.3 Boundary Failure

Failures may occur even when individual components behave correctly:

- information reaches an unauthorized participant;
- the wrong System of Record is used;
- external identity becomes ambiguous;
- credentials exceed required scope;
- delegated or combined privileges exceed the originating authorization;
- classified information leaves through an unauthorized output or destination;
- a manipulated connector, tool, or dependency steers otherwise valid execution;
- an external action has an uncertain result;
- Sandbox activity affects Production; or
- technical access is mistaken for organizational authority.

These are failures of organizational boundaries rather than necessarily failures of individual components.

### 19.4 Environment Failure

Sandbox may fail because its evaluation conditions are unrealistic or unrepresentative.

Production may fail because capabilities, infrastructure, models, identities, state, or external dependencies become unavailable.

Recovery requirements follow organizational consequence rather than assuming identical availability requirements for every capability.

### 19.5 Evaluation Failure

Evaluation itself may be wrong.

Possible causes include:

- inadequate scenarios;
- biased data;
- incorrect expected outcomes;
- missing failure cases;
- missing or unrepresentative adversarial cases;
- misleading metrics;
- incomplete traces;
- evaluation leakage; or
- obsolete qualification conditions.

Qualification and Operational Confidence therefore remain reviewable and revisable.

### 19.6 Cross-Composition Failure

Some of the most consequential failures arise between Compositions:

- correct execution using stale Working Context;
- a qualified Capability Agent operating through an incorrect Execution Graph;
- correct processing against the wrong authoritative source;
- valid Sandbox evidence interpreted beyond its tested scope; or
- organizational knowledge reaching the wrong authority boundary.

No individual Composition can guarantee organizational correctness alone.

Its relationships and boundaries matter equally.

### 19.7 Safe Failure

Where uncertainty may create material consequences, the preferred behavior is:

```text
Uncertainty
     ↓
Preserve state
     ↓
Stop / Wait / Restrict
     ↓
Gather evidence
     ↓
Escalate where required
```

rather than:

```text
Uncertainty
     ↓
Guess
     ↓
Continue
```

> **An AI-First Company must be designed not only to act when it knows what to do, but also to behave safely when it does not.**

---

## 20. Future Evolution

The Reference Design is complete for its defined scope without assuming that every future organizational form or AI capability can already be predicted.

Future experience may justify extensions such as:

- collaboration between multiple Executive Agents;
- interaction models for different forms of human leadership;
- federation or partitioning of large Company Brains;
- increasingly complex Capability composition;
- long-running Execution Graph evolution;
- qualification transfer between related capabilities;
- multiple concurrent Sandbox Organizations;
- cross-company capability interaction; or
- new forms of bounded AI autonomy.

These are possible future extensions, **not unresolved requirements of the current Reference Design**.

### 20.1 Layer Discipline

Future development preserves the distinction:

```text
Architecture
      ↓
Reference Design
      ↓
Technical Requirements
```

A new technology does not automatically require a Reference Design change.

A different technical realization does not automatically require an Architecture change.

A new organizational requirement should not be hidden inside the Technical Requirements when it reveals a genuine architectural concern.

Changes belong to the layer whose responsibility actually changed.

### 20.2 Evidence before Expansion

The Reference Design should grow when organizational evidence demonstrates that an existing Composition or relationship is insufficient.

A new model, framework, agent pattern, or technical capability is not by itself a reason to expand the organizational design.

> **Expand the Reference because the organization requires it, not because technology makes it possible.**
