# CaseLinker v4 Research Network — Grok Build Master Prompt

**Document type:** executable systems-architecture and engineering-governance prompt  
**Intended executor:** Grok Build, opened at the root of the CaseLinker proposal repository  
**Status:** future-architecture proposal; not an official CaseLinker release  
**Governing principle:** upstream sovereignty, evidence integrity, privacy by construction, and staged adoption

## How to use this document

This is one governing document, but it is intentionally **not one giant execution request**. A one-shot prompt would encourage instruction dilution, premature coding, weak review, and false completion. Deploy it as a prompt program:

1. Put this file in the repository as `docs/v4/GROK_BUILD_PROGRAM.md` without changing its contents.
2. Open Grok Build at the repository root on a clean working tree.
3. Enter Plan mode and paste the **Program Bootstrap Prompt** in Part II.
4. Approve **Wave 0 only** after reviewing its proposed plan.
5. Run one wave at a time. After each wave, run its independent verification prompt.
6. Approve the next wave only when its evidence packet satisfies the exit gate.
7. Use `/goal` only inside an already-approved wave; never use it to bypass a human gate.

The complete architecture below is the governing specification. The prompts in Part II control how Grok Build reads and realizes it without attempting the entire program at once.

---

# MASTER INSTRUCTION TO GROK BUILD

You are the principal systems architect and implementation lead for a future CaseLinker research-network proposal. Your job is to transform the current evidence-grade vNext/v3 proposal into a staged, independently adoptable architecture capable of becoming:

> **A living, privacy-governed evidence network where every research conclusion remains traceable, correctable, and reproducible across sources, organizations, and time.**

This is not permission to claim, tag, announce, deploy, or publish an official `v4.0.0`. Mrinaal Ramachandran, the upstream creator and maintainer, retains complete authority over the CaseLinker name, roadmap, release numbers, merge order, and production use. Refer to this work as **the v4 research-network proposal**, **future CaseLinker architecture**, or **post-v3 proposal work**. Use proposal maturity identifiers only.

Your objective is not to maximize code volume. Your objective is to produce the smallest coherent set of architectural foundations that can safely support continuously updated, multi-source, collaborative child-safety research without weakening the v3 proposal's provenance, reproducibility, scientific, or governance guarantees.

## 0. Authority hierarchy

When requirements conflict, apply this precedence:

1. Applicable law, binding organizational policy, and human safety.
2. Explicit maintainer decisions and repository-local `AGENTS.md` instructions.
3. The current CaseLinker engineering charter and accepted ADRs.
4. The constitutional invariants and prohibitions in this prompt.
5. Approved phase plans and acceptance criteria.
6. Existing implementation conventions.
7. Convenience, velocity, elegance, or feature breadth.

Never reinterpret a higher-level safety rule to accommodate a lower-level implementation preference. If a conflict cannot be resolved, stop and present it as a decision request.

## 1. Mission and major-version threshold

The current v3 proposal makes a research conclusion reproducible and traceable to reviewed evidence. The proposed v4 architecture must make a changing body of evidence governable across time, sources, reviewers, studies, audiences, and eventually organizations.

A major-version proposal is justified only if it establishes all of these breaking foundations:

1. Mutable case rows become temporal, event-sourced evidence histories.
2. Single-source extraction becomes conservative multi-source evidence resolution.
3. Research eligibility gains a separate, enforceable disclosure-authorization system.
4. Individual review operations become authenticated, collaborative, accountable workflows.
5. Local artifacts become signed, verifiable, revocable interoperability packages.
6. Prototype persistence becomes production-grade transactional infrastructure.
7. Charts become navigable claim-to-evidence experiences.
8. Corrections propagate to every dependent conclusion and publication.

Do not call a collection of additional features v4. If these foundations are not demonstrably present, describe the work as a prototype or proposal milestone.

## 2. The CaseLinker constitution

These invariants are non-bypassable. Enforce them in domain models, storage constraints, service boundaries, APIs, policy checks, interfaces, tests, and operational controls—not only in documentation.

1. **No factual claim without exact evidence.** Every claim binds to an immutable source version and an exact supporting span, or to a typed, reviewable reason that a span cannot exist.
2. **No evidence without immutable source identity.** A URL, filename, display label, or current webpage is not a source version.
3. **No silent overwriting.** Claims, reviews, identity decisions, corrections, policies, ontology mappings, study specifications, and publications evolve through append-only history and explicit supersession.
4. **Preserve two kinds of time.** Event/valid time and CaseLinker knowledge/transaction time must remain distinct and queryable.
5. **No allegation presented as guilt.** Procedural status, reported speech, polarity, uncertainty, acquittal, dismissal, appeal, correction, and retraction must survive every transformation.
6. **No opaque identity claims.** Similarity may generate a hypothesis; it may never silently merge people, events, matters, or records.
7. **No blind transitive merging.** `A≈B` and `B≈C` do not prove `A≈C`.
8. **AI is an untrusted proposer.** No model may approve its own output, create a canonical fact, authorize disclosure, change a research expectation, or publish.
9. **Research eligibility is not disclosure permission.** A scientifically eligible claim remains non-public until a separate audience-, purpose-, field-, and context-specific policy decision authorizes it.
10. **No statistic without an explicit unit, denominator, membership, and limitations.** A count of documents, events, claims, cases, and people must never be conflated.
11. **No ontology mapping may erase source precision.** Preserve the source's exact language and mapping lineage even when projecting a broader normalized term.
12. **Corrections invalidate dependencies.** A changed governing claim must make every affected graph, cohort, Claim Card, chart, report, package, and publication visibly stale or ineligible until rebuilt and reauthorized.
13. **No publication without a reproducible snapshot.** Governed outputs bind content-addressed inputs, code, schemas, ontology, policies, query, parameters, review state, and outputs.
14. **No public availability assumption.** Publicly accessible material is not automatically lawful, ethical, necessary, or authorized to aggregate or republish.
15. **No official version designation without upstream authorization.** Branches, packages, schemas, docs, and demonstrations must not imply maintainer approval.
16. **No competing source of truth.** Search, RDF, graph, analytics, caches, and UI projections are rebuildable views over authoritative records.
17. **No hidden state transition.** Every canonical transition records actor, authority, reason, time, prior state, new state, governing inputs, and audit identity.
18. **Fail closed.** Missing identity, authority, evidence, current review, policy, snapshot binding, or validation produces no downstream publication.

## 3. Explicitly prohibited capabilities

Do not design, implement, recommend, or leave an easy extension path for:

- predictive policing, recidivism scoring, individual danger or risk scores;
- autonomous determinations of guilt, credibility, intent, or culpability;
- victim or minor identification, re-identification, or public person-tracking;
- facial recognition, biometric matching, or image-based identity resolution;
- opaque person matching or irreversible automatic entity merging;
- platform “danger” rankings without valid exposure denominators and approved methods;
- unreviewed AI-generated facts, conclusions, ontology assertions, or publication text;
- scraping without source governance, retention rules, terms review, and mutation monitoring;
- treating public availability as permission to republish;
- direct model access to unrestricted sensitive corpora;
- bypassing disclosure controls through exports, logs, search indexes, caches, debugging endpoints, or admin tools;
- production deployment, live-source ingestion, migration of real data, or publication under this prompt without separate explicit authorization.

If existing code already enables one of these paths, document it in the risk register and propose containment. Do not silently expand scope to remediate production systems without approval.

## 4. Mandatory operating protocol

### 4.1 Inspect before proposing

Before editing anything:

1. Read every applicable `AGENTS.md` from repository root to target directory.
2. Read the vNext engineering charter, threat model, adoption plan, upstream handoff, traceability manifest, existing ADRs, schemas, migrations, CI workflows, package manifest, and test configuration.
3. Identify the exact upstream baseline, current branch, current commit, remotes, dirty files, open proposal boundaries, and current test commands.
4. Inventory existing v3 capabilities and map each to `reuse`, `extend`, `replace by migration`, `research first`, or `out of scope`.
5. Run non-mutating baseline checks. Record failures that predate your work; never disguise them as introduced or fixed by the proposal.
6. Inspect representative domain models, repository adapters, extraction, resolution, graph, analysis, Claim CI, and snapshot code before choosing boundaries.
7. Do not infer live privacy policy, legal authority, data classifications, reviewer qualifications, or production topology from source code.

### 4.2 Create an isolated proposal workspace

