# Wave 0 assumptions

**Kind of document:** proposal-control. Not policy. Not an official CaseLinker release.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Program commit:** `1d36a51d6ea7d69910463cfc9ab6860cf8c21078`  
**Statement labels:** `repository fact` | `inference` | `proposal` | `human decision required`

An assumption is not a fact and not an approval. It is retired only by a cited repository fact, an executed experiment with a falsification record, or a named entry in `DECISION_LOG.md`.

## A. Environment and repository

| ID | Statement | Label | Evidence / owner | Disposition |
|---|---|---|---|---|
| A-ENV-001 | Wave 0 uses worktree `C:\Users\fores\Downloads\CaseLinker-v4-research-network` on branch `proposal/v4-research-network`. | repository fact | `git worktree list`; `git rev-parse --abbrev-ref HEAD` | closed for this wave |
| A-ENV-002 | Host default Python 3.14.2 is outside `requires-python = ">=3.11,<3.14"`. | repository fact | `pyproject.toml` lines 5–6 | closed: CPython 3.12.13 via uv |
| A-ENV-003 | uv 0.11.33, CPython 3.12.13, and a worktree `.venv` were installed on this host. That is a local environment mutation, not a product change. | repository fact | installer output; `.gitignore` line 32 | closed |
| A-ENV-004 | Recorded CI quality jobs run on `ubuntu-latest` with Python 3.12. Windows is not the recorded CI platform. | repository fact | `.github/workflows/quality.yml` lines 20–36 and 90–102 | closed |
| A-ENV-005 | Three fast-suite failures on this Windows host are environment-related, not Wave 0 regressions. | inference | pristine-base pytest at `4a17a9e5` before any v4 file; see `docs/v4/evidence/WAVE-00-EVIDENCE.md` | open until independently reproduced on Ubuntu or dismissed |
| A-ENV-006 | No `upstream` git remote to `mrinaalr/CaseLinker` is configured. Only `origin` = `forest-savage1234/CaseLinker.git`. | repository fact | `git remote -v` | open; adding a remote is not in Wave 0 |
| A-ENV-007 | The Grok session workspace is `C:\Users\fores`. Wave 0 git and quality commands ran only in the CaseLinker worktree. | repository fact | session workspace; worktree path | closed |

## B. Authority and identity

| ID | Statement | Label | Evidence / owner | Disposition |
|---|---|---|---|---|
| A-GOV-001 | Upstream `mrinaalr/CaseLinker` retains official naming, merge, tag, and production authority. | repository fact | `AGENTS.md` lines 3–5; `docs/adr/0000-vnext-governance-and-versioning.md`; `docs/vnext/ENGINEERING_CHARTER.md` §2 | standing |
| A-GOV-002 | This work is a research-network **proposal**. It is not CaseLinker v4.0.0. | human decision required | operator binding instruction; `docs/v4/GROK_BUILD_PROGRAM.md` §0 and §2.15 | standing |
| A-GOV-003 | Upstream has not recorded a disposition of the v3 proposal. | repository fact | no maintainer decision file; `docs/vnext/DRAFT_PULL_REQUEST.md` is a draft | open; disposition = **unknown** |
| A-GOV-004 | The approved v4 starting commit is `4a17a9e5`, including the four post-`802fb7d2` CI/handoff commits. `802fb7d2` remains only the historical v3 M07 checkpoint. | human decision required | operator binding decision 1 | closed for Wave 0 |
| A-GOV-005 | `proposal/v3-foundation` and `main` must remain unmodified. The untracked v3-tree program copy must remain. | human decision required | operator binding decisions 2 and 11 | standing |

## C. Scientific and safety

| ID | Statement | Label | Evidence / owner | Disposition |
|---|---|---|---|---|
| A-SCI-001 | Public-enforcement records are a selected corpus, not a population denominator. | repository fact | `docs/vnext/ENGINEERING_CHARTER.md` §4.5; `src/caselinker/analysis/claims.py` `LIMITATIONS` lines 12–21 | standing invariant |
| A-SCI-002 | Research eligibility is not disclosure authorization. | repository fact | ADR 0007 “Distinct decisions”; `src/caselinker/resolution/publication.py` lines 37–38; `evidence_pack.py` lines 38–42 | standing invariant |
| A-SCI-003 | Caller-supplied `AttributedSubject` aliases are matching inputs, not resolved person identities. | repository fact | `docs/vnext/LEGAL_EVENT_METHOD.md`; `src/caselinker/extraction/legal_events.py` `AttributedSubject` | standing |
| A-SCI-004 | No authorized reviewer qualification, independence, or two-person-control policy exists in-repo. | repository fact | `docs/vnext/THREAT_MODEL.md` “Required deployment controls”; `ReviewerRole` enum only at `assertions/models.py` lines 79–82 | human decision required |
| A-SCI-005 | No authorized disclosure policy content, jurisdiction, audience, or retention schedule exists in-repo. | repository fact | threat model residual risks; no policy package under `src/caselinker` | human decision required |
| A-SCI-006 | Any two-source/two-reviewer slice is a synthetic experimental hypothesis, not an authorized workflow or corpus decision. | human decision required | operator binding decision 8 | standing |

## D. Architecture (must not be treated as selected products)

| ID | Statement | Label | Evidence / owner | Disposition |
|---|---|---|---|---|
| A-ARCH-001 | vNext authoritative persistence today is SQLite with abort-on-update/delete triggers. | repository fact | `migrations/sqlite/0001_source_documents.sql`, `0002_assertion_ledger.sql`, `0003_assertion_review_lineage.sql`; ADR 0004 | standing description of current code |
| A-ARCH-002 | Legacy `src/Storage Layer/storage_postgres.py` is a mutable case-row store, not the vNext ledger. | repository fact | file header; ADR 0002 context | standing |
| A-ARCH-003 | PostgreSQL as a future transactional system of record is a program proposal, not an accepted ADR. | proposal | `docs/v4/GROK_BUILD_PROGRAM.md` §6.1 | deferred to a later ADR + technical experiment |
| A-ARCH-004 | Graph, search, Claim Cards, and Evidence Packs are rebuildable projections, not sources of truth. | repository fact | ADR 0008; charter §6 item 8; program CONST-016 | standing |
| A-ARCH-005 | Assertions have `valid_from` / `valid_to` and `created_at` but no proven as-known/valid-time query contract. | repository fact | `src/caselinker/assertions/models.py` lines 251–258; `migrations/sqlite/0002_assertion_ledger.sql` lines 11–12, 22 | gap |
| A-ARCH-006 | No first-class identity-hypothesis, source-family, dependency-edge, or disclosure-decision types exist in `src/caselinker`. | repository fact | package listing; search of `src/caselinker` | gap |

## E. Explicitly not assumed

The following remain `human decision required` unless a named authority later records them:

- live privacy law, organizational policy, or lawful basis
- reviewer credentials or staffing
- production topology, RPO/RTO, or cloud vendor
- identity-resolution purpose beyond research-integrity
- tenancy / multi-organization model
- approved source classes, retention, or takedown process
- any numerical accuracy, performance, or “v4 readiness” threshold
- that the Windows host failures would also fail on CI Ubuntu
