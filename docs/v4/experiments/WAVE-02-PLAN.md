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

| Experiment | OD-003 | OD-004 | OD-005 | OD-006 | OD-008 | Synthetic fixture without resolving the OD? |
|---|---|---|---|---|---|---|
| W2-E1 | n/a | n/a | n/a | n/a | production claim **blocked** | **yes** — disposable local instance is an instrument, not a vendor decision |
| W2-E2 | production notices **blocked** | n/a | n/a | n/a | n/a | **yes** — fixture registry and synthetic corrections |
| W2-E3 | policy **content blocked** | n/a | reviewers **out of scope** | n/a | n/a | **yes** — supplied synthetic decisions; no lawful basis |
| W2-E4 | n/a | live corpus **blocked** | n/a | n/a | n/a | **yes** — frozen labeled examples |
| W2-E5 | n/a | n/a | n/a | operational identity **blocked** | n/a | **yes** — reversible hypotheses; no canonical person |

### Where `program_clarification_required` is necessary

Stop and ask the human gate owner instead of inventing a requirement when:

- W2-E3 cannot proceed without a real lawful basis, jurisdiction, audience definition, or production minimization rule;
- W2-E1 results are treated as selecting a production vendor, schema, or host;
- W2-E5 cannot proceed without creating a canonical identity, performing a canonical split, or deciding OD-006 scope;
- a reviewer treats Wave 1 r3/r4 disclosure or SoD extras as Wave 2 exit criteria without a human amendment;
- W2-E2 “completeness” is redefined to require the Wave 3 kernel or knowledge of unknowable external dependents;
- which transitions need two-person control is treated as a software decision (OD-005);
- an access-control / role-or-view privilege surface is silently added to W2-E1 to “prevent arbitrary queries.”

Do not silently resolve blocked decisions.

---

## Shared rules (every experiment)

- **Isolation:** one disposable worktree or namespace per experiment, created only after plan approval. Not created by this packet.
- **Fixtures:** synthetic or already-approved policy-safe text only. No live corpus.
- **System under test vs fixture vs oracle:** each experiment names the SUT, the input fixture visible to the SUT, and a separately held oracle. The SUT must not see gold labels, expected closures, expected field matrices, or expected state traces.
- **Wave 1 contracts:** may be *read* as accepted interfaces. Must not be reopened to absorb r3/r4 extras.
- **Promotion:** experiment code stays in the disposable namespace. No import into production `src/caselinker` modules.
- **Gates:** repository authored-file and traceability checks remain required; product-suite rerun is evidence only if actually run.
- **Cleanup:** preserve the experiment report and fixture hashes first. Destructive delete or instance teardown requires an explicit human approval recorded in the decision log.
- **Reproducibility:** pin engine/runtime versions used; record exact fixture hashes **and** oracle hashes; record commands; record declared schedules; seed any concurrency scheduler. Seeded stress is supplementary, not a substitute for declared interleavings.
- **Resource bound:** hours-to-a-few-sessions, not a standing service. No cloud production account. No new paid vendor.
- **Human approval before destructive cleanup:** required.
- **Result vocabulary:** `proceed` (assumption holds for architecture planning), `revise architecture` (assumption fails in a bounded way; record the change), `stop` (assumption fails such that the proposed path is unsafe or the program should not continue on it). An invalid run is none of these.

### Shared result algorithm

Use the same decision algorithm for all five experiments:

1. **Evidence validity.** If the SUT revision, fixture hash, oracle, required case, command, schedule, or required output is missing, the run is incomplete and must be repeated. It is not eligible for an architecture recommendation.
2. **Stop precedence.** If any predeclared fatal condition occurs in a valid run, recommend `stop`.
3. **Revise precedence.** Otherwise, if any mandatory proceed condition fails, recommend `revise architecture` and name the required change.
4. **Proceed.** Recommend `proceed` only if every mandatory proceed condition passes and no revise/stop condition applies.

An invalid run does not create a fourth architecture recommendation. It means the experiment has not yet been validly executed.

For W2-E3, this algorithm governs the mandatory P1–P8 mechanism result. P9 remains a separately reported observational probe: it cannot improve or invalidate the P1–P8 mechanism result, but a confirmed leak still requires a predeclared `revise architecture` or `stop` disposition. `Not evaluable` is an incomplete observational result with a named carry-forward, not a mechanism pass or failure. No P9 outcome authorizes unplanned product repair.

---

## W2-E1 — PostgreSQL transaction invariants

### Identity

- **Experiment identifier:** `W2-E1`
- **§22 family:** 1
- **Risk:** R-CON
- **Requirement:** W2-N2
- **System under test:** a disposable PostgreSQL instance plus the minimum experiment tables and the declared `as_known` / `valid_during` query interfaces.
- **Not the SUT:** fixture SQL, the transaction driver, the harness, or an independent final-state query issued by the oracle.
- **Oracle:** independent final-state SQL (or a hand-enumerated expected row set) and hand-enumerated expected query results, loaded only after the driver has captured session outcomes. The transaction driver must not decide its own correctness.

### Exact assumption

A PostgreSQL database, used as a transactional instrument, can enforce the Wave 1-chosen append-only, bitemporal, and concurrent-review invariants under realistic conflicting transactions **on information actually represented in the experiment schema**, and the declared query interfaces can address the two stored time dimensions independently.

The assumption has two layers. Do not collapse them.

1. **Storage enforcement.** PostgreSQL must reject a structurally collapsed representation, an invalid event interval, an explicitly declared invented-precision condition, non-UTC knowledge time, and in-place mutation of prior knowledge history. The experiment may not claim that PostgreSQL inferred whether a source invented precision from information absent from the schema.
2. **Query-interface correctness.** Declared `as_known` and `valid_during` query interfaces must address the two stored dimensions independently and return independently enumerated expected results.

This experiment does **not** claim that PostgreSQL can reject every arbitrary incorrect `SELECT` issued by a principal with unrestricted table access. That is not a row constraint. If prevention of arbitrary queries is desired, it requires an explicitly scoped role/view privilege experiment; do not silently add that access-control surface here.

Bitemporal here means **independent storage and query** of event/valid time and knowledge/transaction time. Wave 1 (`bitemporal-interval-v1`, `reject_collapsed_clock`) forbids aliasing the two dimensions. It does **not** impose a fixed ordering between them. A future-effective event may be known earlier. Separate dimensions may coincidentally contain equal values without being collapsed.

### Falsifiable hypothesis

Under a pre-declared conflict matrix and the declared barrier schedules:

- two concurrent clients cannot overwrite a committed review, delete or update an append-only row, or both commit conflicting legal reviews of the same subject as if both were currently authoritative;
- a structurally collapsed representation cannot be stored as valid;
- equal timestamps stored in distinct event/valid-time and knowledge/transaction-time fields remain valid;
- the declared `as_known` and `valid_during` interfaces return the independently enumerated two-dimensional results.

**Storage collapse** means one field or alias substituted for both dimensions, either dimension omitted, or `time_model=collapsed`. It does **not** mean “event time later than knowledge time,” “the two values happen to be equal,” or “a client issued an arbitrary collapsed `SELECT`.”

**Query collapse** is detected by C4c-query-control: an intentionally collapsed query returns a result that differs from the independently enumerated correct two-dimensional result. That demonstrates that the harness can detect query collapse. It is not a claim that the database forbids arbitrary SQL.

### Failure condition (before execution)

**Exclusive classification rule.** A valid failing case maps to exactly one of `stop` or `revise architecture`. Use `stop` only when the invariant is unenforceable at any declared database or query-contract boundary (application-only hope), when only a forbidden cross-clock ordering would make it pass, or when a production hosting decision is required to continue. Use `revise architecture` when the same invariant is enforceable after a named change to isolation, constraint, query boundary, idempotency, or outbox/lock design.

