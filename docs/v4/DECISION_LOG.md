# Wave 0 decision log

**Kind of document:** proposal-control.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Statement labels:** `repository fact` | `inference` | `proposal` | `human decision required`

Later waves append. Do not erase. Software does not convert conservative defaults into policy authority.

## D-2026-08-15-001 — Approve Wave 0 discovery only

- **Label:** human decision required (decided)
- **Decision:** Execute Wave 0 only. No product code, schema, migration, CI, tag, release, deployment, live-data migration, publication, or Wave 1.
- **Authority:** operator binding approval of the Wave 0 plan
- **Consequence:** control-plane documents under `docs/v4/` plus one authorized later push of this branch

## D-2026-08-15-002 — v4 base commit

- **Label:** human decision required (decided)
- **Decision:** Start from `4a17a9e5fdf74057de08a819291bf1606b8e3b45`.
- **Rationale recorded by operator:** commits after historical checkpoint `802fb7d2` are verified CI and handoff corrections and must not be discarded.
- **Not decided:** official upstream adoption of those commits
- **Note:** `802fb7d2` remains the v3 M07 implementation checkpoint in `docs/vnext/traceability.v1.json`. That field is not rewritten in Wave 0.

## D-2026-08-15-003 — Isolated workspace

- **Label:** human decision required (decided)
- **Decision:** Branch `proposal/v4-research-network`; worktree `C:\Users\fores\Downloads\CaseLinker-v4-research-network`.
- **Constraints:** do not alter `main` or `proposal/v3-foundation`; copy (do not move or delete) the governing program from the home file; leave the v3 untracked copy untouched.
- **Hash required:** SHA-256 `1F0B496DD38FFD35F3CFB9F8F83B27AFA8DB1EAA4A04177A544165D72AB01A33`

## D-2026-08-15-004 — Local environment mutation authorized

- **Label:** human decision required (decided)
- **Decision:** Installing uv 0.11.33, CPython 3.12, project lock sync, and a local `.venv` is an authorized **environment mutation**.
- **Not authorized:** presenting those installs as non-mutating repository checks

## D-2026-08-15-005 — Sole authorized remote write

- **Label:** human decision required (decided)
- **Decision:** After self-verification, push only `proposal/v4-research-network` to `origin`.
- **Forbidden:** PR, tag, release, deploy, publish, write to upstream, alter `main` or `proposal/v3-foundation`

## D-2026-08-15-006 — Highest product-safety risks

- **Label:** human decision required (decided)
- **Decision:** Rank as highest:
  1. reversible identity and same-event resolution without silent false merges;
  2. complete dependency invalidation and correction propagation;
  3. default-deny disclosure enforcement across every output path.
- **Not ranked in the top three:** PostgreSQL invariant enforcement (later technical experiment)

## D-2026-08-15-007 — Vertical slice status

- **Label:** human decision required (decided)
- **Decision:** The program’s two-source/two-reviewer twelve-step path is a synthetic experimental hypothesis only.
- **Not decided:** reviewer policy, production workflow, or corpus authorization

## D-2026-08-15-008 — Statement labeling

- **Label:** human decision required (decided)
- **Decision:** Every material Wave 0 statement is `repository fact`, `inference`, `proposal`, or `human decision required`.

## D-2026-08-15-009 — Wave 0 verification revision

- **Label:** human decision required (decided)
- **Decision:** Apply `GROK_BUILD_PROGRAM.md` §32. Correct documentation/governance findings only. Do not begin Wave 1 or modify product code.
- **Authority:** operator revision instruction after independent verification failed
- **Consequence:** replace false byte-store implication; complete the 69-ID registry with one bucket each; mark GOV-003 `partial`; assign owner / decision authority / blocking gate or `blocked`; complete phase-gate fields; distinguish Wave 0 artifact acceptance from Phase 0; append findings to the evidence packet without erasure

## D-2026-08-15-010 — Wave 0 documentation completion

