# Wave 2 planning review 03 — independent re-verification

**Reviewed planning commit:** `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`

**Original packet:** `ed7597a4efbf5ad0a60318cb59193093a178c451`

**Administrative state reconciled during review:** `232c8703f4c79c47fffa3aca70861e6c2905c3bf`

**Remote HEAD verified during review:** `232c8703f4c79c47fffa3aca70861e6c2905c3bf`

**Boundary reviewed:** proposed `WAVE-02-ASSURANCE.md`, `WAVE-02-REQUIREMENTS-MAP.md`, `WAVE-02-PLAN.md` at `5fb8913e`; administrative `EXECUTION_STATE.md` at `232c8703`

**Governing source:** `GROK_BUILD_PROGRAM.md` §22; `STRATEGY.md`

**Disposition:** `planning_review_pass`

**human_approved:** false

**Wave 2 legal state:** `unstarted`

**Packet status:** remains `proposed`

**Experiments executed:** false

This review recommends that the human gate owner may approve the proposed packet. It does not itself approve, freeze, or start Wave 2.

## Independence declaration

The reviewer identified H1–H6 against planning packet `ed7597a4efbf5ad0a60318cb59193093a178c451` and specified the remediation criteria later recorded in the Wave 2 remediation playbook.

The reviewer did **not** author or edit repository repair `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`. The reviewer did **not** author administrative commit `232c8703f4c79c47fffa3aca70861e6c2905c3bf`.

Prior participation as the independent reviewer that produced H1–H6 is permitted. Authorship of the repair is not. This record is a re-verification of that repair, not a builder self-review.

Same-model limitation: a separate conversation using the same model is not organizational independence. That limitation remains visible. It does not convert this record into builder authorship.

## Commits verified

| Role | SHA |
|---|---|
| Original packet | `ed7597a4efbf5ad0a60318cb59193093a178c451` |
| Planning repair under review | `5fb8913e78d0e54ed25021bb34fcade43d2aff3c` |
| Parent of planning repair | `31d3c85d92aac4f49448a2e8f123b2dc37359664` |
| Administrative state | `232c8703f4c79c47fffa3aca70861e6c2905c3bf` |
| Remote `origin/proposal/v4-research-network` during review | `232c8703f4c79c47fffa3aca70861e6c2905c3bf` |

The three packet files are unchanged between `5fb8913e` and `232c8703`. The only file in that range is `docs/v4/EXECUTION_STATE.md`.

## Stage 1 — repair verification

H1–H6 are closed. No new critical or high finding was introduced by the repair.

| ID | Finding | Verdict | Precise evidence |
|---|---|---|---|
| H1 | Impossible/undefined arbitrary-query rejection | **Closed** | Assurance W2-N2 (`WAVE-02-ASSURANCE.md` L30) splits storage enforcement from declared `as_known` / `valid_during` correctness and states PostgreSQL is not claimed to reject every arbitrary `SELECT`. Plan W2-E1 (`WAVE-02-PLAN.md` L147, L187, L206–L207) replaces C4c with C4c-storage and C4c-query-control; the direct SQL adversary is storage-mutation only. Map W2-N2 (`WAVE-02-REQUIREMENTS-MAP.md` L37) forbids treating arbitrary SQL rejection as a storage-oracle pass. Equal timestamps in distinct clock fields remain valid (assurance L30; plan C4b). Invented precision is tested only as an explicitly declared / schema-represented condition (plan C4e). |
| H2 | Under-specified concurrency evidence | **Closed** | Plan `WAVE-02-PLAN.md` L218–L227 declares deterministic barrier schedules for C1, C2, C5, C6, C7, and C8, with isolation, both winner permutations, expected commit/abort, 5s barrier timeout, deadlock retry, seed `w2e1-sched-v1`, and an independent final-state SQL oracle. The driver is not the oracle (L227). Seeded stress cannot replace declared interleavings (L219). |
| H3 | Self-referential and directionally inconsistent closure oracle | **Closed** | Plan L409 freezes `A → B` as “B depends on A.” L419 forbids comparing registry closure to itself. L468–L472 require a separately hashed oracle artifact loaded only after SUT capture. Expected closures are hand-enumerated (F-chain / F-diamond / F-cycle / F-incomplete, L478–L488). F-incomplete missing edge is `A → D`, not `D → A`. `create_artifact(id, input_ids)` and adversarial silent creation are defined (L452, L488). Map W2-N3a–c (L39–L41) name the same oracle fields. |
| H4 | Different-matter fixtures mislabeled as independent corroboration | **Closed** | Assurance W2-N5 (L34) and plan L763 require same-matter independent provenance. IND-1 / IND-2 (`WAVE-02-PLAN.md` L833–L834, L847) share `evt_alpha` / `clm_alpha` with distinct originating paths. UNREL-1 / UNREL-2 (L839–L840) are labeled `unrelated`, not corroboration. Orthogonal axes are family × claim × evidence treatment (L790–L798). Partial-rewrite and empty-lineage outcomes are frozen (L804–L805). |
| H5 | Recovery asks the Wave 1 surface to represent a canonical split | **Closed** | Assurance W2-N6 (L35) tests reopening a mistaken hypothesis decision without creating or splitting a canonical identity. Plan L952–L955 removes I-false-first. I-false-decision (L982–L986) is `confirmed_same` → `reopened` → `unresolved` with append-only evidence and distinct subject ids. Stop is reserved for infeasibility without canonical merge/split (plan L1015). OD-006 remains blocked. |
| H6 | Incomplete or overlapping result classification | **Closed** | Shared algorithm in `WAVE-02-REQUIREMENTS-MAP.md` L19–L30 and `WAVE-02-PLAN.md` L96–L107: invalid evidence → repeat; otherwise stop > revise architecture > proceed. Assurance W2-N7 / W2-N12 (L36, L40) require exhaustive exclusive mapping. Each experiment has an `invalid / incomplete` row that is not an architecture recommendation (plan L357, L505, L713, L862, L1014). E3 keeps P9 observational and outside the P1–P8 mechanism bar while a confirmed leak still forces revise or stop (map L30; plan L107, L715–L716). |