The experiment **stops** if any of the following occurs even once in a valid run:

- a committed review row is updated or deleted and the only remaining protection is application-only hope;
- two conflicting reviews of the same subject are both visible as the current legal successor and no database/query-contract boundary can prevent it;
- a structurally collapsed representation is stored as valid and cannot be rejected by any named constraint or query-contract boundary (application-only hope);
- the only way to hold the invariant is a forbidden cross-clock ordering (event time must precede knowledge time, or the reverse);
- the experiment requires a production hosting decision to continue.

The experiment **revises architecture** if it is valid, no stop condition applies, and any mandatory proceed condition fails — including a named isolation level, constraint, query boundary, idempotency design, or outbox/lock assumption that must change. Example: an inverted event interval is stored as valid under the first attempted CHECK, but a named revised CHECK would reject it. That is `revise architecture`, not `stop`.

The following are mandatory proceed conditions. Failure of any of them, absent a stop condition, is `revise architecture`:

- a future-effective or coincident-value pair stored as separate dimensions is rejected as intrinsically invalid;
- an inverted event interval, an explicitly declared invented-precision condition, or malformed/non-UTC knowledge time is stored as valid;
- a prior knowledge-time record is mutated in place;
- a retry creates a second review identity for the same idempotency key;
- a declared `as_known` or `valid_during` interface returns a result that differs from the independently enumerated expected set;
- C4c-query-control fails to distinguish a collapsed query from the correct two-dimensional result (the harness cannot detect query collapse);
- a required schedule’s expected commit, abort, serialization failure, or idempotent replay does not occur, or the independent final-state oracle disagrees with the expected authoritative rows / current-successor count.

### Smallest permitted experimental surface

A disposable local PostgreSQL instance (process or container) plus the **minimum** tables needed to represent:

- an append-only review/decision row with abort-on-update/delete;
- **separate** event/valid-time and knowledge/transaction-time columns (not one timestamp reused);
- an explicit `time_model` column or equivalent structural marker;
- a `precision` / `precision_source` representation sufficient to reject `precision_source=invented` and a structurally inconsistent precision/value pair that the schema can represent (for example `precision=day` with a month-only start);
- declared `as_known` and `valid_during` query interfaces (views, functions, or pinned SQL shapes) that address those columns independently;
- a linear successor / current-review constraint or equivalent exclusion;
- two concurrent client sessions driven by named barriers.

Not permitted: Alembic/Flyway production migration, cloud selection, copying the full logical model, replacing v3 SQLite, adding `psycopg` to production dependencies, or a role/view privilege experiment unless separately approved.

The “direct SQL client” adversary is restricted to **storage mutation and constraint-bypass attempts** (UPDATE/DELETE of append-only rows, in-place knowledge-time mutation, inserting a collapsed representation, omitting a required dimension). It is not evidence that arbitrary `SELECT` was forbidden.

### Preflight

If no approved disposable PostgreSQL runtime is available, W2-E1 is **blocked/incomplete**. It is not passed, not failed, and must not be used to select infrastructure.

### Synthetic or approved fixture

Synthetic assertion/review identities only (`rev_`, `asrt_` style opaque ids). No source passages. Conflict scripts are code, not corpus.

### Realistic conflicts to run (declared now)

| Case | Kind | What it tests |
|---|---|---|
| C1 | conflict | Two sessions accept vs reject the same current review |
| C2 | conflict | Session A appends a successor while session B still reads the predecessor as current |
| C3 | invalid | UPDATE or DELETE against an append-only row |
| C4a | **valid storage** | Future-effective event: event interval starts after knowledge time; both dimensions stored and independently queryable |
| C4b | **valid storage** | Coincident values: event-time start and knowledge time share a calendar instant but remain separate columns; required positive control |
| C4c-storage | **invalid storage** | Structurally collapsed representation: one field or alias substituted for both dimensions, either dimension omitted, or `time_model=collapsed` |
| C4c-query-control | **harness negative control** | An intentionally collapsed query returns a result that differs from the independently enumerated correct two-dimensional result |
| C4d | **invalid storage** | Inverted **event** interval (`start` after `end`) |
| C4e | **invalid storage** | Explicitly declared invented precision (`precision_source=invented`) or a structurally inconsistent precision/value pair that the schema represents. Not a claim that PostgreSQL inferred invented precision from source prose. |
| C4f | **invalid storage** | Malformed or non-UTC knowledge time |
| C4g | **invalid storage** | In-place UPDATE of a prior knowledge-time value |
| C5 | query + conflict | As-known query while a concurrent insert commits a later knowledge time; must not rewrite prior knowledge history |
| C6 | conflict | Correction vs “publish/eligible” flag on the same subject (fixture flag only; not OD-003) |
| C7 | conflict | Identical retry with the same idempotency key |
| C8 | conflict | Write skew: two sessions each think they are the sole first approver |

### Deterministic concurrency schedules

For C1, C2, C5, C6, C7, and C8, the pass evidence is the declared barrier schedule, not favorable timing. Seeded stress repetitions, if added, are supplementary diagnostics and do not substitute for these interleavings.

**Shared schedule rules**

- Primary named isolation candidate: `SERIALIZABLE` for both T1 and T2, matching the logical-model analysis that review linearization and correction-vs-publish need serializable or equivalent predicate locks. `REPEATABLE READ` may be measured as a diagnostic alternative. Proceed names the isolation level that actually held.
- Barrier wait timeout: 5 seconds. On timeout the run is incomplete unless the schedule’s expected result is abort and the timed-out session is aborted with the expected final state.
- Deadlock: abort both sessions, retry the same schedule once. If deadlock persists and the independent final state does not match the expected row set, the run is incomplete — not a silent pass.
- Exact replay seed: `w2e1-sched-v1`. Randomized stress, if later added, must record its own seed and cannot replace these schedules.
- After both sessions terminate, the oracle issues an independent final-state SQL query and compares it to the hand-enumerated expected row set. The driver log is not the oracle.

Notation: `BEGIN`, `READ`, `WRITE`, `BARRIER Bn`, `COMMIT`. “Winner permutation” means which session is scheduled to reach `COMMIT` first after the last shared barrier.

#### C1 — accept vs reject the same current review

Initial state: subject `S` has current review `R0`. T1 attempts accept successor `R1` (idempotency key `K1`). T2 attempts reject successor `R2` (key `K2`). Isolation: `SERIALIZABLE` / `SERIALIZABLE`.

**C1-W1 (T1 winner)**

1. T1 `BEGIN`; T2 `BEGIN`
2. T1 `READ` current of `S` → `R0`; T2 `READ` current of `S` → `R0`
3. `BARRIER B1` (both have observed `R0`)
4. T1 `WRITE` accept `R0→R1`
5. `BARRIER B2`
6. T2 `WRITE` reject `R0→R2`
7. `BARRIER B3`
8. T1 `COMMIT` — expected: commit
9. `BARRIER B4`
10. T2 `COMMIT` — expected: abort or serialization failure
11. Oracle: authoritative current = `R1`; current-successor count = 1; `R2` not current

**C1-W2 (T2 winner):** same reads and writes; T2 `COMMIT` before T1 `COMMIT`. Expected: `R2` current; count = 1; `R1` not current.

#### C2 — successor append while predecessor still appears current

Initial state: current `R0`. T1 appends `R1`. T2 still treats `R0` as current and appends `R2`. Isolation: `SERIALIZABLE` / `SERIALIZABLE`.

**C2-W1 (T1 commits before T2 writes)**

1. T1 `BEGIN`; T2 `BEGIN`
2. T2 `READ` current → `R0`
3. `BARRIER B1`
4. T1 `READ` current → `R0`; T1 `WRITE` `R1`; T1 `COMMIT`
5. `BARRIER B2`
6. T2 `WRITE` `R2` based on `R0`; T2 `COMMIT` — expected: abort or serialization failure
7. Oracle: current = `R1`; successor count = 1

