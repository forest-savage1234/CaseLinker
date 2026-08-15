# Wave 0 requirements and gap matrix

**Kind of document:** proposal-control. Not a completion scorecard.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**vNext historical checkpoint (not the v4 base):** `802fb7d244e3751b42dbb20cc8d258e1b71adbc7`  
**Labels:** `repository fact` | `inference` | `proposal` | `human decision required`

Status values used here:

- `present_in_v3` — implemented on the proposal branch with tests
- `partial` — some structure exists; the requirement is not met
- `absent` — no implementation
- `policy_blocked` — software cannot close this without named human authority
- `out_of_scope_wave0` — recorded only

No requirement is “done.” Wave 0 creates the registry. Closure needs implementation or policy artifact, a positive test, a negative/adversarial test, and a later gate.

Columns: `id`, invariant, current evidence, gap, risk, proposed boundary, acceptance evidence, human authority, status.

## Constitutional invariants (CONST-001…018)

| ID | Invariant | Current evidence (fact) | Gap | Risk | Proposed boundary | Acceptance evidence | Human authority | Status |
|---|---|---|---|---|---|---|---|---|
| CONST-001 | No factual claim without exact evidence | `Assertion` requires evidence or typed span-unavailable reason (`assertions/models.py` 289–302; ADR 0003) | none for v3 assertions; UI/legacy paths unenforced | evidence-free claims in unused stacks | keep ledger; do not serialize legacy dicts as claims | existing unit tests; later export tests | none for the kernel | present_in_v3 / partial globally |
| CONST-002 | No evidence without immutable source identity | `SourceDocumentVersion` + digest (`documents/models.py`; ADR 0002) | no authenticity/mutation machine | substituted or rotated web pages | source governance context | mutation/version tests (later) | OD-004 | partial |
| CONST-003 | No silent overwriting | SQL abort triggers; append-only reviews (ADR 0004) | no general correction/supersession engine for dependents | silent history loss | temporal kernel | trigger + lineage tests (exist); impact tests (absent) | none | present_in_v3 for rows; partial for dependents |
| CONST-004 | Preserve two kinds of time | `valid_from`/`valid_to` + `created_at` | no as-known/valid-time query contract | time collapse | temporal kernel | January/February scenario (later) | none | partial |
| CONST-005 | No allegation as guilt | reported predicates; six distinct event types (ADR 0006; `claims.py` limitations) | UX/legacy `booking_status` still exists | readers infer guilt | keep reported vs resolved; UX later | existing extractor tests; later comprehension study | none for kernel | present_in_v3 / partial globally |
| CONST-006 | No opaque identity claims | `AttributedSubject` is caller-supplied; no merge type in `src/caselinker` | no hypothesis type; legacy clustering exists | silent person merge | identity hypothesis context; isolate clustering | false-merge tests (later) | OD-006 | partial / research first |
| CONST-007 | No blind transitive merging | no merge implementation in vNext | clustering/legacy similarity | A≈B≈C collapse | same as CONST-006 | transitivity adversarial tests | OD-006 | absent (good) / residual in legacy |
| CONST-008 | AI is an untrusted proposer | no vNext model path writes canonical facts; charter §4 | legacy ML extra exists; not in core CI | self-approval | AI execution record | later AI-governance tests | none yet | partial |
| CONST-009 | Eligibility ≠ disclosure | ADR 0007; `publication.py` 37–38; Evidence Pack exclusion | no PDP/PEP | eligible data published | disclosure context | three-view tests (later) | OD-003 | partial (separation stated; enforcement absent) |
| CONST-010 | No statistic without unit/denominator/membership/limitations | cohort unit `legal_event`; full membership; `LIMITATIONS` | only one unit; no study registry | unit confusion | scientific workbench later | existing cohort tests | none for current unit | present_in_v3 for that unit |
| CONST-011 | Ontology mapping must not erase source precision | `cl:legalEventType` kept beside broader CAC class (ADR 0008) | limited mapping set | term collapse | keep projection adapter | existing golden digest tests | ontology maintainer later | present_in_v3 for legal-event profile |
| CONST-012 | Corrections invalidate dependencies | live eligibility on review change (ADR 0007) | no transitive dependency graph | stale Claim Cards/packs remain usable | correction/impact engine | completeness tests (later) | none | partial |
| CONST-013 | No publication without reproducible snapshot | snapshot manifests + pipeline re-verify (ADR 0001, 0011) | no signed publication object | unverifiable outputs | keep snapshots; publication later | existing CLI tests | none | present_in_v3 for research artifacts |
| CONST-014 | No public-availability assumption | threat model boundary 1; handoff non-goals | README live-demo language exists | over-collection / republication | do not treat README as policy | human review of communications | OD-004 | policy_blocked |
| CONST-015 | No official version without upstream | ADR 0000; AGENTS.md; pyproject 0.0.0 | communication drift | false v4.0.0 claim | proposal language only | this program | upstream only | present_in_v3 / standing |
| CONST-016 | No competing source of truth | vNext projections are derived | legacy DB/UI/RDF pools coexist | dual-write ambiguity | isolate stacks | later reconciliation tests | none | partial |
| CONST-017 | No hidden state transition | review/resolution records actor-ish ids and times | no authn; limited reason codes | unauditable authority | review workspace later | later audit tests | OD-005 | partial |
| CONST-018 | Fail closed | many v3 fail-closed constructors and CLI exits | missing policy currently yields “no disclosure engine” rather than an explicit deny decision object | implicit allow via leftover serializers | default-deny PDP later | alternate-path tests | OD-003 | partial |

