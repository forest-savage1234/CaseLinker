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

## D-2026-08-15-029 — Record Wave 2 planning review (`planning_review_pass`)

- **Label:** repository fact of a completed planning review
- **Decision:** Record `docs/v4/evidence/WAVE-02-PLAN-REVIEW.md` of commit `ed7597a4efbf5ad0a60318cb59193093a178c451`. Disposition `planning_review_pass`. No traceable critical/high planning defect remains. Wave 2 `legal_state` remains `unstarted`. The packet remains `proposed`. Do **not** set `human_approved`. Do **not** execute experiments.
- **Independence limitation:** same-model reviewer; this conversation lineage previously authored the packet. Not organizational independence. Documentation gates were rerun. Experiment procedures were not run.
- **Does not decide:** human approval of Wave 2; execution; vendor or policy selection; Phase 0 / Gate 0; official version; Wave 3
- **Consequence:** Human gate owner decides whether to approve the proposed packet. Medium/low residuals remain non-blocking carry-forward unless the human converts them.

## D-2026-08-15-030 — Wave 2 planning review 02 is `review_invalid`

- **Label:** repository fact of a failed independence check
- **Decision:** Record `docs/v4/evidence/WAVE-02-PLAN-REVIEW-02.md`. Disposition `review_invalid`. This conversation lineage authored and revised the Wave 2 planning packet and authored the prior review. The packet was **not** evaluated. The prior review remains on disk as history and is **not** a valid independent review. Wave 2 `legal_state` remains `unstarted`. The packet remains `proposed`. Do **not** set `human_approved`. Do **not** execute experiments.
- **Does not rewrite:** D-027, D-028, D-029, or `WAVE-02-PLAN-REVIEW.md`
- **Does not decide:** the technical merit of the proposed packet; human approval; execution
- **Consequence:** A genuinely fresh conversation must perform the independent planning review. D-029 is not independent acceptance.

## D-2026-08-15-031 — Revise proposed Wave 2 planning packet (falsifiability and oracles)

- **Label:** repository fact of an operator-authorized planning revision
- **Decision:** Revise the **proposed** Wave 2 planning packet so that each experiment’s claim matches what its permitted surface can prove, and so that each experiment has an independent oracle, a reproducible procedure, a valid-run gate, and an exhaustive stop / revise / proceed mapping. The packet being revised is `ed7597a4efbf5ad0a60318cb59193093a178c451`. The starting branch HEAD was `31d3c85d92aac4f49448a2e8f123b2dc37359664`. The containing commit records this proposed revision. Wave 2 `legal_state` remains `unstarted`. The packet remains `proposed`. No experiment was run. No prior review was rewritten. Independent re-verification of this revision is required.
- **Does not rewrite:** D-027, D-028, D-029, D-030, `WAVE-02-PLAN-REVIEW.md`, or `WAVE-02-PLAN-REVIEW-02.md`
- **Does not decide:** Wave 2 approval, freeze, or execution; vendor, schema, identity-policy, disclosure-policy, or official-version selection; any blocked OD-*; Phase 0 / Gate 0; Wave 3
- **Consequence:** Request independent re-verification of this revision by a reviewer outside the builder lineage. Do not begin execution.

## D-2026-08-15-032 — Record valid independent Wave 2 planning re-verification

- **Label:** repository fact of a completed valid independent planning re-verification
- **Decision:** Record `docs/v4/evidence/WAVE-02-PLAN-REVIEW-03.md` as the valid independent re-verification of planning packet `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`. Review-record commit `4c52b41aa03725cde9c1d2b4224a12259397152b`. Disposition `planning_review_pass`. The reviewer identified H1–H6 and specified remediation criteria but did not author or edit repair `5fb8913e`. H1–H6 are closed. No new critical/high finding remains. Material residuals M1–M4 remain non-blocking execution or administrative controls. Wave 2 `legal_state` remains `unstarted`. The packet remains `proposed`. `human_approved` remains false. `experiments_executed` remains false.
- **Does not rewrite:** D-027, D-028, D-029, D-030, D-031, `WAVE-02-PLAN-REVIEW.md`, or `WAVE-02-PLAN-REVIEW-02.md`
- **Historical invalidity preserved:** D-029’s recorded `planning_review_pass` remains invalid because its reviewer authored the packet. D-030 is `review_invalid`. The unpushed local attempt `a9b2c7fa2482d71d38dadf88dfef03d5e742ed3b` is not valid acceptance.
- **Does not decide:** Wave 2 approval, freeze, or execution; vendor, schema, identity-policy, disclosure-policy, or official-version selection; any blocked OD-*; Phase 0 / Gate 0; Wave 3
- **Consequence:** The next authority belongs solely to the human gate owner deciding whether to approve and freeze exactly `5fb8913e78d0e54ed25021bb34fcade43d2aff3c` for Wave 2 experiment execution only. This decision does not approve, freeze, or execute Wave 2.

## D-2026-08-15-033 — Human approves and freezes Wave 2 planning packet

