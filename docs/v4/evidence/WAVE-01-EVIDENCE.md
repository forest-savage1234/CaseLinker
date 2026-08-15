# WAVE-01 evidence packet

```yaml
wave: "01"
status: "self_verified"
approved_base_commit: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
wave_00_accepted_closeout: "a370cfbc6ee419746cf925a682b85da1efd1193e"
result_commit: "uncommitted"
primary_proof_obligation: "temporal evidence network expressed as versioned policy-neutral contracts before infrastructure"
requirements_closed: []
requirements_partially_met_added_this_wave:
  - RESOLVE-001
  - RESOLVE-002
  - RESOLVE-003
  - RESOLVE-004
  - RESOLVE-005
  - AI-001
  - AI-002
  - OPS-001
adrs:
  - docs/v4/adr/W1-001-versioned-json-contracts.md
  - docs/v4/adr/W1-002-bitemporal-identities-transitions.md
  - docs/v4/adr/W1-003-lineage-and-hypotheses.md
  - docs/v4/adr/W1-004-eligibility-disclosure-authority.md
  - docs/v4/adr/W1-005-projections-ai-logical-postgres.md
migrations: []
implementation:
  - src/caselinker/v4_contracts/validate.py
  - schemas/v4/
tests:
  - tests/unit/v4/
independent_review_status: "not_started"
human_accepted: false
wave_02: "unstarted"
```

## Proof

Five distinctions are executable on policy-safe fixtures:

| Distinction | Test |
|---|---|
| Allegation is not guilt | unchanged v3 extractors; Wave 1 does not add a guilt type |
| Event time is not knowledge time | `test_knowledge_time_is_not_event_time` |
| Similarity is not identity | `test_similarity_does_not_create_identity` |
| Eligibility is not disclosure | `test_eligibility_is_not_disclosure` |
| Projection is not source of truth | `test_authoritative_projection_is_rejected` |

## Slice order (tests before implementation)

Recorded in git: failing test commits precede the schema/ADR commits for slices A–E.

## What Wave 1 did not do

No live migration, no Postgres service, no object store, no IdP, no policy content, no Wave 2 experiments, no official version.

## Rollback

Revert Wave 1 commits on `proposal/v4-research-network`. `main` and `proposal/v3-foundation` unchanged.