## Prohibited capabilities (PROHIB)

| ID | Prohibition | Current evidence | Gap / containment | Status |
|---|---|---|---|---|
| PROHIB-001 | Predictive policing / individual risk scores | not in `src/caselinker` | do not extend triage toward individual danger | absent in vNext; watch legacy triage |
| PROHIB-002 | Autonomous guilt/credibility | extractors do not accept their own output (ADR 0005–0006) | keep | present_in_v3 restraint |
| PROHIB-003 | Victim/minor identification or public person-tracking | aliases are matching inputs, not published | no disclosure engine | policy_blocked |
| PROHIB-004 | Facial recognition / biometrics | not present | do not add | absent |
| PROHIB-005 | Opaque person matching / irreversible auto-merge | no vNext merge | isolate legacy clustering | research first |
| PROHIB-006 | Platform danger rankings without denominators | Claim limitations forbid it (`claims.py` 12–21) | watch stats UI | partial globally |
| PROHIB-007 | Unreviewed AI facts | no vNext AI writer | ML extra exists | partial |
| PROHIB-008 | Ungoverned scraping | `scripts/scraper/` exists | do not extend; record in risk register | residual |
| PROHIB-009 | Public ⇒ republish | stated in threat model | no operational takedown | policy_blocked |
| PROHIB-010 | Direct model access to unrestricted corpora | core CI excludes ML extra (`quality.yml` `no-extra ml`) | keep | partial |
| PROHIB-011 | Bypass disclosure via export/log/cache/admin | no PDP; Evidence Pack excludes source text | alternate paths untested | absent enforcement |
| PROHIB-012 | Production deploy / live migrate / publish under this program | not done | standing stop | standing |
| PROHIB-013 | Official version designation | no tags | standing stop | standing |

## Domain families

### TEMP — temporal evidence

| ID | Requirement | Evidence | Gap | Status |
|---|---|---|---|---|
| TEMP-001 | Distinct valid and knowledge time | fields exist | no query contract | partial |
| TEMP-002 | As-known and valid-during queries | absent | implement later | absent |
| TEMP-003 | Do not synthesize precision | date extractor rejects invalid/future dates (ADR 0006) | interval/open dates undefined | partial |

### SOURCE — source governance

| ID | Requirement | Evidence | Gap | Status |
|---|---|---|---|---|
| SOURCE-001 | Immutable version identity | ADR 0002 | none for identity | present_in_v3 |
| SOURCE-002 | Mutation / takedown / authenticity monitoring | absent | research first | absent; OD-004 |
| SOURCE-003 | Hostile-input defenses for acquisition | path/symlink checks in snapshot/CLI | no governed collector | partial |

### RESOLVE — corroboration and identity

