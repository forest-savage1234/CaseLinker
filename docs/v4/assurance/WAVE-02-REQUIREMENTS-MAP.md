# Wave 2 requirements-to-plan map

**Status:** `proposed`. Not frozen. Not approved.  
**Mapped against:** `WAVE-02-ASSURANCE.md` (proposed)  
**Wave 2 legal state:** `unstarted`  
**No requirement is implemented or §18.4 `closed`.**

Disposition vocabulary for this planning packet:

| Disposition | Meaning |
|---|---|
| `planned` | In-scope experiment or process obligation if the plan is approved |
| `deferred` | Named in §22’s neighborhood but deeper behavior belongs to a later wave |
| `blocked` | Cannot be completed as a production or policy claim without a named OD-* |
| `out_of_scope` | Not a Wave 2 exit requirement |

Do not mark anything `implemented` or `closed`.

## Exit requirements

| ID | Requirement | Disposition | Proposed experiment | Falsification criterion | Intended evidence | Dependency | Owner | Blocking OD-* |
|---|---|---|---|---|---|---|---|---|
| W2-N1 | Isolated disposable namespaces | planned | all | Any experiment writes into production modules, `main`, or `proposal/v3-foundation` | Isolation record; worktree/namespace id; diff scope | plan approval | program operator (tracking) | none for isolation; OD-008 for any hosted claim |
| W2-N2 | Postgres append-only, independent-dimension bitemporal, conflicting-review invariants | planned (instrument only) | W2-E1 | Silent lost update; illegal overwrite; dimensions aliased/omitted/queried as one; future-effective or coincident pair rejected as intrinsically invalid; inverted event interval, invented precision, non-UTC knowledge time, or in-place knowledge mutation stored as valid; two conflicting reviews both committing as legal | Conflict matrix including C4a–C4g; isolation-level measurements; independent-query checks | none | program operator (tracking) | OD-008 **blocks production selection**, not the disposable instrument |
| W2-N3 | Fixture-relative invalidation without graph authority | planned | W2-E2 | See W2-N3a–c | Manifest, registry closure, coverage status, fail-closed traces | none | program operator (tracking) | none for fixtures; OD-003 blocks production notices |
| W2-N3a | Closure correctness over the registered set | planned | W2-E2 | Registered transitive omitted; cycle drops nodes or fails to terminate | Impact-set vs registry closure | W2-N3 | program operator (tracking) | none for fixtures |
| W2-N3b | Registration coverage vs declared fixture universe | planned | W2-E2 | Manifest-declared edge or input created without registration and without detection | Registry-vs-manifest coverage | W2-N3 | program operator (tracking) | none for fixtures |
| W2-N3c | Incomplete-state fail-closed | planned | W2-E2 | Coverage not established but result claims complete impact | Explicit `incomplete` on F-incomplete / F-missing-reg / F-silent-create | W2-N3 | program operator (tracking) | none for fixtures |
| W2-N4 | Default-deny disclosure; distinct views; no alternate-path leak | planned (synthetic decisions) | W2-E3 | Missing policy authorizes; views collapse; internal field appears on any probed path | Leakage probe table; three-view field matrices | none | program operator (tracking) | OD-003 **blocks policy content**; synthetic fixtures allowed |
| W2-N5 | Independent corroboration ≠ syndication/duplication | planned | W2-E4 | Copy or syndicate counted as independent; genuine independent pair classified as the same family **or** improperly suppressed as non-independent evidence; single opaque score is the decision; one-example-per-label pack | Multi-example confusion table; structured reasons | none | program operator (tracking) | OD-004 blocks live corpus |
| W2-N6 | Reversible identity; no blind A≈B≈C | planned | W2-E5 | Automatic A=C; irreversible merge; negative evidence dropped; false-merge cannot reopen | Adversarial fixture outcomes; state traces | none | program operator (tracking) | OD-006 **blocks operational identity**; no canonical person |
| W2-N7 | Pre-declared falsification and thresholds | planned | plan artifact | Execution begins without recorded failure conditions | this map; `WAVE-02-PLAN.md` | plan approval | program operator (tracking) | none |
| W2-N8 | Policy-safe synthetic fixtures only | planned | all | Live corpus, real PII, or invented lawful basis used | Fixture inventory and provenance | D-007 | program operator (tracking) | OD-003/004 |
| W2-N9 | Measure; do not promote spikes | planned | all | Spike imported into `src/caselinker` production path | Module path audit; evidence “not promoted” statement | W2-N1 | program operator (tracking) | none |
| W2-N10 | Record architecture implications | planned | all | Proceed/revise/stop lacks a target-architecture note | per-experiment implication section | W2-N12 | program operator (tracking) | none |
| W2-N11 | Evidence packet + five reports | planned | all | Wave marked verified without reports | `WAVE-02-EVIDENCE.md` (execution only) | execution approval | program operator (tracking) | none |
| W2-N12 | Proceed / revise / stop per experiment | planned | all | Ambiguous “looks good” without a threshold | recommendation field on each report | W2-N7 | program operator (tracking) | none |
| W2-N13 | No Wave 3 temporal kernel | planned (prohibition) | — | Kernel, live rebuild queue, or production SoR appears | diff scope vs `src/caselinker` kernel paths | — | program operator (tracking) | none |
| W2-N14 | Human-approved cleanup after evidence preserved | planned | all | Destructive delete before evidence or without approval | cleanup decision id | W2-N11 | program operator (tracking) | human cleanup approval |
| W2-N15 | Success ≠ production architecture | planned (prohibition) | all | Vendor, schema, or policy selected because an experiment passed | decision log remains silent on those selections | OD-003/006/008 | program operator (tracking) | OD-003, OD-006, OD-008 |