**C2-W2a (both write before either commits; T1 winner)**

1. T1 `BEGIN`; T2 `BEGIN`
2. T1 `READ` `R0`; T2 `READ` `R0`
3. `BARRIER B1`
4. T1 `WRITE` `R1`; T2 `WRITE` `R2`
5. `BARRIER B2`
6. T1 `COMMIT` — expected: commit
7. `BARRIER B3`
8. T2 `COMMIT` — expected: abort or serialization failure
9. Oracle: current = `R1`; successor count = 1

**C2-W2b (both write before either commits; T2 winner):** same through `BARRIER B2`; T2 `COMMIT` then T1 `COMMIT`. Expected: current = `R2`; count = 1.

#### C5 — as-known query vs later knowledge insert

Initial state: `R0` with knowledge time `KT0` and event interval `ET0`. T2 will insert `R1` with `KT1 > KT0`. Isolation: `SERIALIZABLE` / `SERIALIZABLE`.

**C5-W1 (query started before later insert commits)**

1. T1 `BEGIN`; T1 issues declared `as_known(as_of=KT0)` and holds the snapshot
2. `BARRIER B1`
3. T2 `BEGIN`; T2 `WRITE` `R1` at `KT1`; T2 `COMMIT`
4. `BARRIER B2`
5. T1 re-reads `as_known(as_of=KT0)` through the declared interface; T1 `COMMIT`
6. Oracle: both T1 observations equal the hand-enumerated `{R0}` set; `R0` knowledge history is unchanged; `R1` is visible to `as_known(as_of=KT1)` and not to `as_known(as_of=KT0)`

**C5-W2 (insert commits before the query begins)**

1. T2 inserts and commits `R1` at `KT1`
2. `BARRIER B1`
3. T1 `as_known(as_of=KT0)` — expected `{R0}` only
4. Oracle: `R0` unmodified; two-dimensional query results match the hand-enumerated sets

#### C6 — correction vs publish/eligible fixture flag

Initial state: current `R0`, fixture flag `eligible=false`. T1 appends a correction successor. T2 sets `eligible=true` on what it believes is current. Isolation: `SERIALIZABLE` / `SERIALIZABLE`. The flag is a fixture only; it does not decide OD-003.

**C6-W1 (T1 correction winner)**

1. T1 `BEGIN`; T2 `BEGIN`
2. T1 `READ` `R0`; T2 `READ` `R0`
3. `BARRIER B1`
4. T1 `WRITE` correction successor `R1`; T2 `WRITE` `eligible=true` on the row it believes is current
5. `BARRIER B2`
6. T1 `COMMIT` — expected: commit
7. `BARRIER B3`
8. T2 `COMMIT` — expected: abort or serialization failure
9. Oracle: exactly one current successor (`R1`); `eligible` is whatever that successor stored; both-current is forbidden

**C6-W2 (T2 flag winner):** same through `BARRIER B2`; T2 `COMMIT` then T1 `COMMIT`. Expected: exactly one current successor matching T2’s write; T1 aborts or serializes. Does not decide OD-003.

#### C7 — identical retry, same idempotency key

Initial state: no row with key `K`. T1 and T2 both insert review `R1` with key `K`. Isolation: `SERIALIZABLE` / `SERIALIZABLE` (a unique constraint on the idempotency key is an allowed named architecture-compatible boundary).

**C7-W1 (concurrent insert):** both `BEGIN`, `BARRIER B1`, both `WRITE` key `K`, `BARRIER B2`, both `COMMIT`. Expected: exactly one review identity; the other session aborts or performs an idempotent replay of the same identity.

**C7-W2 (replay after commit):** T1 commits `R1`/`K`; `BARRIER B1`; T2 retries `K`. Expected: idempotent replay; no second identity.

#### C8 — write skew, sole first approver

Initial state: no first approver. Each session reads approver count = 0 and writes itself as first approver. Isolation: `SERIALIZABLE` / `SERIALIZABLE`.

**C8-W1 / C8-W2:** both `BEGIN`, both `READ` count=0, `BARRIER B1`, both `WRITE`, `BARRIER B2`, each winner permutation of `COMMIT`. Expected: one commit, one abort or serialization failure; oracle first-approver count = 1.

### Query expected sets (hand-enumerated)

Using C4a fixture `ET.start=2026-12-01`, `KT=2026-06-01T00:00:00Z` and C4b fixture `ET.start=2026-06-01`, `KT=2026-06-01T00:00:00Z` stored as distinct columns:

- `as_known(as_of=KT)` returns the row if knowledge time ≤ `as_of`, regardless of whether `ET.start` is after `KT`.
- `valid_during(2026-12-01)` returns the C4a row and does not require `KT` to equal that date.
- A collapsed query that predicates on a single timestamp as if it were both clocks is the C4c-query-control input; its result must differ from the two-dimensional expected set above.

### Measurements

- invariant-violation count (must be 0 on the pass path)
- whether C4a and C4b are accepted and remain independently queryable
- whether C4c-storage and C4d–C4g are rejected
- whether C4c-query-control detects query collapse
- whether declared `as_known` and `valid_during` results match the hand-enumerated sets
- serialization-failure / deadlock count by isolation level
- lost-update count
- whether abort triggers fire on C3 and C4g
- whether C7 is idempotent
- whether each declared schedule produced the expected commit/abort and oracle row set
- wall time only as a diagnostic, not a pass threshold

### Thresholds

| Result | Threshold |
|---|---|
| invalid / incomplete | Missing disposable Postgres runtime, SUT revision, fixture hash, oracle, required case, command, schedule, or output. Repeat. Not an architecture recommendation. |
| `stop` | An invariant cannot be enforced at the declared database/query-contract boundary without application-only hope, or only a forbidden cross-clock ordering makes it pass, or a production hosting decision is required to continue. |
| `revise architecture` | No stop condition, but a named isolation level, constraint, query boundary, idempotency design, or outbox/lock assumption must change; or a mandatory proceed condition failed. |
| `proceed` | All mandatory schedules and temporal cases pass at an explicitly named architecture-compatible boundary; C4a/C4b accepted as independent dimensions; C4c-storage and C4d–C4g rejected; C4c-query-control detects collapse; declared query interfaces match the independent expected sets; C3 denied; C7 idempotent; zero silent invariant violations. |

### Required negative and adversarial cases

