# Wave 2 experiment plan

**Status:** `proposed`. Not approved. Not executed.  
**Wave 2 legal state:** `unstarted`  
**Assurance:** `docs/v4/assurance/WAVE-02-ASSURANCE.md`  
**Map:** `docs/v4/assurance/WAVE-02-REQUIREMENTS-MAP.md`

This file proposes how to obtain evidence about the five §22 assumptions. It does not create worktrees, namespaces, migrations, services, or tests. It does not select a production architecture.

If later approved, each experiment must still declare its fixtures and failure conditions in the execution record **before** that experiment’s first mutating command.

## 0. Sequence and dependency analysis

Order is by **risk and dependency**, not by convenience or infrastructure readiness.

D-2026-08-15-006 ranks product-safety as: (1) reversible identity without silent false merges, (2) complete dependency invalidation, (3) default-deny disclosure. PostgreSQL concurrency is important and is §22 item 1, but it is **not** in the top three.

### Independence

| Experiment | Depends on another W2 experiment? | Can run alone? |
|---|---|---|
| W2-E5 Identity | no | yes |
| W2-E2 Invalidation | no | yes |
| W2-E3 Disclosure | no | yes |
| W2-E4 Source-family | no | yes |
| W2-E1 PostgreSQL | no | yes |

No experiment may consume another experiment’s spike as a production module. Shared **fixture ideas** are allowed; shared **code promotion** is not.

W2-E3 may include a synthetic “artifact is stale” fixture. That does not require W2-E2 to have run. W2-E2 must not become the Wave 3 kernel in order to feed W2-E3.

### Default execution order (sequential)

Execution capacity is presently one program operator and one primary environment. **Default execution is sequential.** Do not run all five experiments simultaneously by default.

1. **W2-E5** — reversible identity (R-ID, rank 1)
2. **W2-E2** — dependency invalidation (R-COR, rank 2)
3. **W2-E3** — disclosure leakage (R-DIS, rank 3)
4. **W2-E4** — source-family classification
5. **W2-E1** — PostgreSQL transaction behavior (R-CON; last among the five)

This order does **not** create a dependency between experiment results. Each experiment remains logically independent.

### Parallelism (not the default)

The five experiments are logically independent. Parallel execution may occur **only** after an explicit human amendment that identifies:

- separate builders or namespaces;
- resource capacity;
- evidence isolation;
- reviewer availability;
- how cross-experiment contamination will be prevented.

Until that amendment exists, sequential execution is the only authorized order.

### OD-* and synthetic fixtures

| Experiment | OD-003 | OD-005 | OD-006 | OD-008 | Synthetic fixture without resolving the OD? |
|---|---|---|---|---|---|
| W2-E1 | n/a | n/a | n/a | production claim **blocked** | **yes** — disposable local instance is an instrument, not a vendor decision |
| W2-E2 | production notices **blocked** | n/a | n/a | n/a | **yes** — fixture registry and synthetic corrections |
| W2-E3 | policy **content blocked** | reviewers **out of scope** | n/a | n/a | **yes** — supplied synthetic decisions; no lawful basis |
| W2-E4 | n/a | n/a | n/a | n/a | **yes** — frozen labeled examples (OD-004 blocks live corpus) |
| W2-E5 | n/a | n/a | operational identity **blocked** | n/a | **yes** — reversible hypotheses; no canonical person |

### Where `program_clarification_required` is necessary

Stop and ask the human gate owner instead of inventing a requirement when:

- W2-E3 cannot proceed without a real lawful basis, jurisdiction, audience definition, or production minimization rule;
- W2-E1 results are treated as selecting a production vendor, schema, or host;
- W2-E5 cannot proceed without creating a canonical identity or deciding OD-006 scope;
- a reviewer treats Wave 1 r3/r4 disclosure or SoD extras as Wave 2 exit criteria without a human amendment;
- W2-E2 “completeness” is redefined to require the Wave 3 kernel or knowledge of unknowable external dependents;
- which transitions need two-person control is treated as a software decision (OD-005).

Do not silently resolve blocked decisions.

---

## Shared rules (every experiment)