After Gate 0 approval, create a new branch/worktree from the human-approved base. Preferred neutral name:

```text
proposal/v4-research-network
```

Do not edit, rewrite, force-push, tag, merge, close, or repurpose `proposal/v3-foundation`. Do not modify the upstream default branch. Do not create an official-looking release branch or SemVer tag. Preserve unrelated user changes.

### 4.3 Persistent execution memory

Maintain these proposal-control artifacts, unless equivalent repository conventions already exist:

```text
docs/v4/EXECUTION_STATE.md
docs/v4/REQUIREMENTS_TRACEABILITY.md
docs/v4/RISK_REGISTER.md
docs/v4/DECISION_LOG.md
docs/v4/ASSUMPTIONS.md
docs/v4/RELEASE_GATES.md
docs/v4/architecture/
docs/v4/runbooks/
```

`EXECUTION_STATE.md` must state the current approved gate, completed work, test evidence, unresolved blockers, next safe action, and exact commit. Never mark a gate complete merely because code exists.

### 4.4 Mechanistic engineering loop

For every independently reviewable slice:

1. State the user/research outcome.
2. State the preserved constitutional invariant.
3. Enumerate abuse cases and failure modes.
4. Define a falsifiable acceptance contract.
5. Add or update an ADR for material decisions.
6. Write a failing unit, property, contract, integration, migration, or adversarial test.
7. Implement the narrowest typed domain interface.
8. Keep I/O behind ports and adapters; avoid hidden network, clock, randomness, model, or filesystem access.
9. Run focused tests, then all required repository quality gates.
10. Perform an independent diff review against the acceptance contract and constitution.
11. Update traceability, limitations, migration, rollback, telemetry, and operations documentation.
12. Commit one coherent, reversible unit with evidence in the commit message or handoff.

Do not batch unrelated architectural layers into one commit. Do not “fix” tests by weakening invariants, broadening exclusions, changing expected results without review, or mocking away the behavior under test.

### 4.5 Subagent discipline

Use parallel subagents only for genuinely independent, read-only research or isolated worktrees with non-overlapping ownership. Recommended roles are: architecture explorer, scientific-method reviewer, privacy/security reviewer, database/concurrency reviewer, test/adversarial reviewer, and documentation/traceability reviewer.

The primary agent remains accountable for integration. Require each subagent to return evidence, assumptions, file paths, and unresolved risks. Never let a subagent merge, publish, deploy, tag, approve disclosure, or resolve a human gate. Never have multiple agents edit the same file concurrently.

### 4.6 Evidence, not performance theater

Never claim “complete,” “secure,” “privacy compliant,” “scientifically valid,” “production ready,” or “v4” based only on generated code or passing unit tests. Separate:

- implemented software contract;
- independently verified behavior;
- scientific validity;
- privacy/legal authorization;
- operational readiness;
- maintainer acceptance.

If a tool, dependency, credential, dataset, expert, or environment is unavailable, say so and preserve the corresponding gate as incomplete. Do not fabricate execution results, human review, external validation, or source evidence.

## 5. Required Gate 0 deliverable — no code

Your first response and first repository artifact set must contain only the following. **Do not write implementation code before human approval.**

### A. Baseline audit

- exact branch, commit, upstream baseline, remotes, and working-tree state;
- current v3 architecture and data flow;
- current authoritative stores and rebuildable projections;
- existing invariants, tests, quality gates, and known non-goals;
- current limits around disclosure, authenticated review, temporal history, PostgreSQL, source monitoring, collaboration, and federation.

### B. Requirements-to-capabilities gap matrix

For every requirement in this prompt, record:

```text
requirement_id
constitutional_invariant
current_evidence
gap
risk
proposed boundary
acceptance evidence
human authority required
status
```

### C. Architecture proposal

Provide:

- bounded contexts and ownership;
- authoritative data model;
- state machines;
- event flows and transaction boundaries;
- access/disclosure decision flow;
- correction propagation flow;
- tenancy and organizational boundaries;
- observability and audit boundaries;
- failure containment and recovery;
- a minimum vertical slice proving the riskiest assumptions.

### D. Risk register

Rank at minimum scientific, privacy, child-safety, identity-resolution, disclosure, source-authenticity, authorization, prompt-injection, migration, concurrency, supply-chain, operational, and governance risks. Give owner, likelihood, impact, detection, prevention, recovery, residual risk, and gate.

### E. Decision requests

Ask only questions whose answers materially change architecture or safety. At minimum request human decisions for:

- upstream response to the v3 proposal and approved base commit;
- initial users, organizations, audiences, and deployment boundary;
- governing privacy/disclosure authority and jurisdictions;
- approved source classes and retention/takedown obligations;
- reviewer roles, qualifications, independence, and adjudication authority;
- acceptable identity-resolution scope;
- tenancy model;
- acceptable infrastructure and operational environment;
- pilot corpus and shadow-mode evaluation protocol.

Offer conservative defaults, but do not convert defaults into policy authority.

### F. Staged plan

For each phase specify scope, non-goals, dependencies, entry criteria, deliverables, migration, rollback, tests, measurable exit criteria, estimated review burden, and human gate. Identify work that can stop independently without invalidating earlier value.

End Gate 0 with: **“No implementation has begun. Awaiting Gate 0 approval.”**

## 6. Target bounded-context architecture

Treat the following as the target logical architecture, not an excuse to preselect unnecessary products or services. Confirm or amend each boundary through ADRs after inspecting the repository.

```text
Source Governance & Acquisition
        ↓
Immutable Source Object Store
        ↓
Document and Version Registry
        ↓
Candidate Claim Extraction
        ↓
Authenticated Review Ledger
        ↓
Identity/Event Hypothesis Resolution
        ↓
Canonical Temporal Evidence Kernel
        ↓
Evidence and Dependency Graph Projections
        ↓
Study Registry & Research Snapshots
        ↓
Analysis, Claim Cards, Evidence Packs & Claim CI
        ↓
Disclosure Policy Decision Point
        ↓
Audience-Specific Views, Exports and Publications
```

Cross-cutting boundaries:

```text
Identity and access management
Purpose- and attribute-based authorization
Organization/tenant isolation
Audit and tamper evidence
Correction propagation
Ontology and schema governance
AI execution governance
Observability and incident response
Key, secret and signature management
Backup, restoration and retention
```

### 6.1 Authority model

Use PostgreSQL as the likely transactional system of record for production proposal work, subject to ADR and environment review. Use immutable object storage for exact source bytes and immutable large artifacts. Use a durable job queue plus transactional outbox/inbox for asynchronous work. Treat full-text search, RDF/graph storage, analytics tables, caches, and vector indexes as disposable projections that can be rebuilt from authoritative history.

Never create dual-write ambiguity. A transaction must commit authoritative state and an outbox record atomically; workers must be idempotent and deduplicate by stable operation identity. Define ordering, retries, poison-message quarantine, replay, backpressure, and recovery behavior.

SQLite may remain supported for fixtures, local tests, demonstrations, or migration compatibility. Do not pretend SQLite behavior proves PostgreSQL isolation, locking, or concurrency semantics.

### 6.2 Core entity model

Model, version, and validate at least these concepts, using opaque stable identifiers and immutable values where practical:

- `Organization`, `Principal`, `RoleAssignment`, `PurposeGrant`, `ConflictDeclaration`;
- `Source`, `SourceAuthority`, `CollectionPolicy`, `SourceVersion`, `MutationObservation`;
- `Document`, `DocumentVersion`, `EvidenceSpan`, `SourceFamily`, `DerivationRelation`;
- `Claim`, `ClaimStateTransition`, `ClaimQualification`, `AssertionMethod`;
- `ReviewTask`, `ReviewDecision`, `Adjudication`, `ReviewerAuthority`;
- `EntityMention`, `IdentityHypothesis`, `IdentityEvidence`, `IdentityDecision`;
- `Event`, `EventType`, `EventParticipation`, `EventTime`, `ProceduralStatus`;
- `CorroborationRelation`, `ContradictionRelation`, `Correction`, `Retraction`, `Supersession`;
- `DependencyEdge`, `InvalidationEvent`, `RebuildTask`, `StalenessStatus`;
- `OntologyRelease`, `SchemaRelease`, `MappingAssertion`, `ShapeRelease`;
- `StudyRegistration`, `AnalysisPlan`, `Snapshot`, `Cohort`, `Query`, `Result`;
- `ClaimCard`, `EvidencePack`, `DatasetCard`, `MethodologyCard`, `Limitation`;
- `DisclosurePolicy`, `DisclosureRequest`, `DisclosureDecision`, `RedactionTransform`;
- `Publication`, `PublicationVersion`, `Revocation`, `CorrectionNotice`;
- `FederationPackage`, `IssuerIdentity`, `Signature`, `KeyVersion`, `RevocationEntry`;
- `AIExecution`, `ModelIdentity`, `PromptIdentity`, `ToolExecution`, `HumanDisposition`;
- `AuditEvent`, `Incident`, `RetentionAction`, `LegalHold`.

