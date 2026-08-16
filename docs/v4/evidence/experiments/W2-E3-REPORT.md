# W2-E3 r2 builder report — default-deny disclosure and leakage

**Status:** builder evidence only; not an independent checkpoint, Wave 2
acceptance, product repair, or production disclosure policy.

**Evidence eligibility:** valid builder result; independent checkpoint pending.
A reviewer who did not author or repair this r2 must independently verify it
before any continuation decision.

## Preserved prior attempt

W2-E3 r1 is preserved at `4e620ab45e2dd771e6ed04eca243259bafb610a8` on
`experiment/w2-e3` and draft PR #1. D-2026-08-15-036 recorded the independent
checkpoint disposition `repeat_experiment`. R1 is ineligible because:

1. required cache, search, log, error, and administrative bypass attempts were
   recorded as metadata rather than executed;
2. M3 substituted the separately identified `D-revoked` decision instead of
   revoking or expiring the same previously allowed decision;
3. nested denied keys or values inside an allowed field were invisible to a
   top-level field-name scorer.

`experiments/w2e3/invalid-original-4e620ab/` records the r1 commit, parent, PR,
git blobs, and SHA-256 values. R1 was not amended, deleted, force-pushed, or
represented as eligible.

## Lineage and isolation

| Item | Value |
|---|---|
| Experiment | `W2-E3` r2 |
| Branch | `experiment/w2-e3-r2` |
| Approved and published parent | `64dc010feaf8fc79a61bea8b70e2386fa39ce546` |
| Frozen planning packet | `5fb8913e78d0e54ed25021bb34fcade43d2aff3c` |
| Namespace | `experiments/w2e3` |
| SUT revision | `w2e3-disclosure-v2` |
| Product source changes | none |
| Network or live data | none |

The base was clean before the namespace was created. At execution, all changes
were confined to `experiments/w2e3`; this report was added only after the run.
The three frozen packet files remained byte-identical to `5fb8913e`.

## Frozen inputs and implementation

| Artifact | SHA-256 |
|---|---|
| Input fixture | `887421f98da909e9a0a0441248e66833d647440956677bdcaf790cc95a02da39` |
| Oracle expected sets | `539596c7c0c5ff71da06a8f096d6829280d16c71d839797ce62bedad0e0f74dd` |
| Shared evaluator | `0f1b195f0cf77e54ba518d70628946cfdf33fabf4bf59a7724fa1ba28433cc74` |
| P1–P8 adapters | `04bdc2767c8746ad586a2d63ae5bac8427bb49ea246d3a4499de9096b38eeecb` |
| SUT driver | `88dba912391010ffb4bf71cb130d5ac612a25b11affff0a3b8ac357c1ae6ba60` |
| Harness | `85c461686887dc035f996ef1c480d8a9990ebcd1ec154c468c1b9be422a12750` |

The fixture contains supplied synthetic decisions and transformations, but no
key containing `expected`, `gold`, or `oracle`. The SUT CLI accepts only
`--fixture` and `--output`. The harness hashed the oracle bytes before launch,
staged only the fixture and three SUT files in a temporary directory, captured
the completed SUT output, and only then deserialized the oracle. The staged
directory was destroyed after capture.

The SUT does not inspect canary strings, expected labels, or the frozen answer
matrix. It fail-closes when a projected value contains a nested name outside
the supplied allowed set, or a scalar equal to a value of an unauthorized
source field. The harness independently reconstructs that denied surface from
the fixture subject and the oracle expected field set after output capture.

## Commands

```text
python -B experiments/w2e3/harness/run_w2e3.py
python -B experiments/w2e3/sut/driver.py --fixture experiments/w2e3/fixtures/input_fixture.json --output experiments/w2e3/outputs/sut_output.json
```

The first command is the governed run. The second records the SUT interface;
the governed harness used the same interface in the isolated stage.

## P1–P8 mechanism result

| Gate | Result |
|---|---|
| Valid run | `true` |
| Mechanism pass | `true` |
| Recommendation | `proceed` |
| Findings | 0 |
| Required paths | 8 of 8 on every run |
| Runs | 16 |
| Independently parsed path observations | 128 |
| Shared evaluator calls | 128, one exact `(run, path)` call each |
| Eligibility/disclosure confusion | 0 |
| Internal leaks on non-internal decisions | 0 |
| Distinct internal/research/public views | `true` |
| M1–M5 | all pass |
| Nested-structure fail-closed | pass |

Every path was scored from its path-specific raw representation: JSON keys,
CSV headers, bundle entry names, cache representation, search-document fields,
log keys, error safe-context keys, or administrative rows. The harness then
walked the parsed structure recursively for denied keys and denied source
values. It did not accept a SUT-reported field-name list as the oracle.

### Required bypass execution

On every run the adapters actually constructed the unsafe sources:

| Probe | Attack constructed | Independent proof |
|---|---|---|
| P4 | in-memory cache seeded from the full subject | source field names equal the complete subject, not the already-filtered view |
| P5 | search document built from the unminimized internal record | same full-subject field-name set |
| P6 | full-record log line, including `repr(record)` | `repr_computed` and positive `repr_char_length` |
| P7 | error payload containing `repr(record)` | same representation proof |
| P8 | administrative listing that attempted to skip the PEP | `skip_enforcement_attempted` and a later evaluator call |

Rendered output still used only the shared evaluator’s structurally projected
view. Direct publication of the constructed attack payloads did not occur.

### Baseline field sets on every P1–P8 path

| Run | Independently observed fields |
|---|---|
| D-missing | `{}` |
| D-internal | `{display_name, internal_note, public_aggregate_count, research_status}` |
| D-research | `{public_aggregate_count, research_status}` |
| D-public | `{public_aggregate_count}` |
| D-expired | `{}` |
| D-revoked | `{}` |
| D-invalid | `{}` |
| D-deny | `{}` |

