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
  legal_state: "human_approved"
  human_accepted: false
  official_version_claim: false
wave_02:
  legal_state: "unstarted"
gate_0: "not_complete"
approved_base_commit: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
branch: "proposal/v4-research-network"
primary_proof_obligation: "temporal evidence network expressed as versioned policy-neutral contracts before infrastructure"
```

## Wave 0 (closed)

Operator accepted the packet at `a370cfbc` including the Codex pass of `8cf2d8d1`. That does not complete Phase 0, approve a pilot, authorize deployment, or confer an official version.

## Wave 1 (human_approved → implementing)

Approved plan with binding modifications: dependency-ordered contract slices; tests before implementation; schemas/validators as the executable surface; ADRs `Status: Proposed` in `docs/v4/adr/`; PostgreSQL logical analysis only.

Slices: A kernel → B time/identity/state → C lineage/hypotheses → D eligibility/disclosure/authority → E projections/audit/AI + logical Postgres.

## Next safe action

Implement Wave 1 slices in order. Stop at `self_verified`. Do not begin Wave 2.
