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

## Shared valid-run and result algorithm

Every planned experiment uses this algorithm. It is the W2-N7 / W2-N12 requirement.

1. **Evidence validity.** If the SUT revision, fixture hash, oracle artifact, required case, command, declared schedule, or required output is missing, the run is incomplete and must be repeated. It is not eligible for an architecture recommendation.
2. **Stop precedence.** If any predeclared fatal condition occurs in a valid run, recommend `stop`.
3. **Revise precedence.** Otherwise, if any mandatory proceed condition fails, recommend `revise architecture` and name the required change.
4. **Proceed.** Recommend `proceed` only if every mandatory proceed condition passes and no revise/stop condition applies.

An invalid run does not create a fourth architecture recommendation.

For W2-E3, this algorithm governs the mandatory P1–P8 mechanism result. P9 is a separately reported observational probe: it cannot improve or invalidate the P1–P8 mechanism result, but a confirmed leak still requires a predeclared `revise architecture` or `stop` disposition. `Not evaluable` is an incomplete observational result with a named carry-forward, not a mechanism pass or failure. No P9 outcome authorizes unplanned product repair.

## Exit requirements

| ID | Requirement | Disposition | Proposed experiment | Falsification criterion | Oracle | Intended evidence | Dependency | Owner | Blocking OD-* |
|---|---|---|---|---|---|---|---|---|---|
| W2-N1 | Isolated disposable namespaces | planned | all | Any experiment writes into production modules, `main`, or `proposal/v3-foundation` | Isolation record vs declared namespace id and diff-scope allowlist | Isolation record; worktree/namespace id; diff scope | plan approval | program operator (tracking) | none for isolation; OD-008 for any hosted claim |
| W2-N2 | Postgres storage enforcement of append-only / independent-dimension bitemporal / conflicting-review invariants, plus correctness of the declared two-dimensional query interfaces | planned (instrument only) | W2-E1 | Silent lost update; illegal overwrite; structurally collapsed representation stored as valid; future-effective or coincident pair rejected as intrinsically invalid; inverted event interval, explicitly declared invented precision, non-UTC knowledge time, or in-place knowledge mutation stored as valid; two conflicting reviews both committing as legal; declared `as_known` / `valid_during` interface returning a result that differs from the independently enumerated two-dimensional expected set | Independent final-state SQL or hand-enumerated expected row set; hand-enumerated query expected sets. The transaction driver is not the oracle. Do not treat arbitrary SQL rejection as a storage-oracle pass. | Conflict matrix including C4a, C4b, C4c-storage, C4c-query-control, C4d–C4g; named barrier schedules for C1, C2, C5, C6, C7, C8; isolation-level measurements; independent-query checks | none | program operator (tracking) | OD-008 **blocks production selection**, not the disposable instrument. Missing disposable Postgres runtime → blocked/incomplete, not a vendor selection. |
| W2-N3 | Fixture-relative invalidation without graph authority | planned | W2-E2 | See W2-N3a–c | Separately hashed oracle artifact loaded only after SUT output is captured | Manifest, registry closure, coverage status, fail-closed traces, both fixture hashes | none | program operator (tracking) | none for fixtures; OD-003 blocks production notices |
| W2-N3a | Closure correctness over the registered set | planned | W2-E2 | Registered transitive omitted; cycle drops nodes or fails to terminate; SUT closure used as its own gold | Hand-enumerated `expected_impact_by_corrected_node` in the oracle artifact. Convention: `A → B` means B depends on A. | Impact-set vs hand-enumerated registry closure | W2-N3 | program operator (tracking) | none for fixtures |
| W2-N3b | Registration coverage vs declared fixture universe | planned | W2-E2 | Manifest-declared edge or input created without registration and without detection | Frozen `manifest_edges` vs `registered_edges` in the oracle artifact, compared by the harness after SUT capture | Registry-vs-manifest coverage; expected missing `A → D` on F-incomplete | W2-N3 | program operator (tracking) | none for fixtures |
| W2-N3c | Incomplete-state fail-closed | planned | W2-E2 | Coverage not established but result claims complete impact | Oracle `expected_coverage_status` and `expected_missing_edges`; never generated by the SUT closure function | Explicit `incomplete` on F-incomplete / F-missing-reg / F-silent-create | W2-N3 | program operator (tracking) | none for fixtures |
| W2-N4 | Default-deny disclosure; distinct views; no alternate-path leak on P1–P8 | planned (synthetic decisions) | W2-E3 | Missing policy authorizes; views collapse; an internal field appears on any of P1–P8 contrary to the supplied decision; any P1–P8 adapter maintains its own allowlist or hard-coded expected matrix | One experiment-level evaluator of the frozen supplied decision plus independently enumerated expected field sets. Labels and expected outputs are oracle-only. | Leakage probe table for P1–P8; three-view field matrices; metamorphic field/audience cases | none | program operator (tracking) | OD-003 **blocks policy content**; synthetic fixtures allowed |
| W2-N4-P9 | Observational probe of existing Evidence Pack / Claim Card entry points | planned (observational; outside P1–P8 bar) | W2-E3 P9 | Confirmed leak ignored; P9 treated as a P1–P8 pass/fail substitute; unplanned product repair begun | Supplied synthetic decision plus the declared synthetic mapping to `ClaimCard.to_dict` / `EvidencePackAssembler.assemble`. Classifications: confirmed leak, path lacks enforcement, not evaluable. | Separate P9 observation record and disposition; named carry-forward if leak or not evaluable | W2-N4 | program operator (tracking) | OD-003 blocks real policy; product repair out of scope |
| W2-N5 | Independent corroboration ≠ syndication/duplication and ≠ unrelated events | planned | W2-E4 | Copy, syndicate, shared-release, or partial-rewrite counted as independent; genuine same-matter independent pair classified as the same family **or** improperly suppressed; unrelated-event pair labeled independent corroboration; single opaque score is the decision; one-example-per-label pack; evaluation gold visible to the SUT | Frozen evaluation-pack gold matrix on orthogonal axes (source-family relationship, claim relationship, evidence treatment). Gold labels and expected reason codes are oracle-only. | Multi-example confusion table; structured reasons; development-pack vs evaluation-pack hashes | none | program operator (tracking) | OD-004 blocks live corpus |
| W2-N6 | Reversible identity-hypothesis decision; no blind A≈B≈C; no canonical identity or split | planned | W2-E5 | Automatic A=C; canonical person or merged identity row created; negative evidence dropped; mistaken `confirmed_same` cannot reopen; subject IDs collapsed or a split operation invented | Hand-enumerated expected state traces for I-trans, I-contra, I-reopen, I-false-decision, I-same-event. The hypothesis engine is not its own oracle. | Adversarial fixture outcomes; complete state traces; distinct subject ids throughout | none | program operator (tracking) | OD-006 **blocks operational identity**; no canonical person |
| W2-N7 | Pre-declared falsification, valid-run gates, and exhaustive result mapping | planned | plan artifact | Execution begins without recorded failure conditions, valid-run gates, or exclusive stop/revise/proceed mappings | This map plus `WAVE-02-PLAN.md` shared result algorithm | this map; `WAVE-02-PLAN.md` | plan approval | program operator (tracking) | none |
| W2-N8 | Policy-safe synthetic fixtures only | planned | all | Live corpus, real PII, or invented lawful basis used | Fixture inventory and provenance statements | Fixture inventory and provenance | D-007 | program operator (tracking) | OD-003/004 |
| W2-N9 | Measure; do not promote spikes | planned | all | Spike imported into `src/caselinker` production path | Module path audit vs production allowlist | Module path audit; evidence “not promoted” statement | W2-N1 | program operator (tracking) | none |
| W2-N10 | Record architecture implications no broader than the evidence | planned | all | Proceed/revise/stop lacks a target-architecture note, or the note selects a vendor, schema, policy, or official version | per-experiment implication section vs the measured cases | per-experiment implication section | W2-N12 | program operator (tracking) | none |
| W2-N11 | Evidence packet + five reports | planned | all | Wave marked verified without reports | Presence of execution-only artifacts | `WAVE-02-EVIDENCE.md` (execution only) | execution approval | program operator (tracking) | none |
| W2-N12 | Proceed / revise / stop per experiment with stop > revise > proceed | planned | all | Ambiguous “looks good”; a valid outcome maps to both revise and stop, or to neither; an invalid run is treated as an architecture result | Shared result algorithm in this map and `WAVE-02-PLAN.md` | recommendation field on each report plus valid-run determination | W2-N7 | program operator (tracking) | none |
| W2-N13 | No Wave 3 temporal kernel | planned (prohibition) | — | Kernel, live rebuild queue, or production SoR appears | diff scope vs `src/caselinker` kernel paths | diff scope vs `src/caselinker` kernel paths | — | program operator (tracking) | none |
| W2-N14 | Human-approved cleanup after evidence preserved | planned | all | Destructive delete before evidence or without approval | cleanup decision id | cleanup decision id | W2-N11 | program operator (tracking) | human cleanup approval |
| W2-N15 | Success ≠ production architecture | planned (prohibition) | all | Vendor, schema, or policy selected because an experiment passed | decision log remains silent on those selections | decision log remains silent on those selections | OD-003/006/008 | program operator (tracking) | OD-003, OD-006, OD-008 |