Eight run states denied all fields across every path: D-missing, D-expired,
D-revoked, D-invalid, D-deny, M3-after, N-nested-key, and N-nested-value.

### Metamorphic observations

| Case | Observation on every P1–P8 path | Result |
|---|---|---|
| M1 remove `display_name` from supplied allow set | only `internal_note`, `research_status`, `public_aggregate_count` remain | pass |
| M2 change to D-public | only `public_aggregate_count` remains | pass |
| M3 revoke the same `D-internal` decision | before has four fields; after is empty; `decision_id`, audience, purpose, allowed fields, effect, and expiry are unchanged; only `revocation_state` changes from `active` to `revoked` | pass |
| M4 add unauthorized `internal_decoy` | decoy absent; original four authorized fields remain | pass |
| M5 reorder keys and change irrelevant whitespace | authorization field set unchanged; no extra field | pass |

### Structural fail-closed observations

| Case | Observation on every P1–P8 path | Result |
|---|---|---|
| N-nested-key: unauthorized name inside an allowed field | empty/denied; evaluator reason `nested_unauthorized_structure` | pass |
| N-nested-value: unauthorized source value inside an allowed field | empty/denied; evaluator reason `nested_unauthorized_structure` | pass |

No adapter contains its own audience allowlist or a hard-coded expected matrix.

## P9 observational result

P9 was run separately from the P1–P8 mechanism score against the exact existing
entry points:

- `ClaimCardBuilder.build` and `ClaimCard.to_dict`
- `EvidencePackAssembler.assemble` and `EvidencePack.canonical_json`

Classification: **`path_lacks_enforcement`**. No `confirmed_leak` was observed.

The allowed `public_aggregate_count` was mapped to a synthetic
`CohortResult.numerator`. `internal_note` and `display_name` have no product key
on these entry points. `research_status` could not be supplied through
`ClaimCardBuilder.build` because the builder owns fixed limitations. None of the
three denied tagged values appeared in the Claim Card or Evidence Pack output.
The entry points expose no supplied-decision hook, so this observation is not
proof that the existing serializers are disclosure-safe.

Named carry-forward: Wave 5 must add an authorized supplied-decision enforcement
hook before Claim Card or Evidence Pack entry points can support a
disclosure-safety claim. No product code was repaired or changed in this run.

## Exhaustive disposition

The frozen precedence was applied as `invalid → repeat`; otherwise
`stop > revise architecture > proceed`.

- Invalid/incomplete conditions: none.
- Stop conditions: none.
- Revise conditions: none. P9 did not confirm a leak.
- Proceed conditions: P1–P8 mechanism pass, and P9 is not `confirmed_leak`.

One experiment-level recommendation is therefore **`proceed`**, with the P9
carry-forward above. P9 did not improve or invalidate the P1–P8 result.

## Architecture implication and boundary

This result supports requiring every experiment output path to consult one
supplied decision, default-denying missing/invalid/expired/revoked decisions,
failing closed on unauthorized nested structure, and treating projections as
outputs rather than authority. It also shows that existing Claim Card/Evidence
Pack entry points lack the hook required to make that enforcement claim.

This result does **not** decide lawful bases, jurisdictions, real audiences,
field-minimization rules, separation of duties, OD-003, Wave 5 policy content,
product repair, deployment, or an official version. The synthetic evaluator and
adapters are disposable and prohibited from production promotion.

## Generated evidence hashes

| Artifact | SHA-256 |
|---|---|
| SUT output | `1868dc2b4eaebdb1041a839a67f69995e21ae3c8d99e9770d37e29b75e90775d` |
| Comparison | `9ec51c8db34426a80420dc8627adff468f0a1d057f36107f34a9dafcf9fb89cf` |
| P9 observation | `e8ab6defa5027fe0c774350a1ed1594063bd8679b584c7a665323b9c36943723` |
| Run sequence | `1be0bfdf1d2ce20df5e8c7eb990374fbc5d0e0046dba66a7520ad2d079331a72` |
| Freeze record | `fdbedf85cbb63c6fce10072cd0a42c0db6633a488343dde3937dc84f72e21e4d` |

The nine sequence records have strictly increasing sequence numbers and
`monotonic_ns` values. Oracle load is sequence 5, after SUT completion and
output capture at sequences 3 and 4.

## Validation

- JSON fixture and oracle parsing: pass.
- Ruff check and format check for `experiments/w2e3`: pass.
- Repository checker: pass for 8,620 tracked files after staging.
- Traceability checker: pass for 7 milestones.
- `git diff --cached --check`: pass.
- Final staged scope: this report plus 14 files under `experiments/w2e3`;
  no production module, product test, decision record, or execution-state file.
- Full approved pytest surface with explicit writable basetemp: 483 passed,
  the same three documented Windows-baseline failures, coverage 94.17%.
- Production `src/caselinker` and repository tests were not changed.

The three baseline failures remain:

1. POSIX-versus-Windows external-path separator rendering.
2. Windows symlink creation privilege (`WinError 1314`).
3. Windows N-Triples canonical ordering changes the expected failure message.

Packet identity and staged diff scope were rechecked after packaging. The
evidence commit identity and final clean-tree state are reported at handoff.

## Next gate

This builder report does not unlock W2-E4. A reviewer who did not author or
repair W2-E3 r2 must perform the required read-only checkpoint. Any
continuation then requires a separate explicit human decision. W2-E4, W2-E1,
Wave 2 acceptance, cleanup, deployment, and official-version claims remain
locked.
