# W1-010: Freeze Wave 1 assurance boundary and pause further patching

- **Status:** Proposed
- **Scope:** CaseLinker v4 research-network proposal only
- **Upstream:** not accepted
- **Authority:** operator strategy adoption 2026-08-15 (D-2026-08-15-019)

## Context

Wave 1 was approved as “formal contracts before infrastructure” (`GROK_BUILD_PROGRAM.md` §21; D-2026-08-15-013). Four consecutive verification/repair cycles (through r4 on `ac52ab84`) then repeatedly restructured the disclosure-decision and state-transition contracts.

`STRATEGY.md` §3.5 and §6 require a pause when successive repairs change the meaning of the same contract. The next action is not automatically another local patch.

W1-009 records the r4 authority-binding repair as history. This ADR freezes the original Wave 1 boundary.

## Decision

1. Adopt `docs/v4/STRATEGY.md` as the delivery method beside the governing program.
2. Freeze Wave 1 acceptance in `docs/v4/assurance/WAVE-01-ASSURANCE.md`.
3. Map every exit requirement in `WAVE-01-REQUIREMENTS-MAP.md`.
4. Keep Wave 1 at `self_verified` on `ac52ab84`. Do not implement r5. Do not start Wave 2. Do not mark `gate_ready` from this ADR.
5. Commission a clean-room review of `ac52ab84` against the frozen §21 + D-013 boundary.
6. A blocking finding must name its governing basis. Ambiguity is `program_clarification_required`.

## Consequences

Further disclosure or SoD fields are later-wave or require an explicit, accepted boundary amendment. Repair ADRs W1-006…W1-009 remain historical.
