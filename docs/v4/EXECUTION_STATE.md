# Execution state

**Governing identity:** v4 in design, proposal in identity, no official release claim.

```yaml
wave_00:
  legal_state: "closed"
  human_accepted: true
  accepted_closeout_commit: "a370cfbc6ee419746cf925a682b85da1efd1193e"
  independent_reviewer: "Codex"
  independent_review_status: "pass"
  reviewed_commit: "8cf2d8d1513a83023b2921b99b15ec84c2b4ab7e"
wave_01:
  legal_state: "closed"
  implementation_commit: "740862d339d8e1ea29f42d30144d51cb076045b0"
  accepted_implementation_commit: "740862d339d8e1ea29f42d30144d51cb076045b0"
  accepted_gate_ready_commit: "c30a1d3f4175d50b5461799194ea54b960d41624"
  prior_implementation_commit: "ac52ab84dead1ef5aebd74e0291c01bca0b461d5"
  withdrawn_gate_ready_commit: "ae7ce4947efe0dbdd15e645b4df14ecc7c68fdcb"
  w1n15_tests_first_commit: "34930959e884b8c188c99eaf11012625ede82ef0"
  r4_tests_first_commit: "08390048"
  r4_repair_commit: "7521bfb8"
  failed_verification_commit: "f41568e294e9becf032af0904f1ee51483742b4a"
  prior_failed_verification_commit: "e968bdfbe7602c2f1ba0dd3d010f3922e3c78c22"
  assurance_boundary: "frozen"
  process_state: "human_accepted"
  independent_reviewer: "same-model Grok (worktree-isolated; reran gates)"
  independent_review_status: "gate_ready_recommended"
  independent_review_record: "docs/v4/evidence/WAVE-01-W1N15-REVIEW.md"
  prior_review_status: "review_invalid"
  prior_review_record: "docs/v4/evidence/WAVE-01-CLEANROOM-REVIEW.md"
  implementation_paused: true
  human_accepted: true
  official_version_claim: false
wave_02:
  legal_state: "unstarted"
  planning_status: "proposed"
  planning_decision: "D-2026-08-15-027"
  planning_revision: "D-2026-08-15-028"
  proposed_assurance_contract: "docs/v4/assurance/WAVE-02-ASSURANCE.md"
  proposed_requirements_map: "docs/v4/assurance/WAVE-02-REQUIREMENTS-MAP.md"
  proposed_experiment_plan: "docs/v4/experiments/WAVE-02-PLAN.md"
  proposed_primary_proof_obligation: "obtain evidence about the hardest assumptions before committing the architecture to them"
  experiments_executed: false
  official_version_claim: false
gate_0: "not_complete"
approved_base_commit: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
branch: "proposal/v4-research-network"
primary_proof_obligation: "temporal evidence network expressed as versioned policy-neutral contracts before infrastructure"
strategy: "docs/v4/STRATEGY.md"
assurance_contract: "docs/v4/assurance/WAVE-01-ASSURANCE.md"
```

## Wave 0

Closed. Operator accepted `a370cfbc` including Codex pass of `8cf2d8d1`. Not Phase 0 complete.

## Wave 1

Closed. Operator accepted implementation `740862d3` and gate-ready record `c30a1d3f` (D-026), including the valid W1-N15 review. The prior clean-room review remains `review_invalid`. Disclosure and SoD were not reopened. This does **not** complete Phase 0 or Gate 0, establish an official version, authorize deployment or upstream adoption, resolve any blocked OD-* decision, or authorize Wave 2 implementation. Wave 2 remains unstarted.

## Wave 2

Unstarted. A planning packet is **proposed** (D-027) and was revised (D-028: W2-P1…P5). It is not frozen or approved. No experiment has been executed. No worktree, namespace, migration, service, schema, or test was created for Wave 2. This does **not** approve Wave 2, select infrastructure, invent policy content, complete Phase 0 or Gate 0, or authorize Wave 3.

## Next safe action

Fresh independent review of the **revised** proposed Wave 2 assurance and experiment plan. Do not execute Wave 2 until that plan is independently reviewed and explicitly approved. Phase 0 / Gate 0 remain incomplete. Do not reopen Wave 1 disclosure or SoD contracts.