C3, C4c-storage, C4c-query-control, C4d–C4g, C8, and a direct SQL client restricted to storage mutation and constraint-bypass attempts. C4a and C4b are required **positive** cases, including coincident values in distinct clock fields.

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E1-REPORT.md` (created only during execution): conflict matrix, named schedules, isolation level, SQL under test, logs of aborts, independent oracle queries, recommendation.

### Reproducibility

Record PostgreSQL major version, `default_transaction_isolation`, fixture SQL hashes, oracle expected-set hashes, client script revision, schedule identifiers, and seed `w2e1-sched-v1`.

### Isolation, bounds, reuse, cleanup

- Disposable instance in an experiment namespace. Not the developer’s long-lived database.
- Bound: one local instance; tear down after evidence + human cleanup approval.
- **Prohibited production reuse:** do not copy the spike schema into `migrations/` or treat pass as OD-008.
- Cleanup: dump evidence, then human-approved instance destroy.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| Whether a future SoR *candidate* can hold these stored-data invariants and whether the declared query interfaces address two dimensions; what isolation/constraint shape Wave 3 should assume **if** Postgres remains a candidate | Production vendor, host, managed service, schema, RPO/RTO, replacement of SQLite, invented-precision inference from source prose, or arbitrary-SQL prevention |

---

## W2-E2 — Transitive dependency invalidation

### Identity

- **Experiment identifier:** `W2-E2`
- **§22 family:** 2
- **Risk:** R-COR
- **Requirement:** W2-N3
- **System under test:** the experiment registry and its impact/coverage operations, including `create_artifact(id, input_ids)`.
- **Not the SUT:** the frozen input fixture, the separately hashed oracle artifact, the harness comparator, or any graph projection.
- **Oracle:** a separately hashed oracle artifact loaded by the harness only after SUT output is captured.

### Exact assumption

An authoritative dependency registry, separate from any graph projection, can (1) compute a correct transitive closure over **registered** edges, (2) prevent or detect silent creation of artifact inputs and dependencies without registration, and (3) return an explicit incomplete/fail-closed result when registration coverage cannot be established.

Wave 2 can demonstrate completeness **relative to a declared fixture universe**. It cannot prove knowledge of unknowable external dependencies.

### One edge convention (frozen)

> `A → B` means “B depends on A”; correcting A may impact B.

This matches Wave 1 `dependency-edge-v1` used as `from_id=A`, `to_id=B`, `edge_kind=derived_from` (B is derived from A). Every fixture, figure, and expected set in this experiment uses that direction. F-incomplete therefore uses missing `A → D`, not `D → A`, when D depends on A.

### Three proof obligations (do not collapse)

1. **Closure correctness.** Every transitive dependent in the authoritative **registered** set is found.
2. **Registration coverage.** Artifact inputs and dependencies cannot be created silently without registration, **or** an independent reconciliation mechanism detects the omission against the declared fixture universe.
3. **Incomplete-state behavior.** When coverage cannot be established, the system returns explicit `incomplete` / fail-closed and must **not** claim complete impact.

A frozen fixture **manifest** is the coverage universe. A separately hashed **oracle artifact** holds expected closures and coverage status. A graph projection may **expose** disagreement with the registry or the manifest. The projection must not become authoritative. Do not compare registry closure to itself.

### Falsifiable hypothesis

Correcting claim A marks every transitive dependent that is in the registered set, using the frozen `A → B` convention. Coverage against the frozen manifest is either complete or reported incomplete. A rebuilt graph projection that omits, adds, or reorders edges cannot change the authoritative impact set or convert an incomplete coverage result into “complete.” Silent creation without a registry edge is detected by independent reconciliation.

### Failure condition (before execution)

**Stop** if, in a valid run:

- completeness requires treating the graph projection as authoritative;
- impact cannot be bounded inside the fixture universe;
- coverage and closure cannot be distinguished;
- the only available oracle is the SUT closure function applied to its own output.

**Revise architecture** if the run is valid, no stop condition applies, and any mandatory proceed condition fails.

Mandatory proceed conditions:

- every hand-enumerated registered transitive is present in the impact set;
- F-cycle terminates with the enumerated finite members;
- every manifest-declared edge is registered **or** coverage is reported `incomplete` with the enumerated missing edges;
- incomplete coverage never claims complete impact;
- projection never wins;
- F-silent-create is detected by reconciliation of artifact inputs against registered edges.

### Smallest permitted experimental surface

An in-memory or file-backed **registry** of dependency edges, a **frozen input fixture** listing artifacts and declared inputs, a **separately hashed oracle artifact**, and a deliberately **non-authoritative** projection copy.

Operations visible to the SUT:

- `register_edge(from_id, to_id)`
- `create_artifact(id, input_ids)` — the normal path **must** register a corresponding `input → id` edge for each input
- `correct_node(id)`
- `compute_impact(id)`
- `coverage_status()` as reported by the SUT (the harness still decides correctness against the oracle)

Harness-only operations, not visible as ordinary SUT inputs:

- load the oracle artifact after SUT output is captured;
- compare artifact inputs in the frozen manifest with registered edges and return `incomplete` when they disagree (independent reconciliation);
- compare SUT impact sets to `expected_impact_by_corrected_node`.

Adversarial bypass, fixture-only: create or alter the fixture artifact record **without** writing the registry edge. This remains a fixture mechanism, not the Wave 3 kernel.

Not permitted: Wave 3 temporal kernel, live rebuild workers, production notices, writing impact into `src/caselinker`, using the projection as the coverage oracle, or generating expected impact sets from the SUT closure function.

### Two hashed artifacts

| Artifact | Visible to SUT? | Contents |
|---|---|---|
| Input fixture | yes | artifact ids, `input_ids`, registered edges to load, correction subjects, projection copy. No gold labels, no expected closures, no coverage answers. |
| Oracle artifact | no — harness after capture only | `manifest_edges`; `registered_edges`; `expected_impact_by_corrected_node`; `expected_coverage_status`; `expected_missing_edges`; `expected_projection_disagreements` |

The reproduction record must preserve both hashes and show that only the input-fixture hash was available to the SUT.

### Synthetic or approved fixture

Expected impact sets are hand-enumerated for these small graphs **before** execution. They may not be generated by the SUT closure function, imported from its output, or made visible as ordinary inputs to the SUT.

| Fixture | Input shape (`A → B` = B depends on A) | Oracle (hand-enumerated) |
|---|---|---|
| F-chain | `A → B → C → D`, all edges in registry and manifest | correct A → `{B, C, D}`; coverage `complete` |
| F-diamond | `A → B`, `A → C`, `B → D`, `C → D`, all registered and manifested | correct A → `{B, C, D}`; coverage `complete` |
| F-cycle | `A → B → C → A`, all registered and manifested | correct A → finite `{B, C}` (corrected subject A is **not** included unless a later amendment explicitly freezes self-impact); coverage `complete`; must terminate |
| F-stale | `A → B`; B already marked stale; edges registered and manifested | correct A → `{B}`; B remains stale; not reported fresh; coverage `complete` |
| F-incomplete | Manifest declares `A → D` (D depends on A). Registry has no other edges, or has only unrelated registered edges, and **lacks** `A → D`. Projection may also show `A → D` so disagreement is visible. | correct A → registered closure (empty if A has no registered dependents) **plus** `coverage=incomplete`, `expected_missing_edges={A → D}` |
| F-missing-reg | Manifest includes node X; correction of X is attempted though X was never registered | `coverage=incomplete`; no complete-impact claim |
| F-silent-create | Normal path: `create_artifact(D, input_ids=[A])` must register `A → D`. Adversarial path: write artifact D with input A **without** the registry edge. | adversarial path → independent reconciliation returns `incomplete`; missing `A → D` reported |

The **oracle artifact**, not the projection and not the SUT closure, is the closure and coverage gold.

### Measurements

- impact-set equality against the hand-enumerated `expected_impact_by_corrected_node`
- registry-vs-manifest coverage: missing edges, extra edges, coverage status
- explicit `incomplete` / fail-closed on F-incomplete, F-missing-reg, and F-silent-create
- termination on F-cycle (finite, recorded members `{B, C}`)
- count of projection/registry/manifest disagreements and which side was treated as authority (must be registry for closure, manifest/oracle for coverage)
- both artifact hashes, with proof that the oracle hash was not an SUT input

### Thresholds

| Result | Threshold |
|---|---|
| invalid / incomplete | Missing SUT revision, input-fixture hash, oracle hash, required fixture, command, or output; or the oracle was visible to the SUT. Repeat. |
| `stop` | Completeness requires treating the graph projection as authoritative; or impact cannot be bounded inside the fixture universe; or coverage and closure cannot be distinguished; or the only oracle is the SUT closure. |
| `revise architecture` | No stop condition, but additional edge kinds, creation-time registration hooks, or stale-state model are required; still registry-authoritative and manifest-relative. |
| `proceed` | All registered transitives match the hand-enumerated sets; cycles terminate at `{B, C}`; every manifest-declared edge is registered **or** coverage is reported incomplete with the enumerated missing edges; incomplete coverage never claims complete impact; projection never wins; F-silent-create is detected by reconciliation. |

### Required negative and adversarial cases

| Case | Expected outcome |
|---|---|
| F-cycle | Terminates; impact of A = `{B, C}` |
| F-incomplete | `incomplete`; missing `A → D`; no complete-impact claim |
| F-missing-reg | `incomplete`; no complete-impact claim |
| F-silent-create (adversarial) | reconciliation `incomplete`; missing `A → D` |
| Double correction of A | Second `correct_node(A)` with the same idempotency key does not invent extra dependents and does not drop `{B, C, D}` on F-chain |
| Correction of an already-stale node (F-stale) | B remains in the impact set and is not reported fresh |
| Projection invents extra dependents | Extra projection edges ignored for impact; recorded as `expected_projection_disagreements`; registry still wins |

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E2-REPORT.md`: both fixture hashes, impact sets, fail-closed traces, recommendation.