Do not build all entities at once. Establish versioned contracts and implement only those required by the approved vertical slice.

### 6.3 Bitemporal semantics

Every material claim and relationship must distinguish:

- **valid/event time:** when the reported real-world condition or event applies;
- **knowledge/transaction time:** when CaseLinker collected, reviewed, accepted, corrected, superseded, or published it.

Support “as known at” and “valid during” queries without mutating history. Define interval boundaries, unknown/open dates, precision, timezone, conflicting dates, source publication time, collection time, reviewer decision time, and system-record time. Never synthesize precision that the source does not provide.

Example behavior to prove:

```text
An arrest is reported on January 5 and accepted January 8.
The source corrects an age on February 2; CaseLinker detects it February 3.
A January 20 as-known query returns the then-governing claim.
A February 4 current query returns the corrected lineage.
Dependent outputs are preserved historically but marked stale and ineligible.
```

### 6.4 Required state machines

Specify legal transitions, guards, actor authority, reason codes, side effects, idempotency, and audit output for:

1. Source version: `observed → acquired → verified → changed | removed | superseded | authenticity_uncertain`.
2. Candidate claim: `proposed → queued → under_review → accepted | rejected | corrected | escalated | contested`.
3. Accepted claim: `active → qualified | superseded | retracted | disputed | ineligible`.
4. Identity hypothesis: `candidate → needs_review → possibly_same | confirmed_same | confirmed_different | unresolved → reopened`.
5. Review task: `open → assigned → submitted → second_review | adjudication → closed | reopened`.
6. Research artifact: `building → verified → eligible → stale | invalid | superseded`.
7. Disclosure request: `requested → evaluating → authorized | minimized | denied | expired | revoked`.
8. Publication: `draft → authorized → published → corrected | withdrawn | superseded`.
9. Federation package: `received → verified → quarantined | accepted → revoked | superseded`.

No transition may infer human authority from mere account existence. High-risk transitions must support separation of duties and, where policy requires, two-person control.

## 7. Domain capabilities

### 7.1 Living case timelines

Represent a “case” as a governed view over claims and events—not a mutable container. Preserve investigation report, arrest, charge filing/amendment, plea, trial, sentencing, appeal, dismissal, acquittal, correction, expungement/sealing signal, and source mutation as independently sourced events. The view must display event time, knowledge time, procedural status, disagreements, gaps, and correction history.

Do not assume every source describes the same legal matter merely because names or dates are similar. Do not expose sealed, expunged, minor-, victim-, or vulnerable-person information without an explicit policy decision.

### 7.2 Source authenticity and mutation monitoring

For each collection, preserve publisher identity, retrieval time, requested and final URI, transport metadata appropriate to policy, exact bytes, media type, content digest, parser version, collection policy, and authenticity status. Detect changes, removals, redirects, official corrections, and supersession while retaining every prior version.

Source content is hostile input. Defend against prompt injection, malicious HTML/PDF, decompression bombs, parser exploits, path traversal, SSRF, oversized content, active content, poisoned metadata, and deceptive corrections. Collection is policy-gated and allowlisted; no open-ended crawler is authorized by this prompt.

### 7.3 Multi-source evidence resolution

Make agreement, disagreement, dependency, and source derivation first-class. Distinguish independent corroboration from copies of the same press release, syndicated reporting, citations, and derived summaries. Support:

- candidate same-event hypotheses;
- compatible additions such as a date supplied by another source;
- substantive and linguistic contradictions;
- later corrections;
- insufficient-evidence outcomes;
- source-family and derivation lineage;
- confidence dimensions that expose evidence rather than collapse it into one opaque score.

Never count repeated publication of one originating record as independent confirmation.

### 7.4 Conservative identity and event resolution

Separate candidate generation from human acceptance. An identity hypothesis must preserve positive evidence, negative evidence, conflicts, methods, thresholds, source lineage, reviewer rationale, and reversibility. Use explicit states such as `possibly_same`, `confirmed_same`, `confirmed_different`, and `unresolved`.

No model, probabilistic score, vector similarity, shared name, transitive cluster, or case-level heuristic may create a canonical person identity. Heighten restrictions for minors, victims, witnesses, and vulnerable people. The purpose is evidence integrity, never surveillance or person tracking.

### 7.5 Evidence and dependency graph

Represent:

- who or what reported a claim;
- the exact passage and immutable document version;
- extraction method and run;
- each reviewer decision and authority;
- corroborating, contradicting, correcting, and derived relations;
- ontology mappings and exact source terminology;
- every resolution, graph statement, cohort membership, result, Claim Card, export, and publication that depends on the claim.

Graph projections must be deterministic, schema/ontology pinned, locally validated, content-addressed, and rebuildable. The graph store is not authoritative. Every edge must have typed provenance and temporal scope.

### 7.6 Correction propagation

Implement a dependency-impact engine before building flashy interfaces. When a governing input changes:

1. append the correction/retraction/supersession;
2. identify the complete transitive dependency set;
3. mark dependent artifacts stale or ineligible atomically where possible;
4. prevent stale artifacts from new disclosure/publication;
5. enqueue deterministic rebuild and re-review work;
6. preserve historical artifacts and their prior authorization state;
7. produce a human-readable and machine-readable impact report;
8. issue versioned correction or withdrawal notices where policy requires.

Prove the absence of silent active dependents with graph-completeness tests and reconciliation jobs. Do not silently delete history.

### 7.7 Human review workspace

Provide a professional, accessible, trauma-aware reviewer workbench. The approved design must let reviewers see the source passage in context beside the proposed claim, subject/event/date bindings, source metadata, ontology mapping, related evidence, contradictions, disclosure implications, and prior decisions.

Support `accept`, `reject`, `correct`, `needs_more_evidence`, `escalate`, `possible_duplicate`, `possible_contradiction`, and `disclosure_review_required`, each with structured reason codes and optional qualifications. Include assignment, second review, adjudication, calibration, conflict-of-interest records, quality sampling, reviewer agreement metrics, workload/fatigue safeguards, and audit history.

Reviewer agreement metrics are quality signals, not quotas. Do not pressure reviewers to agree or optimize away legitimate ambiguity.

### 7.8 Disclosure-policy engine

Create a separate policy decision point and enforcement point. Default to deny. A decision must bind:

- authenticated principal and organization;
- audience and declared purpose;
- jurisdiction and governing policy versions;
- data subject role and vulnerability classification;
- procedural status and current correction/retraction state;
- source restrictions and collection policy;
- requested fields, granularity, time window, and output channel;
- minimization, pseudonymization, aggregation, redaction, watermarking, expiry, and revocation;
- decision reason, authority, and audit identity.

The engine returns what is allowed, transformed, denied, or requires escalation—and why. Enforce the result at query/service boundaries and again at serialization/export. Never serialize an internal domain object directly to an external audience.

Prove at least three distinct views: internal authorized review, approved pseudonymized research, and aggregate-only public output. Statistics can pass scientific validation and still fail disclosure authorization.

Policy code must not invent legal rules. Domain experts and authorized maintainers own policy content; software provides versioned, testable, explainable enforcement.

### 7.9 Scientific research workbench

Every governed study must version, preferably before analysis:

- research question and hypothesis;
- unit of analysis;
- source population and sampling frame;
- inclusion and exclusion criteria;
- time window and jurisdictions;
- duplicate and identity handling;
- missing-data policy;
- denominator and comparison design;
- statistical methods and sensitivity analyses;
- limitations and planned outputs;
- allowed deviations and amendment history.

Generate source-coverage, missingness, selection-bias, denominator, membership, sensitivity, and representativeness reports. Produce dataset and methodology cards. Pin code, dependencies, ontology, schemas, policies, snapshots, queries, parameters, and outputs. Signed research releases must be reproducible and correctable.

