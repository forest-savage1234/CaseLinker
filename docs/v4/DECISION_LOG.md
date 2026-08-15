# Wave 0 decision log

**Kind of document:** proposal-control.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Statement labels:** `repository fact` | `inference` | `proposal` | `human decision required`

Later waves append. Do not erase. Software does not convert conservative defaults into policy authority.

## D-2026-08-15-001 — Approve Wave 0 discovery only

- **Label:** human decision required (decided)
- **Decision:** Execute Wave 0 only. No product code, schema, migration, CI, tag, release, deployment, live-data migration, publication, or Wave 1.
- **Authority:** operator binding approval of the Wave 0 plan
- **Consequence:** control-plane documents under `docs/v4/` plus one authorized later push of this branch

## D-2026-08-15-002 — v4 base commit

- **Label:** human decision required (decided)
- **Decision:** Start from `4a17a9e5fdf74057de08a819291bf1606b8e3b45`.
- **Rationale recorded by operator:** commits after historical checkpoint `802fb7d2` are verified CI and handoff corrections and must not be discarded.
- **Not decided:** official upstream adoption of those commits
- **Note:** `802fb7d2` remains the v3 M07 implementation checkpoint in `docs/vnext/traceability.v1.json`. That field is not rewritten in Wave 0.

## D-2026-08-15-003 — Isolated workspace

- **Label:** human decision required (decided)
- **Decision:** Branch `proposal/v4-research-network`; worktree `C:\Users\fores\Downloads\CaseLinker-v4-research-network`.
- **Constraints:** do not alter `main` or `proposal/v3-foundation`; copy (do not move or delete) the governing program from the home file; leave the v3 untracked copy untouched.
- **Hash required:** SHA-256 `1F0B496DD38FFD35F3CFB9F8F83B27AFA8DB1EAA4A04177A544165D72AB01A33`

## D-2026-08-15-004 — Local environment mutation authorized

- **Label:** human decision required (decided)
- **Decision:** Installing uv 0.11.33, CPython 3.12, project lock sync, and a local `.venv` is an authorized **environment mutation**.
- **Not authorized:** presenting those installs as non-mutating repository checks

## D-2026-08-15-005 — Sole authorized remote write

- **Label:** human decision required (decided)
- **Decision:** After self-verification, push only `proposal/v4-research-network` to `origin`.
- **Forbidden:** PR, tag, release, deploy, publish, write to upstream, alter `main` or `proposal/v3-foundation`

## D-2026-08-15-006 — Highest product-safety risks

- **Label:** human decision required (decided)
- **Decision:** Rank as highest:
  1. reversible identity and same-event resolution without silent false merges;
  2. complete dependency invalidation and correction propagation;
  3. default-deny disclosure enforcement across every output path.
- **Not ranked in the top three:** PostgreSQL invariant enforcement (later technical experiment)

## D-2026-08-15-007 — Vertical slice status

- **Label:** human decision required (decided)
- **Decision:** The program’s two-source/two-reviewer twelve-step path is a synthetic experimental hypothesis only.
- **Not decided:** reviewer policy, production workflow, or corpus authorization

## D-2026-08-15-008 — Statement labeling

- **Label:** human decision required (decided)
- **Decision:** Every material Wave 0 statement is `repository fact`, `inference`, `proposal`, or `human decision required`.

## D-2026-08-15-009 — Wave 0 verification revision

- **Label:** human decision required (decided)
- **Decision:** Apply `GROK_BUILD_PROGRAM.md` §32. Correct documentation/governance findings only. Do not begin Wave 1 or modify product code.
- **Authority:** operator revision instruction after independent verification failed
- **Consequence:** replace false byte-store implication; complete the 69-ID registry with one bucket each; mark GOV-003 `partial`; assign owner / decision authority / blocking gate or `blocked`; complete phase-gate fields; distinguish Wave 0 artifact acceptance from Phase 0; append findings to the evidence packet without erasure

## D-2026-08-15-010 — Wave 0 documentation completion

- **Label:** human decision required (decided)
- **Decision:** Documentation-only revision: add a program-section crosswalk (IDs may aggregate); add REVIEW-005, OPS-006, OPS-007, EVAL-001; write conceptual Gate 0 architecture flows; do not invent policy or thresholds.
- **Authority:** operator instruction after further Wave 0 review
- **Consequence:** `REQUIREMENTS_TRACEABILITY.md` crosswalk + 73 IDs; `architecture/GATE0_PROPOSAL.md`; evidence buckets reconciled to 0/42/31

## Ownership convention

- **Accountable owner:** person or role who must keep the item visible and stop dependent work. Until a specialist is named, the Wave 0 program operator (this fork’s operator) is the tracking owner only.
- **Decision authority:** who may decide the substance. If unnamed, the item is **blocked**.
- **Blocking gate:** earliest wave/phase that must not start, or must not be marked complete, until the decision exists.
- Software defaults are not authority.

## Open decisions (no software default is authority)

| ID | Question | Accountable owner | Decision authority | Blocking gate | Status |
|---|---|---|---|---|---|
| OD-001 | Upstream maintainer disposition of the v3 proposal | program operator (tracking) | upstream maintainer (`mrinaalr`) — named by charter, not yet recorded as responding | any official naming, merge, or “adopted” claim; Phase 0 exit | **blocked** (disposition **unknown**) |
| OD-002 | Initial users, organizations, audiences, deployment boundary | program operator (tracking) | unassigned organizational sponsor | Phase 3 / Wave 5 entry; any pilot | **blocked** |
| OD-003 | Governing privacy/disclosure authority and jurisdictions | program operator (tracking) | unassigned authorized privacy/legal authority | Wave 5 / Gate 3; DISCLOSE-002/003 content | **blocked** |
| OD-004 | Approved source classes, retention, takedown | program operator (tracking) | unassigned source-governance / legal authority | live or expanded collection; SOURCE-002 | **blocked** |
| OD-005 | Reviewer roles, qualifications, independence, adjudication | program operator (tracking) | unassigned review-governance authority | Wave 5 authenticated review | **blocked** |
| OD-006 | Acceptable identity-resolution scope | program operator (tracking) | unassigned child-safety + scientific authority | Wave 4 / Gate 2; R-ID | **blocked** |
| OD-007 | Tenancy model | program operator (tracking) | unassigned organizational sponsor (same as OD-002 unless split) | OPS-004; Wave 8 tenant tests | **blocked** |
| OD-008 | Acceptable infrastructure and operational environment | program operator (tracking) | unassigned infrastructure/operations authority | Wave 8 / Gate 6; object store, Postgres production claim | **blocked** |
| OD-009 | Pilot corpus and shadow-mode protocol | program operator (tracking) | unassigned scientific + disclosure authority | Wave 7; Phase 0 “approved pilot” | **blocked** |
| OD-010 | Who performs independent Wave 0 verification | program operator (tracking) | program operator may **request**; `gate_ready` requires an independent reviewer to be named | Wave 0 `gate_ready`; Wave 1 must not start | **blocked** until a named independent reviewer records a pass |
| OD-011 | Whether to add a read-only `upstream` remote | program operator (tracking) | program operator (local git config only); does not create upstream authority | not required for Wave 0; optional later | open, not blocking Wave 0 re-verification |

No policy, legal rule, reviewer qualification, or numerical quality threshold is recorded as decided.