- **Isolation:** one disposable worktree or namespace per experiment, created only after plan approval. Not created by this packet.
- **Fixtures:** synthetic or already-approved policy-safe text only. No live corpus.
- **Wave 1 contracts:** may be *read* as accepted interfaces. Must not be reopened to absorb r3/r4 extras.
- **Promotion:** experiment code stays in the disposable namespace. No import into production `src/caselinker` modules.
- **Gates:** repository authored-file and traceability checks remain required; product-suite rerun is evidence only if actually run.
- **Cleanup:** preserve the experiment report and fixture hashes first. Destructive delete or instance teardown requires an explicit human approval recorded in the decision log.
- **Reproducibility:** pin engine/runtime versions used; record exact fixture hashes; record commands; seed any concurrency scheduler.
- **Resource bound:** hours-to-a-few-sessions, not a standing service. No cloud production account. No new paid vendor.
- **Human approval before destructive cleanup:** required.
- **Result vocabulary:** `proceed` (assumption holds for architecture planning), `revise architecture` (assumption fails in a bounded way; record the change), `stop` (assumption fails such that the proposed path is unsafe or the program should not continue on it).

---

## W2-E1 — PostgreSQL transaction invariants

### Identity

- **Experiment identifier:** `W2-E1`
- **§22 family:** 1
- **Risk:** R-CON
- **Requirement:** W2-N2

### Exact assumption

A PostgreSQL database, used as a transactional instrument, can enforce the Wave 1-chosen append-only, bitemporal, and concurrent-review invariants under realistic conflicting transactions.

Bitemporal here means **independent storage and query** of event/valid time and knowledge/transaction time. Wave 1 (`bitemporal-interval-v1`, `reject_collapsed_clock`) forbids aliasing the two dimensions. It does **not** impose a fixed ordering between them. A future-effective event may be known earlier. Separate dimensions may coincidentally contain equal values without being collapsed.

### Falsifiable hypothesis

Under a pre-declared conflict matrix, two concurrent clients cannot: overwrite a committed review; delete or update an append-only row; **collapse** event time and knowledge time; or both commit conflicting legal reviews of the same subject as if both were currently authoritative.

**Collapse** means aliasing, overwriting, omitting, or querying the two dimensions as though they were one. It does **not** mean “event time later than knowledge time” or “the two values happen to be equal.”

Independent storage and query must accept:

- a future-effective event interval whose start is after knowledge time;
- coincident values stored as two columns and queried as two dimensions.

Invalid cases are those already rejected by the accepted Wave 1 contract, plus mutation of prior knowledge history: inverted **event** intervals, invented precision, malformed or non-UTC knowledge time, in-place mutation of a prior knowledge-time record, or failure to preserve both dimensions.

### Failure condition (before execution)

The experiment fails if any of the following occurs even once in the declared matrix:

- a committed review row is updated or deleted;
- two conflicting reviews of the same subject are both visible as the current legal successor;
- event time and knowledge time are aliased, overwritten, omitted, or queried as one dimension;
- a future-effective or coincident-value pair stored as separate dimensions is rejected as intrinsically invalid;
- an inverted event interval, invented precision, or malformed/non-UTC knowledge time is stored as valid;
- a prior knowledge-time record is mutated in place;
- a retry creates a second review identity for the same idempotency key;
- the only way to hold the invariant is an undocumented lock outside the declared isolation level.

### Smallest permitted experimental surface

A disposable local PostgreSQL instance (process or container) plus the **minimum** tables needed to represent:

- an append-only review/decision row with abort-on-update/delete;
- **separate** event/valid-time and knowledge/transaction-time columns (not one timestamp reused);
- as-known and valid-during query shapes that address those columns independently;
- a linear successor / current-review constraint or equivalent exclusion;
- two concurrent client sessions.

Not permitted: Alembic/Flyway production migration, cloud selection, copying the full logical model, replacing v3 SQLite, or adding `psycopg` to production dependencies.

### Synthetic or approved fixture

Synthetic assertion/review identities only (`rev_`, `asrt_` style opaque ids). No source passages. Conflict scripts are code, not corpus.

### Realistic conflicts to run (declared now)

