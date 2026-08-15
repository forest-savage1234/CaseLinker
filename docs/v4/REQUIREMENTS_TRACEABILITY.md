# Wave 0 requirements and gap matrix

**Kind of document:** proposal-control. Not a completion scorecard.  
**Approved base:** `4a17a9e5fdf74057de08a819291bf1606b8e3b45`  
**vNext historical checkpoint (not the v4 base):** `802fb7d244e3751b42dbb20cc8d258e1b71adbc7`  
**Labels:** `repository fact` | `inference` | `proposal` | `human decision required`

No requirement is “done.” Wave 0 only registers requirements. Closure needs an implementation or policy artifact, one positive test, one negative/adversarial test, a traceability link, **and** any required human authority (`GROK_BUILD_PROGRAM.md` §18.4). Therefore `requirements_closed` is empty.

## Status vocabulary (exactly one per ID)

| Status | Meaning |
|---|---|
| `present_in_v3` | Implemented on the proposal branch with tests for a **narrow** declared scope |
| `partial` | Some structure exists; the v4 requirement is not met |
| `absent` | No implementation of the required control |
| `policy_blocked` | Software cannot close this without named human authority |

## Evidence-status buckets (exactly one per ID)

Used in `docs/v4/evidence/WAVE-00-EVIDENCE.md`:

| Bucket | Rule |
|---|---|
| `closed` | Meets §18.4 closure. **None** in Wave 0. |
| `partially_met` | Status is `present_in_v3` or `partial` |
| `unmet` | Status is `absent` or `policy_blocked` |

Dual statuses such as “present_in_v3 / partial globally” are forbidden. Residual legacy risk is recorded in **Gap** and **Risk**, not by splitting the status.

Required fields on every row: `requirement_id`, `constitutional_invariant`, `current_evidence`, `gap`, `risk`, `proposed_boundary`, `acceptance_evidence`, `human_authority_required`, `status`.

---

## Constitutional invariants (CONST-001…018)

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| CONST-001 | No factual claim without exact evidence | `Assertion` requires evidence or typed span-unavailable reason (`assertions/models.py` 289–302; ADR 0003) | Legacy UI/dicts are unenforced | evidence-free claims outside the ledger | keep ledger; do not serialize legacy dicts as claims | existing assertion unit tests; later export tests | none for the kernel | partial |
| CONST-002 | No evidence without immutable source identity | `SourceDocumentVersion` + digest (`documents/models.py`; ADR 0002) | no authenticity/mutation machine; **bytes not stored** | substituted pages; unrestorable evidence | source governance + future object store | mutation/version tests (later) | OD-004 | partial |
| CONST-003 | No silent overwriting | SQL abort triggers; append-only reviews (ADR 0004) | no general dependent-invalidation engine | silent history loss downstream | temporal kernel + dependency registry | trigger tests exist; impact tests absent | none | partial |
| CONST-004 | Preserve two kinds of time | `valid_from`/`valid_to` + `created_at` | no as-known/valid-time query contract | time collapse | temporal kernel | January/February scenario (later) | none | partial |
| CONST-005 | No allegation as guilt | reported predicates; six event types (ADR 0006; `claims.py` limitations) | UX/legacy `booking_status` still exists | readers infer guilt | keep reported vs resolved; UX later | existing extractor tests; later comprehension study | none for the kernel | partial |
| CONST-006 | No opaque identity claims | `AttributedSubject` is caller-supplied; no merge type in `src/caselinker` | no hypothesis type; legacy clustering exists | silent person merge | identity-hypothesis context; isolate clustering | false-merge tests (later) | OD-006 | partial |
| CONST-007 | No blind transitive merging | no merge implementation in vNext | legacy similarity/clustering can still imply transitivity | A≈B≈C collapse | same as CONST-006 | transitivity adversarial tests | OD-006 | partial |
| CONST-008 | AI is an untrusted proposer | no vNext model path writes canonical facts; charter §4 | legacy ML extra exists; not in core CI | self-approval | AI execution record | later AI-governance tests | none yet | partial |
| CONST-009 | Eligibility ≠ disclosure | ADR 0007; `publication.py` 37–38; Evidence Pack exclusion | no PDP/PEP | eligible data published | disclosure context | three-view tests (later) | OD-003 | partial |
| CONST-010 | No statistic without unit/denominator/membership/limitations | cohort unit `legal_event`; full membership; `LIMITATIONS` | only one unit; no study registry | unit confusion | scientific workbench later | existing cohort tests | none for that unit | present_in_v3 |
| CONST-011 | Ontology mapping must not erase source precision | `cl:legalEventType` kept beside broader CAC class (ADR 0008) | limited mapping set | term collapse | keep projection adapter | existing golden digest tests | ontology maintainer (unnamed; blocked for expansion) | present_in_v3 |
| CONST-012 | Corrections invalidate dependencies | live eligibility on review change (ADR 0007) | no transitive dependency graph | stale Claim Cards/packs remain usable | correction/impact engine | completeness tests (later) | none | partial |
| CONST-013 | No publication without reproducible snapshot | snapshot manifests + pipeline re-verify (ADR 0001, 0011) | no signed publication object | unverifiable outputs | keep snapshots; publication later | existing CLI tests | none | present_in_v3 |
| CONST-014 | No public-availability assumption | threat model boundary 1; handoff non-goals | README live-demo language exists | over-collection / republication | do not treat README as policy | human review of communications | OD-004 | policy_blocked |
| CONST-015 | No official version without upstream | ADR 0000; AGENTS.md; pyproject 0.0.0 | communication drift | false v4.0.0 claim | proposal language only | this program + no tags | upstream maintainer | present_in_v3 |
| CONST-016 | No competing source of truth | vNext projections are derived | legacy DB/UI/RDF pools coexist | dual-write ambiguity | isolate stacks | later reconciliation tests | none | partial |
| CONST-017 | No hidden state transition | review/resolution record ids and times | no authn; limited reason codes | unauditable authority | review workspace later | later audit tests | OD-005 | partial |
| CONST-018 | Fail closed | many v3 fail-closed constructors and CLI exits | missing policy yields no deny object rather than explicit deny | implicit allow via leftover serializers | default-deny PDP later | alternate-path tests | OD-003 | partial |