### Reproducibility

Pin input-fixture JSON hash, oracle-artifact hash, and the closure algorithm revision. No hidden graph database. Show that only the input-fixture hash was available to the SUT.

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
- **Requirement:** W2-N4 (P1–P8) and W2-N4-P9 (observational)
- **System under test:** one shared supplied-decision evaluator plus P1–P8 output adapters that consult it.
- **Not the SUT:** the frozen supplied decisions, the independently enumerated expected field sets, or the P9 observational probe of existing product entry points.
- **Oracle:** the frozen supplied decision plus independently enumerated expected field sets. Labels and expected outputs are oracle-only, not SUT inputs.

### Exact assumption

A mechanism can enforce **supplied** purpose/audience/field decisions, default-deny when a decision is missing, emit distinct internal / research / public projections, and keep internal fields out of alternate serializers, exports, caches, search, logs, error output, and administrative paths.

### Falsifiable hypothesis

Given only synthetic decisions, (1) missing or invalid policy cannot authorize, (2) the three experiment views contain different allowed fields, (3) every P1–P8 output path is either empty/denied or a field-subset of the supplied decision for that audience, and (4) adapters cannot pass a changed fixture by hard-coding the original expected matrix because they share one evaluator.

### One decision evaluator

P1–P8 must use **one** experiment-level decision evaluator. Each output adapter may serialize differently. It may **not** maintain a separate audience allowlist or hard-code the frozen expected matrix.

Evaluator contract:

- input: subject record + supplied decision `{audience, purpose, allowed_fields[], deny\|allow, expiry, revocation_state}`;
- output: the allowed field set, or deny-all;
- missing, expired, or revoked decision → deny-all;
- eligibility flags are not consulted as authorization.

### Failure condition (before execution)

**Stop** if, in a valid P1–P8 run:

- leakage cannot be prevented on a named P1–P8 path without inventing policy content;
- eligibility cannot be kept distinct from disclosure;
- a confirmed P9 leak would require unapproved product repair to continue the experiment.

**Revise architecture** if the run is valid, no stop condition applies, and any mandatory P1–P8 proceed condition fails, or if P9 confirms a leak (experiment-level disposition; the P1–P8 mechanism result is still reported separately).

Mandatory P1–P8 proceed conditions:

- missing, expired, or revoked fixtures deny all fields on every P1–P8 path;
- the three views are distinct field sets;
- zero internal fields on P1–P8 for non-internal decisions;
- every adapter consults the shared evaluator (no per-adapter allowlist);
- every metamorphic case below matches its expected observation.

P9 does not improve a failed P1–P8 result into a pass. A P9 `not evaluable` result does not invalidate a P1–P8 pass.

### Smallest permitted experimental surface

- Synthetic decision objects: `{audience, purpose, allowed_fields[], deny|allow}` supplied by the fixture, not by a policy engine that invents rules.
- One shared evaluator.
- Three experiment-only projection builders: `internal`, `research`, `public`.
- A leakage harness that renders the same subject through P1–P8.
- A read-only observational probe of the existing product entry points named in P9.

Not permitted: real lawful bases; production audience definitions; final minimization rules; adopting Wave 1 r4 extras as the exit bar; a product HTTP API; unapproved product-code repair.

The three views are a **hypothesis to test**, not an adopted audience policy (`GATE0_PROPOSAL.md` §2).

### Synthetic or approved fixture

Policy-safe subject record with clearly tagged fields, for example: `internal_note`, `display_name`, `research_status`, `public_aggregate_count`. Decisions (SUT sees the decision object; it does **not** see expected output matrices):

- D-missing: no policy → deny all
- D-internal: allow `internal_note`, `display_name`, `research_status`, `public_aggregate_count`
- D-research: allow `research_status`, `public_aggregate_count`
- D-public: allow `public_aggregate_count`
- D-expired / D-revoked: deny all

Independently enumerated expected field sets (oracle-only):

| Decision | Expected fields on every P1–P8 path |
|---|---|
| D-missing | `{}` |
| D-internal | `{internal_note, display_name, research_status, public_aggregate_count}` |
| D-research | `{research_status, public_aggregate_count}` |
| D-public | `{public_aggregate_count}` |
| D-expired | `{}` |
| D-revoked | `{}` |

No real case text. No victim-identifying data.

### Leakage probes (required)

| Probe | Path | Role |
|---|---|---|
| P1 | Canonical JSON serializer | mechanism |
| P2 | Alternate serializer (CSV or similar) | mechanism |
| P3 | Export bundle / zip listing | mechanism |
| P4 | Cache dump or memoized object repr | mechanism |
| P5 | Search-index document | mechanism |
| P6 | Application log line | mechanism |
| P7 | Exception / error payload | mechanism |
| P8 | Administrative listing or debug endpoint stub | mechanism |
| P9 | Existing v3 Evidence Pack / Claim Card **read-only observational probe** | observational |

### Metamorphic cases (required; P1–P8)

Hold the evaluator fixed. Do not retune adapters against expected lists.

| ID | Change | Expected observation |
|---|---|---|
| M1 | Remove one previously allowed field from the supplied decision | That field disappears from every P1–P8 path; other allowed fields remain |
| M2 | Change audience (D-internal → D-public) while holding the subject constant | Output field set becomes `{public_aggregate_count}` on every P1–P8 path |
| M3 | After an allowed D-internal run, revoke or expire the same decision | Subsequent P1–P8 outputs are empty/denied |
| M4 | Add a decoy internal field `internal_decoy` that was not present when the adapters were first written, and do not add it to the supplied allowed set | `internal_decoy` appears on no P1–P8 path |
| M5 | Mutate field order and irrelevant values (`display_name` spelling-preserving whitespace, JSON key order) without changing authorization | Authorization outcome unchanged; no extra field authorized |

### P9 — make the observational probe evaluable

**Exact existing entry points** (read-only; do not modify):

- `caselinker.analysis.claims.ClaimCardBuilder.build` and `ClaimCard.to_dict`
- `caselinker.analysis.evidence_pack.EvidencePackAssembler.assemble` and `EvidencePack.canonical_json`

These paths currently assemble a cohort Claim Card and an Evidence Pack index. They exclude `source_text`, `personal_display_labels`, and `disclosure_authorization` as pack-level exclusions. They predate a disclosure-decision PEP.

**Synthetic input mapping** (policy-safe; no live corpus):

| Tagged fixture field | Mapping rule |
|---|---|
| `public_aggregate_count` | May be copied into a synthetic `CohortResult.numerator` / claim-text count if a disposable in-memory `CohortResult` can be constructed without product mutation |
| `research_status` | May be copied into synthetic `limitations` text only if that field is being used as a tagged carrier; otherwise unmappable |
| `internal_note` | No corresponding product key. Recorded as **unmappable** unless a later authorized amendment names a real product field. |
| `display_name` | No corresponding product key on Claim Card / Evidence Pack (`personal_display_labels` is an exclusion label, not an input). Unmappable. |

If a disposable in-memory `CohortResult` cannot be constructed without editing product code or inventing real policy content, P9 is `not evaluable`.