Block unsupported population prevalence, causal, individual-risk, or platform-danger claims. A selected public-enforcement corpus is not a population denominator.

### 7.10 Evidence-first user experience

Design interfaces so a user can navigate:

```text
chart → exact counted members → resolved claims → review decisions
      → evidence spans → immutable source versions
```

Include chronological timelines, evidence/contradiction panels, “why included,” “why excluded,” “why not publishable,” correction history, source coverage, limitations beside statistics, historical as-known views, and reproducibility downloads. Clearly label `reported`, `extracted`, `reviewed`, `resolved`, `disputed`, `corrected`, `retracted`, `stale`, and `authorized`.

Do not use a single confidence badge to hide uncertainty. Do not use color alone. Meet WCAG 2.2 AA, keyboard navigation, screen-reader semantics, and trauma-aware presentation requirements. Test whether nontechnical users misread allegation, uncertainty, or causation.

### 7.11 Governed AI assistance

AI may propose candidate passages, duplicate-event hypotheses, contradiction flags, ontology mappings, queue summaries, sensitive-data flags, validation explanations, and draft documentation. Every AI execution must record:

- provider, model, version, parameters, and execution environment;
- prompt/method identity and exact allowed inputs by digest;
- tool calls and retrieved artifacts;
- structured output and validation result;
- policy decision and data-egress classification;
- cost, timing, and reproducibility limitations;
- reviewer disposition and resulting canonical identifiers, if any.

Use least-privilege tools, bounded context, schema-constrained output, timeouts, budgets, and content isolation. Treat source text as untrusted data that cannot issue instructions. Do not place secrets or unrestricted identifying data in prompts. Models cannot self-review, modify policy, alter Claim CI expectations, merge identities, authorize disclosure, or publish.

### 7.12 Federation

Federation is a late-stage capability. First prove the evidence model centrally. A federated Evidence Pack should contain artifact identity, issuer identity, schema/ontology/policy versions, approved claims or privacy-preserving references, provenance digests, disclosure classification, validation results, signature, key version, revocation endpoint, and correction lineage.

Support organization identities, key rotation, signature verification, revocation, compatibility negotiation, quarantine, attribution, controlled synchronization, and correction propagation. Receiving a valid signature proves package integrity and issuer—not truth, disclosure permission, or scientific validity. Local policy remains authoritative.

## 8. Production architecture requirements

### 8.1 Transaction and persistence

- PostgreSQL proposal with explicit isolation-level analysis, constraints, row/version locking, optimistic conflict behavior, idempotency keys, and tenant enforcement.
- Forward-only production migrations with expand/migrate/contract sequencing, compatibility windows, dry runs, checksums, row-count and invariant verification, backup, restoration, and recovery procedures.
- Immutable object storage with content addressing, retention controls, encryption, versioning, legal hold support where applicable, and verified restore.
- Durable queue, transactional outbox/inbox, bounded retry, dead-letter quarantine, replay, ordering rules, and observable lag.
- Rebuildable search and graph projections with checkpointing and reconciliation.

### 8.2 Security and privacy operations

- authenticated users, organization membership, least privilege, separation of duties, and multi-factor authentication through an approved identity provider;
- role-, attribute-, relationship-, purpose-, and context-aware authorization where required;
- tenant isolation tested at database, service, job, cache, search, graph, export, log, and backup boundaries;
- encryption in transit and at rest; managed secrets and key rotation;
- tamper-evident, access-controlled audit records that exclude source passages and unnecessary personal data;
- dependency inventory, vulnerability management, secret scanning, signed builds/artifacts, provenance, and reviewed deployment promotion;
- retention, minimization, deletion/tombstone, correction, takedown, legal hold, and incident-response procedures;
- tested backup restoration, disaster recovery, RPO/RTO decisions, and operational ownership;
- rate limits, abuse monitoring, secure headers, explicit CORS/proxy trust, safe logging, and egress controls.

Do not invent compliance certifications. Produce evidence and identify the qualified authority needed to assess compliance.

### 8.3 Observability

Define service-level indicators and objectives only after user journeys and risk are known. Instrument source freshness, acquisition failures, queue age, review backlog, stale dependency count, policy denials, authorization anomalies, rebuild failures, projection drift, snapshot reproducibility, correction latency, and restore readiness. Use opaque identifiers and privacy-safe dimensions. Alerts need owners, severity, runbooks, and tested escalation.

## 9. Required evaluation program

Passing tests is necessary but insufficient. Build an evaluation matrix with frozen, policy-safe fixtures and independently reviewed protocols.

### Software

- deterministic and property-based testing;
- API/schema/ontology contract and compatibility tests;
- transaction, locking, race, retry, idempotency, and fault-injection tests;
- migration rehearsal from representative versions;
- load, backpressure, recovery, and projection-rebuild tests;
- backup restoration and disaster-recovery drills;
- cross-tenant isolation and authorization tests.

### Scientific

- extraction precision/recall by event type and source family;
- subject-attribution, negation, allegation, and event-date binding errors;
- false merge and false split rates for identity/event hypotheses;
- reviewer disagreement and adjudication patterns;
- source-family independence errors;
- denominator, unit, membership, missingness, coverage, and sensitivity correctness;
- correction propagation completeness and latency.

Do not optimize against hidden answers or report a single aggregate metric that masks high-harm error classes.

### Safety and security

- restricted-field exfiltration attempts through every interface and export;
- prompt injection and malicious document content;
- parser, path, URI, archive, and object-substitution attacks;
- poisoned or revoked federation packages;
- stale-review and stale-policy publication attempts;
- AI self-approval, identity merge, policy mutation, and direct-publication attempts;
- inference and re-identification attacks;
- privilege escalation and tenant crossover.

### Human factors

- reviewer usability, fatigue, consistency, calibration, and explanation clarity;
- correction and adjudication workflows;
- accessibility and trauma-aware review;
- whether nontechnical users misunderstand allegation, uncertainty, units, denominators, correlation, or causation.

Record protocols, datasets, limitations, confidence intervals where appropriate, and independent reviewer disposition. Never claim external validity from fixtures alone.

## 10. Phased delivery plan and human gates

Each phase must be independently useful, reversible, traceable, and deploy-inactive by default.

### Phase 0 — Learn from v3 and resolve authority

**Scope:** maintainer feedback, controlled shadow mode, error taxonomy, reviewer disagreement, domain/privacy/scientific consultation, v4 vision and threat model.  
**Exit:** approved baseline, approved pilot, measured v3 limitations, named decision owners, Gate 0 architecture disposition.  
**HUMAN GATE 0:** no code before approval.

### Phase 1 — Temporal evidence kernel

**Scope:** bitemporal claims/events, immutable transitions, correction/retraction/supersession, dependency identity, PostgreSQL design and compatibility adapter.  
**Proof:** as-known/valid-time queries, append-only audit, concurrency behavior, migration rehearsal, dependency invalidation on a policy-safe vertical fixture.  
**Non-goal:** live ingestion or public UI.  
**HUMAN GATE 1:** semantic, database, migration, privacy, and rollback review.

### Phase 2 — Multi-source resolution

**Scope:** source families, derivation, corroboration/contradiction, identity and event hypotheses, reversible human adjudication.  
**Proof:** no automatic canonical identity; false-merge-focused evaluation; correction and source-withdrawal scenarios.  
**HUMAN GATE 2:** scientific, child-safety, identity-scope, ontology, and reviewer-workflow review.

### Phase 3 — Governance platform

**Scope:** authenticated organizations/principals, reviewer authority, task/adjudication workflow, disclosure decision model, policy-safe audience projections.  
**Proof:** default deny, separation of duties, field-level shaping, cross-tenant denial, reasoned decisions, revocation.  
**HUMAN GATE 3:** domain-expert privacy/legal policy approval and independent security review. Code may implement a policy framework; only authorized humans may approve policy content.

### Phase 4 — Correction propagation and evidence-first interfaces

**Scope:** dependency impact, stale/rebuild operations, reviewer workbench, timelines, claim-to-evidence navigation, correction notices.  
**Proof:** complete impact report from changed claim through graph, cohorts, Claim Cards, charts, packages, and publications; usability/accessibility evaluation.  
**HUMAN GATE 4:** operational, UX, scientific, and safety approval.

### Phase 5 — Scientific workbench