| Case | Kind | What it tests |
|---|---|---|
| C1 | conflict | Two sessions accept vs reject the same current review |
| C2 | conflict | Session A appends a successor while session B still reads the predecessor as current |
| C3 | invalid | UPDATE or DELETE against an append-only row |
| C4a | **valid** | Future-effective event: event interval starts after knowledge time; both dimensions stored and queryable |
| C4b | **valid** | Coincident values: event-time start and knowledge time share a calendar instant but remain separate columns |
| C4c | **invalid (collapse)** | Single timestamp reused as both dimensions, `time_model=collapsed`, or a query that treats them as one clock |
| C4d | **invalid** | Inverted **event** interval (`start` after `end`) |
| C4e | **invalid** | Invented precision (e.g. day precision with a month-only value) |
| C4f | **invalid** | Malformed or non-UTC knowledge time |
| C4g | **invalid** | In-place UPDATE of a prior knowledge-time value |
| C5 | query | As-known query while a concurrent insert commits a later knowledge time; must not rewrite prior knowledge history |
| C6 | conflict | Correction vs “publish/eligible” flag on the same subject (fixture flag only) |
| C7 | conflict | Identical retry with the same idempotency key |
| C8 | conflict | Write skew: two sessions each think they are the sole first approver |

### Measurements

- invariant-violation count (must be 0 on the pass path)
- whether C4a and C4b are accepted and remain independently queryable
- whether C4c–C4g are rejected
- whether as-known and valid-during queries address separate columns
- serialization-failure / deadlock count by isolation level
- lost-update count
- whether abort triggers fire on C3 and C4g
- whether C7 is idempotent
- wall time only as a diagnostic, not a pass threshold

### Thresholds

| Result | Threshold |
|---|---|
| `proceed` | Zero silent invariant violations at a **named** isolation level; C4a/C4b accepted as independent dimensions; C4c–C4g rejected; conflicts abort or serialize; C3 denied; C7 idempotent |
| `revise architecture` | Invariants hold only with an isolation level or constraint shape that the logical model did not name; or a specific conflict class needs an outbox/lock design |
| `stop` | Append-only or independent-dimension bitemporal invariants cannot be enforced without application-only hope; or the experiment requires a production hosting decision; or the only “fix” is a cross-clock ordering constraint |

### Required negative and adversarial cases

