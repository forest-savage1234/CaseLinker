# Research Layer Index

**Document date:** 2026-08-16  
**Owner:** Forest Savage (`forest-savage1234`)  
**Kind:** contributor-owned preservation index  
**Official product status:** none

This file is a map, not a release. It records where research and proposal
trees live, how they differ from official-track work, and which freeze
points preserve them. It does not claim official CASE-UCO-SDK 2.0,
CaseLinker 3.0, CaseLinker 4.0, or CAC Ontology 4.0 status.

## 1. Purpose and status

The research layer is complementary architectural work. It is:

- **contributor-owned** — authored and preserved by the contributor on
  personal forks and clearly labeled `research-freeze/` and `proposal/`
  refs;
- **non-authoritative** — it does not set roadmap, merge order, version
  numbers, or production policy for any upstream project;
- **non-substituting** — it does not replace official-track reviews,
  incremental PRs, or released 1.x / 3.x product lines;
- **recoverable** — freeze tags pin exact commits so the trees remain
  checkout-able if feature or proposal branches later move.

Maintainers retain complete authority over names, releases, and what
(if anything) is adopted.

## 2. Official-track versus research-only

Two tracks exist. They may share ideas, files, or people. They do not
share release authority.

| Track | What it is | What it is not |
|---|---|---|
| **Official-track** | Maintainer-controlled product lines and the incremental contributions submitted for those lines | A license to treat a fork commit as a released version |
| **Research-only / proposal** | Contributor-owned architecture, experiments, and parked later stages, labeled so they cannot be mistaken for releases | An official 2.0, 3.0, or 4.0 product |

### 2.1 Official-track homes (do not freeze-over, do not rewrite)