## Related program IDs (partial only)

These IDs may gain **experimental evidence**. None are `closed`.

| ID | Wave 2 effect | Still open |
|---|---|---|
| CONST-004 / TEMP-* | W2-E1 may show whether Postgres can hold two times under conflict | Wave 3 kernel |
| CONST-012 / CORRECT-001…003 | W2-E2 tests fixture-relative closure, coverage, and fail-closed incomplete state | Wave 3 engine; production notices; unknowable externals |
| CONST-009 / DISCLOSE-001…004 | W2-E3 tests enforcement of **supplied** decisions and leakage | OD-003; Wave 5 PDP |
| CONST-006 / 007 / RESOLVE-003…005 | W2-E5 tests reversibility and non-transitivity | OD-006; Wave 4 |
| CONST-010 / 011 / RESOLVE-001…002 | W2-E4 tests family vs independent on frozen examples | OD-004 live corpus |
| CONST-016 | W2-E2/E3 treat projections as non-authoritative | standing |
| OPS-001 / R-CON | W2-E1 disposable instrument | OD-008 production |
| REVIEW-001 / R-AUTH | not exercised as authentication | OD-005 |

## Explicitly not Wave 2 blockers

| Item | Why not Wave 2 | Belongs |
|---|---|---|
| Field-for-field external PDP object from Wave 1 r4 | Historical over-specification; §22 asks whether supplied decisions can be enforced safely | Wave 5 or `program_clarification_required` |
| SoD governance-decision ids on every transition | OD-005; Wave 1 residual M1 | Wave 5 |
| Wiring `reported-claim-v1` into extractors | Wave 1 residual; not a §22 assumption | later implementation wave |
| Canonical person store | Forbidden by §22 item 5 | never a Wave 2 success condition |
| Production Postgres vendor / schema / hosting | OD-008 | Wave 8 |
| Real audience / lawful-basis / minimization policy | OD-003 | Wave 5 |
| Fixture correction-impact **kernel** | Wave 3 primary proof | Wave 3 |

## Sequence (summary)

Full analysis: `docs/v4/experiments/WAVE-02-PLAN.md` §0.

**Default order is sequential:** **W2-E5 → W2-E2 → W2-E3 → W2-E4 → W2-E1**.

The five experiments remain logically independent. Simultaneous execution is **not** authorized by default. Parallel execution requires an explicit human amendment naming builders/namespaces, capacity, evidence isolation, reviewer availability, and contamination controls.

No experiment depends on resolving OD-003, OD-005, OD-006, or OD-008. Each may use synthetic fixtures. Production or policy claims remain blocked. Wave 2 completeness on W2-E2 is relative to a declared fixture universe.