**Supplied synthetic decision used to classify fields:** D-public (allow only `public_aggregate_count`) unless the probe is explicitly re-run with D-missing. Denied fields are every tagged field not in that allowed set.

**Classifications**

| Label | Meaning |
|---|---|
| `confirmed_leak` | An internal-tagged field, or a mapped equivalent of a denied field, **emerges** in `ClaimCard.to_dict()` or `EvidencePack.canonical_json` contrary to the supplied synthetic decision. |
| `path_lacks_enforcement` | The entry point runs and produces output but has no hook that consults the supplied decision. This is an architecture gap, not automatically a proved data leak. Upgrade to `confirmed_leak` if a denied mapped value still appears. |
| `not_evaluable` | The entry point cannot accept a policy-safe synthetic mapping (no field correspondence; constructor requires live snapshot/cohort objects that cannot be fabricated without product mutation; or invoking it would invent real policy content). Incomplete observational result. Name a carry-forward. Do not invent real policy. |

**Disposition rules**

- Report P9 separately from the P1–P8 mechanism result.
- A `confirmed_leak` cannot be ignored. Experiment-level recommendation is at least `revise architecture` with a named carry-forward that the product path requires a later authorized repair. Use `stop` if continuing would require changing those product paths now, or if the leak shows the proposed three-view mechanism cannot be adopted until that path is repaired.
- `path_lacks_enforcement` without a confirmed leak is a named carry-forward. It does not by itself invalidate a P1–P8 pass.
- `not_evaluable` is an incomplete observational result with a named carry-forward. It is not a mechanism pass or failure.
- No P9 outcome authorizes unplanned product repair.

### Measurements

- field-presence matrix: view × field × probe for P1–P8
- metamorphic observations M1–M5
- proof that every adapter called the shared evaluator (call count / identity)
- separate P9 observation record (entry point, mapping used, classification, carry-forward)
- deny-on-missing count
- eligibility-vs-disclosure confusion count (must be 0)
- any residual leak with exact path

### Thresholds

The experiment emits **one** architecture recommendation. The P1–P8 mechanism result is an input to that recommendation, not a second recommendation.

P1–P8 mechanism pass means: D-missing/expired/revoked deny; three views distinct; zero internal fields on P1–P8 for non-internal decisions; shared evaluator used; M1–M5 pass.

| Result | Threshold |
|---|---|
| invalid / incomplete | Missing SUT revision, fixture hash, oracle expected-set hash, required probe, command, or P1–P8 output. Repeat. P9 `not_evaluable` does **not** make the P1–P8 run incomplete. |
| `stop` | Leakage cannot be prevented on a named P1–P8 path without inventing policy content; eligibility cannot be kept distinct from disclosure; **or** a confirmed P9 leak would require unapproved product repair to continue. |
| `revise architecture` | No stop condition, and any of: P1–P8 mechanism pass fails in a bounded way (enforcement must move; a metamorphic case failed; an adapter bypassed the shared evaluator); **or** P9 is a `confirmed_leak` that can be carried forward without repairing product code now. |
| `proceed` | P1–P8 mechanism pass **and** P9 is not a `confirmed_leak`. P9 may be `path_lacks_enforcement` or `not_evaluable` with a named carry-forward. |

### Required negative and adversarial cases