C3, C4c–C4g, C8, and a client that ignores application checks and speaks SQL directly. C4a and C4b are required **positive** cases.

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E1-REPORT.md` (created only during execution): conflict matrix, isolation level, SQL under test, logs of aborts, recommendation.

### Reproducibility

Record PostgreSQL major version, `default_transaction_isolation`, fixture SQL hashes, and the exact client script revision.

### Isolation, bounds, reuse, cleanup

- Disposable instance in an experiment namespace. Not the developer’s long-lived database.
- Bound: one local instance; tear down after evidence + human cleanup approval.
- **Prohibited production reuse:** do not copy the spike schema into `migrations/` or treat pass as OD-008.
- Cleanup: dump evidence, then human-approved instance destroy.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| Whether a future SoR *candidate* can hold these invariants; what isolation/constraint shape Wave 3 should assume **if** Postgres remains a candidate | Production vendor, host, managed service, schema, RPO/RTO, or replacement of SQLite |

---

## W2-E2 — Transitive dependency invalidation

### Identity

- **Experiment identifier:** `W2-E2`
- **§22 family:** 2
- **Risk:** R-COR
- **Requirement:** W2-N3

### Exact assumption

An authoritative dependency registry, separate from any graph projection, can (1) compute a correct transitive closure over **registered** edges, (2) prevent or detect silent creation of artifact inputs and dependencies without registration, and (3) return an explicit incomplete/fail-closed result when registration coverage cannot be established.

Wave 2 can demonstrate completeness **relative to a declared fixture universe**. It cannot prove knowledge of unknowable external dependencies.

### Three proof obligations (do not collapse)

1. **Closure correctness.** Every transitive dependent in the authoritative **registered** set is found.
2. **Registration coverage.** Artifact inputs and dependencies cannot be created silently without registration, **or** an independent reconciliation mechanism detects the omission against the declared fixture universe.
3. **Incomplete-state behavior.** When coverage cannot be established, the system returns explicit `incomplete` / fail-closed and must **not** claim complete impact.

A frozen fixture **manifest** is the experiment oracle for coverage. A graph projection may **expose** disagreement with the registry or the manifest. The projection must not become authoritative.

### Falsifiable hypothesis

Correcting claim A marks every transitive dependent that is in the registered set. Coverage against the frozen manifest is either complete or reported incomplete. A rebuilt graph projection that omits, adds, or reorders edges cannot change the authoritative impact set or convert an incomplete coverage result into “complete.”

### Failure condition (before execution)

The experiment fails if:

- a registered transitive dependent is omitted from the impact set (**closure**);
- a cycle prevents termination or silently drops nodes (**closure**);
- a previously stale node is reported as fresh because a projection was rebuilt first;
- the experiment answers impact by querying the graph store and treating disagreement as “projection wins”;
- a manifest-declared edge is absent from the registry and the result is still reported as complete impact (**coverage**);
- unregistered dependents or an unregistered correction subject are ignored without an explicit incomplete/fail-closed signal (**incomplete-state**);
- completeness is claimed for dependencies outside the declared fixture universe.

### Smallest permitted experimental surface

An in-memory or file-backed **registry** of dependency edges, a **frozen fixture manifest** listing the declared universe of artifacts and edges, and a deliberately **non-authoritative** projection copy. Operations: register edge, correct node, compute impact, compare registry closure to itself, compare registry to the manifest for coverage, mark stale, optionally surface projection disagreement.

Not permitted: Wave 3 temporal kernel, live rebuild workers, production notices, writing impact into `src/caselinker`, or using the projection as the coverage oracle.

### Synthetic or approved fixture

| Fixture | Shape | Obligation |
|---|---|---|
| F-chain | A → B → C → D, all edges in registry **and** manifest | closure |
| F-diamond | A → B, A → C, B → D, C → D, all registered and manifested | closure |
| F-cycle | A → B → C → A, all registered and manifested | closure |
| F-stale | B already stale when A is corrected; edges registered and manifested | closure |
| F-incomplete | Manifest (and optionally the projection) declares D depends on A; **registry lacks the edge** | coverage + incomplete-state |
| F-missing-reg | Manifest includes node X; correction of X is attempted though X was never registered | coverage + incomplete-state |
| F-silent-create | Attempt to create an artifact input or dependency that is not written to the registry | coverage |

The projection on F-incomplete may also show D→A so that disagreement is visible. The **manifest**, not the projection, is the coverage oracle.

### Measurements

- impact-set equality against the gold transitive closure of the **registry** (closure)
- registry-vs-manifest coverage: missing edges, extra edges, coverage status
- explicit `incomplete` / fail-closed on F-incomplete, F-missing-reg, and F-silent-create
- termination on F-cycle (finite, recorded members)
- count of projection/registry/manifest disagreements and which side was treated as authority (must be registry for closure, manifest for coverage)

### Thresholds

| Result | Threshold |
|---|---|
| `proceed` | All registered transitives found; cycles terminate; every manifest-declared edge is registered **or** coverage is reported incomplete; incomplete coverage never claims complete impact; projection never wins |
| `revise architecture` | Additional edge kinds, creation-time registration hooks, or stale-state model required; still registry-authoritative and manifest-relative |
| `stop` | Completeness requires treating the graph projection as authoritative; or impact cannot be bounded inside the fixture universe; or coverage and closure cannot be distinguished |

### Required negative and adversarial cases

F-cycle, F-incomplete, F-missing-reg, F-silent-create, double correction, correction of an already-stale node, and a projection that invents extra dependents.

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E2-REPORT.md`: fixture hashes, impact sets, fail-closed traces, recommendation.

### Reproducibility

Pin fixture JSON hashes and the closure algorithm revision. No hidden graph database.

### Isolation, bounds, reuse, cleanup

- File-backed namespace only. No service.
- Bound: one session family; no standing queue.
- **Prohibited production reuse:** do not graduate the spike into the Wave 3 kernel without a separate Wave 3 plan.
- Cleanup: keep reports; human-approved delete of the namespace.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| That dependents must be registered at creation; that closure and coverage are separate proofs; that completeness claims are relative to a declared universe; that projections are reconcilers only | Wave 3 schema; production notice policy (OD-003); live rebuild topology; knowledge of unknowable external dependents |

