# Wave 2 planning review of `ed7597a4`

**Reviewed commit:** `ed7597a4efbf5ad0a60318cb59193093a178c451`  
**Parent planning commit:** `1cb519fad7632a9fad39131fea35b9eff196876c`  
**Boundary reviewed:** proposed `WAVE-02-ASSURANCE.md`, `WAVE-02-REQUIREMENTS-MAP.md`, `WAVE-02-PLAN.md`  
**Governing source:** `GROK_BUILD_PROGRAM.md` §22; `STRATEGY.md`  
**Reviewer:** same-model Grok general-purpose agent.  
**Independence limitation:** this conversation lineage previously authored the proposed packet and the W2-P1–P5 revision. That is not organizational independence and is not a separate-conversation clean room. The limitation is material and must remain visible. Gates required for a documentation-only planning review were rerun. Experiment procedures were **not** run because no experiment is authorized.  
**Wave 2 legal state:** remains `unstarted`  
**Packet status:** remains `proposed`. Not frozen. Not human-approved.  
**Disposition:** `planning_review_pass`  
**human_approved:** false  
**Experiments executed:** false

This review recommends that the human gate owner may approve the proposed packet. It does not itself approve or start Wave 2.

## Stage 1 verdict (before D-027, D-028, or the revision diff)

The proposed packet is a coherent, falsifiable plan for the five §22 experiment families. It stays inside Wave 2: disposable surfaces, synthetic fixtures, no temporal kernel, no production selection, no official version.

No Stage 1 finding is classified critical/high. Residual items are recorded below as medium/low or later work.

### Per-experiment Stage 1 notes

| ID | §22 trace | Could fail? | Oracle independent? | Smallest surface disposable? | Becomes later wave? |
|---|---|---|---|---|---|
| W2-E1 | item 1 | yes | conflict matrix + SQL-direct client | yes — local instance | no; production reuse forbidden |
| W2-E2 | item 2 | yes, if gold impact sets are hand-enumerated | manifest independent for coverage; closure gold must not be SUT-computed | yes — file-backed | no; kernel forbidden |
| W2-E3 | item 3 | yes | supplied decisions vs field-presence matrix | yes — in-process harness | no; P9 forbids product repair |
| W2-E4 | item 4 | yes | frozen gold labels vs reason-emitting output | yes — frozen files | no |
| W2-E5 | item 5 | yes | behavioral fixtures (no A=C, reopen) | yes — fixture driver | no; no person table |

Sequential default E5→E2→E3→E4→E1 is feasible for one operator and matches D-006 risk rank. Sequence is not a result dependency. Synthetic fixtures do not resolve OD-003/005/006/008.

Event/valid time and knowledge/transaction time are treated as independent dimensions. Closure is separated from registration coverage. Projections are non-authoritative. Alternate-path leakage is in the probe list. Independent-pair false-negative and false-positive both fail W2-E4. Identity remains reversible without canonical merge or blind transitivity.

## Stage 2 reconciliation

D-027 records the original proposal. D-028 records the W2-P1–P5 revision. D-027 was not rewritten. Diff `1cb519fa..ed7597a4` is documentation-only.

| ID | Stage 2 result |
|---|---|
| W2-P1 | **Confirmed.** C4 no longer treats future-effective or coincident values as intrinsically invalid. Collapse is aliasing/omitting/querying as one clock. Aligned with Wave 1 `reject_collapsed_clock` and inverted-interval / invented-precision / UTC checks. Did not weaken §22. |
| W2-P2 | **Confirmed.** W2-N3 is three obligations: registered-set closure, manifest-relative coverage, incomplete-state fail-closed. Completeness is fixture-universe-relative. Projection is not the oracle. Did not start Wave 3. Residual: operations text still says “compare registry closure to itself” (M1). |
| W2-P3 | **Confirmed.** Independent-pair failure is classification **or** suppression. Multi-example matrix frozen in the plan. Residual: partial-rewrite gold is not named in the failure/proceed sentences (M3). |
| W2-P4 | **Confirmed.** P9 is observational, cannot be ignored, yields `revise architecture` or `stop` with a named carry-forward, and must not trigger unapproved product repair. Residual: map W2-N4 still says “any probed path” (M4). |
| W2-P5 | **Confirmed.** Sequential default. Parallel only after an explicit human amendment. No result dependency introduced. |

