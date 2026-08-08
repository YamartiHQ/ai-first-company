# Architecture Knowledge Graph

## Purpose

This document is a derived semantic representation of the validated concepts and relationships in the AI-First Company Architecture. It makes the architecture machine-readable in principle and can support glossary generation, architecture diagrams, semantic navigation, consistency validation, dependency and impact analysis, Architecture coverage analysis, explainable downstream reasoning, and validation scenarios.

This document does not implement those uses. It remains intentionally conceptual, vendor-neutral, and implementation-independent.

## Authority and Source-of-Truth Rule

[ARCHITECTURE.md](ARCHITECTURE.md) is the authoritative source of Architecture concepts, responsibilities, boundaries, and relationships. [PROJECT.md](../PROJECT.md) governs the repository and its evolution. This Knowledge Graph is derived from those sources and cannot redefine, extend, or override them.

If this document conflicts with `ARCHITECTURE.md`, `ARCHITECTURE.md` is authoritative. A graph entry without traceable Architecture support is invalid, even if it would be useful to an implementation.

## Graph Model

The graph uses three conceptual elements:

1. **Concept Node** — a validated Architecture concept with an organizational meaning or boundary.
2. **Relationship Edge** — a directional semantic relationship supported by the Architecture.
3. **Concept Attribute** — concise metadata such as the authoritative definition, organizational responsibility, boundary, lifecycle behavior, source section, related concepts, common confusion, stability status, or permitted specialization.

The graph describes organizational meaning. It does not define a technical schema, serialization format, storage model, query language, API, or product behavior.

### Relationship status

- **Explicit** — stated directly by the Architecture.
- **Derived** — logically necessary to connect multiple explicit Architecture statements without changing their meaning.
- **Illustrative** — useful for explanation or possible future extension, but not part of the authoritative graph.

Only Explicit and carefully justified Derived edges appear in the authoritative Relationship Catalog.

Authoritative inventory: **61 Concept Nodes**, **77 Explicit relationships**, **5 Derived relationships**, and **27 controlled relationship types**. Validated properties, evaluation dimensions, responsibilities, and illustrative material are excluded from these counts.

![Selected Architecture Concept families covering foundations, knowledge and context, capabilities and operation, and governance and evolution.](diagrams/company-ontology-overview.png)

*Selected Concept families for orientation. The catalogs below remain the complete derived semantic representation.*

## Concept Catalog

All nodes below are stable only to the extent supported by their cited Architecture sections. “Boundary” records the most important exclusion; it is not a complete restatement of the chapter.

### Organization, identity, and execution environment