---

## Prohibited capabilities (PROHIB-001…013)

`constitutional_invariant` names the CONST the prohibition protects.

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| PROHIB-001 | CONST-005, CONST-010 | not in `src/caselinker` | legacy triage exists | individual danger scores | do not extend triage toward individual risk | later adversarial scan of scoring APIs | none | partial |
| PROHIB-002 | CONST-005, CONST-008 | extractors do not accept their own output (ADR 0005–0006) | other stacks | autonomous guilt | keep extractor restraint | existing extractor tests | none | present_in_v3 |
| PROHIB-003 | CONST-006, CONST-009 | aliases are matching inputs | no disclosure engine | victim/minor identification | no person-tracking features | later export/redaction tests | OD-003, OD-006 | policy_blocked |
| PROHIB-004 | CONST-006 | no facial/biometric code in `src/caselinker` | no regression that forbids adding it | biometric identity | do not add | later prohibited-capability scan | none | absent |
| PROHIB-005 | CONST-006, CONST-007 | no vNext merge type | isolate legacy clustering | irreversible auto-merge | hypothesis context only | false-merge tests | OD-006 | partial |
| PROHIB-006 | CONST-010 | Claim limitations forbid platform-danger (`claims.py` 12–21) | other stats UIs | unsupported rankings | keep generated claim text | existing claim tests; later UI audit | none | partial |
| PROHIB-007 | CONST-008 | no vNext AI writer | ML extra exists | unreviewed AI facts | AI execution record | later AI-governance tests | none | partial |
| PROHIB-008 | CONST-002, CONST-014 | `scripts/scraper/` exists | ungoverned collection | hostile/unlawful ingest | do not extend scrapers | later collection-policy tests | OD-004 | partial |
| PROHIB-009 | CONST-014 | stated in threat model | no operational takedown | republication | policy-gated collection | later retention/takedown tests | OD-004 | policy_blocked |
| PROHIB-010 | CONST-008 | core CI uses `--no-extra ml` (`quality.yml`) | optional extra still lockable | unrestricted model corpus | keep extra out of core CI | CI config review | none | partial |
| PROHIB-011 | CONST-009, CONST-018 | no PDP; Evidence Pack excludes source text | alternate paths untested | disclosure bypass | default-deny at every serializer | later alternate-path tests | OD-003 | absent |
| PROHIB-012 | CONST-015, CONST-018 | no deploy/migrate/publish from this program | standing stop must be re-asserted | accidental production use | program stop conditions | process evidence (no tags/deploys) | operator + upstream | present_in_v3 |
| PROHIB-013 | CONST-015 | no tags | communication drift | official version claim | proposal identity | `git tag` empty | upstream maintainer | present_in_v3 |

---

## TEMP — temporal evidence

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| TEMP-001 | CONST-004 | `valid_from`/`valid_to`/`created_at` fields | no documented two-time semantics | time collapse | temporal kernel | bitemporal contract tests (later) | none | partial |
| TEMP-002 | CONST-004 | absent query API | as-known/valid-during not implemented | wrong historical answers | temporal kernel | January/February scenario | none | absent |
| TEMP-003 | CONST-004 | date extractor rejects invalid/future dates (ADR 0006) | interval/open dates undefined | invented precision | temporal kernel | precision-rejection tests | none | partial |