- **Label:** human decision required (decided)
- **Decision:** Documentation-only revision: add a program-section crosswalk (IDs may aggregate); add REVIEW-005, OPS-006, OPS-007, EVAL-001; write conceptual Gate 0 architecture flows; do not invent policy or thresholds.
- **Authority:** operator instruction after further Wave 0 review
- **Consequence:** `REQUIREMENTS_TRACEABILITY.md` crosswalk + 73 IDs; `architecture/GATE0_PROPOSAL.md`; evidence buckets reconciled to 0/42/31

## D-2026-08-15-011 — Record Codex Wave 0 verification pass

- **Label:** repository fact of an operator instruction to record a completed independent review
- **Decision:** Record that **Codex** independently verified commit `8cf2d8d1513a83023b2921b99b15ec84c2b4ab7e` with disposition **pass**. Set Wave 0 `independent_review_status: pass` and legal state `gate_ready`. Do **not** set `human_accepted`. Do **not** begin Wave 1.
- **Authority:** operator administrative closeout after the named independent review
- **Consequence:** control-plane status only; no product change; Phase 0 remains incomplete

## D-2026-08-15-012 — Operator accepts and closes Wave 0

- **Label:** human decision required (decided)
- **Decision:** Accept the Wave 0 evidence packet at `a370cfbc6ee419746cf925a682b85da1efd1193e`, including Codex’s independent verification of `8cf2d8d1513a83023b2921b99b15ec84c2b4ab7e`. Set Wave 0 to `human_accepted` and `closed`.
- **Does not decide:** Phase 0 completion, pilot approval, deployment, official version, Wave 1 implementation, Wave 2
- **Consequence:** Wave 1 **planning** may be presented; Wave 1 implementation awaits a separate explicit plan approval

## D-2026-08-15-013 — Wave 1 plan approved

- **Label:** human decision required (decided)
- **Decision:** Approve the Wave 1 plan with binding modifications (slice order, tests-before-implementation, schemas as the executable surface, Proposed ADRs under `docs/v4/adr/`, Postgres logical-only).
- **State:** Wave 0 remains `human_accepted`/`closed`. Wave 1 is `human_approved` (was `proposed`; not unstarted). Wave 2 remains `unstarted`.
- **Does not decide:** Phase 0, pilot, deploy, official version, Wave 2

## D-2026-08-15-014 — Wave 1 revision_required

- **Label:** repository fact
- **Decision:** Independent verification of `b73cccc6f96b2b5d343df8b3cbbdb484ffc1ad45` failed. Wave 1 is `revision_required`. Wave 0 stays closed. Wave 2 stays unstarted. Apply §32 without broadening scope.

## D-2026-08-15-015 — Wave 1 second verification failure

- **Label:** repository fact
- **Decision:** Independent re-verification of `3f57afe1a11b97e608bae4b184396240262a65c4` failed. Wave 1 is `revision_required`. Not `gate_ready`. Wave 0 stays closed. Wave 2 stays unstarted.

## D-2026-08-15-016 — Wave 1 third verification failure

- **Label:** repository fact
- **Decision:** Independent re-verification of `e968bdfbe7602c2f1ba0dd3d010f3922e3c78c22` failed. Wave 1 is `revision_required`. Not `gate_ready`. Wave 2 stays unstarted.

## D-2026-08-15-017 — Wave 1 fourth verification failure

- **Label:** repository fact
- **Decision:** Independent re-verification of `f41568e294e9becf032af0904f1ee51483742b4a` failed. Wave 1 is `revision_required`. Not `gate_ready`. Wave 2 stays unstarted.

## D-2026-08-15-018 — Wave 1 r4 repair self-verified

- **Label:** repository fact
- **Decision:** Tests-first commit `08390048` and contract repair `7521bfb8` close the four accepted r4 findings under self-verification. Wave 1 returns to `self_verified`, not `gate_ready` or `human_accepted`. Wave 2 stays unstarted pending independent re-verification.

## D-2026-08-15-019 — Adopt strategy; freeze Wave 1 boundary; pause further implementation