| Concept | Concise definition | Primary organizational responsibility | Boundary | Authoritative source | Immediately related concepts |
|---|---|---|---|---|---|
| AI-First Company | An organization whose organizational architecture is intentionally designed for durable human–AI collaboration. | Organize outcomes, capabilities, authority, and accountability for AI-first operation. | AI systems do not replace accountable human leadership. | [AI-First Company Definition](ARCHITECTURE.md#ai-first-company-definition) | Company Capability, Decision Mandate, Controlled Execution |
| Company Identity | The identity through which the company is recognized and represented. | Maintain a coherent company identity across independent identity systems. | It is distinct from Product Identity and legal availability is not established by one source. | [Company Identity and Product Identity](ARCHITECTURE.md#company-identity-and-product-identity) | Product Identity, Brand Identity, Legal Identity |
| Product Identity | The identity of a product offered by the company. | Identify a product without conflating it with the company. | It need not equal Company Identity. | [Company Identity and Product Identity](ARCHITECTURE.md#company-identity-and-product-identity) | Company Identity, Brand Identity |
| Brand Identity | Recognizable name and visual elements associated with a company or product. | Identify brand elements that may require conflict review. | It does not prescribe branding or establish legal availability. | [Brand Identity](ARCHITECTURE.md#brand-identity) | Company Identity, Product Identity, Evidence |
| Legal Identity | The legally recognized company identity. | Carry statutory, contractual, and accountable company existence. | It is distinct from Financial Identity. | [Legal Identity and Financial Identity](ARCHITECTURE.md#legal-identity-and-financial-identity) | Company Identity, Financial Identity |
| Financial Identity | The operational financial identity needed for company payments and paid dependencies. | Enable attributable business financial operation. | It does not itself establish Legal Identity. | [Legal Identity and Financial Identity](ARCHITECTURE.md#legal-identity-and-financial-identity) | Legal Identity, Company Execution Environment |
| Company Execution Environment | The controlled environment in which company work is performed and company assets are handled. | Provide bounded, attributable, recoverable execution. | It is a capability pattern, not a prescribed device, platform, or stack. | [Company Execution Environment Concepts](ARCHITECTURE.md#company-execution-environment-concepts) | Persistent Execution Environment, Trust Domain, Recoverability |
| Persistent Execution Environment | A Company Execution Environment that retains sufficient authorized state or has a tested recovery path for work to resume across sessions and disruptions. | Preserve execution continuity across interruptions. | Persistence requires neither continuous nor unattended operation and does not imply public inbound access. | [Company Execution Environment Concepts](ARCHITECTURE.md#company-execution-environment-concepts) | Company Execution Environment, System Work, Recoverability |
| Session Work | Work performed within an active human-controlled session. | Support bounded interactive work. | It ends with, or remains dependent on, the active session. | [Session Work and System Work](ARCHITECTURE.md#session-work-and-system-work) | System Work, Company Execution Environment |
| System Work | Work performed through company-controlled systems beyond a single interactive session. | Execute authorized work with durable context and controls. | It does not grant itself authority. | [Session Work and System Work](ARCHITECTURE.md#session-work-and-system-work) | Controlled Execution, Working Context, Persistent Execution Environment |
| Trust Domain | A security boundary separating company-only identities, systems, data, and recovery paths. | Limit cross-domain compromise and unintended access. | It is not equivalent to secrecy or physical isolation. | [Trust Domain Isolation](ARCHITECTURE.md#trust-domain-isolation) | Company Execution Environment, Access Boundary, Information Classification |
| Data Custody | The accountable control of company data, including access, retention, portability, and recovery. | Keep company data controlled and recoverable. | Custody is not necessarily physical hosting or exclusive storage. | [Data Custody and Systems of Record](ARCHITECTURE.md#data-custody-and-systems-of-record) | System of Record, Recoverability |
| System of Record | The authoritative source for a defined class of information. | Establish where authoritative information for a bounded class originates. | It is not automatically Company State or Company Memory; synchronized, replicated, or cached copies are not automatically systems of record. | [Data Custody and Systems of Record](ARCHITECTURE.md#data-custody-and-systems-of-record) | Evidence, Data Custody |
| Access Boundary | The boundary through which identities or systems may reach company capabilities and data. | Restrict access paths to justified, controlled channels. | It does not require public inbound access. | [Access Boundary](ARCHITECTURE.md#access-boundary) | Trust Domain, Information Classification, Company Execution Environment |
| Recoverability | The ability to restore required company operation, access, and data after loss or failure. | Make continuity testable rather than assumed. | Copies without validated restoration do not establish recoverability. | [Recoverability](ARCHITECTURE.md#recoverability) | Company Execution Environment, Data Custody, Company Memory |

### Knowledge, representation, and access

| Concept | Concise definition | Primary organizational responsibility | Boundary | Authoritative source | Immediately related concepts |
|---|---|---|---|---|---|
| Knowledge Lifecycle | The governed progression from the External World through Evidence and evaluated knowledge to retained artifacts or archive. | Keep epistemic status and retention decisions explicit. | Lifecycle stages are not automatic promotions. | [Knowledge Lifecycle](ARCHITECTURE.md#knowledge-lifecycle) | Evidence, Working Knowledge, Validated Knowledge, Company Artifact, Company Memory, Archive |
| External World | The pre-observation source of conditions, events, experiences, and material from company operations and the surrounding external environment. | Define what may need to be observed before it is intentionally retained as Evidence. | Source material is not Evidence until it has been observed and retained. | [External World](ARCHITECTURE.md#external-world) | Evidence, Continuous Environmental Intelligence |
| Evidence | Observed information retained for evaluation without an accepted conclusion. | Make observations attributable and available for reasoning and review. | Evidence is not automatically Knowledge or Company Memory. | [Evidence](ARCHITECTURE.md#evidence) | Knowledge, Organizational Event, Outcome, Capability History |
| Knowledge | Organizational understanding relevant to a purpose. | Support interpretation and Intent Generation. | It is not automatically validated, durable, authoritative, or a Company Artifact. | [Knowledge Definition](ARCHITECTURE.md#knowledge-definition) | Evidence, Working Knowledge, Validated Knowledge, Intent Generation |
| Working Knowledge | Current analysis, hypotheses, interpretations, and developing understanding. | Support exploration before sufficient validation. | It may be incomplete or wrong and is not automatically retained. | [Working Knowledge](ARCHITECTURE.md#working-knowledge) | Evidence, Validated Knowledge, Working Context |
| Validated Knowledge | Knowledge accepted as sufficiently reliable for its stated purpose through accountable validation. | Establish what the company currently accepts as reliable. | Validation is purpose- and context-dependent and does not by itself require retention. | [Validated Knowledge](ARCHITECTURE.md#validated-knowledge) | Working Knowledge, Company Artifact, Evidence |
| Company Artifact | Validated knowledge intentionally preserved because it has lasting company value. | Preserve durable organizational meaning in reviewable form. | Only material passing the Company Artifact Test belongs; not every record qualifies. | [Company Artifact](ARCHITECTURE.md#company-artifact) | Company Memory, Canonical Representation, Decision Record, Mandate Registry |
| Decision Record | A Company Artifact that preserves a consequential decision and its context. | Retain decision, rationale, evidence, authority, and review conditions where warranted. | It does not require a separate registry concept. | [Decision Records](ARCHITECTURE.md#decision-records) | Company Artifact, Decision Mandate, Company Memory |
| Company Memory | The curated collection of Company Artifacts intentionally preserved by the company. | Preserve enduring identity, knowledge, decisions, and understanding. | It is not an unrestricted activity log, Company State, or current working context. | [Company Memory Definition](ARCHITECTURE.md#company-memory-definition) | Company Artifact, Archive, Company State, Knowledge Representation |
| Archive | Retained Company Artifacts that are no longer operationally active. | Preserve historical or reference value under policy. | Archived does not mean deleted or currently operative. | [Archive](ARCHITECTURE.md#archive) | Company Artifact, Company Memory |
| Knowledge Representation | The organizational form through which a Company Artifact is expressed and used. | Keep authoritative meaning distinct from replaceable representations. | A representation does not independently create authoritative meaning. | [Knowledge Representation](ARCHITECTURE.md#knowledge-representation) | Company Artifact, Canonical Representation, Derived Representation |
| Canonical Representation | The authoritative representation of one Company Artifact. | Preserve the accepted organizational meaning against which other representations are checked. | Each Company Artifact has exactly one canonical representation at a time. | [Canonical Representation](ARCHITECTURE.md#canonical-representation) | Company Artifact, Derived Representation |
| Derived Representation | A replaceable representation produced from the Canonical Representation for a particular consumer or purpose. | Make organizational knowledge usable in additional forms without changing authority. | It remains traceable to the Canonical Representation and must not silently become authoritative. | [Derived Representations](ARCHITECTURE.md#derived-representations) | Canonical Representation, Company Artifact, Knowledge Access |
| Knowledge Access | The capability that prepares the smallest sufficient Working Context for authorized work. | Select, retrieve, synthesize, and deliver relevant organizational knowledge. | It does not make organizational decisions or maximize information volume. | [Knowledge Access](ARCHITECTURE.md#knowledge-access) | Working Context, Context Selection, Knowledge Retrieval, Knowledge Synthesis, Context Delivery |
| Working Context | The smallest sufficient set of organizational knowledge, current Company State, and applicable authorization information required for one activity. | Give an authorized human or AI system sufficient, current context for bounded work. | It is temporary and activity-specific, not Company Memory, a permanent dossier, or unrestricted access. | [Working Context](ARCHITECTURE.md#working-context) | Knowledge Access, Company State, Knowledge, Controlled Execution |
| Pull Access | Knowledge Access initiated in response to a current activity or request. | Prepare context when work asks for it. | It does not imply unrestricted browsing of all organizational information. | [Pull Access](ARCHITECTURE.md#pull-access) | Knowledge Access, Working Context |
| Push Access | Knowledge Access that evaluates an Organizational Event as relevant and updates or delivers the appropriate Working Context. | Maintain relevant context without requiring a prior explicit request. | Push delivery does not expand authorization, and an event does not automatically create Intent or work. | [Push Access](ARCHITECTURE.md#push-access) | Knowledge Access, Organizational Event, Working Context |
| Context Selection | The Knowledge Access capability that determines the smallest sufficient information scope. | Limit Working Context to what the activity needs. | The objective is sufficiency, not maximum information. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) | Working Context, Information Classification |
| Knowledge Retrieval | The Knowledge Access capability that obtains selected information from appropriate organizational sources. | Retrieve relevant knowledge, state, artifacts, and governance information. | It does not prescribe retrieval technology. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) | Company Memory, Company State, Knowledge Representation |
| Knowledge Synthesis | The Knowledge Access capability that organizes retrieved information into coherent context. | Relate information, remove unnecessary material, and resolve organizational context. | It does not make the organizational decision. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) | Working Context, Knowledge Retrieval |
| Context Delivery | The Knowledge Access capability that supplies completed Working Context to the authorized performer. | Deliver sufficient context to the human or AI system doing the work. | Delivery does not grant decision or execution authority. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) | Working Context, Information Classification, Decision Mandate |

### Capabilities, operation, intelligence, and authorization

| Concept | Concise definition | Primary organizational responsibility | Boundary | Authoritative source | Immediately related concepts |
|---|---|---|---|---|---|
| Company Capability | A defined organizational ability that enables the organization to perform a specific class of work. | Express what the company can do independently of who or what currently performs it. | A capability is not a team, role, tool, Agent, workflow, or current implementation. | [Company Capability Definition](ARCHITECTURE.md#company-capability-definition) | Controlled Execution, Operational Confidence, Standing Authorization |
| Operating Cycle | The repeating organizational sequence that turns Evidence and Knowledge into accountable action and learning. | Connect sensing, understanding, Intent, execution, outcomes, and learning. | One cycle is scoped to one Intent; cycles may run concurrently. | [Operating Cycle Definition](ARCHITECTURE.md#operating-cycle-definition) | Evidence, Knowledge, Intent Generation, Intent, Controlled Execution, Outcome |
| Intent Generation | The transformation of organizational Knowledge into explicit organizational work. | Convert relevant organizational understanding into Intent. | It does not itself authorize execution. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) | Knowledge, Intent, Decision Mandate |
| Intent | Explicit organizational work to be performed. | Provide the work definition passed toward authorization, admission, and execution. | Intent is not authority, implementation, admission, or execution. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) | Intent Generation, Controlled Execution, Work Admission |
| Controlled Execution | The capability that performs admitted, authorized organizational work within defined boundaries. | Coordinate execution, preserve case consistency, observe work, and capture outcomes. | It does not create its own authority or admit unlimited work. | [Controlled Execution Definition](ARCHITECTURE.md#controlled-execution-definition) | Intent, Work Admission, Working Context, Company Capability, Outcome |
| Work Admission | The decision boundary that determines whether authorized Intent may enter execution now. | Protect readiness, capacity, priority, and coordination constraints. | Authorization alone does not guarantee immediate admission. | [Work Admission](ARCHITECTURE.md#work-admission) | Intent, Controlled Execution, Company State |
| Outcome | The observed result of Controlled Execution. | Close the learning loop by making results available as Evidence. | An Outcome does not automatically create another Intent or Company Memory. | [Controlled Execution Outcomes](ARCHITECTURE.md#controlled-execution-outcomes) | Controlled Execution, Evidence, Operating Cycle |
| Organizational Event | An attributable, observable occurrence or change of state significant to the organization. | Make relevant organizational change observable to State, Knowledge Access, and Operating Cycles. | An event describes change; it does not automatically become Evidence, create Intent, authorize work, or perform work. | [Organizational Event Definition](ARCHITECTURE.md#organizational-event-definition) | Evidence, Company State, Push Access, Intent Generation |
| Operational Confidence | Context-specific, evidence-based confidence that a Company Capability can produce acceptable outcomes within defined boundaries. | Support authorization decisions and identify capability improvement opportunities. | It is not universal, permanent, authority, or a property of implementation identity alone. | [Operational Confidence Definition](ARCHITECTURE.md#operational-confidence-definition) | Company Capability, Confidence Profile, Capability History, Standing Authorization, Capability Improvement |
| Confidence Profile | The maintained representation of Operational Confidence for a bounded capability context. | Record evaluated dimensions, evidence scope, limitations, and review conditions. | A single score cannot represent all contexts or dimensions. | [Confidence Profile](ARCHITECTURE.md#confidence-profile) | Operational Confidence, Company Capability, Capability History |
| Capability History | A durable, governed organizational record preserving sufficient Evidence to understand how a capability performed over time. | Support qualification, comparison, review, and improvement across relevant contexts and implementations. | It is not an unrestricted permanent copy of operational data and does not automatically qualify replacement implementations. | [Capability History](ARCHITECTURE.md#capability-history) | Evidence, Operational Confidence, Company Artifact |
| Capability Improvement | The evidence-based responsibility for identifying how an organizational capability should improve over time. | Identify improvement opportunities and possible causes across knowledge, context, policy, process, human guidance, and implementations. | It does not select, authorize, or execute an improvement; selected changes follow applicable governance and the Operating Cycle. | [Capability Improvement](ARCHITECTURE.md#capability-improvement) | Operational Confidence, Company Capability, Evidence |
| Standing Authorization | A revocable governance decision permitting recurring actions through a Company Capability within explicit boundaries. | Avoid repeated approval without abandoning accountable authority. | It is not created by confidence, broad purpose, implementation identity, or convenience. | [Standing Authorization Definition](ARCHITECTURE.md#standing-authorization-definition) | Operational Confidence, Company Capability, Decision Mandate, Controlled Execution |
| Continuous Environmental Intelligence | The capability that continuously observes relevant changes in the external environment and transforms significant observations into organizational Evidence. | Make relevant external change observable by producing attributable Evidence from significant observations. | It does not perform Proposal Evaluation, prioritize responses, create proposals, recommend action, decide, authorize, execute, or monitor internal operation. | [Environmental Intelligence Definition](ARCHITECTURE.md#environmental-intelligence-definition) | External World, Evidence |
| Proposal Evaluation | The evaluation of a supported proposal using the Impact and Urgency dimensions and a Response Class before accountable routing. | Make prioritization explicit before a proposal reaches decision authority. | Priority does not authorize execution and not every proposal becomes Intent. | [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) | Evidence, Response Class, Decision Mandate |
| Response Class | The proposal-local response posture P0 through P4. | Communicate the required response posture after evaluation. | P0 through P3 prioritize an active or potential response; P4 records no active response. It is not a company-wide priority taxonomy and does not grant authority. | [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) | Proposal Evaluation, Decision Mandate |

### Authority, information, and current state

| Concept | Concise definition | Primary organizational responsibility | Boundary | Authoritative source | Immediately related concepts |
|---|---|---|---|---|---|
| Role | A broad organizational label that may combine title, status, activities, authority, and representation. | Provide a label only where organizational or external needs justify it. | It is not the preferred unit for routing bounded operational authority. | [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates) | Decision Mandate, Mandate Holder |
| Decision Mandate | A bounded assignment of decision domain, purpose, outcome, authority, accountability, approval, access, escalation, and review. | Route consequential proposals to explicit accountable human authority. | It does not remove statutory, legal, contractual, emergency, or safety authority. | [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates) | Mandate Holder, Qualified Reviewer, Mandate Registry, Standing Authorization |
| Mandate Holder | The accountable human authorized to make company decisions within a Decision Mandate boundary. | Exercise bounded company decision authority. | Ordinary contribution does not make a person the Mandate Holder. | [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates) | Decision Mandate, Qualified Reviewer |
| Qualified Reviewer | A person or organization providing specialist Evidence or professional judgment. | Inform an accountable decision where specialist qualification is needed. | Review normally informs but does not replace the company's accountable Decision Mandate unless law requires otherwise. | [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates) | Decision Mandate, Mandate Holder, Evidence |
| Mandate Registry | The authoritative durable record of active Decision Mandates. | Make decision authority explicit, transferable, reviewable, and recoverable. | It is not an organization chart, hierarchy, employee directory, communication platform, or a decision-history store. | [Mandate Registry](ARCHITECTURE.md#mandate-registry) | Decision Mandate, Company Artifact, Company Memory |
| Founder Continuity | Founder Continuity defines how organizational accountability, authority, organizational knowledge, and operational continuity are preserved when the primary accountable individual becomes unavailable. | Preserve organizational operability across temporary or permanent unavailability of the primary accountable individual. | It applies to the primary accountable organizational role, not only a legal founder. It does not define technical disaster recovery, cybersecurity, infrastructure recovery, password management, backup technologies, or country-specific legal succession, and it does not replace Company Memory, Decision Mandates, Standing Authorization, Company State, Information Classification, Company Identity, Operational Confidence, or the Company Execution Environment. | [Founder Continuity Definition](ARCHITECTURE.md#founder-continuity-definition) | Company Memory, Decision Mandate, Standing Authorization, Company State, Information Classification, Company Identity, Operational Confidence, Company Execution Environment |
| Information Classification | The classification of information before distribution to humans or AI systems. | Maximize justified transparency while minimizing unnecessary exposure. | It defines what may be shared, not who decides. | [Information Classification Purpose](ARCHITECTURE.md#information-classification-purpose) | Information Class, Decision Mandate, Knowledge Access |
| Information Class | One of the Architecture's general sharing classes: Company-visible, Mandate-restricted, or Secret. | Express the permitted organizational audience for information. | Classification does not itself grant decision authority or imply unrestricted access. | [Information Classes](ARCHITECTURE.md#information-classes) | Information Classification, Working Context, Access Boundary |
| Company State | The explicit, current representation of operational truth appropriate to the company. | Give humans and authorized AI systems the same current operational basis. | It is not Company Memory, documentation, or historical knowledge. | [Company State Purpose](ARCHITECTURE.md#company-state-purpose) | Evidence, System of Record, Organizational Event, Company Memory, Working Context |

## Relationship Vocabulary

The vocabulary is directional. Optionality is edge metadata rather than a separate predicate where the underlying relationship meaning is unchanged. Markdown rows mark optional relationships explicitly in their semantic explanation, and the structured block uses `optional: true`. The gated lifecycle relationship `may become` remains distinct because it expresses a conditional change of concept state rather than optional execution of an otherwise identical relationship.

| Relationship | Meaning |
|---|---|
| `is specialization of` | The source is a narrower validated form of the target. |
| `is distinct from` | The source and target must not be collapsed into one concept. |
| `contains` | The source intentionally includes one or more target instances. |
| `has component capability` | The target is a conceptual responsibility within the source capability. |
| `produces` | The source results in or creates the target; edge metadata records when this is optional. |
| `consumes` | The source uses the target as an input. |
| `prepares` | The source assembles the target for a defined purpose. |
| `delivers` | The source supplies the completed target to its authorized consumer. |
| `contributes to` | The source provides input to the target without being sufficient by itself. |
| `may become` | The source can transition to the target only after the target's criteria are met. |
| `informs` | The source supports but does not determine the target. |
| `evaluates` | The source applies its defined assessment responsibility to the target. |
| `identifies` | The source reveals candidate target opportunities without executing them. |
| `authorizes recurring actions through` | The source permits bounded recurring action using the target capability. |
| `constrains` | The source limits the permissible scope or handling of the target. |
| `updates` | The source causes an attributable change to the target; edge metadata records when this is optional. |
| `triggers` | The source starts evaluation by the target without predetermining its result; edge metadata records when this is optional. |
| `is derived from` | The source is generated from and remains traceable to the target. |
| `performs work through` | The source performs organizational work through the target Company Capability. |
| `is executed through` | Authorized instances of the source are performed by the target execution capability. |
| `requires` | The source is valid only when the target governance condition exists. |
| `records` | The source is the authoritative record of target instances. |
| `assigns` | The source determines a target classification under its stated rules. |
| `routes to` | The source sends a proposal to the target authority without granting a decision. |
| `has authoritative representation` | The source has exactly one target representation that carries its accepted meaning. |
| `is represented by` | The source's bounded assessment is maintained in the target. |
| `holds` | The source human carries accountability within the target mandate. |

## Relationship Catalog

Relationship IDs are stable local identifiers rather than ordinal positions. They are not required to form a contiguous sequence.

The limitation column is normative for interpreting the edge. Cardinality is stated only where the Architecture makes it conceptually clear.

### Identity and execution environment edges

| ID | Edge | Status | Semantics, optionality, and limitation | Traceability |
|---|---|---|---|---|
| R02 | Company Identity `is distinct from` Product Identity | Explicit | The identities may be related but need not be the same. | [Company Identity and Product Identity](ARCHITECTURE.md#company-identity-and-product-identity) |
| R03 | Legal Identity `is distinct from` Financial Identity | Explicit | Legal recognition and attributable financial operation remain separate capabilities whose records and changes must be maintained independently. | [Legal Identity and Financial Identity](ARCHITECTURE.md#legal-identity-and-financial-identity) |
| R04 | Persistent Execution Environment `is specialization of` Company Execution Environment | Derived | Persistence means that sufficient authorized state or a tested recovery path survives interruption so work can resume across sessions and disruptions. It requires neither continuous nor unattended operation. | [Specialization: Company Execution Environment Concepts](ARCHITECTURE.md#company-execution-environment-concepts), [Limitation: Availability and Unattended Operation](ARCHITECTURE.md#availability-and-unattended-operation) |
| R05 | System Work `consumes` Working Context | Explicit | System Work requires sufficient company context; context remains temporary and bounded. | [Session Work and System Work](ARCHITECTURE.md#session-work-and-system-work), [Working Context](ARCHITECTURE.md#working-context) |
| R06 | System Work `is executed through` Controlled Execution | Explicit | Only admitted, authorized System Work is executed; System Work does not grant itself authority. | [Session Work and System Work](ARCHITECTURE.md#session-work-and-system-work), [Controlled Execution Definition](ARCHITECTURE.md#controlled-execution-definition) |
| R07 | Trust Domain `constrains` Company Execution Environment | Derived | The execution environment must preserve the applicable security and administrative isolation boundary; isolation does not prescribe a platform. | [Company Execution Environment Concepts](ARCHITECTURE.md#company-execution-environment-concepts), [Trust Domain Isolation](ARCHITECTURE.md#trust-domain-isolation) |
| R09 | Recoverability `constrains` Company Execution Environment | Derived | The environment must preserve the state, recovery path, and alternate capacity required by its recovery responsibility. | [Company Execution Environment Concepts](ARCHITECTURE.md#company-execution-environment-concepts), [Recoverability](ARCHITECTURE.md#recoverability) |

### Knowledge, representation, and access edges

| ID | Edge | Status | Semantics, optionality, and limitation | Traceability |
|---|---|---|---|---|
| R10 | External World `contributes to` Evidence | Explicit | **Optional.** Material from company operations or the surrounding environment becomes Evidence only after observation and retention. | [External World](ARCHITECTURE.md#external-world), [Evidence](ARCHITECTURE.md#evidence) |
| R11 | Evidence `contributes to` Knowledge | Explicit | **Optional.** Evaluation and interpretation are required; Evidence is not automatically Knowledge. | [Knowledge Lifecycle](ARCHITECTURE.md#knowledge-lifecycle), [Evidence](ARCHITECTURE.md#evidence) |
| R12 | Working Knowledge `may become` Validated Knowledge | Explicit | Accountable validation is required for the stated purpose and context. | [Working Knowledge](ARCHITECTURE.md#working-knowledge), [Validated Knowledge](ARCHITECTURE.md#validated-knowledge) |
| R13 | Validated Knowledge `may become` Company Artifact | Explicit | Intentional preservation and the Company Artifact Test are required; retention is not automatic. | [Company Artifact](ARCHITECTURE.md#company-artifact), [Company Artifact Test](ARCHITECTURE.md#company-artifact-test) |
| R14 | Decision Record `is specialization of` Company Artifact | Explicit | Only decision records with lasting company value are Company Artifacts. | [Decision Records](ARCHITECTURE.md#decision-records) |
| R15 | Mandate Registry `is specialization of` Company Artifact | Explicit | The registry is a durable Company Artifact and the authoritative record of active mandates. | [Mandate Registry](ARCHITECTURE.md#mandate-registry) |
| R16 | Company Memory `contains` Company Artifact | Explicit | Company Memory is the curated collection of retained Company Artifacts, not all activity. Cardinality: zero or more artifacts. | [Company Memory Definition](ARCHITECTURE.md#company-memory-definition) |
| R17 | Archive `contains` Company Artifact | Explicit | The contained artifacts are retained but no longer operationally active. | [Archive](ARCHITECTURE.md#archive) |
| R18 | Company Artifact `has authoritative representation` Canonical Representation | Explicit | Cardinality: exactly one canonical representation per artifact at a time. | [Canonical Representation](ARCHITECTURE.md#canonical-representation) |
| R19 | Derived Representation `is derived from` Canonical Representation | Explicit | A Company Artifact may have zero or more derived representations; each remains traceable and non-authoritative. | [Derived Representations](ARCHITECTURE.md#derived-representations) |
| R21 | Knowledge Access `consumes` Company Memory | Explicit | **Optional.** Only relevant, authorized retained knowledge is selected. | [Knowledge Access Inputs](ARCHITECTURE.md#knowledge-access-inputs) |
| R22 | Knowledge Access `consumes` Company State | Explicit | **Optional.** Current State may enter context but remains distinct from durable Memory. | [Knowledge Access Inputs](ARCHITECTURE.md#knowledge-access-inputs) |
| R23 | Knowledge Access `consumes` Knowledge Representation | Explicit | **Optional.** Access uses appropriate representations without changing their authority. | [Relationship to Knowledge Access](ARCHITECTURE.md#relationship-to-knowledge-access), [Knowledge Access Inputs](ARCHITECTURE.md#knowledge-access-inputs) |
| R24 | Knowledge Access `consumes` Information Classification | Explicit | **Optional.** Classification limits what may enter the prepared context. | [Knowledge Access Inputs](ARCHITECTURE.md#knowledge-access-inputs) |
| R25 | Knowledge Access `consumes` Decision Mandate | Explicit | **Optional.** Applicable mandate information supplies decision and authority boundaries; access does not confer them. | [Knowledge Access Inputs](ARCHITECTURE.md#knowledge-access-inputs) |
| R26 | Knowledge Access `prepares` Working Context | Explicit | The result is the smallest sufficient temporary context for one activity. | [Knowledge Access Outcome](ARCHITECTURE.md#knowledge-access-outcome), [Working Context](ARCHITECTURE.md#working-context) |
| R27 | Knowledge Access `has component capability` Context Selection | Explicit | Context Selection determines the smallest sufficient information scope. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) |
| R28 | Knowledge Access `has component capability` Knowledge Retrieval | Explicit | Retrieval obtains selected information from organizational sources. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) |
| R29 | Knowledge Access `has component capability` Knowledge Synthesis | Explicit | Synthesis organizes selected information into coherent context. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) |
| R30 | Knowledge Access `has component capability` Context Delivery | Explicit | Delivery supplies completed context to the authorized performer. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) |
| R31 | Context Selection `contributes to` Working Context | Explicit | Selection is necessary but not sufficient to prepare the context. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) |
| R32 | Knowledge Retrieval `contributes to` Working Context | Explicit | Retrieval supplies selected material; it does not by itself create coherent context. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) |
| R33 | Knowledge Synthesis `contributes to` Working Context | Explicit | Synthesis organizes retrieved material without making organizational decisions. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) |
| R34 | Context Delivery `delivers` Working Context | Explicit | Delivery is to the authorized human or AI system performing the activity and grants no authority. | [Knowledge Access Capabilities](ARCHITECTURE.md#knowledge-access-capabilities) |
| R35 | Working Context `contains` Knowledge | Explicit | Only activity-relevant knowledge is included; the context is temporary. | [Working Context](ARCHITECTURE.md#working-context) |
| R36 | Working Context `contains` Company State | Explicit | Only the state needed for the activity is included; State remains independently authoritative. | [Working Context](ARCHITECTURE.md#working-context) |
| R37 | Push Access `consumes` Organizational Event | Explicit | Only relevant events may initiate context preparation; they do not automatically create work. | [Push Access](ARCHITECTURE.md#push-access), [Relationship to Organizational Events](ARCHITECTURE.md#relationship-to-organizational-events) |

### Operation, evidence, confidence, and authorization edges

| ID | Edge | Status | Semantics, optionality, and limitation | Traceability |
|---|---|---|---|---|
| R39 | Operating Cycle `contains` Evidence | Explicit | Evidence is the starting input to one Intent-scoped cycle and also returns from outcomes. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) |
| R40 | Operating Cycle `contains` Knowledge | Explicit | Knowledge supports understanding within the cycle. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) |
| R41 | Operating Cycle `contains` Intent Generation | Explicit | Intent Generation forms proposed action but does not authorize it. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) |
| R42 | Operating Cycle `contains` Intent | Explicit | One cycle is scoped to one Intent; multiple cycles may run concurrently. | [Operating Cycle Definition](ARCHITECTURE.md#operating-cycle-definition), [Concurrent Operating Cycles](ARCHITECTURE.md#concurrent-operating-cycles) |
| R43 | Operating Cycle `contains` Controlled Execution | Explicit | The cycle performs only admitted and authorized work. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) |
| R44 | Operating Cycle `contains` Outcome | Explicit | The observed result closes the cycle through new Evidence. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) |
| R45 | Intent Generation `consumes` Knowledge | Explicit | Knowledge informs proposed Intent; it does not predetermine action. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) |
| R46 | Intent Generation `produces` Intent | Explicit | The Intent remains subject to accountable authorization and work admission. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence) |
| R47 | Intent `is executed through` Controlled Execution | Explicit | Only authorized and admitted Intent is performed; Intent is not execution. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence), [Controlled Execution Definition](ARCHITECTURE.md#controlled-execution-definition) |
| R48 | Controlled Execution `consumes` Intent | Explicit | Execution preserves the intended outcome and constraints. | [Foundational Responsibilities](ARCHITECTURE.md#foundational-responsibilities) |
| R49 | Controlled Execution `consumes` Working Context | Explicit | Execution receives sufficient temporary context, not unrestricted organizational knowledge. | [Relationship to Other Architecture Capabilities](ARCHITECTURE.md#relationship-to-other-architecture-capabilities-1) |
| R50 | Controlled Execution `performs work through` Company Capability | Explicit | Controlled Execution performs authorized organizational work through applicable Company Capabilities, which remain distinct from their current implementations. | [Relationship to Other Architecture Capabilities](ARCHITECTURE.md#relationship-to-other-architecture-capabilities-1) |
| R51 | Controlled Execution `produces` Outcome | Explicit | The Outcome is captured and made observable. | [Controlled Execution Outcomes](ARCHITECTURE.md#controlled-execution-outcomes) |
| R52 | Controlled Execution `produces` Evidence | Explicit | Execution activity and outcome observations become attributable Evidence when retained. | [Controlled Execution Outcomes](ARCHITECTURE.md#controlled-execution-outcomes) |
| R53 | Outcome `produces` Evidence | Explicit | Outcome Evidence supports learning; it does not automatically produce another Intent. | [Operating Cycle Sequence](ARCHITECTURE.md#operating-cycle-sequence), [Controlled Execution Outcomes](ARCHITECTURE.md#controlled-execution-outcomes) |
| R54 | Work Admission `evaluates` Intent | Derived | Work Admission evaluates whether an already authorized Intent satisfies dependencies, organizational capacity, and execution readiness before entry into execution. It does not grant authority. | [Work Admission](ARCHITECTURE.md#work-admission) |
| R90 | Controlled Execution `has component capability` Work Admission | Explicit | Work Admission evaluates already-authorized Intent for readiness, dependencies, and capacity; it does not grant authority. | [Work Admission](ARCHITECTURE.md#work-admission) |
| R55 | Organizational Event `contributes to` Evidence | Explicit | **Optional.** Significance, attribution, and retention determine whether the event supplies Evidence. | [Organizational Role](ARCHITECTURE.md#organizational-role) |
| R56 | Organizational Event `updates` Company State | Explicit | **Optional.** The update must be attributable; an Organizational Event is not itself the complete Company State. | [Organizational Role](ARCHITECTURE.md#organizational-role), [Company State Changes](ARCHITECTURE.md#company-state-changes) |
| R57 | Organizational Event `triggers` Intent Generation | Explicit | **Optional.** The event may initiate evaluation; it does not automatically create Intent or work. | [Organizational Role](ARCHITECTURE.md#organizational-role) |
| R58 | Controlled Execution `produces` Organizational Event | Explicit | **Optional.** Significant execution occurrences may be recorded as Organizational Events; not every execution detail becomes one. | [Relationship to Other Architecture Capabilities](ARCHITECTURE.md#relationship-to-other-architecture-capabilities-2) |
| R59 | Evidence `contributes to` Capability History | Explicit | Attributable operational Evidence accumulates across relevant contexts and implementations. | [Capability History](ARCHITECTURE.md#capability-history) |
| R60 | Capability History `informs` Operational Confidence | Explicit | History supports context-specific confidence and does not grant authority. | [Capability History](ARCHITECTURE.md#capability-history), [Continuous Evaluation](ARCHITECTURE.md#continuous-evaluation) |
| R61 | Operational Confidence `evaluates` Company Capability | Explicit | Evaluation is bounded by outcome, context, risk, implementation, and current evidence. | [Capability-Specific Confidence](ARCHITECTURE.md#capability-specific-confidence) |
| R62 | Operational Confidence `is represented by` Confidence Profile | Explicit | Multiple dimensions and contexts remain visible; no universal scalar is implied. | [Confidence Profile](ARCHITECTURE.md#confidence-profile) |
| R63 | Operational Confidence `identifies` Capability Improvement | Explicit | Evidence reveals improvement opportunities across the capability, not just its current implementation. | [Capability Improvement](ARCHITECTURE.md#capability-improvement) |
| R64 | Operational Confidence `informs` Standing Authorization | Explicit | Confidence is necessary decision support but never grants authority. | [Relationship to Operational Confidence](ARCHITECTURE.md#relationship-to-operational-confidence) |
| R65 | Standing Authorization `authorizes recurring actions through` Company Capability | Explicit | Authorization is bounded, attributable, reviewable, and revocable. A replacement implementation does not automatically inherit qualification or authorization. | [Standing Authorization Definition](ARCHITECTURE.md#standing-authorization-definition), [Material Implementation Change](ARCHITECTURE.md#material-implementation-change) |
| R66 | Standing Authorization `requires` Decision Mandate | Explicit | An accountable governance decision within the applicable mandate is required. | [Authorization Boundaries](ARCHITECTURE.md#authorization-boundaries), [Standing Authorization Decision Boundaries](ARCHITECTURE.md#standing-authorization-decision-boundaries) |
| R67 | Capability History `produces` Company Artifact | Explicit | **Optional.** A Capability History may produce a Company Artifact only when the retained material possesses lasting organizational value and passes the Company Artifact Test. | [Relationship to Company Memory](ARCHITECTURE.md#relationship-to-company-memory-1) |
| R68 | Standing Authorization `may become` Decision Record | Explicit | The authorization decision may be retained when it has lasting value; the authorization itself is not Company Memory by default. | [Relationship to Company Memory](ARCHITECTURE.md#relationship-to-company-memory-2) |

### Environmental intelligence, proposals, governance, and state edges

| ID | Edge | Status | Semantics, optionality, and limitation | Traceability |
|---|---|---|---|---|
| R69 | Continuous Environmental Intelligence `produces` Evidence | Explicit | Significant external observations become attributable Evidence; other observations do not automatically become Evidence. The capability does not create proposals, prioritize, recommend, decide, authorize, or execute. | [Environmental Intelligence Definition](ARCHITECTURE.md#environmental-intelligence-definition), [Foundational Responsibilities](ARCHITECTURE.md#foundational-responsibilities-1) |
| R73 | Proposal Evaluation `assigns` Response Class | Explicit | P0–P4 supports proposal prioritization only and does not authorize execution. | [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) |
| R74 | Proposal Evaluation `routes to` Decision Mandate | Explicit | The proposal is routed to accountable human authority; not every proposal becomes Intent. | [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) |
| R75 | Mandate Registry `records` Decision Mandate | Explicit | It is the authoritative record of active mandates and their boundaries, holders, review, and transfer state. | [Mandate Registry](ARCHITECTURE.md#mandate-registry) |
| R76 | Mandate Holder `holds` Decision Mandate | Explicit | One human may hold multiple mandates; authority follows the mandate rather than rank. | [Roles and Decision Mandates](ARCHITECTURE.md#roles-and-decision-mandates) |
| R78 | Information Classification `contains` Information Class | Explicit | The model defines three general classes for sharing scope. | [Information Classes](ARCHITECTURE.md#information-classes) |
| R79 | Information Classification `constrains` Working Context | Derived | Context preparation must respect classification and authorized audience; classification does not grant decision authority. | [Knowledge Access Inputs](ARCHITECTURE.md#knowledge-access-inputs), [Information and Decision Authority](ARCHITECTURE.md#information-and-decision-authority) |
| R80 | Company State `is derived from` Evidence | Explicit | State should be derived from authoritative Evidence and systems whenever practical. | [Company State Characteristics](ARCHITECTURE.md#company-state-characteristics) |
| R81 | Company State `is distinct from` Company Memory | Explicit | State answers what is true now; Memory preserves what happened and what was intentionally retained. | [Company State and Company Memory](ARCHITECTURE.md#company-state-and-company-memory) |

### Founder continuity edges

| ID | Edge | Status | Semantics, optionality, and limitation | Traceability |
|---|---|---|---|---|
| R82 | Founder Continuity `consumes` Company Memory | Explicit | Company Memory supports Knowledge Continuity by preserving required organizational knowledge beyond individual memory. It is not sufficient for Founder Continuity and is not redefined by it. | [Founder Continuity Responsibilities](ARCHITECTURE.md#founder-continuity-responsibilities), [Founder Continuity Relationships](ARCHITECTURE.md#founder-continuity-relationships) |
| R83 | Founder Continuity `requires` Decision Mandate | Explicit | Decision Mandates must remain operable or explicitly transferable. No mandate or authority transfers automatically. | [Founder Continuity Responsibilities](ARCHITECTURE.md#founder-continuity-responsibilities), [Founder Continuity Relationships](ARCHITECTURE.md#founder-continuity-relationships) |
| R84 | Standing Authorization `contributes to` Founder Continuity | Explicit | **Optional.** Existing bounded recurring actions may continue where their authorization remains valid. Standing Authorization neither replaces a Decision Mandate nor expands or transfers automatically. | [Founder Continuity Relationships](ARCHITECTURE.md#founder-continuity-relationships) |
| R85 | Company State `informs` Founder Continuity | Explicit | Current unavailability, active mandates, open decisions, and blocked work support continuity decisions. Company State does not itself provide continuity or authority. | [Founder Continuity Relationships](ARCHITECTURE.md#founder-continuity-relationships) |
| R86 | Information Classification `constrains` Founder Continuity | Explicit | Classification continues to constrain continuity-related information and access. It neither grants authority nor declassifies information. | [Founder Continuity Relationships](ARCHITECTURE.md#founder-continuity-relationships) |
| R87 | Company Identity `contributes to` Founder Continuity | Explicit | An identity distinguishable from one individual supports continuity. This relationship does not define ownership transfer or legal succession. | [Founder Continuity Relationships](ARCHITECTURE.md#founder-continuity-relationships) |
| R88 | Operational Confidence `informs` Founder Continuity | Explicit | **Optional.** Confidence may inform whether a Company Capability can continue within established boundaries. A substitute or replacement implementation does not inherit confidence or authorization through this relationship. | [Founder Continuity Relationships](ARCHITECTURE.md#founder-continuity-relationships) |
| R89 | Company Execution Environment `contributes to` Founder Continuity | Explicit | **Optional.** Technical availability and access continuity may support Founder Continuity, but infrastructure recovery alone does not provide organizational continuity. | [Founder Continuity Relationships](ARCHITECTURE.md#founder-continuity-relationships) |

## Subtypes and Specializations

### Validated specializations

| General concept | Validated specialization | Status and boundary | Source |
|---|---|---|---|
| Company Artifact | Decision Record | Explicit specialization; only records with lasting company value qualify. | [Decision Records](ARCHITECTURE.md#decision-records) |
| Company Artifact | Mandate Registry | Explicit specialization; the registry is a durable Company Artifact. | [Mandate Registry](ARCHITECTURE.md#mandate-registry) |
| Company Execution Environment | Persistent Execution Environment | Derived specialization; persistence narrows availability behavior without selecting an implementation. | [Company Execution Environment Concepts](ARCHITECTURE.md#company-execution-environment-concepts) |
| Information Class | Company-visible | Explicit class; broadly available to authorized company participants. | [Information Classes](ARCHITECTURE.md#information-classes) |
| Information Class | Mandate-restricted | Explicit class; limited to responsible mandates and required qualified reviewers. | [Information Classes](ARCHITECTURE.md#information-classes) |
| Information Class | Secret | Explicit class; limited to the minimum necessary identities and systems. | [Information Classes](ARCHITECTURE.md#information-classes) |
| Response Class | P0 Immediate; P1 Required; P2 Recommended; P3 Observe; P4 Closed | Explicit proposal-local classes; not a company-wide priority taxonomy. | [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) |

Context Selection, Knowledge Retrieval, Knowledge Synthesis, and Context Delivery are component capabilities of Knowledge Access, not subtypes. Humans, AI systems, Agents, tools, software, and automation are possible implementations or participants, not Company Capability subtypes.

### Validated properties, evaluation dimensions, and responsibilities

These entries preserve validated Architecture meaning but are not authoritative Concept Nodes. They describe a property, evaluation dimension, or responsibility of an existing concept and are excluded from Concept Node and relationship counts.

| Owning concept | Property, dimension, or responsibility | Kind | Validated meaning | Source |
|---|---|---|---|---|
| Company Memory | Knowledge Independence | Validated property | Company Memory does not depend on one person, AI system, provider, product, runtime, or storage technology. | [Knowledge Independence and Knowledge Portability](ARCHITECTURE.md#knowledge-independence-and-knowledge-portability) |
| Company Memory | Knowledge Portability | Validated property | Required organizational knowledge can be preserved and transferred across implementation changes; portability supports but does not alone establish Knowledge Independence. | [Knowledge Independence and Knowledge Portability](ARCHITECTURE.md#knowledge-independence-and-knowledge-portability) |
| Proposal Evaluation | Impact | Evaluation dimension | The magnitude of a proposal's possible consequence, evaluated independently of Urgency. | [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) |
| Proposal Evaluation | Urgency | Evaluation dimension | The time available before a decision or action is required, evaluated independently of Impact. | [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) |
| Founder Continuity | Accountability Continuity | Validated responsibility | Define how accountable decision-making continues or is deliberately suspended during primary-individual unavailability. | [Founder Continuity Responsibilities](ARCHITECTURE.md#founder-continuity-responsibilities) |
| Founder Continuity | Authority Continuity | Validated responsibility | Keep Decision Mandates operable or transferable through explicit governance without automatic authority transfer. | [Founder Continuity Responsibilities](ARCHITECTURE.md#founder-continuity-responsibilities) |
| Founder Continuity | Operational Continuity | Validated responsibility | Determine which authorized organizational work may continue, pause, or require escalation without broadening authority. | [Founder Continuity Responsibilities](ARCHITECTURE.md#founder-continuity-responsibilities) |
| Founder Continuity | Knowledge Continuity | Validated responsibility | Keep required organizational knowledge available through Company Memory rather than individual memory. | [Founder Continuity Responsibilities](ARCHITECTURE.md#founder-continuity-responsibilities) |
| Founder Continuity | Access Continuity | Validated responsibility | Keep required organizational access available through governed responsibility while preserving the distinction between access and authority. | [Founder Continuity Responsibilities](ARCHITECTURE.md#founder-continuity-responsibilities) |

### Illustrative only

The Architecture gives ordinary examples of Company Artifacts, observation domains, organizational events, impact domains, implementations, and identity evidence sources. These examples do not establish authoritative taxonomies.

Possible patterns such as `Governance Artifact -> Policy -> Standard -> Guideline -> Rule`, `Decision -> Strategic | Operational | Emergency`, or `Knowledge -> Research | Lesson | Reference` remain illustrative. They must not be added as validated nodes or edges unless `ARCHITECTURE.md` first defines their distinct organizational meaning.

## Cross-Cutting Constraints

| Constraint | Graph consequence | Source |
|---|---|---|
| Human accountability | Consequential decisions must terminate at an accountable human Decision Mandate. AI participation never removes human accountability. | [Humans and AI Systems](ARCHITECTURE.md#humans-and-ai-systems), [Decision Mandate Principles](ARCHITECTURE.md#decision-mandate-principles) |
| Authority is separate from information and confidence | Access to information, high Operational Confidence, or high priority cannot grant authority. | [Information and Decision Authority](ARCHITECTURE.md#information-and-decision-authority), [Relationship to Operational Confidence](ARCHITECTURE.md#relationship-to-operational-confidence), [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) |
| Evidence first | Significant observations, decisions, execution, and outcomes remain attributable and reviewable. | [Evidence](ARCHITECTURE.md#evidence), [Operational Confidence Principles](ARCHITECTURE.md#operational-confidence-principles) |
| Non-automatic transitions | Evidence, Knowledge, artifacts, Intent, State changes, authorization, and subsequent work require their own criteria and boundaries. | [Knowledge Lifecycle](ARCHITECTURE.md#knowledge-lifecycle), [Organizational Role](ARCHITECTURE.md#organizational-role), [Proposal Evaluation](ARCHITECTURE.md#proposal-evaluation) |
| Information minimization | Working Context is the smallest sufficient context and respects classification; Secret values remain minimally exposed. | [Knowledge Access Principles](ARCHITECTURE.md#knowledge-access-principles), [Information Classes](ARCHITECTURE.md#information-classes) |
| Implementation independence | Company Capabilities, Company Memory, and organizational authority remain distinct from current people, Agents, tools, vendors, or technical systems. | [Implementation Independence](ARCHITECTURE.md#implementation-independence), [Knowledge Independence and Knowledge Portability](ARCHITECTURE.md#knowledge-independence-and-knowledge-portability) |
| Replacement does not inherit confidence or authority | Material implementation change requires review, requalification, and authorization adjustment where relevant. | [Material Implementation Change](ARCHITECTURE.md#material-implementation-change), [Requalification and Replay](ARCHITECTURE.md#requalification-and-replay) |
| Retention is intentional | Company Memory contains only validated Company Artifacts selected for lasting value; Archive and deletion follow policy. | [Company Artifact Test](ARCHITECTURE.md#company-artifact-test), [Archive](ARCHITECTURE.md#archive) |
| Canonical authority | Each Company Artifact has one authoritative representation; derived forms remain traceable and replaceable. | [Canonical Representation](ARCHITECTURE.md#canonical-representation), [Derived Representations](ARCHITECTURE.md#derived-representations) |
| Concurrent operation | Multiple Operating Cycles may share capabilities and State but remain scoped to their own Intent and execution context. | [Concurrent Operating Cycles](ARCHITECTURE.md#concurrent-operating-cycles) |
| External and internal observation remain distinct | Continuous Environmental Intelligence observes external change; internal operation is represented through events, outcomes, Evidence, State, and Operating Cycles. | [Environmental Intelligence Definition](ARCHITECTURE.md#environmental-intelligence-definition), [Organizational Role](ARCHITECTURE.md#organizational-role) |
| Capability-level improvement | Improvement targets the organizational capability and follows Evidence instead of assuming the current implementation is the cause. | [Capability Improvement](ARCHITECTURE.md#capability-improvement) |

## Traceability Model

Every authoritative graph entry must carry:

- a stable local identifier;
- an Architecture heading link;
- an Explicit or Derived status;
- a concise statement of the supporting meaning;
- any limitation needed to prevent an invalid inference.

A Derived edge must cite every Architecture section needed for the inference. A Concept Node is removed from this graph when its authoritative Architecture support is removed. Renaming a heading requires updating its graph trace without changing meaning unless the Architecture change explicitly changes meaning.

Traceability is one-way: this graph points to `ARCHITECTURE.md`. The existence of an entry here cannot be used as evidence to add or preserve a concept in the Architecture.

## Validation Rules

An authoritative graph revision is valid only when all of the following hold:

1. Every node maps to a validated Architecture concept and a resolvable heading.
2. Every edge uses the controlled Relationship Vocabulary.
3. Every edge maps two cataloged nodes and has a resolvable Architecture trace.
4. Every Derived edge is necessary, narrowly worded, and justified by all cited statements.
5. Optional relationships carry explicit optionality metadata; gated lifecycle transitions may use `may become`, and no lifecycle promotion is implied.
6. Company State and Company Memory remain distinct.
7. Working Context remains temporary, sufficient, activity-specific, classified, and non-authoritative.
8. Company Capability remains independent of its current implementation.
9. Operational Confidence remains separate from Standing Authorization and cannot grant authority.
10. Controlled Execution cannot create authority; Organizational Events and Outcomes cannot automatically create Intent or work.
11. Canonical and Derived Representations remain distinguishable and traceable.
12. A replacement implementation cannot inherit qualification or authorization without the required review.
13. Continuous Environmental Intelligence remains external observation rather than internal execution.
14. Capability Improvement remains evidence-based and capability-focused.
15. No downstream product concept, company-specific choice, vendor, technology schema, obsolete concept, or unsupported taxonomy enters the authoritative graph.

Concepts removed from the Architecture are invalid graph nodes and must not be preserved as compatibility aliases.

## Derived Representations

The following fenced YAML is a human-readable interchange example of the graph catalogs. It is not normative, does not define field types, and does not select YAML, a graph database, or any other implementation technology. The Markdown catalogs and this block are both subordinate to `ARCHITECTURE.md`. Each structured relationship ID resolves to the Relationship Catalog row with the same ID, where its Architecture trace and limitation are recorded.

```yaml
architecture_knowledge_graph:
  authority: ARCHITECTURE.md
  governance: ../PROJECT.md
  status: derived
  counts:
    concept_nodes: 61
    explicit_relationships: 77
    derived_relationships: 5
    relationship_types: 27
  concepts:
    - { id: ai_first_company, label: "AI-First Company", trace: "ARCHITECTURE.md#ai-first-company-definition" }
    - { id: company_identity, label: "Company Identity", trace: "ARCHITECTURE.md#company-identity-and-product-identity" }
    - { id: product_identity, label: "Product Identity", trace: "ARCHITECTURE.md#company-identity-and-product-identity" }
    - { id: brand_identity, label: "Brand Identity", trace: "ARCHITECTURE.md#brand-identity" }
    - { id: legal_identity, label: "Legal Identity", trace: "ARCHITECTURE.md#legal-identity-and-financial-identity" }
    - { id: financial_identity, label: "Financial Identity", trace: "ARCHITECTURE.md#legal-identity-and-financial-identity" }
    - { id: company_execution_environment, label: "Company Execution Environment", trace: "ARCHITECTURE.md#company-execution-environment-concepts" }
    - { id: persistent_execution_environment, label: "Persistent Execution Environment", trace: "ARCHITECTURE.md#company-execution-environment-concepts" }
    - { id: session_work, label: "Session Work", trace: "ARCHITECTURE.md#session-work-and-system-work" }
    - { id: system_work, label: "System Work", trace: "ARCHITECTURE.md#session-work-and-system-work" }
    - { id: trust_domain, label: "Trust Domain", trace: "ARCHITECTURE.md#trust-domain-isolation" }
    - { id: data_custody, label: "Data Custody", trace: "ARCHITECTURE.md#data-custody-and-systems-of-record" }
    - { id: system_of_record, label: "System of Record", trace: "ARCHITECTURE.md#data-custody-and-systems-of-record" }
    - { id: access_boundary, label: "Access Boundary", trace: "ARCHITECTURE.md#access-boundary" }
    - { id: recoverability, label: "Recoverability", trace: "ARCHITECTURE.md#recoverability" }
    - { id: knowledge_lifecycle, label: "Knowledge Lifecycle", trace: "ARCHITECTURE.md#knowledge-lifecycle" }
    - { id: external_world, label: "External World", trace: "ARCHITECTURE.md#external-world" }
    - { id: evidence, label: "Evidence", trace: "ARCHITECTURE.md#evidence" }
    - { id: knowledge, label: "Knowledge", trace: "ARCHITECTURE.md#knowledge-definition" }
    - { id: working_knowledge, label: "Working Knowledge", trace: "ARCHITECTURE.md#working-knowledge" }
    - { id: validated_knowledge, label: "Validated Knowledge", trace: "ARCHITECTURE.md#validated-knowledge" }
    - { id: company_artifact, label: "Company Artifact", trace: "ARCHITECTURE.md#company-artifact" }
    - { id: decision_record, label: "Decision Record", trace: "ARCHITECTURE.md#decision-records" }
    - { id: company_memory, label: "Company Memory", trace: "ARCHITECTURE.md#company-memory-definition" }
    - { id: archive, label: "Archive", trace: "ARCHITECTURE.md#archive" }
    - { id: knowledge_representation, label: "Knowledge Representation", trace: "ARCHITECTURE.md#knowledge-representation" }
    - { id: canonical_representation, label: "Canonical Representation", trace: "ARCHITECTURE.md#canonical-representation" }
    - { id: derived_representation, label: "Derived Representation", trace: "ARCHITECTURE.md#derived-representations" }
    - { id: knowledge_access, label: "Knowledge Access", trace: "ARCHITECTURE.md#knowledge-access" }
    - { id: working_context, label: "Working Context", trace: "ARCHITECTURE.md#working-context" }
    - { id: pull_access, label: "Pull Access", trace: "ARCHITECTURE.md#pull-access" }
    - { id: push_access, label: "Push Access", trace: "ARCHITECTURE.md#push-access" }
    - { id: context_selection, label: "Context Selection", trace: "ARCHITECTURE.md#knowledge-access-capabilities" }
    - { id: knowledge_retrieval, label: "Knowledge Retrieval", trace: "ARCHITECTURE.md#knowledge-access-capabilities" }
    - { id: knowledge_synthesis, label: "Knowledge Synthesis", trace: "ARCHITECTURE.md#knowledge-access-capabilities" }
    - { id: context_delivery, label: "Context Delivery", trace: "ARCHITECTURE.md#knowledge-access-capabilities" }
    - { id: company_capability, label: "Company Capability", trace: "ARCHITECTURE.md#company-capability-definition" }
    - { id: operating_cycle, label: "Operating Cycle", trace: "ARCHITECTURE.md#operating-cycle-definition" }
    - { id: intent_generation, label: "Intent Generation", trace: "ARCHITECTURE.md#operating-cycle-sequence" }
    - { id: intent, label: "Intent", trace: "ARCHITECTURE.md#operating-cycle-sequence" }
    - { id: controlled_execution, label: "Controlled Execution", trace: "ARCHITECTURE.md#controlled-execution-definition" }
    - { id: work_admission, label: "Work Admission", trace: "ARCHITECTURE.md#work-admission" }
    - { id: outcome, label: "Outcome", trace: "ARCHITECTURE.md#controlled-execution-outcomes" }
    - { id: organizational_event, label: "Organizational Event", trace: "ARCHITECTURE.md#organizational-event-definition" }
    - { id: operational_confidence, label: "Operational Confidence", trace: "ARCHITECTURE.md#operational-confidence-definition" }
    - { id: confidence_profile, label: "Confidence Profile", trace: "ARCHITECTURE.md#confidence-profile" }
    - { id: capability_history, label: "Capability History", trace: "ARCHITECTURE.md#capability-history" }
    - { id: capability_improvement, label: "Capability Improvement", trace: "ARCHITECTURE.md#capability-improvement" }
    - { id: standing_authorization, label: "Standing Authorization", trace: "ARCHITECTURE.md#standing-authorization-definition" }
    - { id: continuous_environmental_intelligence, label: "Continuous Environmental Intelligence", trace: "ARCHITECTURE.md#environmental-intelligence-definition" }
    - { id: proposal_evaluation, label: "Proposal Evaluation", trace: "ARCHITECTURE.md#proposal-evaluation" }
    - { id: response_class, label: "Response Class", trace: "ARCHITECTURE.md#proposal-evaluation" }
    - { id: role, label: "Role", trace: "ARCHITECTURE.md#roles-and-decision-mandates" }
    - { id: decision_mandate, label: "Decision Mandate", trace: "ARCHITECTURE.md#roles-and-decision-mandates" }
    - { id: mandate_holder, label: "Mandate Holder", trace: "ARCHITECTURE.md#roles-and-decision-mandates" }
    - { id: qualified_reviewer, label: "Qualified Reviewer", trace: "ARCHITECTURE.md#roles-and-decision-mandates" }
    - { id: mandate_registry, label: "Mandate Registry", trace: "ARCHITECTURE.md#mandate-registry" }
    - { id: founder_continuity, label: "Founder Continuity", trace: "ARCHITECTURE.md#founder-continuity-definition" }
    - { id: information_classification, label: "Information Classification", trace: "ARCHITECTURE.md#information-classification-purpose" }
    - { id: information_class, label: "Information Class", trace: "ARCHITECTURE.md#information-classes" }
    - { id: company_state, label: "Company State", trace: "ARCHITECTURE.md#company-state-purpose" }
  validated_attributes:
    - { owner: company_memory, name: "Knowledge Independence", kind: property, trace: "ARCHITECTURE.md#knowledge-independence-and-knowledge-portability" }
    - { owner: company_memory, name: "Knowledge Portability", kind: property, trace: "ARCHITECTURE.md#knowledge-independence-and-knowledge-portability" }
    - { owner: proposal_evaluation, name: "Impact", kind: evaluation_dimension, trace: "ARCHITECTURE.md#proposal-evaluation" }
    - { owner: proposal_evaluation, name: "Urgency", kind: evaluation_dimension, trace: "ARCHITECTURE.md#proposal-evaluation" }
    - { owner: founder_continuity, name: "Accountability Continuity", kind: responsibility, trace: "ARCHITECTURE.md#founder-continuity-responsibilities" }
    - { owner: founder_continuity, name: "Authority Continuity", kind: responsibility, trace: "ARCHITECTURE.md#founder-continuity-responsibilities" }
    - { owner: founder_continuity, name: "Operational Continuity", kind: responsibility, trace: "ARCHITECTURE.md#founder-continuity-responsibilities" }
    - { owner: founder_continuity, name: "Knowledge Continuity", kind: responsibility, trace: "ARCHITECTURE.md#founder-continuity-responsibilities" }
    - { owner: founder_continuity, name: "Access Continuity", kind: responsibility, trace: "ARCHITECTURE.md#founder-continuity-responsibilities" }
  relationships:
    - { id: R02, source: company_identity, relation: is_distinct_from, target: product_identity, status: explicit }
    - { id: R03, source: legal_identity, relation: is_distinct_from, target: financial_identity, status: explicit }
    - { id: R04, source: persistent_execution_environment, relation: is_specialization_of, target: company_execution_environment, status: derived }
    - { id: R05, source: system_work, relation: consumes, target: working_context, status: explicit }
    - { id: R06, source: system_work, relation: is_executed_through, target: controlled_execution, status: explicit }
    - { id: R07, source: trust_domain, relation: constrains, target: company_execution_environment, status: derived }
    - { id: R09, source: recoverability, relation: constrains, target: company_execution_environment, status: derived }
    - { id: R10, source: external_world, relation: contributes_to, target: evidence, status: explicit, optional: true }
    - { id: R11, source: evidence, relation: contributes_to, target: knowledge, status: explicit, optional: true }
    - { id: R12, source: working_knowledge, relation: may_become, target: validated_knowledge, status: explicit }
    - { id: R13, source: validated_knowledge, relation: may_become, target: company_artifact, status: explicit }
    - { id: R14, source: decision_record, relation: is_specialization_of, target: company_artifact, status: explicit }
    - { id: R15, source: mandate_registry, relation: is_specialization_of, target: company_artifact, status: explicit }
    - { id: R16, source: company_memory, relation: contains, target: company_artifact, status: explicit }
    - { id: R17, source: archive, relation: contains, target: company_artifact, status: explicit }
    - { id: R18, source: company_artifact, relation: has_authoritative_representation, target: canonical_representation, status: explicit }
    - { id: R19, source: derived_representation, relation: is_derived_from, target: canonical_representation, status: explicit }
    - { id: R21, source: knowledge_access, relation: consumes, target: company_memory, status: explicit, optional: true }
    - { id: R22, source: knowledge_access, relation: consumes, target: company_state, status: explicit, optional: true }
    - { id: R23, source: knowledge_access, relation: consumes, target: knowledge_representation, status: explicit, optional: true }
    - { id: R24, source: knowledge_access, relation: consumes, target: information_classification, status: explicit, optional: true }
    - { id: R25, source: knowledge_access, relation: consumes, target: decision_mandate, status: explicit, optional: true }
    - { id: R26, source: knowledge_access, relation: prepares, target: working_context, status: explicit }
    - { id: R27, source: knowledge_access, relation: has_component_capability, target: context_selection, status: explicit }
    - { id: R28, source: knowledge_access, relation: has_component_capability, target: knowledge_retrieval, status: explicit }
    - { id: R29, source: knowledge_access, relation: has_component_capability, target: knowledge_synthesis, status: explicit }
    - { id: R30, source: knowledge_access, relation: has_component_capability, target: context_delivery, status: explicit }
    - { id: R31, source: context_selection, relation: contributes_to, target: working_context, status: explicit }
    - { id: R32, source: knowledge_retrieval, relation: contributes_to, target: working_context, status: explicit }
    - { id: R33, source: knowledge_synthesis, relation: contributes_to, target: working_context, status: explicit }
    - { id: R34, source: context_delivery, relation: delivers, target: working_context, status: explicit }
    - { id: R35, source: working_context, relation: contains, target: knowledge, status: explicit }
    - { id: R36, source: working_context, relation: contains, target: company_state, status: explicit }
    - { id: R37, source: push_access, relation: consumes, target: organizational_event, status: explicit }
    - { id: R39, source: operating_cycle, relation: contains, target: evidence, status: explicit }
    - { id: R40, source: operating_cycle, relation: contains, target: knowledge, status: explicit }
    - { id: R41, source: operating_cycle, relation: contains, target: intent_generation, status: explicit }
    - { id: R42, source: operating_cycle, relation: contains, target: intent, status: explicit }
    - { id: R43, source: operating_cycle, relation: contains, target: controlled_execution, status: explicit }
    - { id: R44, source: operating_cycle, relation: contains, target: outcome, status: explicit }
    - { id: R45, source: intent_generation, relation: consumes, target: knowledge, status: explicit }
    - { id: R46, source: intent_generation, relation: produces, target: intent, status: explicit }
    - { id: R47, source: intent, relation: is_executed_through, target: controlled_execution, status: explicit }
    - { id: R48, source: controlled_execution, relation: consumes, target: intent, status: explicit }
    - { id: R49, source: controlled_execution, relation: consumes, target: working_context, status: explicit }
    - { id: R50, source: controlled_execution, relation: performs_work_through, target: company_capability, status: explicit }
    - { id: R51, source: controlled_execution, relation: produces, target: outcome, status: explicit }
    - { id: R52, source: controlled_execution, relation: produces, target: evidence, status: explicit }
    - { id: R53, source: outcome, relation: produces, target: evidence, status: explicit }
    - { id: R54, source: work_admission, relation: evaluates, target: intent, status: derived }
    - { id: R90, source: controlled_execution, relation: has_component_capability, target: work_admission, status: explicit }
    - { id: R55, source: organizational_event, relation: contributes_to, target: evidence, status: explicit, optional: true }
    - { id: R56, source: organizational_event, relation: updates, target: company_state, status: explicit, optional: true }
    - { id: R57, source: organizational_event, relation: triggers, target: intent_generation, status: explicit, optional: true }
    - { id: R58, source: controlled_execution, relation: produces, target: organizational_event, status: explicit, optional: true }
    - { id: R59, source: evidence, relation: contributes_to, target: capability_history, status: explicit }
    - { id: R60, source: capability_history, relation: informs, target: operational_confidence, status: explicit }
    - { id: R61, source: operational_confidence, relation: evaluates, target: company_capability, status: explicit }
    - { id: R62, source: operational_confidence, relation: is_represented_by, target: confidence_profile, status: explicit }
    - { id: R63, source: operational_confidence, relation: identifies, target: capability_improvement, status: explicit }
    - { id: R64, source: operational_confidence, relation: informs, target: standing_authorization, status: explicit }
    - { id: R65, source: standing_authorization, relation: authorizes_recurring_actions_through, target: company_capability, status: explicit }
    - { id: R66, source: standing_authorization, relation: requires, target: decision_mandate, status: explicit }
    - { id: R67, source: capability_history, relation: produces, target: company_artifact, status: explicit, optional: true }
    - { id: R68, source: standing_authorization, relation: may_become, target: decision_record, status: explicit }
    - { id: R69, source: continuous_environmental_intelligence, relation: produces, target: evidence, status: explicit }
    - { id: R73, source: proposal_evaluation, relation: assigns, target: response_class, status: explicit }
    - { id: R74, source: proposal_evaluation, relation: routes_to, target: decision_mandate, status: explicit }
    - { id: R75, source: mandate_registry, relation: records, target: decision_mandate, status: explicit }
    - { id: R76, source: mandate_holder, relation: holds, target: decision_mandate, status: explicit }
    - { id: R78, source: information_classification, relation: contains, target: information_class, status: explicit }
    - { id: R79, source: information_classification, relation: constrains, target: working_context, status: derived }
    - { id: R80, source: company_state, relation: is_derived_from, target: evidence, status: explicit }
    - { id: R81, source: company_state, relation: is_distinct_from, target: company_memory, status: explicit }
    - { id: R82, source: founder_continuity, relation: consumes, target: company_memory, status: explicit }
    - { id: R83, source: founder_continuity, relation: requires, target: decision_mandate, status: explicit }
    - { id: R84, source: standing_authorization, relation: contributes_to, target: founder_continuity, status: explicit, optional: true }
    - { id: R85, source: company_state, relation: informs, target: founder_continuity, status: explicit }
    - { id: R86, source: information_classification, relation: constrains, target: founder_continuity, status: explicit }
    - { id: R87, source: company_identity, relation: contributes_to, target: founder_continuity, status: explicit }
    - { id: R88, source: operational_confidence, relation: informs, target: founder_continuity, status: explicit, optional: true }
    - { id: R89, source: company_execution_environment, relation: contributes_to, target: founder_continuity, status: explicit, optional: true }
```

## Relationship to the Reference Design

The Reference Design may consume the Architecture and this derived graph to navigate concepts, explain relationships, check coverage, or support traceable design decisions. It applies organizational truth; it does not define it.

Reference Design compositions and Technical Requirements cannot add, remove, or distort an Architecture concept or edge. When a downstream design or requirement disagrees with this graph, the authoritative Architecture governs and the downstream artifact must adapt.

## Change Governance

Changes follow this order:

1. Validate the organizational concept or relationship in real operation.
2. Update `ARCHITECTURE.md` through the repository's decision and change-control process.
3. Update this graph as a derived representation.
4. Revalidate node traces, edge traces, distinctions, and the structured block.
5. Update downstream derived uses only after the graph is consistent.

Prefer refining relationships, definitions, and specializations over adding top-level nodes. Introduce a new node only when it represents a genuinely distinct organizational responsibility that existing concepts cannot express. Removal from the Architecture requires removal or explicit deprecation here; the graph must never preserve a concept merely for downstream compatibility.

## Failure Modes

- The graph becomes a competing source of architectural truth.
- Useful implementation terms are promoted into Architecture concepts without Architecture support.
- Examples or chapter wording are mistaken for an authoritative taxonomy.
- Derived edges are presented as explicit statements or omit a critical limitation.
- Optional lifecycle transitions are modeled as automatic pipelines.
- Company State, Company Memory, Working Context, and activity logs are collapsed.
- Knowledge, representation, and authority are treated as interchangeable.
- Operational Confidence is treated as authorization.
- A current implementation is treated as the Company Capability itself.
- Replacement implementations inherit confidence or authority without review.
- Organizational Events or Outcomes automatically create Intent or work.
- Derived Representations silently become authoritative.
- Reference Design or Technical Requirements concerns modify the Architecture ontology.
- Obsolete concepts re-enter through diagrams, examples, or compatibility aliases.
- The structured block and the explanatory catalogs drift apart.

## Architecture Principles

1. `ARCHITECTURE.md` is authoritative; the graph is derived.
2. Every Concept Node and Relationship Edge must be traceable to validated Architecture content.
3. Prefer a small set of stable concepts, precise relationships, and explicit specializations.
4. Preserve distinctions between observation, knowledge, state, memory, context, authority, capability, execution, and outcome.
5. Model optionality and decision boundaries explicitly; never infer automatic promotion, authority, or work.
6. Keep organizational meaning independent of vendors, tools, technical schemas, and current implementations.
7. Keep human accountability explicit for consequential decisions.
8. Keep Company Capabilities distinct from the people, AI systems, Agents, tools, software, or automation that currently implement them.
9. Keep authoritative and derived representations distinguishable and traceable.
10. Allow downstream uses, including the Reference Design and Technical Requirements, to consume the Architecture without changing it.