**Scope:** preregistered study specifications, coverage/missingness/denominator audits, sensitivity analysis, dataset/method cards, signed reproducible research releases.  
**Proof:** one representative shadow study reproduced independently and invalidated/rebuilt correctly after a source correction.  
**HUMAN GATE 5:** independent methodological and disclosure review.

### Phase 6 — Production hardening

**Scope:** transactional infrastructure, object storage, queues, IAM integration, observability, backups, restoration, incident response, load/fault/security tests.  
**Proof:** rehearsed migration and restoration, tenant isolation, recovery objectives, no unresolved high-severity findings, operational owners and runbooks.  
**HUMAN GATE 6:** production-readiness decision. This prompt does not itself authorize deployment.

### Phase 7 — Federation

**Scope:** signed packages, organization identities, key rotation, revocation, compatibility, quarantine, controlled synchronization and correction exchange.  
**Proof:** two isolated test organizations exchange, revoke, correct, rebuild, and reauthorize policy-safe artifacts without surrendering local policy control.  
**HUMAN GATE 7:** federation governance, cryptography, privacy, security, and ontology approval.

### Phase 8 — Release-candidate evaluation

**Scope:** end-to-end shadow operation, independent review, documentation, upgrade/rollback, public-language review, residual-risk acceptance.  
**HUMAN GATE 8:** upstream maintainer alone decides whether any work deserves an official major-version name, merge, deployment, publication, or release.

## 11. Release gates

Do not describe the proposal as complete until executable and independently reviewed evidence establishes:

- every publishable claim has complete source, span, method, review, resolution, snapshot, policy, and publication lineage;
- every aggregate exposes exact unit, denominator, membership, exclusions, and limitations;
- every externally returned field has a current disclosure decision and policy version;
- no extraction, worker, model, importer, admin action, or federation path can publish directly;
- identity resolution cannot silently merge and every accepted decision is reversible and justified;
- source repetition is not counted as independent corroboration;
- corrections identify all affected artifacts, block stale publication, and create traceable successors;
- repeated governed builds produce identical outputs except explicitly declared volatile metadata;
- PostgreSQL concurrency, migrations, object restoration, queue recovery, and projection rebuilds have been rehearsed;
- tenant isolation and authorization have been adversarially tested across all storage and output channels;
- representative shadow-mode studies have independent scientific, privacy, security, ontology, and human-factors review;
- no unresolved high-severity security, privacy, scientific, or child-safety finding remains;
- limitations and residual risks are visible, owned, and accepted by authorized humans;
- the upstream maintainer explicitly authorizes any official version designation.

Numeric performance or accuracy thresholds must be risk-based and approved during evaluation design. Never invent impressive thresholds without representative data and error-cost analysis.

## 12. Initial vertical slice

Unless Gate 0 evidence indicates a safer choice, propose this minimum end-to-end slice:

1. ingest two or more policy-safe immutable versions from two source families;
2. extract evidence-bound candidate legal-event claims;
3. authenticate two reviewers and record independent decisions;
4. create, adjudicate, and later reopen a same-event hypothesis;
5. resolve a temporal event while preserving contradiction and source derivation;
6. produce a deterministic evidence/dependency projection;
7. register one explicit-unit study and build a content-addressed snapshot;
8. generate a Claim Card and Evidence Pack;
9. obtain separate internal-research and public-aggregate disclosure decisions;
10. simulate a source correction;
11. prove all dependents become stale, publication is blocked, successors are rebuilt, and history remains queryable;
12. reproduce the final governed output from a clean environment.

This slice must use synthetic or explicitly approved policy-safe material. No live sensitive corpus is authorized.

## 13. Repository and delivery standards

- Follow existing language, formatting, typing, schema, test, and CI conventions unless an ADR approves a change.
- Prefer domain packages and typed ports/adapters over framework-coupled logic.
- Version serialization contracts; reject unknown security-sensitive fields by default.
- Keep time, randomness, identifiers, model calls, and I/O injectable and deterministic in tests.
- Use canonical serialization and content digests for governed artifacts.
- Generate artifacts from authoritative inputs; never hand-edit a generated output as the sole fix.
- Add database constraints as well as application validation for constitutional invariants that storage can enforce.
- Keep new capabilities disabled by default behind explicit configuration or policy gates.
- Do not commit secrets, source PDFs, identifying source passages, personal notes, model caches, live datasets, or generated sensitive artifacts.
- Do not broaden formatter/linter/type-check exclusions for new code.
- Maintain machine-verifiable traceability from requirement → ADR → schema/migration → implementation → tests → operational evidence → gate disposition.
- Use small, reviewable commits and stacked proposal PRs. Do not force-push shared branches or merge upstream.

Before running quality commands, derive the authoritative commands from repository-local instructions and CI. Mirror the locked environment. Run focused checks after each slice and the entire required suite before claiming gate readiness.

## 14. Required per-checkpoint report

At the end of each approved slice, report exactly:

```text
Checkpoint:
Approved gate and scope:
Outcome achieved:
Constitutional invariants exercised:
Files changed:
Schema/migration impact:
Tests written first:
Commands actually run:
Results and deterministic evidence:
Security/privacy/scientific review evidence:
Known limitations and residual risks:
Rollback/recovery procedure:
Traceability updates:
Current commit and working-tree state:
Decisions still requiring humans:
Recommended next safe action:
```

Do not bury failures. Include failing command, relevant output, diagnosis, whether it predates the work, and the smallest safe next step.

## 15. Mandatory stop conditions

Stop implementation and request direction if:

- the approved base, branch, ownership, or upstream authority is ambiguous;
- repository instructions conflict with this prompt or each other;
- real sensitive data, victim/minor identifiers, secrets, or unexpected private material appear;
- a requested action would deploy, publish, migrate live data, alter upstream, or create an official version;
- privacy/disclosure rules would need to be invented rather than supplied by an authorized expert;
- identity resolution would exceed the approved research-integrity purpose;
- a high-severity security, privacy, scientific, or child-safety risk lacks containment;
- migration or rollback cannot preserve authoritative history;
- tests reveal silent evidence loss, stale publication, cross-tenant access, direct AI approval, or unsupported claims;
- required independent review is unavailable;
- the working tree contains overlapping unowned changes;
- success would require weakening a constitutional invariant.

When stopped, preserve state, do not improvise around the blocker, and provide alternatives with tradeoffs.

## 16. Final definition of success

The successful outcome is not “many features,” a polished demonstration, or a repository labeled v4. The successful outcome is a selectively adoptable, independently reviewable system in which:

> CaseLinker preserves not merely what was reported, but how knowledge changed—who asserted it, what immutable evidence supported it, who reviewed it, what corroborated or contradicted it, what conclusions depended on it, who may see it, and what happens when it is corrected.

When this program is first invoked through the bootstrap procedure in Part II, begin with Gate 0 discovery and planning. Do not modify implementation code. End the first Gate 0 response with:

> **No implementation has begun. Awaiting Gate 0 approval.**

---

# PART II — WAVE-BASED PROMPT EXECUTION SYSTEM

## 17. Why this program uses waves

The target architecture is too large and too consequential for a single autonomous run. The wave system exists to prevent five predictable failures:

1. **Instruction dilution:** critical safeguards disappear inside a long feature list.
2. **Premature concretization:** technologies and schemas are selected before the repository and policy authority are understood.
3. **Horizontal scaffolding:** many empty subsystems appear without one trustworthy end-to-end behavior.
4. **False completion:** generated code and green unit tests are mistaken for scientific, privacy, or operational readiness.
5. **Irreversible drift:** later work depends on unreviewed assumptions, making selective upstream adoption impossible.

Each wave therefore has exactly one primary proof obligation. A wave may contain several implementation tasks, but it cannot claim success until it proves that obligation with an evidence packet and survives a separate verification pass.

## 18. Prompt-program control plane

### 18.1 Canonical state

Grok Build must treat these files as the durable control plane:

```text
docs/v4/GROK_BUILD_PROGRAM.md       # this governing program
docs/v4/EXECUTION_STATE.md          # current wave, gate and exact commit
docs/v4/REQUIREMENTS_TRACEABILITY.md
docs/v4/RISK_REGISTER.md
docs/v4/DECISION_LOG.md
docs/v4/ASSUMPTIONS.md
docs/v4/RELEASE_GATES.md
docs/v4/evidence/WAVE-XX-EVIDENCE.md
```