---

## SOURCE — source governance

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| SOURCE-001 | CONST-002 | immutable document/version identity (ADR 0002) | identity ≠ stored bytes | unrestorable source | keep identity; add store later | existing document tests | none | present_in_v3 |
| SOURCE-002 | CONST-002, CONST-014 | absent | no mutation/takedown/authenticity monitor | undetected substitution | source governance | later mutation tests | OD-004 | absent |
| SOURCE-003 | CONST-002, CONST-018 | path/symlink checks in snapshot/CLI | no governed collector | hostile acquisition | collection policy + parser isolation | later parser/SSRF tests | OD-004 | partial |

---

## RESOLVE — corroboration and identity

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| RESOLVE-001 | CONST-002, CONST-011 | absent | no source-family/derivation type | syndicated copies counted as independent | multi-source context | later derivation tests | none | absent |
| RESOLVE-002 | CONST-010 | absent | no corroboration vs syndication distinction | inflated confirmation | multi-source context | later family-count tests | none | absent |
| RESOLVE-003 | CONST-006 | absent in vNext | no reversible hypothesis | silent false merge (R-ID) | identity-hypothesis context | false-merge-first tests | OD-006 | absent |
| RESOLVE-004 | CONST-007 | no vNext transitivity write | legacy clustering residual | blind A≈B≈C | same as RESOLVE-003 | transitivity adversarial tests | OD-006 | absent |
| RESOLVE-005 | CONST-006 | resolver is single-bundle, not multi-source | no same-event hypothesis type | manufactured same-event | event-hypothesis context | later same-event tests | OD-006 | absent |

---

## REVIEW

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| REVIEW-001 | CONST-017 | opaque `reviewer_id` only | no authentication | unauditable review authority | IAM + review ledger | later authn tests | OD-005 | policy_blocked |
| REVIEW-002 | CONST-003, CONST-017 | append-only `ReviewDecision` (ADR 0003–0004) | no authn behind the chain | forged reviewer ids | keep ledger; add authn later | existing review-chain tests | none for storage | present_in_v3 |
| REVIEW-003 | CONST-017 | absent | no second review/adjudication | single-actor high-risk accept | review task machine | later SoD tests | OD-005 | absent |
| REVIEW-004 | CONST-001, CONST-005 | absent | no workbench | reviewers lack source context | later UX wave | later a11y/comprehension tests | none | absent |

---

## DISCLOSE

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| DISCLOSE-001 | CONST-009 | ADR 0007 separates eligibility from disclosure | enforcement absent | eligibility treated as permission | keep the distinction | existing eligibility tests; later PDP tests | OD-003 | partial |
| DISCLOSE-002 | CONST-009, CONST-018 | absent | no default-deny PDP/PEP | R-DIS | disclosure context | later deny-by-default tests | OD-003 | policy_blocked |
| DISCLOSE-003 | CONST-009 | absent | no audience views | over-disclosure | disclosure context | three-view tests | OD-003 | policy_blocked |
| DISCLOSE-004 | CONST-009, CONST-018 | Evidence Pack exclusions only | no enforce-at-serialize | alternate-path leak | every output path | later export/log/cache tests | OD-003 | absent |

---

## CORRECT

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| CORRECT-001 | CONST-012 | review lineage only | no general `DependencyEdge` | incomplete impact | temporal kernel | later dependency tests | none | partial |
| CORRECT-002 | CONST-012 | live eligibility only | dependents can stay eligible | R-COR | correction engine | completeness tests | none | partial |
| CORRECT-003 | CONST-003, CONST-012 | supersession/retraction records exist | no rebuild queue or notices | silent stale outputs | correction engine | later rebuild/notice tests | none | partial |

---

## SCI

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| SCI-001 | CONST-010 | ADR 0009 unit/membership | single unit only | unit confusion | scientific workbench | existing cohort tests | none for `legal_event` | present_in_v3 |
| SCI-002 | CONST-013 | absent | no preregistered study spec | post-hoc methods | scientific workbench | later study-registry tests | OD-009 | absent |
| SCI-003 | CONST-010 | claim text + limitations | other UIs | prevalence/causation claims | keep generated claims | existing claim tests; later UI audit | none | partial |

---

## AI, OPS, FED, UX, GOV

