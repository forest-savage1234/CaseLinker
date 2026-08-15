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
  legal_state: "revision_required"
  failed_verification_commit: "f41568e294e9becf032af0904f1ee51483742b4a"
  prior_failed_verification_commit: "e968bdfbe7602c2f1ba0dd3d010f3922e3c78c22"
  human_accepted: false
  official_version_claim: false
wave_02:
  legal_state: "unstarted"
gate_0: "not_complete"
approved_base_commit: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
branch: "proposal/v4-research-network"
primary_proof_obligation: "temporal evidence network expressed as versioned policy-neutral contracts before infrastructure"
```

## Wave 0

Closed. Operator accepted `a370cfbc` including Codex pass of `8cf2d8d1`. Not Phase 0 complete.

## Wave 1

Independent re-verification of `f41568e2` failed. Wave 1 is `revision_required`, not `gate_ready`, not `human_accepted`. Wave 0 remains closed. Wave 2 remains unstarted.

## Next safe action

Run the red r4 adversarial tests, then apply the smallest contract-only repair. Do not mark `gate_ready`. Do not begin Wave 2.
