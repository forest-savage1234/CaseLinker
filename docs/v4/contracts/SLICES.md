# Wave 1 contract slices

**Status:** Wave 1 `gate_ready`; assurance boundary frozen in `docs/v4/assurance/WAVE-01-ASSURANCE.md`.  
**Not:** Wave 2, Phase 0 complete, official version, live migration, `human_accepted`.

Each slice is independently reviewable. Tests are committed before the contract surface that makes them pass.

| Slice | Coherent behavior | Depends on |
|---|---|---|
| A | Versioned JSON envelope validates or fail-closes; unknown security-sensitive fields rejected | none |
| B | Event time ≠ knowledge time; immutable ids; illegal transitions rejected | A |
| C | Derivation ≠ corroboration; similarity ≠ identity; no blind transitivity | A, B |
| D | Eligibility ≠ disclosure; missing policy version denies; authority is an interface not an IdP | A, B |
| E | Projection ≠ source of truth; audit/AI records cannot publish; Postgres is logical-only | A–D |

ADRs live in `docs/v4/adr/` with `Status: Proposed` so they cannot be mistaken for upstream-accepted `docs/adr/` decisions.
