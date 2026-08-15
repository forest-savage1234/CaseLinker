# Slice B — bitemporal time, identities, transitions

**Requirements:** CONST-003, CONST-004, CONST-017, TEMP-001, TEMP-002, TEMP-003  
**Distinctions:** event time is not knowledge time; silent overwrite is not a legal transition

## Acceptance contract

1. A bitemporal interval with event/valid time, knowledge time, and declared precision is accepted.
2. Knowledge time used as event time, inverted intervals, and invented day precision are rejected.
3. Stable ids match opaque prefixes (`asrt_`, `docv_`, `rvw_`, `dep_`, `evt_`).
4. Only listed state transitions are legal; others fail closed.

## Tests that must fail before implementation

`tests/unit/v4/test_bitemporal_identity.py`