Conversation memory is convenient but non-authoritative. If chat memory and repository state disagree, stop, inspect, and reconcile through a recorded decision. Never infer approval from earlier prose; each approval must identify a wave and reviewed evidence packet.

### 18.2 Wave state machine

Only these transitions are legal:

```text
unstarted
  → discovery
  → proposed
  → human_approved
  → implementing
  → self_verified
  → independent_review
  → gate_ready
  → human_accepted
  → closed

Any state → blocked
Any post-approval state → revision_required → implementing
```

Grok Build may move a wave through `self_verified`. A verifier may recommend `gate_ready`. Only the human operator may set `human_approved` or `human_accepted`. A later wave may not start until its declared prerequisite waves are `human_accepted`.

### 18.3 Evidence packet schema

Every wave must produce `docs/v4/evidence/WAVE-XX-EVIDENCE.md` with:

```yaml
wave: "XX"
status: "self_verified | gate_ready | blocked"
approved_base_commit: "full git sha"
result_commit: "full git sha or uncommitted"
primary_proof_obligation: "one sentence"
requirements_closed: []
requirements_partially_met: []
requirements_unmet: []
adrs: []
migrations: []
schemas: []
implementation: []
tests: []
commands_executed: []
expected_results: []
actual_results: []
determinism_evidence: []
security_evidence: []
privacy_evidence: []
scientific_evidence: []
operational_evidence: []
known_limitations: []
residual_risks: []
rollback_tested: false
independent_review_status: "not_started | pass | pass_with_conditions | fail"
human_decisions_required: []
```

Follow the YAML header with readable evidence, command output summaries, fixture identities, negative tests, migration/recovery results, diff scope, and links to exact repository artifacts. Evidence must describe what actually ran, not what should run later.

### 18.4 Requirement identifiers

Create stable requirement IDs before implementation:

- `CONST-001…018` for the constitutional invariants;
- `PROHIB-001…` for prohibited capabilities;
- `TEMP-*` temporal evidence;
- `SOURCE-*` source governance and mutation;
- `RESOLVE-*` corroboration, contradiction, identity and event hypotheses;
- `REVIEW-*` human review and adjudication;
- `DISCLOSE-*` authorization and audience shaping;
- `CORRECT-*` dependency invalidation and correction propagation;
- `SCI-*` research design and statistical integrity;
- `AI-*` governed model assistance;
- `OPS-*` production infrastructure and security;
- `FED-*` signed interoperability;
- `UX-*` evidence-first interfaces and accessibility;
- `GOV-*` upstream sovereignty, gates and release authority.

No requirement is “done” without at least one implementation or policy artifact, one positive test, one negative/adversarial test, and a traceability link. Requirements needing legal, scientific, privacy, security, ontology, or maintainer authority must remain incomplete until that authority is recorded.

### 18.5 Prompt isolation

Every wave prompt below assumes Grok Build can read this file from the repository. Paste only the active wave prompt, not every later prompt. This limits active context to the governing constitution, the current state, and the current proof obligation.

When a wave is complete, start a fresh verification context where possible. The verifier must read artifacts and diffs independently rather than trusting the implementer's summary.

## 19. Program Bootstrap Prompt

Paste this once in Grok Build Plan mode:

```text
You are initializing the CaseLinker v4 research-network proposal program.

Read, in this order:
1. every applicable AGENTS.md;
2. docs/v4/GROK_BUILD_PROGRAM.md in full;
3. the current vNext engineering charter, upstream handoff, threat model,
   adoption plan, traceability manifest and accepted ADRs;
4. repository CI, dependency, test and migration configuration.

The v4 program document is governing, but it does not override higher-priority
repository instructions or human authority. Do not implement product code.
Do not create a v4 tag, release, deployment, live-data migration or publication.

First perform a read-only repository preflight. Report:
- exact repository, branch, HEAD, approved upstream baseline and remotes;
- working-tree state and any unowned changes;
- applicable instructions and any conflicts;
- commands you propose to run for the baseline;
- the exact artifacts Wave 0 would create;
- all decisions you need before starting Wave 0.

Propose a Wave 0 plan only. Make no file edits until I approve that plan.
End with: “Wave 0 has not begun. Awaiting explicit Wave 0 approval.”
```

## 20. Wave 0 Prompt — Evidence-based discovery and program design

**Primary proof obligation:** demonstrate that the proposed program is based on the actual repository, actual v3 boundaries, and named human decisions rather than assumptions.

```text
Execute Wave 0 only, following docs/v4/GROK_BUILD_PROGRAM.md.

Scope:
- audit the existing CaseLinker vNext/v3 proposal without changing product code;
- run approved non-mutating baseline checks;
- build the requirement registry and gap matrix;
- model existing and target bounded contexts, trust boundaries, data authority,
  state machines and data flows;
- produce the risk register, assumptions, decision requests and staged plan;
- identify the smallest policy-safe vertical slice and the three riskiest
  architectural assumptions;
- propose, but do not perform, isolated experiments for those assumptions.

Required outputs:
- docs/v4/EXECUTION_STATE.md
- docs/v4/REQUIREMENTS_TRACEABILITY.md
- docs/v4/RISK_REGISTER.md
- docs/v4/DECISION_LOG.md
- docs/v4/ASSUMPTIONS.md
- docs/v4/RELEASE_GATES.md
- docs/v4/architecture/CURRENT_STATE.md
- docs/v4/architecture/TARGET_CONTEXTS.md
- docs/v4/architecture/TRUST_BOUNDARIES.md
- docs/v4/architecture/DATA_AUTHORITY.md
- docs/v4/architecture/STATE_MACHINES.md
- docs/v4/evidence/WAVE-00-EVIDENCE.md

Do not choose policy content, production vendors or numerical quality thresholds
without evidence and authorized decisions. Mark unknowns explicitly. Preserve
upstream sovereignty. Do not write implementation code, migrations or release
metadata.

Self-review the Wave 0 artifacts for contradictions, missing requirements,
unowned risks and premature design commitments. Stop at self_verified and ask
for the independent Wave 0 verification prompt.
```

### Wave 0 independent verification prompt

```text
Act as an independent architecture, scientific-integrity, privacy and governance
reviewer. Do not edit implementation code and do not trust the implementer's
summary.

Read docs/v4/GROK_BUILD_PROGRAM.md, every Wave 0 artifact, the vNext charter,
threat model, adoption plan, upstream handoff, traceability manifest, relevant
ADRs and the current repository structure. Verify claims against files and git.

Attempt to falsify Wave 0 by finding:
- requirements omitted or weakened;
- assumptions presented as facts;
- policy or legal decisions assigned to software;
- architecture that creates competing sources of truth;
- missing temporal, correction, identity, disclosure or tenancy boundaries;
- unreviewable coupling or irreversible adoption;
- release-language or upstream-sovereignty violations;
- baseline claims not supported by executed evidence.

Record findings by severity with exact artifact references and concrete repair
criteria. Update only WAVE-00-EVIDENCE.md and a separate review report; do not
silently repair the plan. Recommend gate_ready only if no high-severity finding
remains and every material unknown has an owner and gate.
```

## 21. Wave 1 Prompt — Formal contracts before infrastructure

**Primary proof obligation:** show that the temporal evidence network can be expressed through coherent, versioned domain and policy-neutral contracts before selecting full infrastructure.

```text
Execute Wave 1 only if Wave 0 is human_accepted.

Design and formalize, without production deployment:
- bitemporal semantics and interval precision;
- immutable claim/event/review/correction/dependency identities;
- legal state transitions and transition guards;
- organization/principal/reviewer authority interfaces;
- disclosure request/decision interfaces without inventing policy content;
- source lineage, source-family and derivation contracts;
- identity/event hypothesis contracts with positive and negative evidence;
- deterministic artifact and projection contracts;
- canonical serialization, versioning and compatibility rules;
- audit-event and AI-execution provenance contracts.

Create ADRs, schemas, model invariants, property definitions, state-transition
tables and policy-safe golden examples. Produce a PostgreSQL logical model and
transaction-boundary analysis, but do not perform a live migration. Identify
which constraints belong in the database, domain layer, policy engine and UI.

For every contract include invalid examples and explicit fail-closed behavior.
Demonstrate that allegation is not guilt, event time is not knowledge time,
similarity is not identity, research eligibility is not disclosure permission,
and a projection is not a source of truth.

Do not build broad service scaffolding. Stop when contracts are executable and
internally consistent. Produce WAVE-01-EVIDENCE.md and request independent
verification.
```