### New-finding assessment

No new critical or high planning defect was found in the revised packet.

Checked and not converted into blocking findings:

- claim/surface alignment for all five §22 families;
- independent oracles (SUT does not generate gold);
- deterministic barrier interleavings rather than favorable timing;
- same-matter vs unrelated corroboration;
- absence of hidden canonical merge or split;
- OD-003 / OD-004 / OD-005 / OD-006 / OD-008 remain blocked;
- Wave 3 / 4 / 5 / 8 work is not pulled into the experimental surface;
- one-operator sequential default E5 → E2 → E3 → E4 → E1 is unchanged;
- architecture implications remain no broader than the measured evidence.

## Stage 2 — state and history reconciliation

D-027 through D-031 are preserved. D-027 and D-028 remain the proposal and first revision. D-029 (`WAVE-02-PLAN-REVIEW.md`) remains invalid history (admitted author lineage). D-030 (`WAVE-02-PLAN-REVIEW-02.md`) remains `review_invalid`. D-029 is not independent acceptance.

Administrative commit `232c8703` records D-031 as `planning_revision`, names planning commit `5fb8913e`, keeps `legal_state: unstarted`, `planning_status: proposed`, `human_approved: false`, and `experiments_executed: false`. It does not approve, freeze, or start Wave 2.

The packet remains `proposed`. Wave 2 remains `unstarted`. No experiment evidence is claimed.

## Material residuals

These are not converted into approval conditions. They are execution controls or later administrative tightenings.

| ID | Severity | Item | Evidence | Owner |
|---|---|---|---|---|
| M1 | Medium | Historical `planning_review_status: planning_review_pass` in `EXECUTION_STATE.md` can still be read as if D-029 were currently valid, even though `valid_independent_planning_review` is `false` and the prose says D-029 is invalid history. | `EXECUTION_STATE.md` L41–L47 vs L47 and L73 | administrative recorder at Stage 2 of the review-to-execution playbook |
| M2 | Medium | A PostgreSQL writer may block on a unique or exclusion constraint before the next named barrier. A harness timeout or lock wait must not be scored as scheduler success. If the schedule cannot reach a valid observation, the run is incomplete. | Plan L224–L227 states timeout/deadlock → incomplete, not silent pass. Execution must still distinguish lock wait from barrier success. | W2-E1 builder / harness |
| M3 | Low | E4 evaluation-pack seal should record timestamp and hash evidence at freeze time, not only the later report hashes. | Plan L811–L817 freezes two packs and requires hashes; it does not yet name a seal timestamp field. | W2-E4 builder at freeze |
| M4 | Low | E2 wording that the SUT must not generate its own expected output is already covered by invalid-run gating when gold is SUT-visible. Redundant but not contradictory. | Plan L419, L505 | tracking operator; no packet change required |

## Validation

| Check | Result |
|---|---|
| Remote HEAD / ancestry | `origin/proposal/v4-research-network` = `232c8703`; `5fb8913e` parent = `31d3c85d`; `232c8703` parent = `5fb8913e` |
| Packet identity | assurance, map, and plan unchanged `5fb8913e..232c8703` |
| Repair / admin diffs | repair is documentation-only packet + D-031; admin commit is `EXECUTION_STATE.md` only |
| Authored-file check | passed for 8604 tracked files at the published administrative HEAD |
| Traceability check | passed for seven milestones |
| Prohibited execution artifacts | `WAVE-02-EVIDENCE.md` absent; no experiment namespace, database, or production-module change |
| Experiments run | none |
| Clone / working tree used for review | clean disposable inspection; repository state not modified by this record |

The full product suite was not rerun. A product-suite rerun is not required to review a documentation-only experiment plan.

## Final disposition

`planning_review_pass`

No traceable critical or high planning defect remains inside the proposed §22 boundary after the H1–H6 repair. The human gate owner may accept, reject, or require clarification.

This review is a **recommendation only**. It does **not**:

- mark Wave 2 `human_approved`;
- freeze the contract;
- authorize worktrees, namespaces, or PostgreSQL startup;
- execute any experiment;
- select a vendor, schema, identity policy, disclosure policy, or official version;
- resolve OD-003, OD-004, OD-005, OD-006, or OD-008;
- begin Wave 3, 4, 5, or 8.

Wave 2 remains **`proposed`** and **`unstarted`**.
