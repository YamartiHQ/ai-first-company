# Architecture Glossary

## Purpose and Authority

This glossary is a Derived Representation of [ARCHITECTURE.md](ARCHITECTURE.md) and the [Architecture Knowledge Graph](ARCHITECTURE_KNOWLEDGE_GRAPH.md). It provides concise human-readable definitions and navigation. It cannot add, redefine, or preserve concepts absent from the authoritative Architecture.

Each entry corresponds to exactly one Knowledge Graph Concept Node. Domain grouping is navigational only and does not create a parallel taxonomy.

## Part 1 — Domain-Oriented Glossary

### Architecture

#### AI-First Company

**Definition:** An organization architected for durable Human–AI operation.

**Boundary:** Not defined by technology count or one performer type.

**Architecture source:** [AI-First Company](ARCHITECTURE.md#what-is-an-ai-first-company)

**Related concepts:** [Organizational Identity](#organizational-identity), [Company Brain](#company-brain)

### Identity

#### Organizational Identity

**Definition:** Organization-owned Purpose plus Principles.

**Boundary:** Orients behavior but creates no Authority.

**Architecture source:** [Organizational Identity](ARCHITECTURE.md#organizational-identity)

**Related concepts:** [Organizational Purpose](#organizational-purpose), [Organizational Principle](#organizational-principle), [AI-First Company](#ai-first-company)

#### Organizational Purpose

**Definition:** The enduring reason the organization exists.

**Boundary:** Does not authorize work.

**Architecture source:** [Organizational Purpose](ARCHITECTURE.md#organizational-identity)

**Related concepts:** [Organizational Identity](#organizational-identity)

#### Organizational Principle

**Definition:** A durable rule orienting organizational judgment.

**Boundary:** Distinct from Practice and Policy.

**Architecture source:** [Organizational Principle](ARCHITECTURE.md#principle-practice-and-policy)

**Related concepts:** [Organizational Identity](#organizational-identity)

### Execution Environment

#### Company Execution Environment

**Definition:** A controlled environment for organizational work and assets.

**Boundary:** Implementation-independent.

**Architecture source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment)

**Related concepts:** [Persistent Execution Environment](#persistent-execution-environment), [Trust Domain](#trust-domain), [Access Boundary](#access-boundary), [Recoverability](#recoverability)

#### Persistent Execution Environment

**Definition:** An execution environment with retained state or tested rehydration.

**Boundary:** Does not imply unattended or public operation.

**Architecture source:** [Persistent Execution Environment](ARCHITECTURE.md#company-execution-environment)

**Related concepts:** [Company Execution Environment](#company-execution-environment)

#### Trust Domain

**Definition:** A boundary separating identities, systems, data, credentials, and recovery paths.

**Boundary:** Does not prescribe physical isolation.

**Architecture source:** [Trust Domain](ARCHITECTURE.md#trust-custody-and-access)

**Related concepts:** [Company Execution Environment](#company-execution-environment)

#### Access Boundary

**Definition:** A boundary limiting routes to information and capabilities.

**Boundary:** Reachability is not permission.

**Architecture source:** [Access Boundary](ARCHITECTURE.md#trust-custody-and-access)

**Related concepts:** [Company Execution Environment](#company-execution-environment)

#### Data Custody

**Definition:** Accountable control of data across its lifecycle.

**Boundary:** Does not require physical hosting.

**Architecture source:** [Data Custody](ARCHITECTURE.md#trust-custody-and-access)

**Related concepts:** [Company Brain](#company-brain)

#### System of Record

**Definition:** An authoritative source for a bounded information class.

**Boundary:** Replicas are not automatically authoritative.

**Architecture source:** [System of Record](ARCHITECTURE.md#trust-custody-and-access)

**Related concepts:** [Company State](#company-state), [Company State Fact](#company-state-fact)

#### Recoverability

**Definition:** The ability to restore required operation, access, data, and meaning.

**Boundary:** Copies or restart alone are insufficient.

**Architecture source:** [Recoverability](ARCHITECTURE.md#recoverability-and-rehydration)

**Related concepts:** [Company Execution Environment](#company-execution-environment)

#### Session Work

**Definition:** Interactive work dependent on an active session.

**Boundary:** Not inherently human-only.

**Architecture source:** [Session Work](ARCHITECTURE.md#session-work-and-system-work)

**Related concepts:** [Work Item](#work-item)

#### System Work

**Definition:** Work continuing through company systems beyond one session.

**Boundary:** Does not grant itself Authority.

**Architecture source:** [System Work](ARCHITECTURE.md#session-work-and-system-work)

**Related concepts:** [Work Item](#work-item)

#### Performer Configuration

**Definition:** Material configuration affecting a Performer's capability realization.

**Boundary:** Product features are not concepts by default.

**Architecture source:** [Performer Configuration](ARCHITECTURE.md#performer-configuration-and-memory)

**Related concepts:** [Performer](#performer)

#### Execution Identity

**Definition:** The attributable identity used while acting.

**Boundary:** Distinct from Performer, Capability, and Authority.

**Architecture source:** [Execution Identity](ARCHITECTURE.md#performer-configuration-and-memory)

**Related concepts:** [Performer](#performer)

#### Working Memory

**Definition:** Temporary state used within current work.

**Boundary:** Not Performer Memory or Company Brain.

**Architecture source:** [Working Memory](ARCHITECTURE.md#performer-configuration-and-memory)

**Related concepts:** [Performer](#performer), [Memory Policy](#memory-policy)

#### Performer Memory

**Definition:** Retained performer-specific information influencing later work.

**Boundary:** Must not create Shadow Access or Shadow Truth.

**Architecture source:** [Performer Memory](ARCHITECTURE.md#performer-configuration-and-memory)

**Related concepts:** [Performer](#performer), [Memory Policy](#memory-policy), [Context Construction](#context-construction), [Shadow Truth](#shadow-truth), [Information Classification](#information-classification)

### Information Governance

#### Memory Policy

**Definition:** Rules for writing, retaining, retrieving, transforming, and deleting memory.

**Boundary:** Applies at write and retrieval time.

**Architecture source:** [Memory Policy](ARCHITECTURE.md#performer-configuration-and-memory)

**Related concepts:** [Working Memory](#working-memory), [Performer Memory](#performer-memory), [Shadow Access](#shadow-access)

#### Information Classification

**Definition:** Assignment and maintenance of purpose- and scope-aware handling requirements.

**Boundary:** Does not grant Authority or access.

**Architecture source:** [Information Classification](ARCHITECTURE.md#classification)

**Related concepts:** [Information Class](#information-class), [Working Context](#working-context), [Performer Memory](#performer-memory), [Derived Representation](#derived-representation), [External Interaction](#external-interaction)

#### Information Class

**Definition:** An organization-defined handling category.

**Boundary:** No universal fixed taxonomy is prescribed.

**Architecture source:** [Information Class](ARCHITECTURE.md#classification)

**Related concepts:** [Information Classification](#information-classification)

#### Shadow Access

**Definition:** Information usable outside current authorized access.

**Boundary:** Past access does not create current access.

**Architecture source:** [Shadow Access](ARCHITECTURE.md#purpose--and-scope-aware-governance)

**Related concepts:** [Memory Policy](#memory-policy)

#### Shadow Truth

**Definition:** Non-authoritative information silently governing work.

**Boundary:** Local memory must not override authoritative State.

**Architecture source:** [Shadow Truth](ARCHITECTURE.md#purpose--and-scope-aware-governance)

**Related concepts:** [Performer Memory](#performer-memory)

### Actors and Coordination

#### Actor

**Definition:** An organizational participant able to receive information or assignments.

**Boundary:** Actor status grants no Authority or access.

**Architecture source:** [Actor](ARCHITECTURE.md#actors-performers-and-groups)

**Related concepts:** [Performer](#performer), [Organizational Group](#organizational-group), [Accountability Assignment](#accountability-assignment), [Decision Participation](#decision-participation), [Attention Requirement](#attention-requirement)

#### Performer

**Definition:** An Actor assigned to perform work through an implementation.

**Boundary:** Not the Capability or its Authority.

**Architecture source:** [Performer](ARCHITECTURE.md#actors-performers-and-groups)

**Related concepts:** [Performer Configuration](#performer-configuration), [Execution Identity](#execution-identity), [Working Memory](#working-memory), [Performer Memory](#performer-memory), [Actor](#actor), [Performer Assignment](#performer-assignment)

#### Organizational Group

**Definition:** A governed set of collaborating Actors.

**Boundary:** Membership aggregates no Authority, access, or Accountability.

**Architecture source:** [Organizational Group](ARCHITECTURE.md#actors-performers-and-groups)

**Related concepts:** [Actor](#actor), [Attention Requirement](#attention-requirement), [Capability Implementation](#capability-implementation), [Accountability Assignment](#accountability-assignment), [Decision Participation](#decision-participation)

#### Performer Assignment

**Definition:** Assignment of qualified realization to Capability responsibility in Scope.

**Boundary:** Does not silently grant Authority or Accountability.

**Architecture source:** [Performer Assignment](ARCHITECTURE.md#assignments)

**Related concepts:** [Performer](#performer), [Company Capability](#company-capability), [Work Item](#work-item), [Capability Qualification](#capability-qualification)

#### Accountability Assignment

**Definition:** Assignment of answerability for a defined result or obligation.

**Boundary:** Does not grant Authority, access, or capability.

**Architecture source:** [Accountability Assignment](ARCHITECTURE.md#assignments)

**Related concepts:** [Actor](#actor), [Decision Mandate](#decision-mandate), [Organizational Group](#organizational-group)

#### Decision Participation

**Definition:** Participation in a governed decision mechanism.

**Boundary:** Does not imply Authority or Accountability.

**Architecture source:** [Decision Participation](ARCHITECTURE.md#decision-mechanisms-and-accountability)

**Related concepts:** [Actor](#actor), [Decision](#decision), [Organizational Group](#organizational-group)

#### Attention Requirement

**Definition:** A need for timely consideration by a suitably situated Actor or Group.

**Boundary:** Not necessarily human or hierarchical escalation.

**Architecture source:** [Attention Requirement](ARCHITECTURE.md#attention-routing)

**Related concepts:** [Actor](#actor), [Organizational Group](#organizational-group), [Organizational Event](#organizational-event), [Decision Proposal](#decision-proposal)

### Capabilities

#### Company Capability

**Definition:** A defined organizational ability to perform a class of work.

**Boundary:** Not implementation, performer, skill, model, role, team, or organizational unit.

**Architecture source:** [Company Capability](ARCHITECTURE.md#capability-first)

**Related concepts:** [Performer Assignment](#performer-assignment), [Capability Implementation](#capability-implementation), [Work Item](#work-item), [Dependency Record](#dependency-record), [Recovery](#recovery)

#### Capability Implementation

**Definition:** A particular realization of a Company Capability.

**Boundary:** Does not inherit Authority from the Capability.

**Architecture source:** [Capability Implementation](ARCHITECTURE.md#capability-first)

**Related concepts:** [Company Capability](#company-capability), [Capability Qualification](#capability-qualification), [Performer](#performer), [Organizational Learning Candidate](#organizational-learning-candidate), [Organizational Group](#organizational-group)

#### Capability Qualification

**Definition:** Evidence that a Performer or implementation can perform a Capability in Scope.

**Boundary:** Does not grant Authority or permanent confidence.

**Architecture source:** [Capability Qualification](ARCHITECTURE.md#capability-qualification)

**Related concepts:** [Capability Implementation](#capability-implementation), [Performer](#performer), [Operational Confidence](#operational-confidence), [Performer Assignment](#performer-assignment)

### Organizational Intelligence

#### Company Brain

**Definition:** Organization-owned intelligence across authoritative and retained information.

**Boundary:** Not Actor, Authority, one database, or universal access.

**Architecture source:** [Company Brain](ARCHITECTURE.md#company-brain)

**Related concepts:** [AI-First Company](#ai-first-company), [Data Custody](#data-custody), [Source Claim](#source-claim), [Evidence](#evidence), [Validated Knowledge](#validated-knowledge), [Company Memory](#company-memory)

#### Source Claim

**Definition:** A proposition attributed to a source.

**Boundary:** Not Evidence, State, or organizational truth.

**Architecture source:** [Source Claim](ARCHITECTURE.md#evidence-and-knowledge)

**Related concepts:** [Company Brain](#company-brain), [Evidence](#evidence), [Provenance](#provenance), [Company State Fact](#company-state-fact), [Continuous Environmental Intelligence](#continuous-environmental-intelligence)

#### Evidence

**Definition:** Information retained independently enough to support evaluation.

**Boundary:** Not automatically Knowledge, State, Memory, or Authority.

**Architecture source:** [Evidence](ARCHITECTURE.md#evidence-and-knowledge)

**Related concepts:** [Company Brain](#company-brain), [Source Claim](#source-claim), [Validated Knowledge](#validated-knowledge), [Provenance](#provenance), [Organizational Learning Candidate](#organizational-learning-candidate), [Continuous Environmental Intelligence](#continuous-environmental-intelligence)

#### Validated Knowledge

**Definition:** Understanding accepted for stated Purpose, Scope, time, and conditions.

**Boundary:** Not universal, permanent, or automatically retained.

**Architecture source:** [Validated Knowledge](ARCHITECTURE.md#evidence-and-knowledge)

**Related concepts:** [Company Brain](#company-brain), [Evidence](#evidence), [Organizational Learning Candidate](#organizational-learning-candidate)

#### Company Memory

**Definition:** Historically relevant information intentionally retained.

**Boundary:** Narrower than Company Brain; not current State or Context.

**Architecture source:** [Company Memory](ARCHITECTURE.md#company-memory)

**Related concepts:** [Company Brain](#company-brain), [Company Artifact](#company-artifact)

### Learning

#### Organizational Practice

**Definition:** An approved reusable way of working.

**Boundary:** Distinct from Principle, Policy, and Knowledge.

**Architecture source:** [Organizational Practice](ARCHITECTURE.md#from-experience-to-adopted-learning)

**Related concepts:** [Company Brain](#company-brain), [Company Artifact](#company-artifact), [Organizational Learning Candidate](#organizational-learning-candidate)

#### Experience

**Definition:** Information arising from work, interaction, observation, or outcomes.

**Boundary:** Performer learning is not organizational learning.

**Architecture source:** [Experience](ARCHITECTURE.md#from-experience-to-adopted-learning)

**Related concepts:** [Outcome](#outcome), [Organizational Reflection](#organizational-reflection)

#### Organizational Reflection

**Definition:** Governed examination of Experience and organizational results.

**Boundary:** Does not adopt learning or delay containment.

**Architecture source:** [Organizational Reflection](ARCHITECTURE.md#from-experience-to-adopted-learning)

**Related concepts:** [Experience](#experience), [Organizational Learning Candidate](#organizational-learning-candidate), [Operating Cycle](#operating-cycle), [Organizational Event](#organizational-event)

#### Organizational Learning Candidate

**Definition:** A proposed reusable insight or change produced through Reflection.

**Boundary:** Not adopted learning.

**Architecture source:** [Organizational Learning Candidate](ARCHITECTURE.md#from-experience-to-adopted-learning)

**Related concepts:** [Organizational Reflection](#organizational-reflection), [Evidence](#evidence), [Validated Knowledge](#validated-knowledge), [Organizational Practice](#organizational-practice), [Capability Implementation](#capability-implementation)

#### Performer Rehydration

**Definition:** Reconstruction of sufficient authorized configuration, intelligence, and context.

**Boundary:** Does not inherit stale access, Authority, or confidence.

**Architecture source:** [Performer Rehydration](ARCHITECTURE.md#performer-rehydration)

**Related concepts:** [Company Brain](#company-brain), [Performer](#performer), [Recovery](#recovery)

### Knowledge Representation

#### Company Artifact

**Definition:** Organizational information preserved in reviewable form for continuing value.

**Boundary:** Not every record or observation qualifies.

**Architecture source:** [Company Artifact](ARCHITECTURE.md#organizational-representations)

**Related concepts:** [Company Memory](#company-memory), [Decision Record](#decision-record), [Organizational Practice](#organizational-practice), [Canonical Representation](#canonical-representation), [Company Brain](#company-brain)

#### Canonical Representation

**Definition:** The stable reference representation of bounded meaning.

**Boundary:** Not universally authoritative.

**Architecture source:** [Canonical Representation](ARCHITECTURE.md#organizational-representations)

**Related concepts:** [Company Artifact](#company-artifact), [Derived Representation](#derived-representation)

#### Authoritative Representation

**Definition:** A representation authoritative for a defined question, Scope, and time.

**Boundary:** Authority is bounded.

**Architecture source:** [Authoritative Representation](ARCHITECTURE.md#organizational-representations)

**Related concepts:** [Company State](#company-state)

#### Derived Representation

**Definition:** A representation produced from another for a consumer or purpose.

**Boundary:** Must not silently become authoritative.

**Architecture source:** [Derived Representation](ARCHITECTURE.md#organizational-representations)

**Related concepts:** [Canonical Representation](#canonical-representation), [Provenance](#provenance), [Information Classification](#information-classification)

#### Provenance

**Definition:** Origin, attribution, lineage, timing, and relevant custody.

**Boundary:** Must survive material transformation.

**Architecture source:** [Provenance](ARCHITECTURE.md#provenance-and-transformation)

**Related concepts:** [Source Claim](#source-claim), [Evidence](#evidence), [Derived Representation](#derived-representation), [Company State Fact](#company-state-fact)

### Decision Governance

#### Decision

**Definition:** An authoritative organizational determination within a domain.

**Boundary:** Not proposal, execution, effect, or outcome.

**Architecture source:** [Decision](ARCHITECTURE.md#decisions-and-mandates)

**Related concepts:** [Work Item](#work-item), [Decision Mandate](#decision-mandate), [Decision Proposal](#decision-proposal), [Decision Basis](#decision-basis), [Decision Record](#decision-record), [Decision Participation](#decision-participation)

#### Decision Proposal

**Definition:** A supported option submitted for governed consideration.

**Boundary:** Does not become a Decision automatically.

**Architecture source:** [Decision Proposal](ARCHITECTURE.md#decisions-and-mandates)

**Related concepts:** [Decision](#decision), [Attention Requirement](#attention-requirement)

#### Decision Record

**Definition:** A durable record of a material Decision and its governance.

**Boundary:** Not the Mandate Registry.

**Architecture source:** [Decision Record](ARCHITECTURE.md#decisions-and-mandates)

**Related concepts:** [Company Artifact](#company-artifact), [Decision](#decision), [Decision Basis](#decision-basis)

#### Decision Basis

**Definition:** The information, uncertainty, alternatives, and dissent supporting a Decision.

**Boundary:** Rationale is not Evidence.

**Architecture source:** [Decision Basis](ARCHITECTURE.md#decisions-and-mandates)

**Related concepts:** [Decision](#decision), [Decision Record](#decision-record), [Company Brain](#company-brain)

#### Decision Mandate

**Definition:** A bounded definition of Decision Authority and its governance.

**Boundary:** Does not prescribe a human holder.

**Architecture source:** [Decision Mandate](ARCHITECTURE.md#decisions-and-mandates)

**Related concepts:** [Decision](#decision), [Mandate Registry](#mandate-registry), [Accountability Assignment](#accountability-assignment)

#### Mandate Registry

**Definition:** The authoritative durable record of active Decision Mandates.

**Boundary:** Not an organization chart or decision history.

**Architecture source:** [Mandate Registry](ARCHITECTURE.md#decisions-and-mandates)

**Related concepts:** [Decision Mandate](#decision-mandate)

### Context and Access

#### Knowledge Access

**Definition:** The governed capability supplying information for authorized work.

**Boundary:** Not unrestricted browsing.

**Architecture source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access)

**Related concepts:** [Context Construction](#context-construction), [Pull Access](#pull-access), [Push Access](#push-access)

#### Context Construction

**Definition:** Selection, evaluation, relation, minimization, and delivery of context.

**Boundary:** Not merely retrieval or vector search.

**Architecture source:** [Context Construction](ARCHITECTURE.md#context-construction)

**Related concepts:** [Knowledge Access](#knowledge-access), [Working Context](#working-context), [Company Brain](#company-brain), [Company State](#company-state), [Performer Memory](#performer-memory)

#### Working Context

**Definition:** Temporary purpose-specific context for one activity.

**Boundary:** Not Company Brain or permanent access.

**Architecture source:** [Working Context](ARCHITECTURE.md#context-construction)

**Related concepts:** [Context Construction](#context-construction), [Performer](#performer), [Company State](#company-state), [Work Item](#work-item), [Information Classification](#information-classification)

#### Pull Access

**Definition:** Knowledge Access initiated by current work or request.

**Boundary:** Does not permit unrestricted access.

**Architecture source:** [Pull Access](ARCHITECTURE.md#knowledge-access)

**Related concepts:** [Knowledge Access](#knowledge-access)

#### Push Access

**Definition:** Knowledge Access triggered by relevant change.

**Boundary:** Does not grant Authority or wider access.

**Architecture source:** [Push Access](ARCHITECTURE.md#knowledge-access)

**Related concepts:** [Knowledge Access](#knowledge-access)

### Operation

#### Operating Cycle

**Definition:** Connected but distinct Operating, Learning, and Assurance loops.

**Boundary:** The loops must not collapse.

**Architecture source:** [Operating Cycle](ARCHITECTURE.md#three-connected-loops)

**Related concepts:** [Controlled Execution](#controlled-execution), [Organizational Reflection](#organizational-reflection), [Continuous Assurance](#continuous-assurance)

#### Organizational Intent

**Definition:** An expression of desired organizational work or change.

**Boundary:** Does not create Authority, admission, or execution.

**Architecture source:** [Organizational Intent](ARCHITECTURE.md#sources-and-work-formation)

**Related concepts:** [Work Item](#work-item)

#### Organizational Obligation

**Definition:** Work required by a binding organizational or external condition.

**Boundary:** Does not bypass controls.

**Architecture source:** [Organizational Obligation](ARCHITECTURE.md#sources-and-work-formation)

**Related concepts:** [Work Item](#work-item)

#### Work Item

**Definition:** A bounded unit of organizational work.

**Boundary:** Does not create Capability, Authority, or admission.

**Architecture source:** [Work Item](ARCHITECTURE.md#sources-and-work-formation)

**Related concepts:** [Session Work](#session-work), [System Work](#system-work), [Organizational Intent](#organizational-intent), [Organizational Obligation](#organizational-obligation), [Organizational Event](#organizational-event), [Decision](#decision)

#### Organizational Event

**Definition:** An attributable occurrence significant to operation.

**Boundary:** Not automatically Work, Authority, State, Evidence, Learning, or Attention.

**Architecture source:** [Organizational Event](ARCHITECTURE.md#organizational-events)

**Related concepts:** [Work Item](#work-item), [Company State](#company-state), [Attention Requirement](#attention-requirement), [Continuous Assurance](#continuous-assurance), [Organizational Reflection](#organizational-reflection), [Incident](#incident)

### Controlled Execution

#### Controlled Execution

**Definition:** Performance of admitted authorized work within boundaries.

**Boundary:** Does not create authorization.

**Architecture source:** [Controlled Execution](ARCHITECTURE.md#definition-and-control-plane)

**Related concepts:** [Operating Cycle](#operating-cycle), [Work Admission](#work-admission), [Organizational Control Plane](#organizational-control-plane), [Authorized Effect](#authorized-effect), [External Interaction](#external-interaction), [Organizational Continuity](#organizational-continuity)

#### Work Admission

**Definition:** The boundary deciding whether authorized work may execute now.

**Boundary:** Authorization does not guarantee admission.

**Architecture source:** [Work Admission](ARCHITECTURE.md#work-admission-and-capacity)

**Related concepts:** [Controlled Execution](#controlled-execution), [Company State](#company-state)

#### Organizational Control Plane

**Definition:** The capability enforcing operational constraints.

**Boundary:** Instructions or sandboxing alone are insufficient.

**Architecture source:** [Organizational Control Plane](ARCHITECTURE.md#definition-and-control-plane)

**Related concepts:** [Controlled Execution](#controlled-execution), [External Effect](#external-effect), [Controlled Autonomy](#controlled-autonomy)

#### Authorized Effect

**Definition:** The bounded effect permitted by applicable Authority.

**Boundary:** Distinct from intent, execution, interaction, and outcome.

**Architecture source:** [Authorized Effect](ARCHITECTURE.md#effects-and-external-interaction)

**Related concepts:** [Standing Authorization](#standing-authorization), [Controlled Execution](#controlled-execution)

#### External Interaction

**Definition:** Exchange or invocation beyond the immediate execution boundary.

**Boundary:** Not itself Authority or External Effect.

**Architecture source:** [External Interaction](ARCHITECTURE.md#effects-and-external-interaction)

**Related concepts:** [Controlled Execution](#controlled-execution), [External Effect](#external-effect), [Information Classification](#information-classification), [Continuous Environmental Intelligence](#continuous-environmental-intelligence)

#### External Effect

**Definition:** An externally observable state change produced through execution.

**Boundary:** Distinct from execution and outcome.

**Architecture source:** [External Effect](ARCHITECTURE.md#effects-and-external-interaction)

**Related concepts:** [External Interaction](#external-interaction), [Outcome](#outcome), [Organizational Control Plane](#organizational-control-plane)

#### Outcome

**Definition:** The observed result of organizational work.

**Boundary:** Does not automatically create State, Memory, or learning.

**Architecture source:** [Outcome](ARCHITECTURE.md#effects-and-external-interaction)

**Related concepts:** [Experience](#experience), [External Effect](#external-effect)

### Assurance and Autonomy

#### Continuous Assurance

**Definition:** The capability determining whether trust remains justified during operation.

**Boundary:** Distinct from learning and grants no Authority.

**Architecture source:** [Continuous Assurance](ARCHITECTURE.md#continuous-assurance)

**Related concepts:** [Operating Cycle](#operating-cycle), [Organizational Event](#organizational-event), [Operational Confidence](#operational-confidence), [Shadow Evaluation](#shadow-evaluation), [Controlled Autonomy](#controlled-autonomy), [Controlled Execution](#controlled-execution)

#### Operational Confidence

**Definition:** A current scoped evidence-based assessment of acceptable capability performance.

**Boundary:** Not Authority or a permanent performer score.

**Architecture source:** [Operational Confidence](ARCHITECTURE.md#operational-confidence)

**Related concepts:** [Continuous Assurance](#continuous-assurance), [Standing Authorization](#standing-authorization), [Capability Qualification](#capability-qualification)

#### Shadow Evaluation

**Definition:** Evaluation outside the primary execution control path.

**Boundary:** Not automatically independent or authorizing.

**Architecture source:** [Shadow Evaluation](ARCHITECTURE.md#continuous-assurance)

**Related concepts:** [Continuous Assurance](#continuous-assurance)

#### Standing Authorization

**Definition:** Governed authorization for recurring action within explicit boundaries.

**Boundary:** Evidence and confidence do not create it.

**Architecture source:** [Standing Authorization](ARCHITECTURE.md#standing-authorization)

**Related concepts:** [Authorized Effect](#authorized-effect), [Operational Confidence](#operational-confidence), [Controlled Autonomy](#controlled-autonomy)

#### Controlled Autonomy

**Definition:** Bounded action without case-by-case approval that remains enforceable and reversible.

**Boundary:** Not unlimited or automatically expanding.

**Architecture source:** [Controlled Autonomy](ARCHITECTURE.md#controlled-autonomy)

**Related concepts:** [Standing Authorization](#standing-authorization), [Continuous Assurance](#continuous-assurance), [Organizational Control Plane](#organizational-control-plane)

### State

#### Company State

**Definition:** What the organization currently considers true for operation.

**Boundary:** Not Company Memory or performer-local state.

**Architecture source:** [Company State](ARCHITECTURE.md#company-state)

**Related concepts:** [System of Record](#system-of-record), [Company Brain](#company-brain), [Authoritative Representation](#authoritative-representation), [Context Construction](#context-construction), [Working Context](#working-context), [Organizational Event](#organizational-event)

#### Company State Fact

**Definition:** An attributable assertion accepted into State for bounded Scope and time.

**Boundary:** Distinct from Claim, Evidence, and Event.

**Architecture source:** [Company State Fact](ARCHITECTURE.md#company-state)

**Related concepts:** [Company State](#company-state), [System of Record](#system-of-record), [Source Claim](#source-claim), [Provenance](#provenance)

### Environmental Intelligence

#### Continuous Environmental Intelligence

**Definition:** Ongoing observation of relevant external change into claims, evidence, and events.

**Boundary:** Creates no truth, policy, Authority, or automatic action.

**Architecture source:** [Continuous Environmental Intelligence](ARCHITECTURE.md#continuous-environmental-intelligence)

**Related concepts:** [Source Claim](#source-claim), [Evidence](#evidence), [Organizational Event](#organizational-event), [External Interaction](#external-interaction)

### Continuity and Recovery

#### Organizational Continuity

**Definition:** Preservation or deliberate change of essential operation through disruption.

**Boundary:** Does not mean all work continues.

**Architecture source:** [Organizational Continuity](ARCHITECTURE.md#organizational-continuity)

**Related concepts:** [Dependency Record](#dependency-record), [Controlled Execution](#controlled-execution)

#### Incident

**Definition:** A disruption requiring containment, assessment, reconciliation, and recovery.

**Boundary:** Incident handling is not learning.

**Architecture source:** [Incident](ARCHITECTURE.md#incident-and-containment)

**Related concepts:** [Work Item](#work-item), [Organizational Event](#organizational-event), [Recovery](#recovery)

#### Recovery

**Definition:** Restoration of sufficient organizational conditions for bounded operation.

**Boundary:** Not technical restart.

**Architecture source:** [Recovery](ARCHITECTURE.md#recovery)

**Related concepts:** [Incident](#incident), [Performer Rehydration](#performer-rehydration), [Company Capability](#company-capability)

#### Dependency Record

**Definition:** A governed record of material dependencies and alternatives.

**Boundary:** Recording does not make a dependency reliable.

**Architecture source:** [Dependency Record](ARCHITECTURE.md#organizational-continuity)

**Related concepts:** [Organizational Continuity](#organizational-continuity), [Company Capability](#company-capability)

## Part 2 — Alphabetical Index

- [Access Boundary](#access-boundary)
- [Accountability Assignment](#accountability-assignment)
- [Actor](#actor)
- [AI-First Company](#ai-first-company)
- [Attention Requirement](#attention-requirement)
- [Authoritative Representation](#authoritative-representation)
- [Authorized Effect](#authorized-effect)
- [Canonical Representation](#canonical-representation)
- [Capability Implementation](#capability-implementation)
- [Capability Qualification](#capability-qualification)
- [Company Artifact](#company-artifact)
- [Company Brain](#company-brain)
- [Company Capability](#company-capability)
- [Company Execution Environment](#company-execution-environment)
- [Company Memory](#company-memory)
- [Company State](#company-state)
- [Company State Fact](#company-state-fact)
- [Context Construction](#context-construction)
- [Continuous Assurance](#continuous-assurance)
- [Continuous Environmental Intelligence](#continuous-environmental-intelligence)
- [Controlled Autonomy](#controlled-autonomy)
- [Controlled Execution](#controlled-execution)
- [Data Custody](#data-custody)
- [Decision](#decision)
- [Decision Basis](#decision-basis)
- [Decision Mandate](#decision-mandate)
- [Decision Participation](#decision-participation)
- [Decision Proposal](#decision-proposal)
- [Decision Record](#decision-record)
- [Dependency Record](#dependency-record)
- [Derived Representation](#derived-representation)
- [Evidence](#evidence)
- [Execution Identity](#execution-identity)
- [Experience](#experience)
- [External Effect](#external-effect)
- [External Interaction](#external-interaction)
- [Incident](#incident)
- [Information Class](#information-class)
- [Information Classification](#information-classification)
- [Knowledge Access](#knowledge-access)
- [Mandate Registry](#mandate-registry)
- [Memory Policy](#memory-policy)
- [Operating Cycle](#operating-cycle)
- [Operational Confidence](#operational-confidence)
- [Organizational Continuity](#organizational-continuity)
- [Organizational Control Plane](#organizational-control-plane)
- [Organizational Event](#organizational-event)
- [Organizational Group](#organizational-group)
- [Organizational Identity](#organizational-identity)
- [Organizational Intent](#organizational-intent)
- [Organizational Learning Candidate](#organizational-learning-candidate)
- [Organizational Obligation](#organizational-obligation)
- [Organizational Practice](#organizational-practice)
- [Organizational Principle](#organizational-principle)
- [Organizational Purpose](#organizational-purpose)
- [Organizational Reflection](#organizational-reflection)
- [Outcome](#outcome)
- [Performer](#performer)
- [Performer Assignment](#performer-assignment)
- [Performer Configuration](#performer-configuration)
- [Performer Memory](#performer-memory)
- [Performer Rehydration](#performer-rehydration)
- [Persistent Execution Environment](#persistent-execution-environment)
- [Provenance](#provenance)
- [Pull Access](#pull-access)
- [Push Access](#push-access)
- [Recoverability](#recoverability)
- [Recovery](#recovery)
- [Session Work](#session-work)
- [Shadow Access](#shadow-access)
- [Shadow Evaluation](#shadow-evaluation)
- [Shadow Truth](#shadow-truth)
- [Source Claim](#source-claim)
- [Standing Authorization](#standing-authorization)
- [System of Record](#system-of-record)
- [System Work](#system-work)
- [Trust Domain](#trust-domain)
- [Validated Knowledge](#validated-knowledge)
- [Work Admission](#work-admission)
- [Work Item](#work-item)
- [Working Context](#working-context)
- [Working Memory](#working-memory)

## Glossary Governance

Update the authoritative Architecture first, then the Knowledge Graph, then this glossary. A glossary entry without a matching graph node is invalid. Related-concept links must be supported by at least one graph edge.

## Failure Modes

- A concise glossary definition becomes broader than its Architecture source.
- A deleted concept survives as an alias.
- A domain heading is treated as Architecture ontology.
- Related concepts are added for convenience without graph support.
- Implementation terminology is promoted into the Architecture.