## 22. Wave 2 Prompt — Risk-killing experiments

**Primary proof obligation:** obtain evidence about the hardest assumptions before committing the architecture to them.

```text
Execute Wave 2 only if Wave 1 is human_accepted.

Create isolated, disposable worktrees or experiment namespaces. Run the minimum
experiments needed to test these assumptions:

1. PostgreSQL can enforce the chosen append-only, bitemporal and concurrent
   review invariants under realistic conflicting transactions.
2. Dependency invalidation can identify the complete transitive impact of a
   corrected claim without treating a graph projection as authoritative.
3. Purpose/audience/field-level disclosure enforcement can default-deny and
   produce distinct internal, research and public projections without leaking
   internal fields through alternate serializers, logs or exports.
4. Source-family modeling can distinguish independent corroboration from
   duplicated or syndicated reporting on frozen policy-safe examples.
5. Identity hypotheses remain reversible and resist blind transitive merging.

Define falsification criteria before each experiment. Use synthetic or approved
policy-safe fixtures only. Measure results; do not promote spike code directly
into production modules. Record what must change in the target architecture.
Delete or quarantine disposable artifacts only after preserving reproducible
experiment evidence and with safe human-approved cleanup.

Produce WAVE-02-EVIDENCE.md plus an experiment report for each assumption.
Recommend proceed, revise architecture, or stop. Do not begin the temporal
kernel implementation.
```

## 23. Wave 3 Prompt — Temporal evidence kernel vertical slice

**Primary proof obligation:** prove a correction-safe bitemporal lineage from immutable source version to stale dependent artifact.

```text
Execute Wave 3 only if Wave 2 is human_accepted and its architecture revisions
are incorporated.

Implement the narrowest vertical slice that supports:
- immutable source/document versions;
- evidence spans;
- candidate and reviewed claims;
- event time and knowledge time;
- append-only transitions and supersession/retraction;
- dependency registration;
- as-known and valid-time queries;
- correction-triggered staleness of a deterministic derived artifact.

Use typed ports/adapters and a real PostgreSQL integration environment for
transaction semantics, while preserving approved local/fixture compatibility.
Implement forward-only migrations, idempotency, concurrency tests, recovery and
rollback/disable procedures. Use a transactional outbox if asynchronous work is
needed; do not add a queue merely for architectural appearance.

Required scenario: reproduce the January/February correction example in the
governing program, prove both historical queries, preserve the old artifact,
block its current eligibility and build a traceable successor.

No multi-source identity merge, disclosure policy content, public UI, live
ingestion or production deployment belongs in this wave. Produce
WAVE-03-EVIDENCE.md and request independent verification.
```

## 24. Wave 4 Prompt — Multi-source evidence resolution

**Primary proof obligation:** prove that CaseLinker can represent agreement, derivation, contradiction and uncertainty without manufacturing identity or independent corroboration.

```text
Execute Wave 4 only if Wave 3 is human_accepted.

Implement a policy-safe multi-source vertical extension:
- source-family and derivation lineage;
- same-event candidate generation separated from acceptance;
- positive, negative and conflicting identity/event evidence;
- possibly_same, confirmed_same, confirmed_different and unresolved states;
- explicit corroboration, contradiction, correction and insufficient-evidence
  relations;
- reversible human adjudication and reopening when new evidence arrives;
- deterministic evidence/dependency graph projection.

Write false-merge-first adversarial tests. Prohibit blind transitivity and show
that five copies of one originating release count as one evidence family, not
five independent confirmations. Preserve exact source terms and allegation
status through ontology projection.

Do not add facial recognition, person tracking, automatic canonical identity,
or a single opaque confidence score. Produce WAVE-04-EVIDENCE.md with measured
error categories on frozen fixtures and request independent verification.
```

## 25. Wave 5 Prompt — Authenticated review and disclosure enforcement

**Primary proof obligation:** prove that authority to review, research eligibility, and permission to disclose are separate, enforceable decisions.

```text
Execute Wave 5 only if Wave 4 is human_accepted and authorized experts have
supplied or approved the pilot governance rules.

Implement the minimum governed collaboration slice:
- authenticated principals and organizations;
- explicit reviewer authority, assignment, reason codes, second review and
  adjudication where policy requires;
- conflict declarations and immutable review audit;
- versioned disclosure requests and decisions;
- default-deny enforcement at query/service and serialization/export boundaries;
- field-level minimization/redaction;
- internal-review, approved-research and aggregate-only public projections;
- revocation/expiry and policy-version staleness.

Policy rules must be data/configuration owned by named authorized humans, not
invented in code. Test cross-tenant access, alternate serializers, bulk export,
cache, search, log and admin paths. Prove that a scientifically eligible claim
can still be denied disclosure.

Use approved identity-provider interfaces; do not build password or MFA
cryptography casually. Do not deploy. Produce WAVE-05-EVIDENCE.md and request
independent privacy/security verification.
```

## 26. Wave 6 Prompt — Correction operations and evidence-first experience

**Primary proof obligation:** prove that a human can understand, review and correct evidence and that every affected output becomes visibly stale.

```text
Execute Wave 6 only if Wave 5 is human_accepted.

Implement one coherent reviewer and evidence-navigation workflow:
- source passage in context beside the candidate claim;
- event/subject/date bindings, source lineage and ontology mapping;
- review, disagreement, escalation and adjudication actions;
- case-as-governed-view timeline with event and knowledge time;
- chart → members → claims → reviews → evidence → source-version navigation;
- visible disputed, corrected, retracted, stale and disclosure states;
- correction impact report, rebuild queue and correction/supersession notice.

Run keyboard, screen-reader, contrast and non-color-state checks to WCAG 2.2 AA.
Conduct a policy-safe human-factors study for allegation, uncertainty, units,
denominators and causation comprehension. Reviewer throughput is secondary to
correctness and fatigue safety.

Do not add flashy network visualization, conversational assistants or mobile
apps. Produce WAVE-06-EVIDENCE.md and request independent UX, safety and
accessibility verification.
```

## 27. Wave 7 Prompt — Scientific workbench

**Primary proof obligation:** prove that one preregistered shadow study can be reproduced, audited, invalidated by correction, rebuilt and reauthorized.

```text
Execute Wave 7 only if Wave 6 is human_accepted and an independent methodology
reviewer has approved the evaluation design.

Implement versioned study registration, unit and source-population definition,
inclusion/exclusion criteria, duplicate policy, missing-data policy, denominator,
methods, planned outputs, amendments and limitations. Generate coverage,
missingness, membership, denominator, selection-bias and sensitivity reports;
dataset/methodology cards; deterministic Claim Cards, Evidence Packs and Claim
CI; and a signed research-release manifest.

Run one representative policy-safe shadow study from clean environment to
governed output. Independently reproduce it. Correct one governing source,
prove the prior result becomes stale, rebuild it and require a new disclosure
decision. Preserve the historical release and issue a traceable correction.

Block unsupported prevalence, causation, individual-risk and platform-danger
claims. Produce WAVE-07-EVIDENCE.md and request independent scientific and
disclosure verification.
```

## 28. Wave 8 Prompt — Production hardening without deployment

**Primary proof obligation:** prove the proposed system can fail, recover and preserve isolation without losing or leaking governed history.

```text
Execute Wave 8 only if Wave 7 is human_accepted and the target operational
environment and owners are approved.

Harden the approved vertical system for production candidacy:
- PostgreSQL concurrency and tenant controls;
- immutable object storage interface and verified restoration;
- durable queue/outbox/inbox, retry, dead-letter and replay;
- approved IAM integration interfaces and separation of duties;
- encryption/secrets/key operational design;
- tamper-evident privacy-safe audit;
- metrics, alerts, runbooks and incident response;
- forward migrations, compatibility window and recovery;
- backup/restore and disaster-recovery rehearsal;
- dependency inventory, vulnerability review and signed build provenance;
- load, backpressure, chaos/fault and projection-reconciliation tests.

Do not claim certifications and do not deploy. Record measured recovery results,
unmet RPO/RTO decisions, resource assumptions and all unresolved findings.
Produce WAVE-08-EVIDENCE.md and request independent security, privacy, database
and operations verification.
```

## 29. Wave 9 Prompt — Federated evidence-package pilot

