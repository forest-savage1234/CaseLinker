# Wave 0 risk register

**Kind of document:** proposal-control. Residual risk is not accepted by this file.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**Ranking rule (human decision):** product-safety top three are R-ID, R-COR, R-DIS. PostgreSQL concurrency is important but not top three.

Likelihood/impact are **inferences** for planning, not measured rates.

Ownership convention matches `DECISION_LOG.md`: tracking owner vs decision authority. If decision authority is unnamed, **Status = blocked**.

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
| Accountable owner | program operator (tracking) | human decision required |
| Decision authority | unassigned child-safety + scientific authority (OD-006) | **blocked** |
| Blocking gate | Wave 4 / Gate 2 must not start without OD-006 | human decision required |
| Status | **blocked** | |

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
| Accountable owner | program operator (tracking) | human decision required |
| Decision authority | program operator may authorize **fixture-only** kernel experiments; production correction policy remains unassigned | blocked for any non-fixture claim |
| Blocking gate | Wave 3 may design fixture invalidation; Wave 6 / Gate 4 cannot close without demonstrated completeness | — |
| Status | tracked; **blocked** for production-scope claims | |

### R-DIS — Disclosure bypass on an alternate path

| Field | Content | Label |
|---|---|---|
| Description | A scientifically eligible or internal field exits via serializer, export, log, cache, search, debug, or admin | proposal of the failure mode |
| Current evidence | No PDP/PEP. Evidence Pack excludes source text and disclosure authorization (`evidence_pack.py` 38–42). Threat model says audience policy is mandatory and absent | repository fact |
| L / I | H (once any UI/API is added) / H | inference |
| Detection | alternate-path adversarial tests | proposal |
| Prevention | default deny; enforce at query and again at serialize/export; do not invent policy content | proposal |
| Recovery | revoke; expire; watermark later if policy says so | proposal; policy is human |
| Residual | software cannot invent lawful rules | repository fact of absence |
| Accountable owner | program operator (tracking) | human decision required |
| Decision authority | unassigned authorized privacy/legal authority (OD-003) | **blocked** |
| Blocking gate | Wave 5 / Gate 3; no disclosure **content** in code | human decision required |
| Status | **blocked** | |

## Other ranked risks

| ID | Class | Summary | L/I | Detection | Prevention / recovery | Residual | Accountable owner | Decision authority | Blocking gate | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-SCI | scientific | Selected corpus read as prevalence, causation, or platform danger | M/H | claim-text review; UI audit | keep generated claim text; block unsupported claims | other UIs remain | program operator (tracking) | unassigned methods reviewer (OD-009) | Wave 7 / Gate 5 | **blocked** for any study beyond fixtures |
| R-CH | child-safety | Re-identification or sensational case narrative | M/H | export/redaction review | no live corpus in this program; fixtures only | README live-demo language | program operator (tracking) | unassigned child-safety + legal (OD-004, OD-003) | any non-fixture corpus | **blocked** |
| R-SRC | source authenticity | Bytes substituted; page mutated; no byte store to restore | M/H | digest mismatch if bytes are later supplied | do not claim a store exists; version every future retrieval | unrestorable today | program operator (tracking) | unassigned source-governance (OD-004, OD-008) | live collection; OPS-002 | **blocked** |
| R-AUTH | authorization | `reviewer_id` is an unauthenticated string | H/H if treated as authority | audit of review writes | do not infer authority from id format | anyone can mint an id in tests | program operator (tracking) | unassigned review-governance (OD-005) | Wave 5 | **blocked** |
| R-AI | prompt injection | Hostile source text instructs a model | M/H | prompt/egress review | treat source as data; isolate tools | scrapers/PDF parsers exist | program operator (tracking) | program operator for “no new AI path”; unassigned AI-governance for any model use | any AI assistance wave | **blocked** for model use |
| R-MIG | migration | History lost in a future SoR move | L/H | rehearsal diffs | expand/migrate/contract; no live data now | no vNext Postgres ledger | program operator (tracking) | unassigned infrastructure (OD-008) | any SoR migration | **blocked** |
| R-CON | concurrency | Lost updates under concurrent review | M/M | later Postgres experiment | do not treat SQLite tests as isolation proof | threat-model residual | program operator (tracking) | program operator for experiment design; OD-008 for production | Wave 2 technical experiment; Wave 8 for production claim | tracked; production claim **blocked** |
| R-SUP | supply-chain | Vulnerable or unlocked deps | L/H | pip-audit, CodeQL, Dependabot | keep `--locked`; do not broaden exclusions | host Windows ≠ CI Ubuntu | program operator | program operator (lockfile/CI hygiene) | standing; Wave 0 re-verification | tracked, not blocked |
| R-OPS | operational | Backup/restore untested; dual stack | M/H | restore drill | do not deploy from this program | no vNext restore | program operator (tracking) | unassigned operations (OD-008) | Wave 8 / Gate 6; PROHIB-012 | **blocked** |
| R-GOV | governance | Proposal described as official v4 | M/H | language/tag review | proposal identity; no tags | conversation drift | program operator | program operator for proposal language; upstream for any official name | standing; GOV-001/002 | tracked, not blocked for Wave 0 docs |
| R-TEN | tenancy | Cross-organization leakage if multi-tenant is added | n/a until OD-007 | isolation tests | do not add tenancy without OD-007 | no model yet | program operator (tracking) | unassigned sponsor (OD-007) | OPS-004; Wave 8 | **blocked** |
| R-FED | federation | Signed package treated as truth or disclosure permission | n/a until late | quarantine/revoke tests | signature = integrity+issuer only | not implemented | program operator (tracking) | unassigned federation governance | Wave 9 / Gate 7 | **blocked** |
| R-WIN | evaluation | Windows host fails 3 tests CI Ubuntu may pass | L/M | independent Ubuntu rerun | do not weaken tests | Ubuntu result unknown | program operator | program operator (do not “fix” by weakening) | Wave 0 independent verify may use Ubuntu | tracked, not blocked |
| R-LEG | competing truth | Legacy mutable cases / scrapers / RDF pools | M/H | stack isolation review | do not silently replace; do not extend scrapers | residual legacy paths | program operator | program operator for “no product change in Wave 0”; upstream for legacy retirement | standing containment | tracked; product remediation **out of scope** |

## Risks this program will not “fix” in Wave 0

Wave 0 only records and assigns tracking ownership. Containment that would change product code is out of scope. High-severity items whose decision authority is unnamed remain **blocked**.