| Project | Official home | Current official line | Contributor official-track work (untouched by this freeze) |
|---|---|---|---|
| CASE-UCO-SDK | `vulnmaster/CASE-UCO-SDK` `main` | 1.x (upstream `v1.24.0` line) | Open PR [#110](https://github.com/vulnmaster/CASE-UCO-SDK/pull/110) (Composition Profiles catalog). Closed unmerged PR #107 is **not** official-track. |
| CaseLinker | `mrinaalr/CaseLinker` `main` | upstream `main` at `9da0a4ff` | Open PR [#5](https://github.com/mrinaalr/CaseLinker/pull/5) (`proposal/stage-1-m01`, governance + quality only). Draft PR [#4](https://github.com/mrinaalr/CaseLinker/pull/4) remains a parked architectural map, not a release. |
| CAC Ontology | `Project-VIC-International/CAC-Ontology` `main` | 3.x (`v3.1.0`) | Incremental PRs [#48](https://github.com/Project-VIC-International/CAC-Ontology/pull/48) and [#50](https://github.com/Project-VIC-International/CAC-Ontology/pull/50). Draft PR #49 is **not** official-track. |

Official-track PRs and mainline branches were not modified by this
preservation pass.

### 2.2 Research-only / proposal homes (frozen below)

| Project | Research / proposal home | Working labels used inside the tree | Binding meaning of those labels |
|---|---|---|---|
| CASE-UCO-SDK | `forest-savage1234/CASE-UCO-SDK` `feature/v2-capability-defining-rearchitecture` | Internal docs say “2.0.0” / “2.0.1” | Proposal-generation identifiers only. **Not** an official SDK 2.0 release. |
| CaseLinker vNext / proposed v3 | `forest-savage1234/CaseLinker` `proposal/v3-foundation` | “vNext”, “proposed v3 architecture”, workspace `0.0.0` | ADR 0000: not official CaseLinker 3.0. |
| CaseLinker research-network | `forest-savage1234/CaseLinker` `proposal/v4-research-network` | “v4 research-network proposal” | Not official CaseLinker 4.0. `official_version_claim: false`. |
| CAC foundational architecture | `forest-savage1234/CAC-Ontology` `proposal/issue-44-v4-foundational-architecture` | “v4 foundational architecture” under issue #44 | Draft PR #49 is a review artifact, not CAC 4.0. |

## 3. Frozen trees

All freeze refs use the `research-freeze/` namespace. None is a SemVer
product tag. None was pushed to an upstream remote.

| Freeze tag | SHA | Also labeled | Repository (contributor fork) | Classification | Why it is valuable |
|---|---|---|---|---|---|
| `research-freeze/sdk-advanced-tree-5b1758c` | `5b1758cdc1fb423461a7c852ffa5996b0370235a` | branch `research-freeze/sdk-advanced-tree` | [forest-savage1234/CASE-UCO-SDK](https://github.com/forest-savage1234/CASE-UCO-SDK) | Research-only | Final tip of the advanced construction tree (closed unmerged upstream PR #107). Holds InvestigationWorkflow, Profile Contracts, continuous critique, trajectories, and offline adapters. |
| `research-freeze/caselinker-v3-foundation-4a17a9e5` | `4a17a9e5fdf74057de08a819291bf1606b8e3b45` | branch `research-freeze/caselinker-v3-foundation` | [forest-savage1234/CaseLinker](https://github.com/forest-savage1234/CaseLinker) | Proposal; not official | Exact `proposal/v3-foundation` tip used as the v4 approved base. Holds the complete vNext claim/evidence pipeline. The live branch was not edited, retagged as a release, or force-pushed. |
| `research-freeze/caselinker-v4-research-network-64dc010f` | `64dc010feaf8fc79a61bea8b70e2386fa39ce546` | branch `research-freeze/caselinker-v4-research-network` | [forest-savage1234/CaseLinker](https://github.com/forest-savage1234/CaseLinker) | Research-only | Reconciled research-network tip: Wave 0–1 closeout, valid Wave 2 planning reconciliation (`bedeb04b`), and experiment checkpoints through W2-E3 r1 record / r2 authorization. |
| `research-freeze/cac-draft-pr49-8eb9045` | `8eb9045ce5fd95b80ddc8028f5a13a380d333dc7` | branch `research-freeze/cac-draft-pr49` | [forest-savage1234/CAC-Ontology](https://github.com/forest-savage1234/CAC-Ontology) | Research-only draft | Tip of draft upstream PR [#49](https://github.com/Project-VIC-International/CAC-Ontology/pull/49). Holds Role/Phase operational-record separation and sealed Gate 4.4 evidence. The draft PR itself was not modified. |

Checkout examples (read-only use):

```text
git fetch origin tag research-freeze/sdk-advanced-tree-5b1758c
git switch --detach research-freeze/sdk-advanced-tree-5b1758c

git fetch origin tag research-freeze/caselinker-v3-foundation-4a17a9e5
git switch --detach research-freeze/caselinker-v3-foundation-4a17a9e5

git fetch origin tag research-freeze/caselinker-v4-research-network-64dc010f
git switch --detach research-freeze/caselinker-v4-research-network-64dc010f

git fetch origin tag research-freeze/cac-draft-pr49-8eb9045
git switch --detach research-freeze/cac-draft-pr49-8eb9045
```

## 4. Architectural map — current homes

This section maps major pieces to the tree that currently holds them.
“Current home” means the best preserved implementation or specification,
not an official adoption decision.

### 4.1 Role / Phase separation

| Layer | Current home | Notes |
|---|---|---|
| Type-level Role and Phase spine (`cac-core:Role`, `cac-core:Phase`, `ConditioningPhase`, `cac-core:precedes`) | **Official-track** CAC Ontology 3.x (`v3.1.0` on upstream `main`) | Released. Existing v3 entailments are the compatibility baseline. |
| Operational role/phase *records* versus type-level classifiers; term disposition ledger; v3→proposal migration notes | **Research-only** CAC freeze `research-freeze/cac-draft-pr49-8eb9045` | See `docs/v4-foundational-architecture.md`, `docs/v3-to-v4-migration.md`, `ontology/cacontology-v4-foundation-shapes.ttl`, `testing/v4/`. |
| Offense-trajectory consumption of `hasPhase` / `ConditioningPhase` | **Research-only** SDK freeze `research-freeze/sdk-advanced-tree-5b1758c` (`case_uco.trajectories`) | Reads existing OWL; does not mint CAC terms. Generate-lag for `ConditioningPhase` bindings is documented, not silently claimed complete. |

### 4.2 InvestigationWorkflow, Profile Contracts, continuous critique

| Piece | Current home | Notes |
|---|---|---|
| `InvestigationWorkflow` (Python + C#/Java/Rust logical surface) | **Research-only** SDK freeze `5b1758c` | `python/case_uco/workflow`, `csharp/CaseUco/InvestigationWorkflow.cs`, `java/.../InvestigationWorkflow.java`. Full non-Python handlers remain unfinished in that tree. |
| Profile Contracts | Same freeze | `python/case_uco/contracts`, `topology/contracts/default-bindings.json` |
| Continuous construction critique | Same freeze | `python/case_uco/critique` |
| Composition Profiles / topology spine | **Official-track** SDK 1.x topology work and open PR #110; also present under the research freeze as the base that the advanced tree was stacked on | Official catalog review is PR #110. Do not treat the research freeze as the official catalog. |
| Offline VICS / PhotoDNA / hash-match adapters | **Research-only** SDK freeze `5b1758c` | Investigation-time code refuses `http:` / `https:`. |

Internal filenames such as `docs/V2_ARCHITECTURE.md` are historical
working titles inside the frozen tree. They are not an upstream 2.0
release announcement.

### 4.3 Claim / Evidence system

| Piece | Current home | Notes |
|---|---|---|
| Immutable `SourceDocument` / `SourceDocumentVersion` | **Proposal** CaseLinker freeze `4a17a9e5` | `src/caselinker/documents/`; ADRs 0001–0002. Parked for official review as later stages of draft PR #4. |
| Append-only assertion ledger and review lineage | Same freeze | `src/caselinker/assertions/`; migrations `0002`, `0003`; ADRs 0003–0004. |
| Legal-event extraction and review-aware resolution | Same freeze | `src/caselinker/extraction/`, `src/caselinker/resolution/`; ADRs 0006–0007. |
| Deterministic CAC legal-event projection + SHACL | Same freeze | `src/caselinker/graph/cac_legal_events.py`; ADR 0008. |
| Claim Cards, Evidence Packs, Claim CI, pipeline CLI | Same freeze | `src/caselinker/analysis/claims.py`, `evidence_pack.py`, `claim_ci.py`; ADRs 0009–0011. |
| Official-track slice already offered to the maintainer | CaseLinker PR #5 / `proposal/stage-1-m01` at `fb080b92` | Governance, DCO, quality CI, rewritten security documents only. No claim/evidence implementation. |

### 4.4 CaseLinker research-network contracts (post-v3 proposal)

These exist only on the v4 research-network freeze `64dc010f`. They are
proposal contracts, not product APIs.

| Piece | Path on the v4 freeze | Notes |
|---|---|---|
| Versioned JSON contracts (slices A–E) | `docs/v4/contracts/` | Policy-neutral; not a deployed service. |
| Bitemporal identities and transitions | `docs/v4/adr/W1-002-bitemporal-identities-transitions.md` | Distinguishes event/valid time from knowledge/transaction time. |
| Lineage and hypotheses | `docs/v4/adr/W1-003-lineage-and-hypotheses.md` | Agreement, derivation, contradiction, uncertainty. |
| Eligibility / disclosure / authority | `docs/v4/adr/W1-004-eligibility-disclosure-authority.md` | Eligibility is not disclosure authorization. |
| Wave 2 planning packet | `5fb8913e` (inside this freeze) | Frozen plan. W2-E3 r2 is the only authorized next experiment; r1 at `4e620ab` remains ineligible evidence. |
| Governing program | `docs/v4/GROK_BUILD_PROGRAM.md` | Still a proposal program. Gate 0 is not complete. |

### 4.5 What stays on official-track only

Do not look in the research freezes for these as source of truth:

- CASE-UCO-SDK released 1.x constructors, generator, and published
  packages;
- CAC Ontology 3.x modules, shapes, and `v3.1.0` examples;
- CaseLinker upstream `main` application (legacy ingestion / Postgres /
  visualization stack);
- CaseLinker Stage 1 / M01 review unit (PR #5).

## 5. Governance rules for this layer

1. Do not create SemVer tags (`v2.0.0`, `v3.0.0`, `v4.0.0`, or
   `-alpha` / `-rc` variants) from research or proposal trees.
2. Do not push research-freeze refs to upstream remotes
   (`vulnmaster/CASE-UCO-SDK`, `mrinaalr/CaseLinker`,
   `Project-VIC-International/CAC-Ontology`).
3. Do not edit, force-push, close, or retitle official-track PRs as part
   of preservation work. Draft PR #49 and CaseLinker PR #4 / #5 are
   review artifacts owned by their existing processes.
4. Do not present workspace `0.0.0`, internal “2.0.1” changelog lines,
   or “v4” directory names as shipped product versions.
5. If a freeze branch later receives new commits, leave the annotated
   tag where it is. A new freeze gets a new tag.

## 6. Local and remote locations

| Artifact | Location |
|---|---|
| This index (working copy) | `C:\Users\fores\docs\research\RESEARCH_LAYER.md` |
| CaseLinker v4 working tree | `C:\Users\fores\Downloads\CaseLinker-v4-research-network` |
| CaseLinker v3-foundation working tree | `C:\Users\fores\Downloads\CaseLinker-proposal` |
| CASE-UCO-SDK advanced working tree | `C:\Users\fores\CASE-UCO-SDK` (currently at `5b1758c`) |
| CAC Ontology working tree | `C:\Users\fores\CAC-Ontology` (currently on official-track fix branch; PR #49 tip is the freeze ref, not `HEAD`) |

## 7. Related but not frozen in this pass

These are valuable and still exist. They were left on their current
branches so this pass stayed inside the four requested trees.

| Item | SHA / ref | Suggested later freeze |
|---|---|---|
| CaseLinker Stage 1 / M01 (official-track review unit) | `fb080b92` on `proposal/stage-1-m01` | `research-freeze/caselinker-stage-1-m01-fb080b92` only if the official-track PR moves; otherwise the PR head is the record |
| CaseLinker v3 implementation checkpoint (pre-CI tail) | `802fb7d2` | Optional historical pin under the same v3-foundation tag family |
| CaseLinker Wave 2 planning packet | `5fb8913e` | Already reachable from the v4 freeze; may deserve its own tag if the branch continues |
| CaseLinker W2-E3 r1 ineligible evidence | `4e620ab` + fork PR #1 | Already required to be preserved as ineligible; do not amend |
| SDK topology / catalog official-track tip | `vulnmaster/CASE-UCO-SDK#110` | Official-track; do not freeze as research |

---

*End of index. This document does not constitute a release, a version
claim, or an upstream adoption request.*
