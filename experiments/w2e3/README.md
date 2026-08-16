# W2-E3 disposable experiment

This namespace tests the frozen W2-E3 supplied-decision mechanism and performs
the separate read-only P9 observation. It is not a production policy engine,
does not define real audiences or lawful bases, and must not be promoted into
`src/caselinker`.

The harness stages only the SUT files and input fixture in a temporary directory.
It hashes the oracle as bytes before launch but does not deserialize it until the
SUT has completed and its output has been captured.

Run from the repository root:

```text
python -B experiments/w2e3/harness/run_w2e3.py
```

The underlying SUT interface is:

```text
python -B experiments/w2e3/sut/driver.py --fixture <input_fixture.json> --output <sut_output.json>
```

Only `--fixture` and `--output` are accepted. The oracle is never a SUT argument.