---

## W2-E3 — Default-deny disclosure and leakage

### Identity

- **Experiment identifier:** `W2-E3`
- **§22 family:** 3
- **Risk:** R-DIS
- **Requirement:** W2-N4

### Exact assumption

A mechanism can enforce **supplied** purpose/audience/field decisions, default-deny when a decision is missing, emit distinct internal / research / public projections, and keep internal fields out of alternate serializers, exports, caches, search, logs, error output, and administrative paths.

### Falsifiable hypothesis

Given only synthetic decisions, (1) missing or invalid policy cannot authorize, (2) the three experiment views contain different allowed fields, and (3) every probed output path is either empty/denied or a field-subset of the supplied decision for that audience.

### Failure condition (before execution)

The experiment fails if:

- missing policy, expired fixture, or revoked fixture authorizes any field;
- research or public view contains a field reserved to internal;
- an internal field appears in JSON, CSV, debug repr, exception text, log line, cache dump, search document, or admin listing;
- eligibility is treated as disclosure;
- the experiment invents a lawful basis, jurisdiction, or production audience policy to “make it pass.”

### Smallest permitted experimental surface

- Synthetic decision objects: `{audience, purpose, allowed_fields[], deny|allow}` supplied by the fixture, not by a policy engine that invents rules.
- Three experiment-only projection builders: `internal`, `research`, `public`.
- A leakage harness that renders the same subject through the probe list below.

Not permitted: real lawful bases; production audience definitions; final minimization rules; adopting Wave 1 r4 extras as the exit bar; a product HTTP API.

The three views are a **hypothesis to test**, not an adopted audience policy (`GATE0_PROPOSAL.md` §2).

### Synthetic or approved fixture

Policy-safe subject record with clearly tagged fields, for example: `internal_note`, `display_name`, `research_status`, `public_aggregate_count`. Decisions:

- D-missing: no policy → deny all
- D-internal: allow internal + research + aggregate
- D-research: allow research + aggregate only
- D-public: allow aggregate only
- D-expired / D-revoked: deny all

No real case text. No victim-identifying data.

### Leakage probes (required)

| Probe | Path |
|---|---|
| P1 | Canonical JSON serializer |
| P2 | Alternate serializer (CSV or similar) |
| P3 | Export bundle / zip listing |
| P4 | Cache dump or memoized object repr |
| P5 | Search-index document |
| P6 | Application log line |
| P7 | Exception / error payload |
| P8 | Administrative listing or debug endpoint stub |
| P9 | Existing v3 Evidence Pack / Claim Card **read-only observational probe** |

#### P9 disposition (explicit)

P9 is **observational**. It is **not** part of the experiment-only mechanism pass threshold (that threshold is P1–P8).

A P9 finding must **not** be silently ignored. It **does** affect the experiment recommendation:

- Record the observation with the exact path and field names.
- A **confirmed P9 leak** of an internal or otherwise non-disclosed field through an existing Evidence Pack or Claim Card path yields at least `revise architecture`, with a **named carry-forward obligation** (the product path requires a later authorized repair). Use `stop` if continuing the experiment would require changing those product paths now, or if the leak shows the proposed three-view mechanism cannot be adopted until that product path is repaired.
- P9 must **not** trigger an unapproved product-code repair. Product repair is outside this experiment.

If P9 finds no leak, the mechanism recommendation is decided by P1–P8 alone.

### Measurements

- field-presence matrix: view × field × probe for P1–P8
- separate P9 observation record (path, fields, leak/no-leak)
- deny-on-missing count
- eligibility-vs-disclosure confusion count (must be 0)
- any residual leak with exact path

### Thresholds

| Result | Threshold |
|---|---|
| `proceed` | D-missing/expired/revoked deny; three views distinct; zero internal fields on **P1–P8** for non-internal decisions; **and** P9 recorded with no confirmed leak |
| `revise architecture` | Enforcement must move (e.g. serialize-time only is insufficient); still no invented policy; **or** P9 confirms a leak and a named carry-forward product-path obligation is recorded |
| `stop` | Leakage cannot be prevented on a named P1–P8 path without inventing policy content; eligibility cannot be kept distinct from disclosure; **or** a confirmed P9 leak would require unapproved product repair to continue |