- **Label:** human decision required (decided)
- **Decision:** Forest Savage, as human gate owner, issued the following decision verbatim:

  I approve and freeze exactly Wave 2 planning packet `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`.

  My approval relies on the valid independent review recorded by commit `4c52b41aa03725cde9c1d2b4224a12259397152b` and the administrative reconciliation recorded by commit `bedeb04b15e17885af6fe7a41c963c8cd154ffcd`.

  This approval authorizes execution of the five planned Wave 2 experiments only, sequentially in the governed order beginning with E5. It does not pre-accept any experimental result, approve later-wave implementation, waive an invalid/revise/stop condition, or authorize work beyond the frozen packet.

  No experiment may begin unless the approved commit lineage is verified, the working tree is clean, and the packet remains byte-identical to `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`.

- **Frozen packet:** `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`
- **Valid review record:** `docs/v4/evidence/WAVE-02-PLAN-REVIEW-03.md` at `4c52b41aa03725cde9c1d2b4224a12259397152b`
- **State reconciliation relied upon:** `bedeb04b15e17885af6fe7a41c963c8cd154ffcd`
- **Authorization:** Wave 2 experiments only, sequential order W2-E5 → W2-E2 → W2-E3 → W2-E4 → W2-E1. Next authorized experiment is W2-E5 only. `experiments_executed` remains false. No experiment namespace is created by this decision.
- **Does not rewrite:** D-027 through D-032 or any review record
- **Does not decide:** any experimental result; later-wave implementation; any blocked OD-*; Phase 0 / Gate 0; official version; vendor, schema, identity policy, or disclosure policy
- **Consequence:** The planning packet is frozen and `human_approved`. The only unlocked experiment is W2-E5, and only after the lineage, clean-tree, and packet-identity conditions in the human decision are met.

## D-2026-08-15-034 — Continue after valid W2-E5 r3; authorize W2-E2 only

- **Label:** human decision required (decided), with administrative checkpoint reconciliation
- **Human instruction (verbatim):** “Once the playbook is complete, execute it carefully.”
- **Conservative scope applied:** The completed mission-completion playbook makes its first execution gate the already-reviewed W2-E5 r3 checkpoint. This record therefore applies the instruction only to that presently knowable gate: accept the read-only checkpoint advice for valid W2-E5 r3 evidence commit `105ac4237b767db51c95161e202dacfff0590a92` and authorize W2-E2 as the next named experiment. It is not blanket pre-authorization of outcome-dependent later gates.
- **Eligible W2-E5 evidence:** `105ac4237b767db51c95161e202dacfff0590a92`, parent `e620ec75c334a8e3fa7bd27358ebbdcd3ed3af50`; valid run; recommendation `proceed`; fixture/oracle/SUT/driver/harness hashes match the frozen run record; oracle content was loaded only after SUT completion and output capture.
- **Preserved invalid/incomplete attempts:** `98a171dc6df0c0fa04f9eb22598191f0a48e7efe` (oracle lacked complete I-trans and I-contra traces) and `ce28e88c42223767a1d85f880ea7b6b6a7f28b22` (oracle deserialized and validated before SUT execution). Neither result is eligible evidence.
- **Architecture implication accepted for sequencing only:** A disposable hypothesis driver demonstrated reversible recovery from a mistaken `confirmed_same` decision without destroying evidence or creating a canonical identity. This does not decide OD-006 or select an operational identity model.
- **Authorization:** W2-E2 only, from the still-frozen packet `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`, after verifying this administrative commit, clean state, and packet identity.
- **Does not authorize:** W2-E3, W2-E4, W2-E1, Wave 2 acceptance, Wave 3, production code promotion, canonical merge/split, any blocked OD-* decision, cleanup, deployment, or an official-version claim.
- **Consequence:** W2-E5 is complete with r3 as its sole eligible result. W2-E2 becomes the only unlocked experiment. Every later experiment remains locked pending its own valid result, read-only checkpoint, and explicit human continuation decision.

## D-2026-08-15-035 — Continue after valid W2-E2 r2; authorize W2-E3 only

