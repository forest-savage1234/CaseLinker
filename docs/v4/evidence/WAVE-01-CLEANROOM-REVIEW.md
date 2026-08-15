# Wave 1 clean-room review of `ac52ab84`

**Reviewed implementation:** `ac52ab84dead1ef5aebd74e0291c01bca0b461d5`  
**Process freeze:** `635c8f17317d5ad9dacf6b35a2f78502a0b9af46`  
**Boundary:** `docs/v4/assurance/WAVE-01-ASSURANCE.md`  
**Reviewer:** same-model Grok plan agent (worktree-isolated, read-only). Not organizational independence. Did not implement r3/r4 in that conversation.  
**Gates:** not re-executed by the reviewer. Builder evidence at `7521bfb8` stands as complementary.  
**Disposition recommended:** `gate_ready`  
**Later human disposition:** `review_invalid` (D-2026-08-15-023). `gate_ready` withdrawn.  
**Wave 2:** must not begin until explicit human acceptance.

This file is the independent-review record for D-2026-08-15-020. It does not implement product changes.

## Stage 1 verdict

`ac52ab84` satisfies the frozen Wave 1 assurance contract at the stated interface floor. No traceable critical/high defect was found inside that boundary.

The five distinctions hold at the contract layer. Allegation≠guilt is only negatively demonstrated (no guilt type added; v3 extractors unchanged).

## Traceable critical / high findings

None.

## Medium / low residual

| ID | Severity | Item | Owner |
|---|---|---|---|
| M1 | Medium | SoD governance id required on every transition, including when SoD is false | tracking operator; OD-005 |
| M2 | Medium | Allegation≠guilt has no v4 executable test | tracking operator |
| M3 | Low | Leftover weaker `identity-hypothesis-v1` | Wave 4 / OD-006 |
| M4 | Low | Transition tables live in Python, not the schema | later hardening |
| M5 | Low | Unknown invariant names ignored | later hardening |
| M6 | Low | No inverted-window invalid fixture on the request | later hardening |
| M7 | Process | Reviewer did not rerun gates | human gate owner / CI |
| M8 | Standing | R-ID, R-COR, R-DIS named not closed; OD-003/005/006/008 blocked | named authorities |

## Later-wave (not blockers)

Live PDP/PEP and three views; authenticated reviewers and which transitions need SoD; operational identity resolution; correction-impact kernel; richer compatibility; production infrastructure.

## Ambiguities (do not block the wave)

How much of program §7.8 is the W1-N5 floor; whether allegation≠guilt needs a v4 claim-status contract; whether every transition must carry SoD governance ids.

## Premature specification

r3/r4 pulled Wave 5 disclosure/SoD shape forward. That is why escalation §6 is active. Further refinement of those records does not, by itself, prevent `gate_ready`. No r5 is authorized.
