# Wave 0 risk register

**Kind of document:** proposal-control. Residual risk is not accepted by this file.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Ranking rule (human decision):** product-safety top three are R-ID, R-COR, R-DIS. PostgreSQL concurrency is important but not top three.

Likelihood/impact are **inferences** for planning, not measured rates. Owners listed as “operator / later named role” remain `human decision required` until assigned.

Scale: L = likelihood, I = impact (H/M/L inferences).

## Top-three product-safety risks

### R-ID — Silent false merge of people or events

| Field | Content | Label |
|---|---|---|
| Description | Similarity, shared names, clustering, or transitivity creates a canonical identity or same-event fact | proposal of the failure mode |
| Current evidence | No identity-hypothesis type in `src/caselinker`. Legacy clustering/triage exist. `AttributedSubject` is caller-supplied (`LEGAL_EVENT_METHOD.md`) | repository fact |
| L / I | M / H | inference |
| Detection | false-merge evaluation; review of any merge write path | proposal |
| Prevention | separate candidate generation from acceptance; no automatic canonical person; no A≈B≈C | proposal |
| Recovery | reversible hypothesis states; reopen; preserve negative evidence | proposal |
| Residual | even a careful design can err on ambiguous public text | inference |
| Gate | human identity-scope decision OD-006; later Wave 2 experiment + Wave 4 | human decision required |
| Owner | unassigned | human decision required |

### R-COR — Incomplete dependency invalidation after correction

| Field | Content | Label |
|---|---|---|
| Description | A changed governing claim leaves a Claim Card, cohort, graph, pack, or publication still eligible | proposal of the failure mode |
| Current evidence | Live eligibility covers the resolution that cited a superseded review (ADR 0007). No general `DependencyEdge` / rebuild queue | repository fact |
| L / I | M / H | inference |
| Detection | graph-completeness tests; reconciliation jobs | proposal |
| Prevention | register dependents at creation; fail closed if registry incomplete | proposal |
| Recovery | mark stale; block new disclosure; rebuild successor; keep history | proposal |
| Residual | unknown dependents in legacy UI/exports | inference |
| Gate | later correction wave; not Wave 0 | — |
| Owner | unassigned | human decision required |

### R-DIS — Disclosure bypass on an alternate path

| Field | Content | Label |
|---|---|---|
| Description | A scientifically eligible or internal field exits via serializer, export, log, cache, search, debug, or admin | proposal of the failure mode |
| Current evidence | No PDP/PEP. Evidence Pack excludes source text and disclosure authorization (`evidence_pack.py` 38–42). Threat model says audience policy is mandatory and absent | repository fact |
| L / I | H (once any UI/API is added) / H | inference |
| Detection | alternate-path adversarial tests | proposal |
| Prevention | default deny; enforce at query and again at serialize/export; do not invent policy content | proposal |
| Recovery | revoke; expire; watermark later if policy says so | proposal; policy is human |
| Residual | software cannot invent lawful rules | repository fact of absence + human decision required |
| Gate | OD-003; later Wave 5 | human decision required |
| Owner | unassigned authorized privacy/legal authority | human decision required |

## Other ranked risks

| ID | Class | Summary | Current evidence | L/I | Prevention / recovery (proposal) | Gate |
|---|---|---|---|---|---|---|
| R-SCI | scientific | Selected corpus read as prevalence, causation, or platform danger | `LIMITATIONS` in `claims.py`; other UIs/stats scripts exist | M/H | keep generated claim text; block unsupported claims; independent methods review | later SCI wave; OD-009 |
| R-CH | child-safety | Re-identification or sensational case narrative | charter cohort-first rule; live demo README language | M/H | no live corpus in this program; policy-safe fixtures only | OD-004, OD-009 |
| R-SRC | source authenticity | Bytes substituted; page mutated; deceptive correction | content addressing exists; no mutation monitor | M/H | version every retrieval; quarantine authenticity_uncertain | OD-004 |
| R-AUTH | authorization | `reviewer_id` is an unauthenticated string | `ReviewDecision.reviewer_id` | H/H if review is treated as authority | approved IdP later; do not infer authority from id format | OD-005 |
| R-AI | prompt injection | Hostile source text instructs a model | no vNext AI writer; scrapers/PDF parsers exist | M/H | treat source as data; isolate tools; no secrets in prompts | later AI wave |
| R-MIG | migration | History lost in a future SoR move | SQLite-only vNext; no vNext Postgres ledger | L/H | expand/migrate/contract; rehearsal; no live data now | later; OD-008 |
| R-CON | concurrency | Lost updates or split batches under concurrent review | SQLite tests only; threat model residual | M/M | later Postgres experiment (not top-three product-safety) | Wave 2 technical |
| R-SUP | supply-chain | Vulnerable or unlocked deps | locked `uv.lock`; CI pip-audit/bandit/CodeQL; host Windows ≠ CI Ubuntu | L/H | keep `--locked`; do not broaden exclusions | standing |
| R-OPS | operational | Backup/restore untested; dual stack confusion | no vNext restore drill | M/H | later hardening; do not deploy from this program | OD-008; PROHIB-012 |
| R-GOV | governance | Proposal described as official v4 | no tags; language controls | M/H | proposal identity; upstream only names releases | GOV-001; standing |
| R-TEN | tenancy | Cross-organization leakage if multi-tenant is added later | no tenancy model | n/a until OD-007 | default isolate; test every channel | OD-007 |
| R-FED | federation | Signed package treated as truth or disclosure permission | not implemented | n/a until late | signature = integrity+issuer only | later FED gate |
| R-WIN | evaluation | Windows host fails 3 tests that CI Ubuntu may pass | pristine pytest 374/377 | L/M | classify as environment block; do not weaken tests | independent Ubuntu verify |
| R-LEG | competing truth | Legacy mutable cases / scrapers / RDF pools | present in repo | M/H | do not silently replace; do not extend scrapers | containment |

## Risks this program will not “fix” in Wave 0

Wave 0 only records. Containment that would change product code is out of scope. High-severity items without an owner stay open (`human decision required`).