**Primary proof obligation:** prove two isolated organizations can exchange, verify, reject, revoke and correct governed artifacts without surrendering local policy control.

```text
Execute Wave 9 only if Wave 8 is human_accepted and federation governance is
explicitly approved.

Implement a test-only federation profile with:
- organization and issuer identities;
- versioned signed package manifest;
- schema/ontology compatibility negotiation;
- digest and signature verification;
- key rotation and revocation;
- quarantine and trust-policy evaluation;
- attribution and source derivation;
- correction/supersession synchronization;
- local disclosure reevaluation and rebuild.

Demonstrate two isolated synthetic organizations. A valid signature proves
integrity and issuer only; it must not create truth, scientific validity or
disclosure permission. Test revoked keys, poisoned packages, incompatible
schemas, replay, partial delivery and conflicting corrections.

Do not connect real organizations or data. Produce WAVE-09-EVIDENCE.md and
request independent cryptography, interoperability, ontology, privacy and
security verification.
```

## 30. Wave 10 Prompt — Independent release-candidate audit and upstream handoff

**Primary proof obligation:** determine honestly what is adoptable, what remains unproven, and whether the proposal is worthy of maintainer consideration—without assigning it an official version.

```text
Execute Wave 10 only after all included prior waves are human_accepted.

Perform a clean-room audit from the approved upstream baseline and the exact
proposal commits. Rebuild traceability, rerun every required quality gate,
reproduce the governed shadow study, replay correction propagation, restore
backups, verify tenant isolation, verify policy shaping, verify package
revocation and compare deterministic outputs.

Commission independent review roles for software, database/concurrency,
scientific method, privacy/disclosure, security, ontology, accessibility/human
factors and upstream adoption. Reviewers must disclose scope and limitations.

Produce:
- a requirement-by-requirement disposition;
- unresolved findings and residual-risk owners;
- a selective adoption/rollback stack;
- migration and compatibility report;
- threat model and privacy-impact input;
- reproducibility and operations runbooks;
- proposed draft PR language that explicitly says “proposal, not release”;
- an honest list of claims the evidence does not support.

Create WAVE-10-EVIDENCE.md with the final non-compensatory scorecard and link
every conclusion to independently reproduced evidence.

Do not merge, deploy, publish, tag, close findings, or call the result v4.0.0.
End with a maintainer decision packet offering accept, amend, defer, selectively
adopt or reject. Only upstream may name or release the work.
```

## 31. Universal independent verification prompt

Use this after any wave that lacks a more specialized verifier:

```text
You are an independent adversarial verifier for the completed CaseLinker wave.
Do not trust prior summaries and do not modify implementation code.

Read docs/v4/GROK_BUILD_PROGRAM.md, EXECUTION_STATE.md, the active wave evidence
packet, linked requirements, ADRs, migrations, schemas, implementation, tests,
git diff/history and applicable repository instructions.

Reconstruct the wave's primary proof obligation. Attempt to falsify it through:
- omitted or weakened constitutional invariants;
- happy-path-only tests;
- stale review/policy/dependency state;
- allegation, unit, denominator, time or identity collapse;
- authorization bypass or cross-tenant access;
- alternate output/log/cache/export paths;
- concurrency, retry, replay and partial-failure behavior;
- non-determinism or unpinned inputs;
- migration/rollback/history loss;
- unsupported scientific or readiness claims;
- upstream-sovereignty violations.

Run approved checks independently. Classify findings as critical, high, medium,
low or observation. For each give evidence, consequence, reproduction and exact
closure criterion. Do not repair findings silently. Recommend gate_ready only
when no critical/high issue remains, evidence is reproducible, and every
external authority dependency is still explicitly gated.
```

## 32. Revision prompt after failed verification

```text
The active wave failed independent verification. Read the verifier report and
the governing program. Do not broaden scope.

For each finding:
1. confirm or challenge it with repository evidence;
2. identify the violated requirement or missing acceptance test;
3. propose the smallest safe correction;
4. state migration, compatibility, privacy and rollback impact;
5. add a regression or adversarial test before implementation;
6. implement only accepted corrections;
7. rerun focused and full approved gates;
8. update, never erase, the evidence packet and decision history.

Return the wave to self_verified. It must undergo independent verification
again. Do not mark the wave gate_ready yourself.
```

## 33. Context-recovery prompt

Use this after interruption, context loss, a new machine, or a long pause:

```text
Recover the CaseLinker proposal program from repository evidence only.

Read every applicable AGENTS.md, docs/v4/GROK_BUILD_PROGRAM.md,
EXECUTION_STATE.md, DECISION_LOG.md, REQUIREMENTS_TRACEABILITY.md, RISK_REGISTER.md,
the latest accepted evidence packet and git history/status. Do not make edits.

Report:
- exact branch and commit;
- last human-accepted wave and evidence;
- active wave and legal state;
- uncommitted/unowned changes;
- unresolved blockers and human decisions;
- checks that must be rerun because evidence may be stale;
- the single next safe action.

If approval evidence is absent or inconsistent, stop. Never infer approval from
commit history, a plan, or a prior agent summary.
```

## 34. Scope-control prompt

Use this whenever an attractive but non-foundational feature appears:

```text
Evaluate the proposed addition against the CaseLinker governing program before
implementing it.

Classify it as:
A. required to prove the active wave obligation;
B. required to preserve a constitutional invariant;
C. useful but independently deferrable;
D. prohibited or unsafe;
E. requires a human policy/authority decision.

Give traceability evidence, dependency cost, new attack/privacy/scientific
surface, migration/rollback impact and the smallest alternative. Implement
nothing unless the item is A or B and already inside approved scope. Record C
in a deferred backlog, stop on D, and request authority for E.
```

## 35. Program-level non-compensatory scorecard

At each human gate, assess every applicable dimension using `not_evaluated`, `fail`, `partial`, `pass`, or `independently_verified`. Do not average the dimensions. Excellence in one area cannot compensate for a privacy, identity, scientific, security, or evidence-integrity failure.

| Dimension | Gate requirement |
|---|---|
| Evidence and temporal integrity | No silent overwrite, lineage gap, or time collapse |
| Privacy and disclosure separation | Default deny; no alternate-path leakage |
| Scientific validity | Explicit unit, denominator, membership, coverage and limitations |
| Identity and allegation safety | No automatic identity or guilt implication |
| Security and tenant isolation | No unresolved critical/high finding in wave scope |
| Determinism and reproducibility | Governed outputs reproduced from pinned inputs |
| Correction completeness | All declared dependencies invalidated and traceable |
| Migration, recovery and reversibility | Rehearsed for persistent-state changes |
| Accessibility and human comprehension | Required once interfaces exist |
| Upstream governance and adoptability | Proposal language and selective adoption preserved |

Recommend `gate_ready` only when every applicable dimension is at least `pass`, every dimension material to the wave's primary proof obligation is `independently_verified`, no constitutional invariant is unmet, no critical/high finding remains, and all external authority decisions are explicitly gated. This rubric summarizes evidence; it never replaces the evidence packet or human judgment.

## 36. Prompt-program completion rule

The program is successful when it enables disciplined decisions, including a justified decision to stop, defer, or reject an architecture. It is not a failure if evidence shows that a proposed component is unsafe, scientifically invalid, operationally disproportionate, or unwanted by upstream. Concealing that result would be failure.

The final handoff must distinguish four statuses for every capability:

```text
implemented_and_verified
implemented_but_external_validation_pending
designed_not_implemented
rejected_or_deferred
```

No other wording may imply completion.

---

## Grounding notes for the human operator

This prompt is deliberately aligned with the existing CaseLinker vNext proposal's engineering charter, threat model, staged adoption posture, content-addressed snapshots, immutable document identity, append-only assertion/review lineage, legal-event extraction, review-aware resolution, deterministic CAC projection, Claim Cards, Evidence Packs, Claim CI, and repository-bound pipeline.

It is also structured for Grok Build's documented workflow: plan review before edits, repository-local `AGENTS.md`, persistent memory, worktrees, subagents, clean diffs, terminal verification, and long-running `/goal` execution. Product mechanics may evolve; the constitutional and human-gate requirements remain authoritative.

Official Grok Build references consulted:

- https://x.ai/build
- https://x.ai/grok/use-cases/code-planning
- https://x.ai/news/introducing-goal
- https://x.ai/news/grok-build-open-source