## Related program IDs (partial only)

These IDs may gain **experimental evidence**. None are `closed`.

| ID | Wave 2 effect | Still open |
|---|---|---|
| CONST-004 / TEMP-* | W2-E1 may show whether Postgres can hold two times under conflict and whether the declared query interfaces address those times independently | Wave 3 kernel |
| CONST-012 / CORRECT-001…003 | W2-E2 tests fixture-relative closure, coverage, and fail-closed incomplete state | Wave 3 engine; production notices; unknowable externals |
| CONST-009 / DISCLOSE-001…004 | W2-E3 tests enforcement of **supplied** decisions and leakage on P1–P8; P9 observes existing product paths | OD-003; Wave 5 PDP |
| CONST-006 / 007 / RESOLVE-003…005 | W2-E5 tests reversibility of hypothesis decisions and non-transitivity | OD-006; Wave 4; canonical split |
| CONST-010 / 011 / RESOLVE-001…002 | W2-E4 tests family vs independent vs unrelated on frozen same-matter examples | OD-004 live corpus |
| CONST-016 | W2-E2/E3 treat projections as non-authoritative | standing |
| OPS-001 / R-CON | W2-E1 disposable instrument | OD-008 production |
| REVIEW-001 / R-AUTH | not exercised as authentication | OD-005 |