- **Label:** human decision required (decided), with administrative checkpoint reconciliation
- **Human instruction (verbatim):** “Continue from here”
- **Conservative scope applied:** The instruction follows the read-only W2-E2 r2 checkpoint whose disposition was `continue_to_next_experiment`. This record applies the instruction only to the next governed step, W2-E3. It is not blanket pre-authorization of outcome-dependent W2-E4, W2-E1, or any later gate.
- **Eligible W2-E2 evidence:** `d026ca02d38009181bea1aa5f5821f48a4319057`, parent `faaa4ac021cb9c3ddb5282540cf2a5491c89cd16`; valid run; recommendation `proceed`; frozen fixture, independent oracle, SUT, driver, harness, output, chronology, and comparison hashes matched; oracle content was deserialized only after SUT completion and output capture; nine hand-enumerated fixtures kept closure, registration coverage, and incomplete-state fail-closed behavior distinct; comparison findings were zero.
- **Preserved invalid/incomplete attempt:** `64ac72883711ef83eb02d5a5b8772e81f7ec226c`; its post-run `git diff --check` failed on already-hashed authored files. It remains ineligible and was not rewritten.
- **Checkpoint status and limitation:** The checkpoint conversation did not author, edit, execute, or repair W2-E2 r1 or r2 and performed read-only verification only. It advised `continue_to_next_experiment` with no critical/high finding. It did not rerun the experiment and is not a `WAVE-02-ASSURANCE.md` section 7 gate-ready review; same-model separation is not organizational independence. This limitation is preserved rather than upgraded by this administrative decision.
- **Architecture implication accepted for sequencing only:** The disposable experiment supports bounded dependency impact over an explicitly registered fixture universe, while detecting incomplete registration and refusing a complete-impact claim. It does not prove unknowable external dependents, select a production graph/store, or silently resolve an OD-* decision.
- **Authorization:** W2-E3 only, from the still-frozen packet `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`, and only after this administrative commit is published and its lineage, clean isolated tree, and packet identity are verified.
- **Does not authorize:** W2-E4, W2-E1, Wave 2 acceptance, Wave 3, production code promotion, cleanup of preserved evidence, deployment, any blocked OD-* decision, or an official-version claim.
- **Consequence:** W2-E2 is complete with r2 as its sole eligible result. W2-E3 becomes the only unlocked experiment after publication of this record. Every later experiment remains locked pending its own valid result, read-only checkpoint, and explicit human continuation decision.

## D-2026-08-15-036 — Record W2-E3 r1 repeat_experiment; authorize one bounded r2 only

- **Label:** human decision required (decided), with administrative checkpoint reconciliation
- **Human instruction (verbatim):** “I accept the independent W2-E3 checkpoint disposition `repeat_experiment` for evidence commit `4e620ab45e2dd771e6ed04eca243259bafb610a8`. Preserve that commit and draft PR #1 as W2-E3 r1 evidence. Do not amend, delete, force-push, or represent it as eligible evidence. I authorize one bounded W2-E3 r2 only, after administratively recording this checkpoint. The repeat must: (1) actually execute and independently prove the required cache, search, log, error, and administrative bypass attempts rather than recording them as metadata; (2) exercise M3 by revoking or expiring the same previously allowed decision, preserving its identity and unrelated attributes; (3) add recursive oracle/harness detection for nested denied keys and values, and make the SUT fail closed through a general structural rule—not by recognizing canary strings, expected labels, or the frozen answer matrix; (4) preserve oracle separation, deterministic reproducibility, P9’s observational boundary, and the frozen planning packet; (5) avoid product-code changes, blocked OD decisions, policy invention, later-wave implementation, or production promotion. W2-E4, W2-E1, Wave 2 acceptance, cleanup, deployment, and official-version claims remain locked. A reviewer who did not author or repair W2-E3 r2 must independently verify it before any continuation decision.”
- **Conservative scope applied:** This record transcribes that instruction only. It accepts the independent checkpoint disposition `repeat_experiment` for the named r1 commit, preserves that commit and draft PR #1 as ineligible evidence, and authorizes one bounded W2-E3 r2 after this administrative commit is published. It is not blanket pre-authorization of W2-E4, W2-E1, Wave 2 acceptance, or any later gate.
- **Preserved ineligible W2-E3 r1 evidence:** `4e620ab45e2dd771e6ed04eca243259bafb610a8`, parent `9c481ee78bce8f916b9773f46924558424babdae`; branch `experiment/w2-e3`; draft PR https://github.com/forest-savage1234/CaseLinker/pull/1. This commit and PR remain preserved. They must not be amended, deleted, force-pushed, merged as eligible evidence, or represented as a valid W2-E3 result.
- **Independent checkpoint disposition:** `repeat_experiment`
- **Why r1 is ineligible:** The independent checkpoint found required cases absent, so the invalid/incomplete gate applies before any architecture-result precedence. Specifically: the cache, search, log, error, and administrative bypass attempts were recorded as metadata rather than executed against unsafe sources; M3 substituted the separately identified `D-revoked` decision instead of revoking or expiring the same previously allowed `D-internal` decision while preserving its identity and unrelated attributes; and nested denied keys or values inside an allowed field were invisible to a top-level field-name scorer because the SUT shallow-copied authorized values without a general structural fail-closed rule.
- **Authorization:** one bounded W2-E3 r2 only, from the still-frozen packet `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`, and only after this administrative commit is published and its lineage, a clean isolated experiment working tree, and packet identity are verified. The repeat remains confined to the disposable W2-E3 namespace and must satisfy the five repeat constraints in the human instruction.
- **Does not authorize:** W2-E4, W2-E1, Wave 2 acceptance, Wave 3, product-code changes, blocked OD-* decisions, policy invention, later-wave implementation, production promotion, cleanup of preserved evidence, deployment, or an official-version claim.
- **Continuation gate:** A reviewer who did not author or repair W2-E3 r2 must independently verify that r2 before any continuation decision. This administrative record is not that review.
- **Consequence:** W2-E3 remains incomplete. r1 is preserved and ineligible. The only unlocked work is one bounded W2-E3 r2. Every later experiment remains locked.

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
