# Architecture Glossary

## Purpose and Authority

This glossary is a human-readable Derived Representation of the validated Concept Nodes and relationships in the [Architecture Knowledge Graph](ARCHITECTURE_KNOWLEDGE_GRAPH.md). It is intended for readers, reviewers, and authors of downstream Reference Design and Technical Requirements artifacts, and supports ontology navigation without introducing Architecture concepts.

The order of authority is:

1. [Architecture](ARCHITECTURE.md)
2. [Architecture Knowledge Graph](ARCHITECTURE_KNOWLEDGE_GRAPH.md)
3. This glossary

If these sources conflict, `ARCHITECTURE.md` governs. The definitions, responsibilities, boundaries, source references, and related concepts below are derived from the Knowledge Graph. Domain grouping is navigational only; it does not create a separate taxonomy.

Related Concepts include only concepts identified by the graph's Concept Catalog as immediately related or connected by a validated Relationship Edge.

## Part 1 — Domain-Oriented Glossary

### Identity

#### Brand Identity

**Definition:** Recognizable name and visual elements associated with a company or product.

**Responsibility:** Identify brand elements that may require conflict review.

**Is NOT**

- It does not prescribe branding or establish legal availability.

**Related Concepts:** [Company Identity](#company-identity), [Evidence](#evidence), [Product Identity](#product-identity)

**Architecture Source:** [Company Identity](ARCHITECTURE.md#company-identity) — [Brand Identity](ARCHITECTURE.md#brand-identity)

#### Company Identity

**Definition:** The identity through which the company is recognized and represented.

**Responsibility:** Maintain a coherent company identity across independent identity systems.

**Is NOT**

- It is distinct from Product Identity and legal availability is not established by one source.

**Related Concepts:** [Brand Identity](#brand-identity), [Legal Identity](#legal-identity), [Product Identity](#product-identity)

**Architecture Source:** [Company Identity](ARCHITECTURE.md#company-identity) — [Company Identity and Product Identity](ARCHITECTURE.md#company-identity-and-product-identity)

#### Financial Identity

**Definition:** The operational financial identity needed for company payments and paid dependencies.

**Responsibility:** Enable attributable business financial operation.

**Is NOT**

- It does not itself establish Legal Identity.

**Related Concepts:** [Company Execution Environment](#company-execution-environment), [Legal Identity](#legal-identity)

**Architecture Source:** [Company Identity](ARCHITECTURE.md#company-identity) — [Legal Identity and Financial Identity](ARCHITECTURE.md#legal-identity-and-financial-identity)

#### Legal Identity

**Definition:** The legally recognized company identity.

**Responsibility:** Carry statutory, contractual, and accountable company existence.

**Is NOT**

- It is distinct from Financial Identity.

**Related Concepts:** [Company Identity](#company-identity), [Financial Identity](#financial-identity)

**Architecture Source:** [Company Identity](ARCHITECTURE.md#company-identity) — [Legal Identity and Financial Identity](ARCHITECTURE.md#legal-identity-and-financial-identity)

#### Product Identity

**Definition:** The identity of a product offered by the company.

**Responsibility:** Identify a product without conflating it with the company.

**Is NOT**

- It need not equal Company Identity.

**Related Concepts:** [Brand Identity](#brand-identity), [Company Identity](#company-identity)

**Architecture Source:** [Company Identity](ARCHITECTURE.md#company-identity) — [Company Identity and Product Identity](ARCHITECTURE.md#company-identity-and-product-identity)

### Knowledge

#### Archive

**Definition:** Retained Company Artifacts that are no longer operationally active.

**Responsibility:** Preserve historical or reference value under policy.

**Is NOT**

- Archived does not mean deleted or currently operative.

**Related Concepts:** [Company Artifact](#company-artifact), [Company Memory](#company-memory)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [Archive](ARCHITECTURE.md#archive)

#### Canonical Representation

**Definition:** The authoritative representation of one Company Artifact.

**Responsibility:** Preserve the accepted organizational meaning against which other representations are checked.

**Is NOT**

- More than one authoritative representation for the same Company Artifact at the same time.

**Related Concepts:** [Company Artifact](#company-artifact), [Derived Representation](#derived-representation)

**Architecture Source:** [Knowledge Representation](ARCHITECTURE.md#knowledge-representation) — [Canonical Representation](ARCHITECTURE.md#canonical-representation)

#### Company Artifact

**Definition:** Validated knowledge intentionally preserved because it has lasting company value.

**Responsibility:** Preserve durable organizational meaning in reviewable form.

**Is NOT**

- Only material passing the Company Artifact Test belongs; not every record qualifies.

**Related Concepts:** [Archive](#archive), [Canonical Representation](#canonical-representation), [Capability History](#capability-history), [Company Memory](#company-memory), [Decision Record](#decision-record), [Mandate Registry](#mandate-registry), [Validated Knowledge](#validated-knowledge)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [Company Artifact](ARCHITECTURE.md#company-artifact)

#### Company Memory

**Definition:** The curated collection of Company Artifacts intentionally preserved by the company.

**Responsibility:** Preserve enduring identity, knowledge, decisions, and understanding.

**Is NOT**

- It is not an unrestricted activity log, Company State, or current working context.

**Related Concepts:** [Archive](#archive), [Company Artifact](#company-artifact), [Company State](#company-state), [Knowledge Access](#knowledge-access), [Knowledge Representation](#knowledge-representation)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [Company Memory Definition](ARCHITECTURE.md#company-memory-definition)

#### Context Delivery

**Definition:** The Knowledge Access capability that supplies completed Working Context to the authorized performer.

**Responsibility:** Deliver sufficient context to the human or AI system doing the work.

**Is NOT**

- Delivery does not grant decision or execution authority.

**Related Concepts:** [Decision Mandate](#decision-mandate), [Information Classification](#information-classification), [Knowledge Access](#knowledge-access), [Working Context](#working-context)

**Architecture Source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access) — [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities)

#### Context Selection

**Definition:** The Knowledge Access capability that determines the smallest sufficient information scope.

**Responsibility:** Limit Working Context to what the activity needs.

**Is NOT**

- The objective is sufficiency, not maximum information.

**Related Concepts:** [Information Classification](#information-classification), [Knowledge Access](#knowledge-access), [Working Context](#working-context)

**Architecture Source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access) — [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities)

#### Decision Record

**Definition:** A Company Artifact that preserves a consequential decision and its context.

**Responsibility:** Retain decision, rationale, evidence, authority, and review conditions where warranted.

**Is NOT**

- It does not require a separate registry concept.

**Related Concepts:** [Company Artifact](#company-artifact), [Company Memory](#company-memory), [Decision Mandate](#decision-mandate), [Standing Authorization](#standing-authorization)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [Decision Records](ARCHITECTURE.md#decision-records)

#### Derived Representation

**Definition:** A replaceable representation produced from the Canonical Representation for a particular consumer or purpose.

**Responsibility:** Make organizational knowledge usable in additional forms without changing authority.

**Is NOT**

- It remains traceable to the Canonical Representation and must not silently become authoritative.

**Related Concepts:** [Canonical Representation](#canonical-representation), [Company Artifact](#company-artifact), [Knowledge Access](#knowledge-access)

**Architecture Source:** [Knowledge Representation](ARCHITECTURE.md#knowledge-representation) — [Derived Representations](ARCHITECTURE.md#derived-representations)

#### Evidence

**Definition:** Observed information retained for evaluation without an accepted conclusion.

**Responsibility:** Make observations attributable and available for reasoning and review.

**Is NOT**

- Evidence is not automatically Knowledge or Company Memory.
- Organizational Evidence means Evidence generated or retained through organizational operation; it is not a separate concept or Knowledge Lifecycle stage.

**Related Concepts:** [Capability History](#capability-history), [Company State](#company-state), [Continuous Environmental Intelligence](#continuous-environmental-intelligence), [Controlled Execution](#controlled-execution), [External World](#external-world), [Knowledge](#knowledge-1), [Operating Cycle](#operating-cycle), [Organizational Event](#organizational-event), [Outcome](#outcome)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [Evidence](ARCHITECTURE.md#evidence)

#### External World

**Definition:** The pre-observation source of conditions, events, experiences, and material from company operations and the surrounding external environment.

**Responsibility:** Define what may need to be observed before it is intentionally retained as Evidence.

**Is NOT**

- Source material is not Evidence until it has been observed and retained.

**Related Concepts:** [Continuous Environmental Intelligence](#continuous-environmental-intelligence), [Evidence](#evidence)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [External World](ARCHITECTURE.md#external-world)

#### Knowledge

**Definition:** Organizational understanding relevant to a purpose.

**Responsibility:** Support interpretation and Intent Generation.

**Is NOT**

- It is not automatically validated, durable, authoritative, or a Company Artifact, and it is not one technical representation.

**Related Concepts:** [Evidence](#evidence), [Intent Generation](#intent-generation), [Operating Cycle](#operating-cycle), [Validated Knowledge](#validated-knowledge), [Working Context](#working-context), [Working Knowledge](#working-knowledge)

**Architecture Source:** [Operating Cycle](ARCHITECTURE.md#operating-cycle) — [Knowledge Definition](ARCHITECTURE.md#knowledge-definition)

#### Knowledge Access

**Definition:** The capability that prepares the smallest sufficient Working Context for authorized work.

**Responsibility:** Select, retrieve, synthesize, and deliver relevant organizational knowledge.

**Is NOT**

- It does not make organizational decisions or maximize information volume.

**Related Concepts:** [Company Memory](#company-memory), [Company State](#company-state), [Context Delivery](#context-delivery), [Context Selection](#context-selection), [Decision Mandate](#decision-mandate), [Information Classification](#information-classification), [Knowledge Representation](#knowledge-representation), [Knowledge Retrieval](#knowledge-retrieval), [Knowledge Synthesis](#knowledge-synthesis), [Working Context](#working-context)

**Architecture Source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access)

#### Knowledge Lifecycle

**Definition:** The governed progression from the External World through Evidence and evaluated knowledge to retained artifacts or archive.

**Responsibility:** Keep epistemic status and retention decisions explicit.

**Is NOT**

- Lifecycle stages are not automatic promotions.

**Related Concepts:** [Archive](#archive), [Company Artifact](#company-artifact), [Company Memory](#company-memory), [Evidence](#evidence), [Validated Knowledge](#validated-knowledge), [Working Knowledge](#working-knowledge)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [Knowledge Lifecycle](ARCHITECTURE.md#knowledge-lifecycle)

#### Knowledge Representation

**Definition:** The organizational form through which a Company Artifact is expressed and used.

**Responsibility:** Keep authoritative meaning distinct from replaceable representations.

**Is NOT**

- A representation does not independently create authoritative meaning.

**Related Concepts:** [Canonical Representation](#canonical-representation), [Company Artifact](#company-artifact), [Derived Representation](#derived-representation), [Knowledge Access](#knowledge-access)

**Architecture Source:** [Knowledge Representation](ARCHITECTURE.md#knowledge-representation)

#### Knowledge Retrieval

**Definition:** The Knowledge Access capability that obtains selected information from appropriate organizational sources.

**Responsibility:** Retrieve relevant knowledge, state, artifacts, and governance information.

**Is NOT**

- It does not prescribe retrieval technology.

**Related Concepts:** [Company Memory](#company-memory), [Company State](#company-state), [Knowledge Access](#knowledge-access), [Knowledge Representation](#knowledge-representation), [Working Context](#working-context)

**Architecture Source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access) — [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities)

#### Knowledge Synthesis

**Definition:** The Knowledge Access capability that organizes retrieved information into coherent context.

**Responsibility:** Relate information, remove unnecessary material, and resolve organizational context.

**Is NOT**

- It does not make the organizational decision.

**Related Concepts:** [Knowledge Access](#knowledge-access), [Knowledge Retrieval](#knowledge-retrieval), [Working Context](#working-context)

**Architecture Source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access) — [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities)

#### Pull Access

**Definition:** Knowledge Access initiated in response to a current activity or request.

**Responsibility:** Prepare context when work asks for it.

**Is NOT**

- It does not imply unrestricted browsing of all organizational information.

**Related Concepts:** [Knowledge Access](#knowledge-access), [Working Context](#working-context)

**Architecture Source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access) — [Pull Access](ARCHITECTURE.md#pull-access)

#### Push Access

**Definition:** Knowledge Access that evaluates an Organizational Event as relevant and updates or delivers the appropriate Working Context.

**Responsibility:** Maintain relevant context without requiring a prior explicit request.

**Is NOT**

- Push delivery does not expand authorization, and an event does not automatically create Intent or work.

**Related Concepts:** [Knowledge Access](#knowledge-access), [Organizational Event](#organizational-event), [Working Context](#working-context)

**Architecture Source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access) — [Push Access](ARCHITECTURE.md#push-access)

#### Validated Knowledge

**Definition:** Knowledge accepted as sufficiently reliable for its stated purpose through accountable validation.

**Responsibility:** Establish what the company currently accepts as reliable.

**Is NOT**

- Validation is purpose- and context-dependent and does not by itself require retention.

**Related Concepts:** [Company Artifact](#company-artifact), [Evidence](#evidence), [Working Knowledge](#working-knowledge)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [Validated Knowledge](ARCHITECTURE.md#validated-knowledge)

#### Working Context

**Definition:** The smallest sufficient set of organizational knowledge, current Company State, and applicable authorization information required for one activity.

**Responsibility:** Give an authorized human or AI system sufficient, current context for bounded work.

**Is NOT**

- It is temporary and activity-specific, not Company Memory, a permanent dossier, or unrestricted access.

**Related Concepts:** [Company State](#company-state), [Context Delivery](#context-delivery), [Context Selection](#context-selection), [Controlled Execution](#controlled-execution), [Information Classification](#information-classification), [Knowledge](#knowledge-1), [Knowledge Access](#knowledge-access), [Knowledge Retrieval](#knowledge-retrieval), [Knowledge Synthesis](#knowledge-synthesis), [System Work](#system-work)

**Architecture Source:** [Knowledge Access](ARCHITECTURE.md#knowledge-access) — [Working Context](ARCHITECTURE.md#working-context)

#### Working Knowledge

**Definition:** Current analysis, hypotheses, interpretations, and developing understanding.

**Responsibility:** Support exploration before sufficient validation.

**Is NOT**

- It may be incomplete or wrong and is not automatically retained.

**Related Concepts:** [Evidence](#evidence), [Validated Knowledge](#validated-knowledge), [Working Context](#working-context)

**Architecture Source:** [Company Memory](ARCHITECTURE.md#company-memory) — [Working Knowledge](ARCHITECTURE.md#working-knowledge)

### Capabilities

#### Capability History

**Definition:** A durable, governed organizational record preserving sufficient Evidence to understand how a capability performed over time.

**Responsibility:** Support qualification, comparison, review, and improvement across relevant contexts and implementations.

**Is NOT**

- It is not an unrestricted permanent copy of operational data and does not automatically qualify replacement implementations.

**Related Concepts:** [Company Artifact](#company-artifact), [Evidence](#evidence), [Operational Confidence](#operational-confidence)

**Architecture Source:** [Operational Confidence](ARCHITECTURE.md#operational-confidence) — [Capability History](ARCHITECTURE.md#capability-history)

#### Capability Improvement

**Definition:** The evidence-based responsibility for identifying how an organizational capability should improve over time.

**Responsibility:** Identify improvement opportunities and possible causes across knowledge, context, policy, process, human guidance, and implementations.

**Is NOT**

- It does not select, authorize, or execute an improvement; selected changes follow applicable governance and the Operating Cycle.

**Related Concepts:** [Company Capability](#company-capability), [Evidence](#evidence), [Operational Confidence](#operational-confidence)

**Architecture Source:** [Operational Confidence](ARCHITECTURE.md#operational-confidence) — [Capability Improvement](ARCHITECTURE.md#capability-improvement)

#### Company Capability

**Definition:** A defined organizational ability that enables the organization to perform a specific class of work.

**Responsibility:** Express what the company can do independently of who or what currently performs it.

**Is NOT**

- A capability is not a team, role, tool, Agent, workflow, or current implementation.

**Related Concepts:** [Controlled Execution](#controlled-execution), [Operational Confidence](#operational-confidence), [Standing Authorization](#standing-authorization)

**Architecture Source:** [Company Capabilities](ARCHITECTURE.md#company-capabilities) — [Company Capability Definition](ARCHITECTURE.md#company-capability-definition)

#### Confidence Profile

**Definition:** The maintained representation of Operational Confidence for a bounded capability context.

**Responsibility:** Record evaluated dimensions, evidence scope, limitations, and review conditions.

**Is NOT**

- A single score cannot represent all contexts or dimensions.

**Related Concepts:** [Capability History](#capability-history), [Company Capability](#company-capability), [Operational Confidence](#operational-confidence)

**Architecture Source:** [Operational Confidence](ARCHITECTURE.md#operational-confidence) — [Confidence Profile](ARCHITECTURE.md#confidence-profile)

#### Operational Confidence

**Definition:** Context-specific, evidence-based confidence that a Company Capability can produce acceptable outcomes within defined boundaries.

**Responsibility:** Support authorization decisions and identify capability improvement opportunities.

**Is NOT**

- It is not universal, permanent, authority, or a property of implementation identity alone.

**Related Concepts:** [Capability History](#capability-history), [Capability Improvement](#capability-improvement), [Company Capability](#company-capability), [Confidence Profile](#confidence-profile), [Standing Authorization](#standing-authorization)

**Architecture Source:** [Operational Confidence](ARCHITECTURE.md#operational-confidence) — [Operational Confidence Definition](ARCHITECTURE.md#operational-confidence-definition)

### Operation

#### Company State

**Definition:** The explicit, current representation of operational truth appropriate to the company.

**Responsibility:** Give humans and authorized AI systems the same current operational basis.

**Is NOT**

- It is not Company Memory, documentation, or historical knowledge.

**Related Concepts:** [Company Memory](#company-memory), [Evidence](#evidence), [Knowledge Access](#knowledge-access), [Organizational Event](#organizational-event), [System of Record](#system-of-record), [Working Context](#working-context)

**Architecture Source:** [Company State](ARCHITECTURE.md#company-state) — [Company State Purpose](ARCHITECTURE.md#company-state-purpose)

#### Controlled Execution

**Definition:** The capability that performs admitted, authorized organizational work within defined boundaries.

**Responsibility:** Coordinate execution, preserve case consistency, observe work, and capture outcomes.

**Is NOT**

- It does not create its own authority or admit unlimited work.

**Related Concepts:** [Company Capability](#company-capability), [Evidence](#evidence), [Intent](#intent), [Operating Cycle](#operating-cycle), [Organizational Event](#organizational-event), [Outcome](#outcome), [System Work](#system-work), [Work Admission](#work-admission), [Working Context](#working-context)

**Architecture Source:** [Controlled Execution](ARCHITECTURE.md#controlled-execution) — [Controlled Execution Definition](ARCHITECTURE.md#controlled-execution-definition)

#### Intent

**Definition:** Explicit organizational work to be performed.

**Responsibility:** Provide the work definition passed toward authorization, admission, and execution.

**Is NOT**

- Intent is not authority, implementation, admission, or execution.

**Related Concepts:** [Controlled Execution](#controlled-execution), [Intent Generation](#intent-generation), [Operating Cycle](#operating-cycle), [Work Admission](#work-admission)

**Architecture Source:** [Operating Cycle](ARCHITECTURE.md#operating-cycle) — [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence)

#### Intent Generation

**Definition:** The transformation of organizational Knowledge into explicit organizational work.

**Responsibility:** Convert relevant organizational understanding into Intent.

**Is NOT**

- It does not itself authorize execution.

**Related Concepts:** [Decision Mandate](#decision-mandate), [Intent](#intent), [Knowledge](#knowledge-1), [Operating Cycle](#operating-cycle), [Organizational Event](#organizational-event)

**Architecture Source:** [Operating Cycle](ARCHITECTURE.md#operating-cycle) — [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence)

#### Operating Cycle

**Definition:** The repeating organizational sequence that turns Evidence and Knowledge into accountable action and learning.

**Responsibility:** Connect sensing, understanding, Intent, execution, outcomes, and learning.

**Is NOT**

- A single company-wide serial process; each cycle is scoped to one Intent, and cycles may run concurrently.

**Related Concepts:** [Controlled Execution](#controlled-execution), [Evidence](#evidence), [Intent](#intent), [Intent Generation](#intent-generation), [Knowledge](#knowledge-1), [Outcome](#outcome)

**Architecture Source:** [Operating Cycle](ARCHITECTURE.md#operating-cycle) — [Operating Cycle Definition](ARCHITECTURE.md#operating-cycle-definition)

#### Organizational Event

**Definition:** An attributable, observable occurrence or change of state significant to the organization.

**Responsibility:** Make relevant organizational change observable to State, Knowledge Access, and Operating Cycles.

**Is NOT**

- An event describes change; it does not automatically become Evidence, create Intent, authorize work, or perform work.

**Related Concepts:** [Company State](#company-state), [Controlled Execution](#controlled-execution), [Evidence](#evidence), [Intent Generation](#intent-generation), [Push Access](#push-access)

**Architecture Source:** [Organizational Events](ARCHITECTURE.md#organizational-events) — [Organizational Event Definition](ARCHITECTURE.md#organizational-event-definition)

#### Outcome

**Definition:** The observed result of Controlled Execution.

**Responsibility:** Close the learning loop by making results available as Evidence.

**Is NOT**

- An Outcome does not automatically create another Intent or Company Memory.

**Related Concepts:** [Controlled Execution](#controlled-execution), [Evidence](#evidence), [Operating Cycle](#operating-cycle)

**Architecture Source:** [Controlled Execution](ARCHITECTURE.md#controlled-execution) — [Controlled Execution Outcomes](ARCHITECTURE.md#controlled-execution-outcomes)

#### Session Work

**Definition:** Work performed within an active human-controlled session.

**Responsibility:** Support bounded interactive work.

**Is NOT**

- Work that continues independently of the active human-controlled session.

**Related Concepts:** [Company Execution Environment](#company-execution-environment), [System Work](#system-work)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Session Work and System Work](ARCHITECTURE.md#session-work-and-system-work)

#### System Work

**Definition:** Work performed through company-controlled systems beyond a single interactive session.

**Responsibility:** Execute authorized work with durable context and controls.

**Is NOT**

- It does not grant itself authority.

**Related Concepts:** [Controlled Execution](#controlled-execution), [Persistent Execution Environment](#persistent-execution-environment), [Working Context](#working-context)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Session Work and System Work](ARCHITECTURE.md#session-work-and-system-work)

#### Work Admission

**Definition:** The decision boundary that determines whether authorized Intent may enter execution now.

**Responsibility:** Protect readiness, capacity, priority, and coordination constraints.

**Is NOT**

- Authorization alone does not guarantee immediate admission.

**Related Concepts:** [Company State](#company-state), [Controlled Execution](#controlled-execution), [Intent](#intent)

**Architecture Source:** [Controlled Execution](ARCHITECTURE.md#controlled-execution) — [Work Admission](ARCHITECTURE.md#work-admission)

### Governance

#### Access Boundary

**Definition:** The boundary through which identities or systems may reach company capabilities and data.

**Responsibility:** Restrict access paths to justified, controlled channels.

**Is NOT**

- It does not require public inbound access.

**Related Concepts:** [Company Execution Environment](#company-execution-environment), [Information Classification](#information-classification), [Trust Domain](#trust-domain)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Access Boundary](ARCHITECTURE.md#access-boundary)

#### Decision Mandate

**Definition:** A bounded assignment of decision domain, purpose, outcome, authority, accountability, approval, access, escalation, and review.

**Responsibility:** Route consequential proposals to explicit accountable human authority.

**Is NOT**

- It does not remove statutory, legal, contractual, emergency, or safety authority.

**Related Concepts:** [Knowledge Access](#knowledge-access), [Mandate Holder](#mandate-holder), [Mandate Registry](#mandate-registry), [Proposal Evaluation](#proposal-evaluation), [Qualified Reviewer](#qualified-reviewer), [Standing Authorization](#standing-authorization)

**Architecture Source:** [Decision Mandates](ARCHITECTURE.md#decision-mandates) — [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates)

#### Founder Continuity

**Definition:** Founder Continuity defines how organizational accountability, authority, organizational knowledge, and operational continuity are preserved when the primary accountable individual becomes unavailable. It applies to the primary accountable organizational role and is not limited to a legal founder.

**Responsibility:** Preserve organizational accountability, authority, knowledge, access, and operability when the primary accountable individual is temporarily or permanently unavailable.

**Is NOT**

- Technical disaster recovery, cybersecurity, or infrastructure recovery.
- Password management, backup technologies, or a country-specific legal succession procedure.
- Automatic transfer of authority or access.
- Automatic inheritance of Operational Confidence or authorization.
- Standing Authorization or Company Memory; neither individually replaces Founder Continuity.

**Related Concepts:** [Company Execution Environment](#company-execution-environment), [Company Identity](#company-identity), [Company Memory](#company-memory), [Company State](#company-state), [Decision Mandate](#decision-mandate), [Information Classification](#information-classification), [Operational Confidence](#operational-confidence), [Standing Authorization](#standing-authorization)

**Architecture Source:** [Founder Continuity](ARCHITECTURE.md#founder-continuity) — [Founder Continuity Definition](ARCHITECTURE.md#founder-continuity-definition)

#### Information Class

**Definition:** One of the Architecture's general sharing classes: Company-visible, Mandate-restricted, or Secret.

**Responsibility:** Express the permitted organizational audience for information.

**Is NOT**

- Classification does not itself grant decision authority or imply unrestricted access.

**Related Concepts:** [Access Boundary](#access-boundary), [Information Classification](#information-classification), [Working Context](#working-context)

**Architecture Source:** [Information Classification](ARCHITECTURE.md#information-classification) — [Information Classes](ARCHITECTURE.md#information-classes)

#### Information Classification

**Definition:** The classification of information before distribution to humans or AI systems.

**Responsibility:** Maximize justified transparency while minimizing unnecessary exposure.

**Is NOT**

- It defines what may be shared, not who decides.

**Related Concepts:** [Decision Mandate](#decision-mandate), [Information Class](#information-class), [Knowledge Access](#knowledge-access), [Working Context](#working-context)

**Architecture Source:** [Information Classification](ARCHITECTURE.md#information-classification) — [Information Classification Purpose](ARCHITECTURE.md#information-classification-purpose)

#### Mandate Holder

**Definition:** The accountable human authorized to make company decisions within a Decision Mandate boundary.

**Responsibility:** Exercise bounded company decision authority.

**Is NOT**

- Ordinary contribution does not make a person the Mandate Holder.

**Related Concepts:** [Decision Mandate](#decision-mandate), [Qualified Reviewer](#qualified-reviewer)

**Architecture Source:** [Decision Mandates](ARCHITECTURE.md#decision-mandates) — [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates)

#### Mandate Registry

**Definition:** The authoritative durable record of active Decision Mandates.

**Responsibility:** Make decision authority explicit, transferable, reviewable, and recoverable.

**Is NOT**

- It is not an organization chart, hierarchy, employee directory, communication platform, or a decision-history store.

**Related Concepts:** [Company Artifact](#company-artifact), [Company Memory](#company-memory), [Decision Mandate](#decision-mandate)

**Architecture Source:** [Decision Mandates](ARCHITECTURE.md#decision-mandates) — [Mandate Registry](ARCHITECTURE.md#mandate-registry)

#### Qualified Reviewer

**Definition:** A person or organization providing specialist Evidence or professional judgment.

**Responsibility:** Inform an accountable decision where specialist qualification is needed.

**Is NOT**

- Review normally informs but does not replace the company's accountable Decision Mandate unless law requires otherwise.

**Related Concepts:** [Decision Mandate](#decision-mandate), [Evidence](#evidence), [Mandate Holder](#mandate-holder)

**Architecture Source:** [Decision Mandates](ARCHITECTURE.md#decision-mandates) — [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates)

#### Role

**Definition:** A broad organizational label that may combine title, status, activities, authority, and representation.

**Responsibility:** Provide a label only where organizational or external needs justify it.

**Is NOT**

- It is not the preferred unit for routing bounded operational authority.

**Related Concepts:** [Decision Mandate](#decision-mandate), [Mandate Holder](#mandate-holder)

**Architecture Source:** [Decision Mandates](ARCHITECTURE.md#decision-mandates) — [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates)

#### Standing Authorization

**Definition:** A revocable governance decision permitting recurring actions through a Company Capability within explicit boundaries.

**Responsibility:** Avoid repeated approval without abandoning accountable authority.

**Is NOT**

- It is not created by confidence, broad purpose, implementation identity, or convenience.

**Related Concepts:** [Company Capability](#company-capability), [Controlled Execution](#controlled-execution), [Decision Mandate](#decision-mandate), [Decision Record](#decision-record), [Operational Confidence](#operational-confidence)

**Architecture Source:** [Standing Authorization](ARCHITECTURE.md#standing-authorization) — [Standing Authorization Definition](ARCHITECTURE.md#standing-authorization-definition)

#### Trust Domain

**Definition:** A security boundary separating company-only identities, systems, data, and recovery paths.

**Responsibility:** Limit cross-domain compromise and unintended access.

**Is NOT**

- It is not equivalent to secrecy or physical isolation.

**Related Concepts:** [Access Boundary](#access-boundary), [Company Execution Environment](#company-execution-environment), [Information Classification](#information-classification)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Trust Domain Isolation](ARCHITECTURE.md#trust-domain-isolation)

### Intelligence

#### Continuous Environmental Intelligence

**Definition:** An organizational capability that continuously observes relevant changes in the external environment and transforms significant observations into organizational Evidence.

**Responsibility:** Ensure relevant external change becomes observable to the organization by producing attributable Evidence from significant observations.

**Is NOT**

- Proposal Evaluation.
- Organizational prioritization.
- Decision-making.
- Authorization.
- Execution.
- Recommendation generation.
- Internal operational monitoring.

**Boundary:** Continuous Environmental Intelligence asks whether external change is significant enough to become organizational Evidence. Proposal Evaluation asks what organizational response, if any, should be considered. Downstream processing is not automatic.

**Related Concepts:** [Evidence](#evidence), [External World](#external-world)

**Architecture Source:** [Continuous Environmental Intelligence](ARCHITECTURE.md#continuous-environmental-intelligence) — [Environmental Intelligence Definition](ARCHITECTURE.md#environmental-intelligence-definition)

#### Proposal Evaluation

**Definition:** The evaluation of a supported proposal using the Impact and Urgency dimensions and a Response Class before accountable routing.

**Responsibility:** Make prioritization explicit before a proposal reaches decision authority.

**Is NOT**

- Priority does not authorize execution and not every proposal becomes Intent.

**Related Concepts:** [Decision Mandate](#decision-mandate), [Evidence](#evidence), [Response Class](#response-class)

**Architecture Source:** [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation)

#### Response Class

**Definition:** The proposal-local response posture P0 through P4.

**Responsibility:** Communicate the required response posture after evaluation.

**Is NOT**

- P0 through P3 prioritize an active or potential response; P4 records no active response. It is not a company-wide priority taxonomy and does not grant authority.

**Related Concepts:** [Decision Mandate](#decision-mandate), [Proposal Evaluation](#proposal-evaluation)

**Architecture Source:** [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation)

### Architecture

#### AI-First Company

**Definition:** An organization whose organizational architecture is intentionally designed for durable human–AI collaboration.

**Responsibility:** Organize outcomes, capabilities, authority, and accountability for AI-first operation.

**Is NOT**

- AI systems do not replace accountable human leadership.

**Related Concepts:** [Company Capability](#company-capability), [Controlled Execution](#controlled-execution), [Decision Mandate](#decision-mandate)

**Architecture Source:** [What is an AI-First Company?](ARCHITECTURE.md#what-is-an-ai-first-company) — [AI-First Company Definition](ARCHITECTURE.md#ai-first-company-definition)

#### Company Execution Environment

**Definition:** The controlled environment in which company work is performed and company assets are handled.

**Responsibility:** Provide bounded, attributable, recoverable execution.

**Is NOT**

- It is a capability pattern, not a prescribed device, platform, or stack.

**Related Concepts:** [Persistent Execution Environment](#persistent-execution-environment), [Recoverability](#recoverability), [Trust Domain](#trust-domain)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Company Execution Environment Concepts](ARCHITECTURE.md#company-execution-environment-concepts)

#### Data Custody

**Definition:** The accountable control of company data, including access, retention, portability, and recovery.

**Responsibility:** Keep company data controlled and recoverable.

**Is NOT**

- Custody is not necessarily physical hosting or exclusive storage.

**Related Concepts:** [Recoverability](#recoverability), [System of Record](#system-of-record)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Data Custody and Systems of Record](ARCHITECTURE.md#data-custody-and-systems-of-record)

#### Persistent Execution Environment

**Definition:** A Company Execution Environment that retains sufficient authorized state or has a tested recovery path for work to resume across sessions and disruptions.

**Responsibility:** Preserve execution continuity across interruptions.

**Is NOT**

- Persistence requires neither continuous nor unattended operation and does not imply public inbound access.

**Related Concepts:** [Company Execution Environment](#company-execution-environment), [Recoverability](#recoverability), [System Work](#system-work)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Company Execution Environment Concepts](ARCHITECTURE.md#company-execution-environment-concepts)

#### Recoverability

**Definition:** The ability to restore required company operation, access, and data after loss or failure.

**Responsibility:** Make continuity testable rather than assumed.

**Is NOT**

- Copies without validated restoration do not establish recoverability.

**Related Concepts:** [Company Execution Environment](#company-execution-environment), [Company Memory](#company-memory), [Data Custody](#data-custody)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Recoverability](ARCHITECTURE.md#recoverability)

#### System of Record

**Definition:** The authoritative source for a defined class of information.

**Responsibility:** Establish where authoritative information for a bounded class originates.

**Is NOT**

- It is not automatically Company State or Company Memory; synchronized, replicated, or cached copies are not automatically systems of record.

**Related Concepts:** [Data Custody](#data-custody), [Evidence](#evidence)

**Architecture Source:** [Company Execution Environment](ARCHITECTURE.md#company-execution-environment) — [Data Custody and Systems of Record](ARCHITECTURE.md#data-custody-and-systems-of-record)

## Part 2 — Alphabetical Index

| Concept | Domain |
|---|---|
| [AI-First Company](#ai-first-company) | Architecture |
| [Access Boundary](#access-boundary) | Governance |
| [Archive](#archive) | Knowledge |
| [Brand Identity](#brand-identity) | Identity |
| [Canonical Representation](#canonical-representation) | Knowledge |
| [Capability History](#capability-history) | Capabilities |
| [Capability Improvement](#capability-improvement) | Capabilities |
| [Company Artifact](#company-artifact) | Knowledge |
| [Company Capability](#company-capability) | Capabilities |
| [Company Execution Environment](#company-execution-environment) | Architecture |
| [Company Identity](#company-identity) | Identity |
| [Company Memory](#company-memory) | Knowledge |
| [Company State](#company-state) | Operation |
| [Confidence Profile](#confidence-profile) | Capabilities |
| [Context Delivery](#context-delivery) | Knowledge |
| [Context Selection](#context-selection) | Knowledge |
| [Continuous Environmental Intelligence](#continuous-environmental-intelligence) | Intelligence |
| [Controlled Execution](#controlled-execution) | Operation |
| [Data Custody](#data-custody) | Architecture |
| [Decision Mandate](#decision-mandate) | Governance |
| [Decision Record](#decision-record) | Knowledge |
| [Derived Representation](#derived-representation) | Knowledge |
| [Evidence](#evidence) | Knowledge |
| [External World](#external-world) | Knowledge |
| [Financial Identity](#financial-identity) | Identity |
| [Founder Continuity](#founder-continuity) | Governance |
| [Information Class](#information-class) | Governance |
| [Information Classification](#information-classification) | Governance |
| [Intent](#intent) | Operation |
| [Intent Generation](#intent-generation) | Operation |
| [Knowledge](#knowledge-1) | Knowledge |
| [Knowledge Access](#knowledge-access) | Knowledge |
| [Knowledge Lifecycle](#knowledge-lifecycle) | Knowledge |
| [Knowledge Representation](#knowledge-representation) | Knowledge |
| [Knowledge Retrieval](#knowledge-retrieval) | Knowledge |
| [Knowledge Synthesis](#knowledge-synthesis) | Knowledge |
| [Legal Identity](#legal-identity) | Identity |
| [Mandate Holder](#mandate-holder) | Governance |
| [Mandate Registry](#mandate-registry) | Governance |
| [Operating Cycle](#operating-cycle) | Operation |
| [Operational Confidence](#operational-confidence) | Capabilities |
| [Organizational Event](#organizational-event) | Operation |
| [Outcome](#outcome) | Operation |
| [Persistent Execution Environment](#persistent-execution-environment) | Architecture |
| [Product Identity](#product-identity) | Identity |
| [Proposal Evaluation](#proposal-evaluation) | Intelligence |
| [Pull Access](#pull-access) | Knowledge |
| [Push Access](#push-access) | Knowledge |
| [Qualified Reviewer](#qualified-reviewer) | Governance |
| [Recoverability](#recoverability) | Architecture |
| [Response Class](#response-class) | Intelligence |
| [Role](#role) | Governance |
| [Session Work](#session-work) | Operation |
| [Standing Authorization](#standing-authorization) | Governance |
| [System Work](#system-work) | Operation |
| [System of Record](#system-of-record) | Architecture |
| [Trust Domain](#trust-domain) | Governance |
| [Validated Knowledge](#validated-knowledge) | Knowledge |
| [Work Admission](#work-admission) | Operation |
| [Working Context](#working-context) | Knowledge |
| [Working Knowledge](#working-knowledge) | Knowledge |