Missing policy; revoked/expired; probe that logs the full object; error that includes `repr(record)`; search document built from the internal view; admin path that skips the PEP; M1–M5; decoy field.

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E3-REPORT.md`: field matrices, probe outputs (redacted to field names), P9 observation, recommendation.

### Reproducibility

Pin fixture hashes, oracle expected-set hashes, and harness revision. Record every probe command and the evaluator identity.

### Isolation, bounds, reuse, cleanup

- Experiment-only builders. Do not modify product disclosure schemas to chase r3/r4 extras.
- Bound: in-process harness; no network audience.
- **Prohibited production reuse:** do not ship the harness as a PDP; do not treat synthetic audiences as OD-003.
- Cleanup: keep matrices; human-approved delete of dumps that might contain fixture internals.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| That every experiment output path must consult a supplied decision; default-deny; projections are not authority; that a named existing product path leaked, lacked enforcement, or could not be evaluated | Lawful bases, jurisdictions, real audiences, minimization rules, SoD, Wave 5 policy content, unplanned product repair, or that existing product serializers are safe when P9 is `not_evaluable` or `path_lacks_enforcement` |

---

## W2-E4 — Source-family vs independent corroboration

### Identity

- **Experiment identifier:** `W2-E4`
- **§22 family:** 4
- **Risk:** inflated corroboration / RESOLVE-001/002
- **Requirement:** W2-N5
- **System under test:** the reason-emitting classifier or explicit rules that read Wave 1 `source-lineage-v1` fields (or an experiment-local equivalent) plus raw lineage features.
- **Not the SUT:** the development pack, the evaluation pack, gold labels, or expected reason codes.
- **Oracle:** the frozen evaluation-pack gold matrix. Gold labels and expected reason codes remain oracle-only.

### Exact assumption

Source-family modeling can distinguish independent corroboration of the **same** underlying event or claim from duplicated or syndicated reporting on frozen policy-safe examples, without collapsing the decision into a single opaque confidence score, and without treating unrelated events as corroboration.

### Falsifiable hypothesis

On a frozen multi-example labeled matrix, copies, syndications, shared originating releases, and partial rewrites of the same matter are **not** counted as independent corroboration; genuinely independent sources that report the same frozen event/claim key are classified as independent **and** retained as independent evidence; unrelated-event pairs are labeled `unrelated`, not independent corroboration; contradictions are preserved; each decision emits structured reasons, not one score.

### Failure condition (before execution)

**Stop** if, in a valid run:

- the distinction cannot be made without an opaque score or a live-corpus policy;
- the experiment invents OD-004 source-class policy.

**Revise architecture** if the run is valid, no stop condition applies, and any mandatory proceed condition fails — including a valid misclassification that does not meet a stop condition, or a need for additional lineage fields (for example originating-release id).

Mandatory proceed conditions:

- every copy, syndicate, shared-release, and partial-rewrite pair is **not** counted as independent corroboration;
- every genuine same-matter independent pair is classified independent **and** retained as independent evidence;
- every unrelated-event pair is labeled `unrelated` and is **not** counted as independent corroboration;
- contradictions are preserved, including contradiction inside one syndicated family;
- every decision emits structured reason codes;
- empty-lineage and partial-rewrite pairs match the frozen expected behavior below;
- the scored table uses the evaluation pack, not a one-example-per-label development convenience.

### Smallest permitted experimental surface

A frozen development pack and a separate frozen evaluation pack plus a reason-emitting classifier or explicit rules that read Wave 1 `source-lineage-v1` fields (or an experiment-local equivalent) and raw features (text hashes, wire ids, originating-release ids, bylines, event/claim keys). No ML training on real cases. Do not train or tune on evaluation gold. If a ruleset is adjusted after seeing evaluation gold, the run is invalid.

SUT inputs are raw features only. Do not supply a pre-filled `same_source_family` or gold `relation` for the SUT to echo.

### Orthogonal gold axes

Model every pair on three axes. “Independent source” is not the same proposition as “corroborates this claim.” A pair may have family relationship `independent` and still must **not** be counted as independent corroboration when the claim relationship is `unrelated`. Evidence treatment is a function of both family and claim axes, never of family alone.

| Axis | Allowed values |
|---|---|
| Source-family relationship | `copy`, `syndicate`, `shared-release`, `partial-rewrite`, `independent`, `empty-lineage` |
| Claim relationship | `same/consistent`, `same/contradictory`, `unrelated` |
| Evidence treatment | `retain_as_independent`, `retain_as_contradiction`, `do_not_count_as_independent` |

### Exact expected behavior for named hard cases

| Case | Frozen expected behavior |
|---|---|
| Partial rewrite | Same originating release or near-copy with editorial rewrite (adjectives, reorder). Family = `partial-rewrite`. Treatment = `do_not_count_as_independent`. Reason includes `partial_rewrite` (and `shared_originating_release` when a release id is present). Not independent corroboration. |
| Empty lineage | Missing family id, wire id, release id, and usable derivation links. Family = `empty-lineage`. Treatment = `do_not_count_as_independent`. Reason = `empty_lineage`. Do not invent independence or a score. |
| Shared facts, independent provenance | Same frozen event/claim key; distinct acquisition paths; no shared wire or release id; independently developed detail; no near-copy text. Family = `independent`. Claim = `same/consistent`. Treatment = `retain_as_independent`. |
| Independent reports, same calendar date | Same as above even if both mention the same date. Date overlap is not syndication. |
| Contradiction within one syndicated family | Family = `syndicate`. Claim = `same/contradictory`. Treatment = `do_not_count_as_independent` **and** contradiction preserved (`retain_as_contradiction` as a recorded polarity, not as independent corroboration). |
| Unrelated events | Claim = `unrelated`. Label `unrelated`. Do **not** call this independent corroboration, even if bylines differ. |

### Synthetic or approved fixture (two frozen packs)

Both packs are frozen **before** execution. Each required combination relevant to proceed has **at least two** structurally distinct examples. All policy-safe fiction. No real victims.

**Development pack** may be inspected while building the harness. It is not the scored oracle.

**Evaluation pack** is the scored oracle. Gold labels and expected reason codes are harness-only.

Required evaluation-pack pairs (minimum). Event/claim keys are synthetic (`evt_alpha`, `evt_beta`, `clm_alpha`, …).

| Pair ID | Family | Claim | Treatment | Structural distinction |
|---|---|---|---|---|
| COPY-1 | copy | same/consistent | do_not_count_as_independent | byte-identical reprint of `evt_alpha` |
| COPY-2 | copy | same/consistent | do_not_count_as_independent | near-identical reprint of `evt_alpha`; whitespace and outlet header only |
| SYN-1 | syndicate | same/consistent | do_not_count_as_independent | same wire id; different outlet banner; same body; `evt_alpha` |
| SYN-2 | syndicate | same/consistent | do_not_count_as_independent | same wire id; translated banner; same body hash; `evt_alpha` |
| SYN-CTR-1 | syndicate | same/contradictory | do_not_count_as_independent + contradiction preserved | same wire id; contradictory headline on `evt_alpha` |
| SYN-CTR-2 | syndicate | same/contradictory | do_not_count_as_independent + contradiction preserved | same wire id; contradictory actor string on `evt_alpha` |
| REL-1 | shared-release | same/consistent | do_not_count_as_independent | two outlets quote one official release in full; `evt_alpha` |
| REL-2 | shared-release | same/consistent | do_not_count_as_independent | two outlets quote different excerpts of the same official release; `evt_alpha` |
| RW-1 | partial-rewrite | same/consistent | do_not_count_as_independent | same release; adjectives added only; `evt_alpha` |
| RW-2 | partial-rewrite | same/consistent | do_not_count_as_independent | same release; paragraph reorder plus adjectives; `evt_alpha` |
| IND-1 | independent | same/consistent | retain_as_independent | same `evt_alpha` / `clm_alpha`; distinct originating paths; no shared wire or release; independently developed detail; no near-copy |
| IND-2 | independent | same/consistent | retain_as_independent | same `evt_alpha`; second independent pair with different bylines and different independently developed facts |
| IND-DATE-1 | independent | same/consistent | retain_as_independent | same `evt_alpha`; both mention the same calendar date; otherwise independent |
| IND-DATE-2 | independent | same/consistent | retain_as_independent | same `evt_alpha`; shared date plus shared city name; still no shared provenance |
| IND-CTR-1 | independent | same/contradictory | retain_as_contradiction | two independents of `evt_alpha` disagree on event date |
| IND-CTR-2 | independent | same/contradictory | retain_as_contradiction | two independents of `evt_alpha` disagree on the reported actor |
| UNREL-1 | independent | unrelated | do_not_count_as_independent | distinct events `evt_alpha` vs `evt_beta`; different facts; label `unrelated` |
| UNREL-2 | independent | unrelated | do_not_count_as_independent | distinct events sharing only a calendar date; label `unrelated`, not corroboration |
| EMPTY-1 | empty-lineage | same/consistent | do_not_count_as_independent | same `evt_alpha`; no family/wire/release/derivation fields |
| EMPTY-2 | empty-lineage | unrelated | do_not_count_as_independent | empty lineage and no shared event key |
| X-1 | syndicate | same/contradictory | do_not_count_as_independent | syndicate with contradictory headline — gold remains syndicate, not independent |
| X-2 | independent | same/consistent | retain_as_independent | independents that share a date — gold remains independent |
| X-3 | copy | same/consistent | do_not_count_as_independent | near-copy versus partial-rewrite boundary; frozen gold is `copy` because the body hash still matches after header-only edits, not independent |

IND-1 and IND-2 are **same-matter** independent corroboration. They are not different-event pairs. Different-event pairs are `UNREL-*`.

### Measurements

- confusion table against evaluation-pack gold on all three axes
- reason codes present on every decision
- count of decisions that emitted only a score (must be 0)
- contradiction-preservation check, including syndicated-family contradiction
- count of unrelated pairs labeled as independent corroboration (must be 0)
- development-pack vs evaluation-pack hashes

### Thresholds

| Result | Threshold |
|---|---|
| invalid / incomplete | Missing SUT revision, pack hashes, oracle gold, required pair, command, or output; evaluation gold visible to the SUT; rules tuned on evaluation gold. Repeat. |
| `stop` | Distinction cannot be made without an opaque score or a live-corpus policy. |
| `revise architecture` | A valid misclassification that does not meet stop; or additional lineage fields needed (e.g. originating-release id); still no live corpus. |
| `proceed` | Copy/syndicate/shared-release/partial-rewrite are non-independent; every same-matter independent pair is classified independent **and** retained; unrelated pairs are not corroboration; empty lineage is not independence; contradictions preserved; reasons required; multi-example evaluation pack used. |

### Required negative and adversarial cases

Near-copy with cosmetic rewrite; shared release with contradictory headlines; independent sources that happen to share a date; empty lineage; unrelated events sharing a date; contradiction within one syndicated family; shared facts without shared provenance.

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E4-REPORT.md`: labeled fixtures (redacted to ids and reason codes), confusion table, recommendation.

### Reproducibility

Development-pack hash, evaluation-pack hash, oracle-gold hash, classifier/rules revision. No unseeded model.

### Isolation, bounds, reuse, cleanup

- Frozen files in the experiment namespace.
- Bound: one development pack and one evaluation pack.
- **Prohibited production reuse:** do not adopt the spike as a production scorer.
- Cleanup: keep the labeled pack hashes in evidence; human-approved delete of working copies.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| Which lineage fields Wave 3/4 must persist; that corroboration counts require family separation **and** same-matter claim matching | Live source policy (OD-004); a numeric quality threshold; identity merges (that is W2-E5) |

---

## W2-E5 — Reversible identity hypotheses

### Identity

- **Experiment identifier:** `W2-E5`
- **§22 family:** 5
- **Risk:** R-ID
- **Requirement:** W2-N6
- **System under test:** an experiment driver over Wave 1 `person-hypothesis-v1` / `event-hypothesis-v1` (or an experiment-local copy) that performs hypothesis **state transitions**.
- **Not the SUT:** the frozen fixtures, the expected state traces, or any canonical identity table (which must not exist).
- **Oracle:** hand-enumerated expected state traces, loaded only after SUT output is captured.

### Exact assumption