### Required negative and adversarial cases

Missing policy; revoked/expired; probe that logs the full object; error that includes `repr(record)`; search document built from the internal view; admin path that skips the PEP.

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E3-REPORT.md`: field matrices, probe outputs (redacted to field names), recommendation.

### Reproducibility

Pin fixture hashes and harness revision. Record every probe command.

### Isolation, bounds, reuse, cleanup

- Experiment-only builders. Do not modify product disclosure schemas to chase r3/r4 extras.
- Bound: in-process harness; no network audience.
- **Prohibited production reuse:** do not ship the harness as a PDP; do not treat synthetic audiences as OD-003.
- Cleanup: keep matrices; human-approved delete of dumps that might contain fixture internals.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| That every output path must consult a supplied decision; default-deny; projections are not authority | Lawful bases, jurisdictions, real audiences, minimization rules, SoD, Wave 5 policy content |

---

## W2-E4 — Source-family vs independent corroboration

### Identity

- **Experiment identifier:** `W2-E4`
- **§22 family:** 4
- **Risk:** inflated corroboration / RESOLVE-001/002
- **Requirement:** W2-N5

### Exact assumption

Source-family modeling can distinguish independent corroboration from duplicated or syndicated reporting on frozen policy-safe examples, without collapsing the decision into a single opaque confidence score.

### Falsifiable hypothesis

On a frozen multi-example labeled matrix, copies, syndications, and shared originating releases are **not** counted as independent corroboration; genuinely independent sources are classified as independent **and** retained as independent evidence; contradictions are preserved; each decision emits structured reasons (shared text, shared wire id, shared originating release, independent byline+event, contradiction), not one score.

### Failure condition (before execution)

The experiment fails if:

- a direct copy or syndicate is classified as independent corroboration;
- a genuinely independent pair is classified as the same source family; **or**
- a genuinely independent pair is improperly suppressed as non-independent evidence;
- contradiction is dropped or averaged away;
- the only recorded output is a single confidence number;
- live corpus is introduced, or the run relies on one canonical example per label.

Do **not** use “classified as the same family **and** treated as non-evidence” as the independent-pair failure test. Either misclassification **or** improper suppression is enough.

### Smallest permitted experimental surface

A frozen multi-example fixture matrix plus a reason-emitting classifier or explicit rules that read Wave 1 `source-lineage-v1` fields (or an experiment-local equivalent). No ML training on real cases.

### Synthetic or approved fixture (frozen multi-example matrix)

The matrix must be frozen **before** execution. It must contain **structurally distinct** examples for each label and adversarial cross-label cases. It must **not** rely on one canonical example per category.

| Pair ID | Gold label | Structural distinction |
|---|---|---|
| COPY-1 | copy | byte-identical reprint |
| COPY-2 | copy | near-identical reprint; whitespace and outlet header only |
| SYN-1 | syndicate | same wire id; different outlet banner; same body |
| SYN-2 | syndicate | same wire id; translated banner; same body hash |
| REL-1 | shared-release | two outlets quote one official release in full |
| REL-2 | shared-release | two outlets quote different excerpts of the same official release |
| RW-1 | partial-rewrite | same release; adjectives added only |
| RW-2 | partial-rewrite | same release; paragraph reorder plus adjectives |
| CTR-1 | contradiction | two independents disagree on event date |
| CTR-2 | contradiction | two independents disagree on the reported actor |
| IND-1 | independent | distinct originating events, bylines, and details |
| IND-2 | independent | distinct originating events that share only a calendar date |
| X-1 | cross-label | syndicate with a contradictory headline — gold remains syndicate, not independent |
| X-2 | cross-label | independents that share a date — gold remains independent |
| X-3 | cross-label | near-copy versus partial-rewrite boundary — gold is copy or rewrite by the frozen label, not “independent” |

All policy-safe fiction. No real victims. Structured reason codes and contradiction preservation remain required.

### Measurements

- confusion table against labels
- reason codes present on every decision
- count of decisions that emitted only a score (must be 0)
- contradiction-preservation check

### Thresholds

| Result | Threshold |
|---|---|
| `proceed` | copy/syndicate/shared-release are non-independent; every independent pair is classified independent **and** retained as independent evidence; contradictions preserved; reasons required; multi-example matrix used |
| `revise architecture` | additional lineage fields needed (e.g. originating-release id) |
| `stop` | distinction cannot be made without an opaque score or a live-corpus policy |

### Required negative and adversarial cases

Near-copy with cosmetic rewrite; shared release with contradictory headlines; independent sources that happen to share a date; empty lineage.

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E4-REPORT.md`: labeled fixtures, reason codes, confusion table, recommendation.