The revision corrected the five reported defects coherently. It did not introduce a new critical/high defect, weaken a §22 obligation, or expand Wave 2 into Wave 3/4/5 implementation. Remaining cross-document slop is medium/low.

## Validation (reviewer-executed)

| Command | Result |
|---|---|
| `uv run --locked --no-extra ml python scripts/quality/check_repository.py` | passed (8602 tracked files) |
| `uv run --locked --no-extra ml python scripts/quality/check_traceability.py` | passed (7 milestones) |

Planning commits `1cb519fa` and `ed7597a4` touch only `docs/v4/`. No product module, schema, test, migration, service, database, experiment namespace, or additional worktree was created. Existing worktrees remain the v3-foundation tree and this v4 tree. `WAVE-02-EVIDENCE.md` does not exist. Wave 2 `legal_state` is `unstarted`. `gate_0` is `not_complete`. `official_version_claim` is false.

The full product suite was **not** rerun. A product-suite rerun is not required to review a documentation-only experiment plan.

## Critical / high findings

None inside the proposed Wave 2 planning boundary.

## Medium / low residuals

| ID | Severity | Item | Owner |
|---|---|---|---|
| M1 | Medium | W2-E2 operations still say “compare registry closure to itself.” Closure gold must be hand-enumerated in the fixture (e.g. F-chain → {B,C,D}), not computed by the SUT. | tracking operator; fix at execution freeze or a later plan amendment |
| M2 | Medium | W2-E3 can be gamed with per-probe allowlists. P1–P8 should share one decision-consultation function. | tracking operator; execution constraint |
| M3 | Low | W2-E4 failure/proceed sentences name copy/syndicate/shared-release but not partial-rewrite, which is in the frozen matrix. | tracking operator |
| M4 | Low | Map W2-N4 “any probed path” does not distinguish observational P9 from mechanism P1–P8. Plan text does. | tracking operator |
| M5 | Low | W2-E4 must treat gold labels as oracle-only. Fixtures should expose raw features (hashes, wire ids, bylines), not a pre-filled `same_source_family` that the SUT merely echoes. Reason-code requirement already mitigates this. | tracking operator |
| M6 | Low | W2-E5 must drive hypothesis state transitions, not only re-validate Wave 1 schemas. | tracking operator |
| M7 | Low | F-silent-create needs a defined creation surface to be falsifiable. | tracking operator |
| M8 | Process | Same-conversation authorship of the packet. Not organizational independence. | human gate owner |
| M9 | Standing | OD-003/005/006/008 remain blocked. Windows baseline exceptions unchanged. | named authorities / R-WIN |

M1–M7 are execution-time constraints or later plan tightenings. They are not converted into approval conditions by this review.

## Over-specification / scope-creep

- W2-E3 adds caches, search, errors, and admin to §22’s “serializers, logs or exports.” That matches assigned risk R-DIS. It is not Wave 5 policy content if the harness stays disposable.
- W2-E1 C4d–C4f re-check Wave 1 interval rules inside Postgres. That tests database enforcement, not a silent contract expansion.
- Historical Wave 1 r3/r4 disclosure and SoD extras remain non-goals. Not pulled into the exit bar.

## Final disposition

`planning_review_pass`

No traceable critical/high planning defect remains inside the proposed §22 boundary. The human gate owner may accept, reject, or require clarification. This review does **not** mark Wave 2 `human_approved`, freeze the contract, authorize worktrees or PostgreSQL startup, or execute any experiment.
