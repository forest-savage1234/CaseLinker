# W2-E3 builder report — default-deny disclosure and leakage

**Status:** builder evidence only; not an independent checkpoint, Wave 2
acceptance, product repair, or production disclosure policy.

## Lineage and isolation

| Item | Value |
|---|---|
| Experiment | `W2-E3` |
| Branch | `experiment/w2-e3` |
| Approved and published parent | `9c481ee78bce8f916b9773f46924558424babdae` |
| Frozen planning packet | `5fb8913e78d0e54ed25021bb34fcade43d2aff3c` |
| Namespace | `experiments/w2e3` |
| SUT revision | `w2e3-disclosure-v1` |
| Product source changes | none |
| Network or live data | none |

The base was clean before the namespace was created. At execution, all changes
were confined to `experiments/w2e3`; this report was added only after the run.
The three frozen packet files remained byte-identical to `5fb8913e`.

## Frozen inputs and implementation

| Artifact | SHA-256 |
|---|---|
| Input fixture | `c8d1a6e72ca983594ffb3b77268ed144b28f05e3244e52cb8cc759dc22bb64c2` |
| Oracle expected sets | `4789ed2b1305d74707275911830398ee958e6a7b778df2d4b44f63be1aa7a3ff` |
| Shared evaluator | `d7fea896e0749c411999eb4c089b5e0d0e729d8b93b1c2f8571cf78c53694276` |
| P1–P8 adapters | `2c68aac6894b8dbc03dec20fae1e9dd0cd8873b727c752cab80847269ddc231e` |
| SUT driver | `c45a7a15002d4e4fba1a07c7d77affd6bee993db653a86d1b542181f56158a37` |
| Harness | `295ac2a848a428954cc17bf7259de10838ef3cb861edfa7588878c03f2afc8c5` |

The fixture contains supplied synthetic decisions and transformations, but no
key containing `expected`, `gold`, or `oracle`. The SUT CLI accepts only
`--fixture` and `--output`. The harness hashed the oracle bytes before launch,
staged only the fixture and three SUT files in a temporary directory, captured
the completed SUT output, and only then deserialized the oracle. The staged
directory was destroyed after capture.

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
| Runs | 14 |
| Independently parsed path observations | 112 |
| Shared evaluator calls | 112, one exact `(run, path)` call each |
| Eligibility/disclosure confusion | 0 |
| Internal leaks on non-internal decisions | 0 |
| Distinct internal/research/public views | `true` |
| M1–M5 | all pass |

Every path was scored from its path-specific raw representation: JSON keys,
CSV headers, bundle entry names, cache representation, search-document fields,
log keys, error safe-context keys, or administrative rows. The harness did not
accept a SUT-reported field-name list as the oracle.

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

Six run states denied all fields across every path: D-missing, D-expired,
D-revoked, D-invalid, D-deny, and M3-after.

### Metamorphic observations

| Case | Observation on every P1–P8 path | Result |
|---|---|---|
| M1 remove `display_name` from supplied allow set | only `internal_note`, `research_status`, `public_aggregate_count` remain | pass |
| M2 change to D-public | only `public_aggregate_count` remains | pass |
| M3 revoke after D-internal | before has four fields; after is empty | pass |
| M4 add unauthorized `internal_decoy` | decoy absent; original four authorized fields remain | pass |
| M5 reorder keys and change irrelevant whitespace | authorization field set unchanged; no extra field | pass |

The attempted unsafe inputs for cache, search, log, error, and administrative
paths did not bypass the shared evaluator. No adapter contains its own audience
allowlist.

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
three denied canaries appeared in the Claim Card or Evidence Pack output. The
entry points expose no supplied-decision hook, so this observation is not proof
that the existing serializers are disclosure-safe.

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
and treating projections as outputs rather than authority. It also shows that
existing Claim Card/Evidence Pack entry points lack the hook required to make
that enforcement claim.

This result does **not** decide lawful bases, jurisdictions, real audiences,
field-minimization rules, separation of duties, OD-003, Wave 5 policy content,
product repair, deployment, or an official version. The synthetic evaluator and
adapters are disposable and prohibited from production promotion.

## Generated evidence hashes

| Artifact | SHA-256 |
|---|---|
| SUT output | `6d3cf42b2f7a0ba7fb7710f8bdf7e071760627bff2ada2fa7f0ee7652222aa5c` |
| Comparison | `689eaf793b254b63c5a0e97f0e0098cbce09638022e2ab9e8383e9ef29411814` |
| P9 observation | `e8ab6defa5027fe0c774350a1ed1594063bd8679b584c7a665323b9c36943723` |
| Run sequence | `bfef432528563715170264ed97a3f66e6f3500f5020196baf40d3a82604668f5` |
| Freeze record | `605bc6ac13b14c146cb317c96987bd1a9c22a5cb9d81cdb62d6a4aa4de88670d` |

The nine sequence records have strictly increasing sequence numbers and
`monotonic_ns` values. Oracle load is sequence 5, after SUT completion and
output capture at sequences 3 and 4.

## Validation

- JSON fixture and oracle parsing: pass.
- Ruff check and format check for `experiments/w2e3`: pass.
- Repository checker: pass for 8,618 tracked files after staging.
- Traceability checker: pass for 7 milestones.
- `git diff --cached --check`: pass.
- Final staged scope: this report plus the 12 files under `experiments/w2e3`;
  no production module, product test, decision record, or execution-state file.
- Full approved pytest surface, valid retry with explicit writable basetemp:
  481 passed, the same three Windows baseline failures, coverage 93.81%.
- First pytest attempt: environment-invalid, 401 passed / 83 setup errors because
  the sandbox could not access `C:\Users\fores\AppData\Local\Temp\pytest-of-fores`;
  it is not used as regression evidence.
- Production `src/caselinker` and repository tests were not changed.

The three baseline failures remain:

1. POSIX-versus-Windows external-path separator rendering.
2. Windows symlink creation privilege (`WinError 1314`).
3. Windows N-Triples canonical ordering changes the expected failure message.

Packet identity and staged diff scope were rechecked after packaging. The
evidence commit identity and final clean-tree state are reported at handoff.

## Next gate

This builder report does not unlock W2-E4. A reviewer who did not build or
repair W2-E3 must perform the required read-only checkpoint. Any continuation
then requires a separate explicit human decision.