| requirement_id | constitutional_invariant | current_evidence | gap | risk | proposed_boundary | acceptance_evidence | human_authority_required | status |
|---|---|---|---|---|---|---|---|---|
| AI-001 | CONST-008 | restraint stated; no record type | models could be wired later without provenance | self-approval | AI execution record | later AI-governance tests | none | absent |
| AI-002 | CONST-008, CONST-017 | absent | no execution provenance | unreproducible model output | AI execution record | later provenance tests | none | absent |
| OPS-001 | CONST-003 | SQLite only; Postgres is a proposal | no isolation analysis | concurrency loss | later technical experiment | later Postgres tests | OD-008 | absent |
| OPS-002 | CONST-002 | no object store (see `DATA_AUTHORITY.md`) | bytes unrestorable | evidence loss | future object store | later restore tests | OD-008 | absent |
| OPS-003 | CONST-016, CONST-017 | absent | no outbox/queue | dual-write / lost jobs | later hardening | later idempotency tests | OD-008 | absent |
| OPS-004 | CONST-009 | absent | no tenant model | cross-org leak | later isolation | later isolation tests | OD-007 | policy_blocked |
| OPS-005 | CONST-003 | absent | no backup/restore rehearsal | unrecoverable ledger | later hardening | later restore drill | OD-008 | absent |
| FED-001 | CONST-015, CONST-009 | absent | no signed packages | signature mistaken for truth | late federation | later quarantine/revoke tests | later federation authority | absent |
| UX-001 | CONST-001, CONST-010 | absent | no chart→span navigation | users cannot audit counts | later UX wave | later navigation tests | none | absent |
| UX-002 | CONST-005 | charter states WCAG 2.2 AA | not evidenced | inaccessible or sensational UI | later UX wave | later a11y/comprehension study | none | absent |
| GOV-001 | CONST-015 | ADR 0000; AGENTS.md; charter §2 | communication drift | fork treated as upstream | proposal language | existing docs | upstream maintainer | present_in_v3 |
| GOV-002 | CONST-015 | this program; human gates | gates can be skipped in conversation | unofficial “v4 complete” | wave state machine | process evidence | operator + upstream | present_in_v3 |
| GOV-003 | CONST-015 | this registry file only | **no machine validator** for v4 IDs (vNext checker covers `docs/vnext/traceability.v1.json` only) | drift / omitted IDs | later v4 traceability checker | failing test if an ID lacks fields or bucket | none for a checker; Wave 0 cannot close this | partial |

---

## Evidence-bucket reconciliation (every ID once)

**closed (0):** none.

**partially_met (40):** CONST-001, CONST-002, CONST-003, CONST-004, CONST-005, CONST-006, CONST-007, CONST-008, CONST-009, CONST-010, CONST-011, CONST-012, CONST-013, CONST-015, CONST-016, CONST-017, CONST-018, PROHIB-001, PROHIB-002, PROHIB-005, PROHIB-006, PROHIB-007, PROHIB-008, PROHIB-010, PROHIB-012, PROHIB-013, TEMP-001, TEMP-003, SOURCE-001, SOURCE-003, REVIEW-002, DISCLOSE-001, CORRECT-001, CORRECT-002, CORRECT-003, SCI-001, SCI-003, GOV-001, GOV-002, GOV-003.

**unmet (29):** CONST-014, PROHIB-003, PROHIB-004, PROHIB-009, PROHIB-011, TEMP-002, SOURCE-002, RESOLVE-001, RESOLVE-002, RESOLVE-003, RESOLVE-004, RESOLVE-005, REVIEW-001, REVIEW-003, REVIEW-004, DISCLOSE-002, DISCLOSE-003, DISCLOSE-004, SCI-002, AI-001, AI-002, OPS-001, OPS-002, OPS-003, OPS-004, OPS-005, FED-001, UX-001, UX-002.

Count check: 0 + 40 + 29 = 69 IDs (CONST 18 + PROHIB 13 + TEMP 3 + SOURCE 3 + RESOLVE 5 + REVIEW 4 + DISCLOSE 4 + CORRECT 3 + SCI 3 + AI 2 + OPS 5 + FED 1 + UX 2 + GOV 3).

## Capability classification (v3 → v4 working class)

See also `architecture/CURRENT_STATE.md`. Working class is an **inference** for planning, not an adoption order.

| Capability | Class |
|---|---|
| Snapshots, documents, assertion/review ledger | reuse / extend |
| Platform-mention and reported-legal-event extractors | reuse (fixtures); research first to broaden |
| Review-aware resolution + live eligibility | extend |
| CAC / SHACL / Claim CI / CLI | reuse as projections |
| SQLite adapters | extend for fixtures; replace-by-migration later if a new SoR is accepted |
| Exact source-byte persistence | **absent**; do not treat `storage_key` as a store |
| Legacy cases / scrapers / UI | out of scope for the kernel; contain |
| Identity, federation, disclosure content, IAM | research first + human authority |