- **Label:** human decision required (decided)
- **Decision:** Adopt `docs/v4/STRATEGY.md`. Freeze Wave 1 acceptance in `docs/v4/assurance/WAVE-01-ASSURANCE.md` and map every exit requirement. Keep Wave 1 `self_verified` at `ac52ab84`. Do **not** implement an r5 contract repair. Do **not** mark `gate_ready` from the builder. Do **not** begin Wave 2.
- **Rationale:** four consecutive review/repair cycles restructured the same disclosure and transition contracts. `STRATEGY.md` §6 requires a boundary review rather than another patch.
- **Review target:** `ac52ab84dead1ef5aebd74e0291c01bca0b461d5`
- **Independence:** builders of r3/r4 must not be the independent verifier.
- **Consequence:** r4 is historical implementation. Clean-room review classifies remaining issues against the frozen §21 + D-013 boundary (in-scope defect, later-wave improvement, or `program_clarification_required`).

## D-2026-08-15-020 — Wave 1 clean-room review; `gate_ready`

- **Label:** repository fact of an independent-review recommendation plus operator instruction `STRATEGY.md` §10.7
- **Decision:** Record the clean-room review of `ac52ab84` (`docs/v4/evidence/WAVE-01-CLEANROOM-REVIEW.md`). No traceable critical/high defect remains inside the frozen boundary. Set Wave 1 to `gate_ready`. Do **not** set `human_accepted`. Do **not** begin Wave 2. Do **not** implement r5.
- **Independence limitation:** same-model reviewer; gates not re-executed in that review. Not organizational independence.
- **Does not decide:** Phase 0 completion, official version, policy content, or Wave 2.

## D-2026-08-15-021 — Wave 1 not human-accepted

- **Label:** human decision required (decided)
- **Decision:** Do **not** human-accept Wave 1. `human_accepted` remains false. Wave 1 may stay `gate_ready` from the clean-room review; that is not acceptance.
- **Also decided:** the frozen §21 + D-013 assurance boundary remains adopted; `STRATEGY.md` remains adopted; disclosure and SoD contracts are **not** reopened; Wave 2 remains `unstarted`.
- **Does not decide:** later acceptance, Phase 0 completion, official version, or any product change
- **Consequence:** no Wave 2 planning or implementation; no r5; no disclosure/SoD patch

## D-2026-08-15-022 — Withdraw `gate_ready` (reason 1 of 2): W1-N15 not executable

- **Label:** human decision required (decided)
- **Decision:** Withdraw the present `gate_ready` conclusion. Wave 1 is `revision_required`. `human_accepted` remains false. Wave 2 remains `unstarted`.
- **Traceable basis (reason 1):** W1-N15 requires an **executable v4** demonstration that allegation is not guilt (`WAVE-01-ASSURANCE.md` §2 required distinctions; `GROK_BUILD_PROGRAM.md` §21). The requirements map marked W1-N15 `implemented`. The clean-room review recorded that there is no v4 schema, invariant, or §7 test (M2). Reliance on unchanged v3 extractors / “Wave 1 adds no guilt type” is insufficient.
- **Governing IDs:** W1-N15; CONST-005
- **Not decided yet:** reason 2 of the stated pair (not received)
- **Does not reopen:** disclosure or SoD contracts
- **Does not authorize:** implementation of a repair before the accepted critical/high set is complete

## D-2026-08-15-023 — Withdraw `gate_ready` (reason 2 of 2): review procedurally invalid

- **Label:** human decision required (decided)
- **Decision:** The clean-room review that recommended `gate_ready` is `review_invalid`. Wave 1 remains `revision_required`. `human_accepted` remains false. Wave 2 remains `unstarted`.
- **Traceable basis (reason 2):** `WAVE-01-ASSURANCE.md` §8 requires the independent verifier to rerun the approved gates. `STRATEGY.md` §5 step 4 and §7 require those gates and a valid independent review. The recorded reviewer did not rerun the gates and said so. That is insufficient execution, not a product finding.
- **Governing IDs:** assurance §8 item 3; strategy §4 independent verifier; §5 step 4; §7 stopping rule; disposition `review_invalid`
- **Accepted critical/high set is now complete:** GR-1 (W1-N15 executable allegation≠guilt) and GR-2 (this invalid review)
- **Does not reopen:** disclosure or SoD contracts
- **Next authorized product work:** one coherent W1-N15 revision only, tests first, then a new independent review that reruns the approved gates. No r5 disclosure/SoD patch.

