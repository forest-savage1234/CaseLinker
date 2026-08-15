# WAVE-00 evidence packet

Revised after independent verification failed. Original narrative §§1–8 is preserved. Original YAML as of `bc5d02c3` is copied in §9. Do not treat this file as Gate 0 acceptance.

```yaml
wave: "00"
status: "self_verified"
approved_base_commit: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
program_commit: "1d36a51d6ea7d69910463cfc9ab6860cf8c21078"
prior_artifact_commit: "bc5d02c38afc79538ce62c4d28de70a0caeeb044"
result_commit: "uncommitted"
primary_proof_obligation: "demonstrate that the proposed program is based on the actual repository, actual v3 boundaries, and named human decisions rather than assumptions"
requirements_closed: []
requirements_partially_met:
  - CONST-001
  - CONST-002
  - CONST-003
  - CONST-004
  - CONST-005
  - CONST-006
  - CONST-007
  - CONST-008
  - CONST-009
  - CONST-010
  - CONST-011
  - CONST-012
  - CONST-013
  - CONST-015
  - CONST-016
  - CONST-017
  - CONST-018
  - PROHIB-001
  - PROHIB-002
  - PROHIB-005
  - PROHIB-006
  - PROHIB-007
  - PROHIB-008
  - PROHIB-010
  - PROHIB-012
  - PROHIB-013
  - TEMP-001
  - TEMP-003
  - SOURCE-001
  - SOURCE-003
  - REVIEW-002
  - DISCLOSE-001
  - CORRECT-001
  - CORRECT-002
  - CORRECT-003
  - SCI-001
  - SCI-003
  - GOV-001
  - GOV-002
  - GOV-003
requirements_unmet:
  - CONST-014
  - PROHIB-003
  - PROHIB-004
  - PROHIB-009
  - PROHIB-011
  - TEMP-002
  - SOURCE-002
  - RESOLVE-001
  - RESOLVE-002
  - RESOLVE-003
  - RESOLVE-004
  - RESOLVE-005
  - REVIEW-001
  - REVIEW-003
  - REVIEW-004
  - DISCLOSE-002
  - DISCLOSE-003
  - DISCLOSE-004
  - SCI-002
  - AI-001
  - AI-002
  - OPS-001
  - OPS-002
  - OPS-003
  - OPS-004
  - OPS-005
  - FED-001
  - UX-001
  - UX-002
adrs: []
migrations: []
schemas: []
implementation: []
tests: []
commands_executed:
  - "pre-worktree git revalidation (PowerShell)"
  - "git worktree add -b proposal/v4-research-network <path> 4a17a9e5"
  - "uv 0.11.33 install (environment mutation)"
  - "uv python install 3.12 (environment mutation)"
  - "uv sync --locked --no-extra ml (environment mutation)"
  - "pristine-base quality suite (see below)"
  - "Copy-Item home GROK_BUILD_PROGRAM.md; Get-FileHash SHA256"
  - "git commit program only → 1d36a51d"
expected_results:
  - "pristine suite matches Ubuntu CI on a POSIX host"
  - "Windows host may fail symlink and path-separator tests"
actual_results:
  - "see §2 pristine-base table"
determinism_evidence:
  - "two snapshot builds compared equal; digest 086ba58ad10123f45e56b85ac5464cfce07de21cbd5d01921913ccc0ec33c4fd"
security_evidence:
  - "pip-audit: no known vulnerabilities (pristine)"
  - "bandit -lll: exit 0 (pristine)"
privacy_evidence:
  - "no live corpus accessed"
  - "no policy content invented"
scientific_evidence:
  - "v3 claim limitations and legal_event unit cited from source"
  - "no new scientific claim asserted as validated"
operational_evidence:
  - "toolchain install recorded as environment mutation"
  - "main and proposal/v3-foundation not modified"
known_limitations:
  - "Wave 0 is documentation and planning only"
  - "Windows pytest 3-failure environment block"
  - "upstream disposition unknown"
residual_risks:
  - "R-ID"
  - "R-COR"
  - "R-DIS"
  - "R-GOV communication drift"
  - "R-WIN"
rollback_tested: false
independent_review_status: "not_started"
prior_independent_review_status: "fail"
human_decisions_required:
  - "OD-001 upstream disposition (unknown, blocked)"
  - "OD-002..OD-010 blocked pending named authorities"
  - "OD-011 optional, not blocking Wave 0 re-verification"
```

## 1. Proof obligation

Wave 0 must show the program is grounded in this repository and in named human decisions. It must not implement the temporal kernel, invent policy, or claim Gate 0 acceptance.

## 2. Pristine-base baseline

**Classification:** repository/product checks are read-only with respect to tracked product content. uv/Python/venv are **environment mutations**.

