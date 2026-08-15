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

## Open decisions (no software default is authority)

| ID | Question | Label | Blocks |
|---|---|---|---|
| OD-001 | Upstream maintainer disposition of the v3 proposal | human decision required; currently **unknown** | official naming, merge, any later “adopted” claim |
| OD-002 | Initial users, organizations, audiences, deployment boundary | human decision required | Phase 3+ and any pilot |
| OD-003 | Governing privacy/disclosure authority and jurisdictions | human decision required | disclosure engine **content** |
| OD-004 | Approved source classes, retention, takedown | human decision required | live or even expanded fixture collection |
| OD-005 | Reviewer roles, qualifications, independence, adjudication | human decision required | authenticated review beyond the current enum |
| OD-006 | Acceptable identity-resolution scope | human decision required | Wave 4 identity work |
| OD-007 | Tenancy model | human decision required | isolation design |
| OD-008 | Acceptable infrastructure and operational environment | human decision required | Wave 8 hardening |
| OD-009 | Pilot corpus and shadow-mode protocol | human decision required | scientific evaluation beyond fixtures |
| OD-010 | Who performs independent Wave 0 verification | human decision required | `gate_ready` recommendation |
| OD-011 | Whether to add a read-only `upstream` remote | human decision required | not in Wave 0 |

No policy, legal rule, reviewer qualification, or numerical quality threshold is recorded as decided.