## Explicitly not Wave 2 blockers

| Item | Why not Wave 2 | Belongs |
|---|---|---|
| Field-for-field external PDP object from Wave 1 r4 | Historical over-specification; §22 asks whether supplied decisions can be enforced safely | Wave 5 or `program_clarification_required` |
| SoD governance-decision ids on every transition | OD-005; Wave 1 residual M1 | Wave 5 |
| Wiring `reported-claim-v1` into extractors | Wave 1 residual; not a §22 assumption | later implementation wave |
| Canonical person store or canonical split | Forbidden by §22 item 5 | never a Wave 2 success condition; Wave 4 / OD-006 |
| Production Postgres vendor / schema / hosting | OD-008 | Wave 8 |
| Real audience / lawful-basis / minimization policy | OD-003 | Wave 5 |
| Fixture correction-impact **kernel** | Wave 3 primary proof | Wave 3 |
| Arbitrary-SQL access-control / role-or-view privilege surface | Not a row constraint; not silently added to W2-E1 | later explicitly scoped experiment, if approved |

## Sequence (summary)

Full analysis: `docs/v4/experiments/WAVE-02-PLAN.md` §0.

**Default order is sequential:** **W2-E5 → W2-E2 → W2-E3 → W2-E4 → W2-E1**.

The five experiments remain logically independent. Simultaneous execution is **not** authorized by default. Parallel execution requires an explicit human amendment naming builders/namespaces, capacity, evidence isolation, reviewer availability, and contamination controls.

No experiment depends on resolving OD-003, OD-004, OD-005, OD-006, or OD-008. Each may use synthetic fixtures. Production or policy claims remain blocked. Wave 2 completeness on W2-E2 is relative to a declared fixture universe.