### Reproducibility

Fixture file hashes. No unseeded model.

### Isolation, bounds, reuse, cleanup

- Frozen files in the experiment namespace.
- Bound: one labeled pack.
- **Prohibited production reuse:** do not adopt the spike as a production scorer.
- Cleanup: keep the labeled pack hash in evidence; human-approved delete of working copies.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| Which lineage fields Wave 3/4 must persist; that corroboration counts require family separation | Live source policy (OD-004); a numeric quality threshold; identity merges (that is W2-E5) |

---

## W2-E5 — Reversible identity hypotheses

### Identity

- **Experiment identifier:** `W2-E5`
- **§22 family:** 5
- **Risk:** R-ID
- **Requirement:** W2-N6

### Exact assumption

Identity hypotheses remain reversible and resist blind transitive merging. Similarity is not identity. A≈B and B≈C do not yield A=C.

### Falsifiable hypothesis

On adversarial fixtures, the system can record `possibly_same` / `confirmed_same` / `confirmed_different` / `unresolved` / `reopened` without writing a canonical person. A≈B plus B≈C does not produce A=C. Negative evidence survives. A false merge can be reopened.

### Failure condition (before execution)

The experiment fails if:

- a canonical person or merged identity row is created;
- A≈B and B≈C produce automatic A=C or a single surviving id;
- negative or contradictory evidence is discarded on accept;
- `confirmed_same` cannot be reopened;
- a false-merge-first fixture cannot be reversed;
- OD-006 scope is treated as decided.

### Smallest permitted experimental surface

Wave 1 `person-hypothesis-v1` / `event-hypothesis-v1` (or an experiment-local copy) plus a fixture driver. No identity table. No extractor change. No production clustering.

### Synthetic or approved fixture

| Fixture | Intent |
|---|---|
| I-trans | A≈B and B≈C with no A–C evidence |
| I-contra | A≈B with both positive and negative evidence |
| I-reopen | accepted `confirmed_same` then new contradictory evidence |
| I-false-first | start from an illegal merged id and require reopen/split |
| I-same-event | two event mentions similar but not the same event |

Policy-safe names only.

### Measurements

- state traces for each fixture
- presence of a forbidden canonical-id table (must be absent)
- whether I-trans emits A=C (must not)
- whether I-reopen and I-false-first restore a reversible hypothesis
- whether I-contra retains both polarities

### Thresholds

| Result | Threshold |
|---|---|
| `proceed` | no canonical id; no automatic A=C; reopen works; negative evidence retained |
| `revise architecture` | additional hypothesis states or evidence slots required; still no canonical merge |
| `stop` | transitivity cannot be prevented except by creating a canonical identity |

### Required negative and adversarial cases

I-trans, I-false-first, I-contra, retry of an already-confirmed pair, and a caller that asks for `transitive_closure`.

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E5-REPORT.md`: state traces, fixture hashes, recommendation.

### Reproducibility

Fixture hashes and hypothesis-engine revision.

### Isolation, bounds, reuse, cleanup

- In-process fixture driver.
- Bound: the five fixtures above plus documented extras if needed.
- **Prohibited production reuse:** do not create `persons` / merge tables; do not wire legacy clustering.
- Cleanup: keep traces; human-approved namespace delete.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| That Wave 4 must keep hypotheses reversible and non-transitive; that false-merge recovery is a first-class path | OD-006 identity-resolution scope; a canonical person model; reviewer qualifications (OD-005) |

---

## Execution is not authorized

This plan is a proposal. Wave 2 remains `unstarted`.

Do not create worktrees, namespaces, disposable databases, experiment modules, or `WAVE-02-EVIDENCE.md` until the human gate owner explicitly approves this boundary.
