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
  legal_state: "human_approved"
  planning_status: "frozen"
  planning_decision: "D-2026-08-15-027"
  planning_revision: "D-2026-08-15-031"
  planning_revision_commit: "5fb8913e78d0e54ed25021bb34fcade43d2aff3c"
  frozen_planning_packet: "5fb8913e78d0e54ed25021bb34fcade43d2aff3c"
  approval_decision: "D-2026-08-15-033"
  execution_checkpoint_decision: "D-2026-08-15-034"
  completed_experiments:
    - "W2-E5"
  experiment_results:
    W2-E5:
      status: "valid"
      recommendation: "proceed"
      eligible_evidence_commit: "105ac4237b767db51c95161e202dacfff0590a92"
      invalid_incomplete_attempts:
        - commit: "98a171dc6df0c0fa04f9eb22598191f0a48e7efe"
          reason: "oracle lacked complete I-trans and I-contra traces"
        - commit: "ce28e88c42223767a1d85f880ea7b6b6a7f28b22"
          reason: "oracle deserialized and validated before SUT execution"
      checkpoint_advice: "continue_to_next_experiment"
      checkpoint_decision: "D-2026-08-15-034"
  next_authorized_experiment: "W2-E2"
  planning_review_01_recorded_disposition: "planning_review_pass"
  planning_review_01_validity: "review_invalid"
  planning_review_01_invalidated_by: "D-2026-08-15-030"
  planning_review_01_record: "docs/v4/evidence/WAVE-02-PLAN-REVIEW.md"
  planning_review_01_decision: "D-2026-08-15-029"
  planning_review_02_recorded_disposition: "review_invalid"
  planning_review_02_validity: "review_invalid"
  planning_review_02_record: "docs/v4/evidence/WAVE-02-PLAN-REVIEW-02.md"
  planning_review_02_decision: "D-2026-08-15-030"
  planning_review_03_recorded_disposition: "planning_review_pass"
  planning_review_03_validity: "valid"
  planning_review_03_reviewed_commit: "5fb8913e78d0e54ed25021bb34fcade43d2aff3c"
  planning_review_03_record: "docs/v4/evidence/WAVE-02-PLAN-REVIEW-03.md"
  planning_review_03_record_commit: "4c52b41aa03725cde9c1d2b4224a12259397152b"
  planning_review_03_decision: "D-2026-08-15-032"
  valid_independent_planning_review: true
  proposed_assurance_contract: "docs/v4/assurance/WAVE-02-ASSURANCE.md"
  proposed_requirements_map: "docs/v4/assurance/WAVE-02-REQUIREMENTS-MAP.md"
  proposed_experiment_plan: "docs/v4/experiments/WAVE-02-PLAN.md"
  proposed_primary_proof_obligation: "obtain evidence about the hardest assumptions before committing the architecture to them"
  experiments_executed: true
  human_approved: true
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

Human-approved and frozen (D-033). The frozen planning packet is exactly `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`. Approval relies on the valid independent review at `4c52b41aa03725cde9c1d2b4224a12259397152b` (`WAVE-02-PLAN-REVIEW-03.md`, D-032) and the administrative reconciliation at `bedeb04b15e17885af6fe7a41c963c8cd154ffcd`. Review 01 (D-029) remains `review_invalid`. Review 02 (D-030) remains `review_invalid`.

W2-E5 is complete under D-034. Attempts `98a171dc` and `ce28e88c` remain invalid/incomplete and ineligible. W2-E5 r3 commit `105ac4237b767db51c95161e202dacfff0590a92` is the sole eligible result: valid run, recommendation `proceed`, with oracle content loaded only after SUT completion and output capture. This result is not Wave 2 acceptance and does not decide OD-006 or select a canonical identity model. Later-wave work is not authorized. Invalid/revise/stop conditions are not waived. The only unlocked experiment is W2-E2.

## Next safe action

W2-E2 only, after verifying the D-034 administrative lineage, a clean working tree, and packet identity `5fb8913e78d0e54ed25021bb34fcade43d2aff3c`. Do not start W2-E3, W2-E4, or W2-E1. Phase 0 / Gate 0 remain incomplete. `official_version_claim` remains false.
