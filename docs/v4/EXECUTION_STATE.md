# Execution state — Wave 00

**Kind of document:** proposal-control. Conversation memory is non-authoritative.  
**Governing identity:** v4 in design, proposal in identity, no official release claim.

This file is not required to contain the final branch HEAD after later commits. Report that SHA externally.

```yaml
wave: "00"
legal_state: "self_verified"
gate_0: "not_complete"
human_accepted: false
official_version_claim: false
approved_base_commit: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
historical_v3_implementation_checkpoint: "802fb7d244e3751b42dbb20cc8d258e1b71adbc7"
recorded_upstream_product_baseline: "9da0a4ff8b45df03fed073a9af5c00d22aab0d9d"
program_commit: "1d36a51d6ea7d69910463cfc9ab6860cf8c21078"
artifact_commit: "bc5d02c38afc79538ce62c4d28de70a0caeeb044"
revision_commit: "uncommitted_at_write_time"
result_commit: "uncommitted_at_write_time"
branch: "proposal/v4-research-network"
worktree: "C:\\Users\\fores\\Downloads\\CaseLinker-v4-research-network"
protected_refs:
  main: "9da0a4ff8b45df03fed073a9af5c00d22aab0d9d"
  proposal/v3-foundation: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
primary_proof_obligation: "proposed program is based on the actual repository, actual v3 boundaries, and named human decisions"
```

## Completed work (this wave)

- Read applicable `AGENTS.md`, the v4 program, vNext charter/handoff/threat model/adoption/traceability, ADRs 0000–0011, CI, lockfile, tests, and SQLite migrations.
- Pre-worktree revalidation: no material delta.
- Isolated worktree and branch created from the approved base.
- Authorized local environment mutation: uv 0.11.33, CPython 3.12.13, `uv sync --locked --no-extra ml`.
- Pristine-base quality suite run **before** any tracked v4 file existed in the worktree. Logs live outside the repo (session `wave0-baseline`).
- Governing program copied from the home file, hash-verified, v3 untracked copy left in place, committed unchanged as `1d36a51d`.
- Discovery artifacts written (`bc5d02c3`).
- Independent verification failed (documentation/governance). §32 revision applied: byte-store implication corrected; 69-ID registry reconciled; GOV-003 marked `partial`; owners/authorities/gates assigned or blocked; Wave 0 distinguished from Phase 0; findings appended to the evidence packet.

## Test evidence

See `docs/v4/evidence/WAVE-00-EVIDENCE.md`. Distinguish pristine-base, final-state (after artifact commit; recorded externally if this file is already committed), pre-existing, and environment-related.

## Unresolved blockers

- Upstream maintainer disposition of the v3 proposal: **unknown**.
- OD-002…OD-011 in `DECISION_LOG.md` (policy, identity scope, tenancy, infra, verifier identity).
- Windows host: 3 pytest failures classified as environment-related; not repaired in Wave 0.

## Next safe action

Independent Wave 0 verification of the pushed `proposal/v4-research-network` commits. Do not start Wave 1. Do not mark Gate 0 `human_accepted`.

## What this file does not claim

Implemented software contract beyond v3; scientific validity; privacy/legal authorization; operational readiness; maintainer acceptance; official v4.