| ID | Requirement | Evidence | Gap | Status |
|---|---|---|---|---|
| RESOLVE-001 | Source-family and derivation | absent | research first | absent |
| RESOLVE-002 | Independent corroboration ≠ syndication | absent | research first | absent |
| RESOLVE-003 | Reversible identity hypotheses, no silent merge | absent in vNext | **top risk 1** | absent; OD-006 |
| RESOLVE-004 | No blind transitivity | absent (desired) | protect against adding it | absent |
| RESOLVE-005 | Same-event hypotheses vs acceptance | resolver is single-bundle, not multi-source | **top risk 1** | absent |

### REVIEW

| ID | Requirement | Evidence | Gap | Status |
|---|---|---|---|---|
| REVIEW-001 | Authenticated principals | opaque `reviewer_id` only | **policy_blocked** | absent; OD-005 |
| REVIEW-002 | Append-only decisions | ADR 0003–0004 | none for storage | present_in_v3 |
| REVIEW-003 | Second review / adjudication | absent | later | absent; OD-005 |
| REVIEW-004 | Reviewer workbench | absent | later UX wave | absent |

### DISCLOSE

| ID | Requirement | Evidence | Gap | Status |
|---|---|---|---|---|
| DISCLOSE-001 | Separate eligibility from disclosure | ADR 0007 | enforcement absent | partial |
| DISCLOSE-002 | Default-deny PDP/PEP | absent | **top risk 3** | absent; OD-003 |
| DISCLOSE-003 | Distinct internal / research / public views | absent | later | absent; OD-003 |
| DISCLOSE-004 | Enforce again at serialize/export/log | Evidence Pack exclusions only | **top risk 3** | absent |

### CORRECT

| ID | Requirement | Evidence | Gap | Status |
|---|---|---|---|---|
| CORRECT-001 | Dependency identity | review lineage only | no general dependency edge | partial |
| CORRECT-002 | Complete invalidation | live eligibility only | **top risk 2** | partial |
| CORRECT-003 | Rebuild + preserve history | supersession/retraction records exist | no rebuild queue or notices | partial |

### SCI

| ID | Requirement | Evidence | Gap | Status |
|---|---|---|---|---|
| SCI-001 | Explicit unit/denominator/membership | ADR 0009 | single unit only | present_in_v3 |
| SCI-002 | Preregistered study spec | absent | later | absent; OD-009 |
| SCI-003 | Block prevalence/causation/platform-danger | claim text + limitations | other UIs | partial |

### AI, OPS, FED, UX, GOV

| ID | Requirement | Status | Authority |
|---|---|---|---|
| AI-001 | Models cannot approve/publish/merge/disclose | absent record type; restraint stated | later |
| AI-002 | Execution provenance | absent | later |
| OPS-001 | PostgreSQL SoR analysis | proposal; later technical experiment | OD-008 |
| OPS-002 | Object store + verified restore | absent | OD-008 |
| OPS-003 | Outbox/queue | absent | later |
| OPS-004 | Tenant isolation | absent | OD-007 |
| OPS-005 | Backup/restore rehearsal | absent | OD-008 |
| FED-001 | Signed packages | absent; late | later human gate |
| UX-001 | Chart→member→claim→span navigation | absent | later |
| UX-002 | WCAG 2.2 AA / trauma-aware | stated in charter; not evidenced here | later |
| GOV-001 | Upstream sovereignty | present_in_v3 language | standing |
| GOV-002 | Human gates / no official version | this program | standing |
| GOV-003 | Machine-verifiable v4 traceability | this file (registry only) | Wave 0 |

## Capability classification (v3 → v4 working class)

See also `architecture/CURRENT_STATE.md`. Working class is an **inference** for planning, not an adoption order.

| Capability | Class |
|---|---|
| Snapshots, documents, assertion/review ledger | reuse / extend |
| Platform-mention and reported-legal-event extractors | reuse (fixtures); research first to broaden |
| Review-aware resolution + live eligibility | extend |
| CAC / SHACL / Claim CI / CLI | reuse as projections |
| SQLite adapters | extend for fixtures; replace-by-migration later if a new SoR is accepted |
| Legacy cases / scrapers / UI | out of scope for the kernel; contain |
| Identity, federation, disclosure content, IAM | research first + human authority |