## D-2026-08-15-024 — Authorize W1-N15-only revision

- **Label:** human decision required (decided)
- **Decision:** Apply only the smallest policy-neutral v4 contract/test that allegation is not guilt. Do **not** perform another disclosure or SoD revision. After the repair, obtain a fresh independent review that **reruns** the approved gates. Only if that review is valid and finds no in-boundary critical/high defect may Wave 1 return to `gate_ready` for later human acceptance.
- **Does not decide:** human acceptance, Wave 2, official version

## D-2026-08-15-025 — W1-N15 review valid; Wave 1 `gate_ready` for later acceptance

- **Label:** repository fact of a valid independent review plus D-024
- **Decision:** Record `docs/v4/evidence/WAVE-01-W1N15-REVIEW.md`. The reviewer reran the approved gates. GR-1 is closed. No in-boundary critical/high defect remains. Set Wave 1 to `gate_ready`. Do **not** set `human_accepted`. Do **not** begin Wave 2.
- **Independence limitation:** same-model reviewer. Unlike the prior review, gates were rerun, so this review is not `review_invalid`.
- **Does not decide:** human acceptance, Phase 0, official version, Wave 2

## D-2026-08-15-026 — Operator accepts and closes Wave 1

- **Label:** human decision required (decided)
- **Decision:** Forest Savage, as human gate owner, explicitly human-accepts Wave 1. Accepted implementation `740862d339d8e1ea29f42d30144d51cb076045b0`. Accepted gate-ready record `c30a1d3f4175d50b5461799194ea54b960d41624`. Acceptance boundary: the frozen Wave 1 assurance contract derived from `GROK_BUILD_PROGRAM.md` §21 and D-2026-08-15-013. Set Wave 1 to `human_accepted` and `closed`.
- **Accepted residuals:** documented same-model independence limitation; three unchanged Windows baseline exceptions; recorded medium/low residual items as non-blocking carry-forward work.
- **Valid review:** `docs/v4/evidence/WAVE-01-W1N15-REVIEW.md`. The earlier clean-room review remains `review_invalid`.
- **Does not decide:** Phase 0 or Gate 0 completion; official version; deployment or upstream adoption; any blocked OD-* decision; Wave 2 implementation.
- **Consequence:** Wave 1 is closed. Wave 2 planning is permitted but remains `unstarted`. Wave 2 implementation is not authorized.

## D-2026-08-15-027 — Wave 2 planning proposed (not approved, not started)

- **Label:** repository fact of an operator-authorized planning packet
- **Decision:** Record a **proposed** Wave 2 assurance and experiment plan for human review. Wave 2 `legal_state` remains `unstarted`. Do **not** execute experiments. Do **not** create worktrees, namespaces, migrations, services, or tests. Do **not** mark Wave 2 `human_approved`, `self_verified`, or `gate_ready`.
- **Artifacts:** `docs/v4/assurance/WAVE-02-ASSURANCE.md`; `docs/v4/assurance/WAVE-02-REQUIREMENTS-MAP.md`; `docs/v4/experiments/WAVE-02-PLAN.md`
- **Proposed experiments:** W2-E1 PostgreSQL invariants; W2-E2 dependency invalidation; W2-E3 disclosure leakage; W2-E4 source-family; W2-E5 identity hypotheses
- **Does not decide:** Wave 2 execution; vendor or infrastructure selection; policy content; any blocked OD-*; Phase 0 / Gate 0; official version; Wave 3
- **Consequence:** Human gate owner reviews the proposed boundary. Wave 2 implementation awaits a separate explicit plan approval.

