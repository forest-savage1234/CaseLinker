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
  legal_state: "self_verified"
  implementation_commit: "ac52ab84dead1ef5aebd74e0291c01bca0b461d5"
  r4_tests_first_commit: "08390048"
  r4_repair_commit: "7521bfb8"
  failed_verification_commit: "f41568e294e9becf032af0904f1ee51483742b4a"
  prior_failed_verification_commit: "e968bdfbe7602c2f1ba0dd3d010f3922e3c78c22"
  assurance_boundary: "frozen"
  process_state: "clean_room_review_requested"
  implementation_paused: true
  human_accepted: false
  official_version_claim: false
wave_02:
  legal_state: "unstarted"
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

Wave 1 remains `self_verified` at `ac52ab84`. The r4 repair is already on this commit. The Wave 1 assurance boundary is now frozen to `GROK_BUILD_PROGRAM.md` §21 plus D-2026-08-15-013. Four review/repair cycles triggered the rework escalation rule. Further implementation is paused. Not `gate_ready`. Not `human_accepted`. Wave 0 remains closed. Wave 2 remains unstarted.

## Next safe action

Clean-room independent review of `ac52ab84` against `docs/v4/assurance/WAVE-01-ASSURANCE.md`. Do not implement r5. Do not mark `gate_ready` from the builder role. Do not begin Wave 2.