**When:** after worktree creation, **before** any tracked v4 file existed in the worktree.  
**HEAD then:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Working tree then:** clean (`git status` showed only `## proposal/v4-research-network`).  
**Logs:** `C:\Users\fores\.grok\sessions\C%3A%5CUsers%5Cfores\01a00645-5c6c-76a3-b8dc-1e31c8d483cb\wave0-baseline\` (outside the repository).

| Step | Command (intent) | Exit | Classification |
|---|---|---|---|
| 01 | `uv run --locked --no-extra ml python scripts/quality/check_repository.py` | 0 | pristine pass — “repository check passed for 8523 tracked file(s)” |
| 02 | `check_traceability.py` | 0 | pristine pass — “traceability check passed for 7 milestone(s)” |
| 03 | `ruff check` (strict proposal surface) | 0 | pristine pass |
| 04 | `ruff format --check` | 0 | pristine pass — “59 files already formatted” |
| 05 | `mypy` (34 files) | 0 | pristine pass |
| 06 | `pytest tests/quality tests/unit tests/integration tests/contract --cov=...` | 1 | **environment-related block** — 374 passed, 3 failed, coverage 95.77% |
| 07–08 | snapshot `build` ×2 to `%TEMP%` files | 0 | pristine pass |
| 09 | byte compare of the two snapshots | 0 | pristine pass — `FC: no differences encountered` (cmd `fc` used on the pristine run) |
| 10 | snapshot `verify` | 0 | pristine pass |
| 11 | `CASELINKER_DISABLE_MCP=1 pytest -m smoke` | 0 | pristine pass — 2 passed |
| 12 | `pip-audit --local --skip-editable` | 0 | pristine pass — “No known vulnerabilities found” |
| 13 | `bandit -q -lll -r` strict surface | 0 | pristine pass |

### 2.1 Environment-related pytest failures (not Wave 0 regressions)

Observed on the **pristine** approved base on Windows before any v4 documents existed. Not repaired.

1. `tests/quality/test_repository_checker.py::test_finding_renders_relative_and_external_paths`  
   Expected ` /outside.py: test: detail`; observed `\outside.py: test: detail`.
2. `tests/unit/snapshots/test_manifest.py::test_symlink_input_is_rejected`  
   `OSError: [WinError 1314] A required privilege is not held by the client` creating a symlink.
3. `tests/contract/analysis/test_claim_pipeline_cli.py::test_stale_manifest_and_unbound_projection_are_rejected`  
   Expected message `not bound to the snapshot outputs`; actual `projection is not canonical N-Triples` on a Windows temp path after rewrite.

**inference:** these are host-platform assumptions versus Ubuntu CI (`.github/workflows/quality.yml` `runs-on: ubuntu-latest`). They are not evidence that v3 invariants failed, and they are not evidence that Wave 0 broke tests.

**pre-existing vs environment:** they are environment-related relative to this host. Whether they fail on Ubuntu was not executed here.

## 3. Program copy and first commit

- Source: `C:\Users\fores\docs\v4\GROK_BUILD_PROGRAM.md`
- Destination: worktree `docs/v4/GROK_BUILD_PROGRAM.md`
- SHA-256 (home, dest, and leftover v3 untracked copy): `1F0B496DD38FFD35F3CFB9F8F83B27AFA8DB1EAA4A04177A544165D72AB01A33`
- v3 working tree: still `proposal/v3-foundation` at `4a17a9e5` with untracked `docs/v4/GROK_BUILD_PROGRAM.md` (not deleted)
- Commit: `1d36a51d6ea7d69910463cfc9ab6860cf8c21078` — `docs(v4): add governing research-network program unchanged`  
  Parent: `4a17a9e5`. Diff: one file, 1413 insertions.

## 4. Discovery artifacts

Written after the program commit. Cited v3 facts point at paths and (where practical) line ranges in `CURRENT_STATE.md`, `REQUIREMENTS_TRACEABILITY.md`, and ADRs. Future architecture is labeled `proposal` or `human decision required`.

Highest-risk assumptions (human-ranked; experiments **not** run):

1. Reversible identity / same-event resolution without silent false merges.
2. Complete dependency invalidation and correction propagation.
3. Default-deny disclosure on every output path.

PostgreSQL invariant enforcement is recorded as a later technical experiment only.

The two-source/two-reviewer slice is recorded only as a synthetic experimental hypothesis.

## 5. Final-state validation

Executed after the discovery-artifact commit. Results are summarized in the operator-facing Wave 0 report (external to this file if this file is already part of that commit). Classification rule:

- same 3 Windows failures as pristine → environment-related, not introduced
- new failures in `docs/v4` UTF-8/merge-marker checks → Wave 0 introduced
- product-code failures not seen at pristine → stop and report

## 6. Self-review

Checked for:

- omitted CONST/PROHIB IDs — registry contains CONST-001…018 and PROHIB-001…013
- assumptions presented as facts — assumptions file labels them
- policy assigned to software — OD-003/005 remain human
- competing sources of truth — called out; not “fixed” in code
- missing temporal / correction / identity / disclosure / tenancy boundaries — named as gaps
- release-language — proposal identity used; no tag
- baseline claims — tied to executed pristine logs

No high-severity finding was silently repaired in product code.

## 7. Independent review

`not_started`. Requested after `origin/proposal/v4-research-network` is pushed. Wave 0 does not mark `gate_ready` or Gate 0 complete.

## 8. Rollback

Delete or abandon `proposal/v4-research-network`. `main` and `proposal/v3-foundation` are unmodified. No schema or data migration occurred. `rollback_tested: false` because there is no persistent product state to restore.

## 9. Independent verification findings and disposition (appended; original §§1–8 not erased)

**Prior independent review:** `fail` (high-severity documentation and governance findings).  
**Protocol:** `docs/v4/GROK_BUILD_PROGRAM.md` §32.  
**Product code:** not modified. **Wave 1:** not started.

### 9.1 Packet header as of `bc5d02c38afc79538ce62c4d28de70a0caeeb044` (preserved)

```yaml
wave: "00"
status: "self_verified"
approved_base_commit: "4a17a9e5fdf74057de08a819291bf1606b8e3b45"
program_commit: "1d36a51d6ea7d69910463cfc9ab6860cf8c21078"
result_commit: "uncommitted"
requirements_closed: []
# original lists omitted CONST-007, CONST-014, CONST-015, GOV-003,
# and all PROHIB IDs except a non-ID note "many PROHIB containment items"
independent_review_status: "not_started"
```

Full original lists remain in git blob `bc5d02c3:docs/v4/evidence/WAVE-00-EVIDENCE.md`.

### 9.2 Findings, confirmation, smallest correction

| ID | Finding | Confirm / challenge | Violated requirement | Correction | Migration / privacy / rollback | Tests |
|---|---|---|---|---|---|---|
| F1 | `DATA_AUTHORITY.md` implied exact source bytes have an authoritative store (“restore from object bytes matching digest”) | **Confirmed.** ADR 0002 stores metadata only; `capture()` hashes in-memory bytes (`documents/models.py` 180–204). No object-store port. | CONST-002, SOURCE-001 (identity ≠ bytes), OPS-002 | Rewrite the bytes row: store = **none implemented**; `storage_key` is a name; restore is **not** possible | docs only; no schema change | documentation/final validation; no product test added (Wave 0 forbids product code) |
| F2 | Requirements registry missing required fields; IDs split or omitted from evidence buckets | **Confirmed.** Domain tables lacked the nine fields; YAML omitted CONST-007/014/015, GOV-003, and PROHIB-001…013 as IDs; some rows had dual statuses. | GOV-003; §5.B; §18.4 | Full nine-field matrix; one status; 0/40/29 bucket split | docs only | registry count 69 = 0+40+29 |
| F3 | GOV-003 treated as Wave 0 complete because a registry file exists | **Confirmed.** No machine validator exists (`check_traceability.py` covers vNext only). | GOV-003, §18.4 | Status `partial`; bucket `partially_met`; not closed | docs only | none (checker remains a later proposal) |
| F4 | Risks and open decisions lacked accountable owner, decision authority, and blocking gate | **Confirmed.** Owners were “unassigned”; several gates were “—”. | GOV-002; §5.D–E | Role-based tracking owner + named-or-blocked decision authority + blocking gate on every OD and risk | docs only; does not invent policy authority | none |
| F5 | Phase-gate fields incomplete; Wave 0 acceptance conflatable with Phase 0 | **Confirmed.** Waves 1–10 table omitted migration/rollback/tests/exit/review burden. Phase 0 exit (approved pilot, named owners) was not distinguished. | §5.F; §10 Phase 0 | Complete phase skeletons; explicit Wave 0 ≠ Phase 0 table | docs only | none |
| F6 | Evidence packet did not record independent findings | **Confirmed** at `bc5d02c3` (`independent_review_status: not_started`). | §18.3; §32.8 | This section; prior header preserved; review marked `fail` then new cycle `not_started` | docs only | none |

No finding was challenged. No product implementation was in scope, so §32 step 5 (failing product test first) does not apply; the regression control is the revised documents plus the 69-ID reconciliation.

### 9.3 Revision validation (run on dirty docs, before this correction commit)

Session logs: `wave0-revision`. Same classification as the prior final-state run.

| Check | Exit | Classification |
|---|---|---|
| `check_repository.py` | 0 | pass (docs UTF-8/merge-marker clean) |
| `check_traceability.py` | 0 | pass (vNext 7 milestones unchanged) |
| ruff / mypy | 0 | pass |
| pytest quality+unit+integration+contract | 1 | **environment-related**, same 3 Windows tests as pristine |
| snapshot build ×2 + hash + verify | 0 | pass; tool digest still `086ba58ad10123f45e56b85ac5464cfce07de21cbd5d01921913ccc0ec33c4fd` |
| smoke | 0 | pass (2) |
| pip-audit / bandit `-lll` | 0 | pass |

No product-code diff. No new test failure class.