## D-2026-08-15-028 — Revise proposed Wave 2 planning packet (W2-P1…P5)

- **Label:** repository fact of an operator-authorized planning revision
- **Decision:** Revise the **proposed** Wave 2 packet. Confirm and repair: W2-P1 independent-dimension bitemporal model (no cross-clock ordering); W2-P2 separate closure correctness, registration coverage, and incomplete-state fail-closed; W2-P3 independent-pair failure is classification **or** suppression; W2-P4 explicit P9 disposition; W2-P5 sequential default E5→E2→E3→E4→E1. Wave 2 `legal_state` remains `unstarted`. The packet remains `proposed`, not frozen or human-approved.
- **Does not rewrite:** D-027 or the original proposed-plan commit
- **Does not decide:** Wave 2 execution; experiment worktrees; PostgreSQL startup; product changes; Wave 3; Phase 0 / Gate 0; official version
- **Consequence:** Request a fresh independent review of the revised planning packet. Do not begin execution.

## Ownership convention

- **Accountable owner:** person or role who must keep the item visible and stop dependent work. Until a specialist is named, the Wave 0 program operator (this fork’s operator) is the tracking owner only.
- **Decision authority:** who may decide the substance. If unnamed, the item is **blocked**.
- **Blocking gate:** earliest wave/phase that must not start, or must not be marked complete, until the decision exists.
- Software defaults are not authority.

## Open decisions (no software default is authority)

| ID | Question | Accountable owner | Decision authority | Blocking gate | Status |
|---|---|---|---|---|---|
| OD-001 | Upstream maintainer disposition of the v3 proposal | program operator (tracking) | upstream maintainer (`mrinaalr`) — named by charter, not yet recorded as responding | any official naming, merge, or “adopted” claim; Phase 0 exit | **blocked** (disposition **unknown**) |
| OD-002 | Initial users, organizations, audiences, deployment boundary | program operator (tracking) | unassigned organizational sponsor | Phase 3 / Wave 5 entry; any pilot | **blocked** |
| OD-003 | Governing privacy/disclosure authority and jurisdictions | program operator (tracking) | unassigned authorized privacy/legal authority | Wave 5 / Gate 3; DISCLOSE-002/003 content | **blocked** |
| OD-004 | Approved source classes, retention, takedown | program operator (tracking) | unassigned source-governance / legal authority | live or expanded collection; SOURCE-002 | **blocked** |
| OD-005 | Reviewer roles, qualifications, independence, adjudication | program operator (tracking) | unassigned review-governance authority | Wave 5 authenticated review | **blocked** |
| OD-006 | Acceptable identity-resolution scope | program operator (tracking) | unassigned child-safety + scientific authority | Wave 4 / Gate 2; R-ID | **blocked** |
| OD-007 | Tenancy model | program operator (tracking) | unassigned organizational sponsor (same as OD-002 unless split) | OPS-004; Wave 8 tenant tests | **blocked** |
| OD-008 | Acceptable infrastructure and operational environment | program operator (tracking) | unassigned infrastructure/operations authority | Wave 8 / Gate 6; object store, Postgres production claim | **blocked** |
| OD-009 | Pilot corpus and shadow-mode protocol | program operator (tracking) | unassigned scientific + disclosure authority | Wave 7; Phase 0 “approved pilot” | **blocked** |
| OD-010 | Who performs independent Wave 0 verification | program operator (tracking) | Wave 0 review: **Codex** (pass on `8cf2d8d1`). Operator set `human_accepted` on `a370cfbc` | Wave 1 **implementation** awaits a separate plan approval | Wave 0 **closed** |
| OD-011 | Whether to add a read-only `upstream` remote | program operator (tracking) | program operator (local git config only); does not create upstream authority | not required for Wave 0; optional later | open, not blocking Wave 0 re-verification |

No policy, legal rule, reviewer qualification, or numerical quality threshold is recorded as decided.