Identity hypotheses remain reversible and resist blind transitive merging. Similarity is not identity. A≈B and B≈C do not yield A=C. A mistaken hypothesis **decision** can be reopened without destroying evidence or creating a canonical identity.

This experiment does **not** claim that Wave 2 can split a materialized canonical identity. That belongs to Wave 4 and OD-006.

### Falsifiable hypothesis

On adversarial fixtures, the system can record `possibly_same` / `confirmed_same` / `confirmed_different` / `unresolved` / `reopened` without writing a canonical person. A≈B plus B≈C does not produce A=C. Negative evidence survives. A mistaken `confirmed_same` hypothesis decision can be reopened. Subject IDs remain distinct throughout. Repeating the same transition/idempotency key does not duplicate evidence or create a second hypothesis identity.

Permitted conclusion if the proceed conditions hold:

> A mistaken identity-hypothesis decision can be reopened without destroying evidence or creating a canonical identity.

### Failure condition (before execution)

**Stop** if, in a valid run:

- reversible non-transitive hypotheses are infeasible without creating a canonical identity or performing a canonical merge/split;
- OD-006 scope is treated as decided.

**Revise architecture** if the run is valid, no stop condition applies, and any mandatory proceed condition fails — including a need for additional hypothesis states or evidence slots, still without canonical merge.

Mandatory proceed conditions:

- no canonical person, merged identity row, or split operation exists;
- I-trans does not emit A=C or a single surviving id;
- I-contra retains both polarities;
- I-reopen and I-false-decision follow the frozen traces below;
- subject IDs remain distinct on every fixture;
- retry of the same transition/idempotency key does not duplicate evidence or create a second hypothesis identity;
- a caller that asks for `transitive_closure` does not obtain A=C.

### Smallest permitted experimental surface

Wave 1 `person-hypothesis-v1` / `event-hypothesis-v1` (or an experiment-local copy) plus a fixture driver that **drives state transitions**. No identity table. No extractor change. No production clustering. No “start from an illegal merged id and split it” fixture.

### Synthetic or approved fixture

Policy-safe names only. Subject ids remain `per_*` / `evt_*` and are never rewritten.

| Fixture | Intent |
|---|---|
| I-trans | A≈B and B≈C with no A–C evidence |
| I-contra | A≈B with both positive and negative evidence |
| I-reopen | accepted `confirmed_same` then new contradictory evidence → `reopened` → `confirmed_different` |
| I-false-decision | pair A/B reaches `confirmed_same` as a hypothesis decision; historical supporting evidence remains append-only; new contradictory evidence is appended; the pair transitions to `reopened`, then to `unresolved`. No canonical identity or split. |
| I-same-event | two event mentions similar but not the same event |

I-false-first (start from an illegal merged id and require reopen/split) is **removed**. It asked the Wave 1 surface to represent a canonical split.

### Expected state traces (oracle-only; complete)

Ids below are synthetic. Evidence rows are append-only.

**I-trans**

1. Create `phyp_ab` on `per_a` / `per_b`, method `reviewer_comparison`, `creates_canonical_identity=false`. State `candidate` → `needs_review` → `possibly_same`. Evidence E1 polarity `supports`.
2. Create `phyp_bc` on `per_b` / `per_c`, same method. State `candidate` → `needs_review` → `possibly_same`. Evidence E2 polarity `supports`.
3. Caller requests `transitive_closure` over A–B–C.
4. Expected: no `phyp_ac`; no A=C; no surviving merged id; `per_a`, `per_b`, `per_c` still distinct; both hypotheses remain `possibly_same`; `creates_canonical_identity` remains false.

**I-contra**

1. Create `phyp_ab` on `per_a` / `per_b`. Append E+ (`supports`) to `positive_evidence` and E− (`contradicts`) to `negative_evidence`.
2. State `candidate` → `needs_review` → `possibly_same`.
3. Expected: both polarities still present; neither list emptied; no canonical id.

**I-reopen**

1. `phyp_ab`: `candidate` → `needs_review` → `confirmed_same` with supporting evidence E1 (`supports`) retained.
2. Append new contradictory evidence E2 (`contradicts`) to `negative_evidence`. Do not overwrite E1.
3. State → `reopened` with `prior_state=confirmed_same`.
4. State → `confirmed_different`.
5. Expected: E1 and E2 both present; `per_a` ≠ `per_b`; no split operation; no canonical id.

**I-false-decision**

1. Pair `per_a` / `per_b` reaches `confirmed_same` as a hypothesis decision (`phyp_ab`, `creates_canonical_identity=false`).
2. Historical supporting evidence E1 remains append-only.
3. New contradictory evidence E2 is appended.
4. The pair transitions to `reopened` (`prior_state=confirmed_same`), then to `unresolved` according to this frozen fixture.
5. Expected: subject IDs remain distinct throughout; no canonical identity row; no split operation; E1 and E2 both present.

**I-same-event**

1. Create `ehyp_xy` on `evt_x` / `evt_y` (similar date and place; different event ids).
2. State `candidate` → `needs_review` → `possibly_same` → `confirmed_different`.
3. Expected: `evt_x` ≠ `evt_y`; no event-identity merge; similarity evidence retained.

**Retry / idempotency (all five fixtures)**

Repeating the same transition with the same idempotency key must not duplicate evidence rows or create a second `hypothesis_id`. Expected: same hypothesis identity; evidence counts unchanged.

### Measurements

- state traces for each fixture versus the oracle traces
- presence of a forbidden canonical-id table (must be absent)
- whether I-trans emits A=C (must not)
- whether I-reopen and I-false-decision match the traces above
- whether I-contra retains both polarities
- whether retry duplicates evidence or hypothesis ids (must not)
- whether any fixture rewrote subject ids (must not)

### Thresholds

| Result | Threshold |
|---|---|
| invalid / incomplete | Missing SUT revision, fixture hash, oracle-trace hash, required fixture, command, or output. Repeat. |
| `stop` | Reversible non-transitive hypotheses are infeasible without canonical merging or splitting; or OD-006 is treated as decided. |
| `revise architecture` | Additional hypothesis states or evidence slots required; still no canonical merge; or a valid trace mismatch that does not meet stop. |
| `proceed` | No canonical id; no automatic A=C; I-false-decision and I-reopen match the frozen traces; negative evidence retained; retries are idempotent; subject ids remain distinct. |

### Required negative and adversarial cases

| Case | Expected outcome |
|---|---|
| I-trans | No A=C; three distinct subject ids |
| I-false-decision | Reopen to `unresolved`; evidence preserved; no split |
| I-contra | Both polarities retained |
| Retry of an already-confirmed pair | Same `hypothesis_id`; no duplicate evidence |
| Caller asks for `transitive_closure` | Denied as proof; no new confirmed pair |

### Evidence artifacts

`docs/v4/evidence/experiments/W2-E5-REPORT.md`: state traces, fixture hashes, oracle-trace hashes, recommendation.

### Reproducibility

Fixture hashes, oracle-trace hashes, and hypothesis-engine revision.

### Isolation, bounds, reuse, cleanup

- In-process fixture driver.
- Bound: the five fixtures above plus documented extras if needed.
- **Prohibited production reuse:** do not create `persons` / merge tables; do not wire legacy clustering; do not implement a canonical split.
- Cleanup: keep traces; human-approved namespace delete.

### Architecture this result may / may not decide

| May inform | May not decide |
|---|---|
| That Wave 4 must keep hypotheses reversible and non-transitive; that false **decision** recovery is a first-class path that does not require a canonical identity | OD-006 identity-resolution scope; a canonical person model; a canonical split; reviewer qualifications (OD-005) |

---

## Execution is not authorized

This plan is a proposal. Wave 2 remains `unstarted`.

Do not create worktrees, namespaces, disposable databases, experiment modules, or `WAVE-02-EVIDENCE.md` until the human gate owner explicitly approves this boundary.
