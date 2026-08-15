# Slice A — versioned contract kernel

**Wave:** 1  
**State:** implemented (kernel validator + envelope schema)  
**Requirements:** CONST-015, CONST-018, GOV-002  
**Distinctions:** a document is not valid merely because it is JSON; unknown security-sensitive fields fail closed

## Acceptance contract

1. A versioned envelope with `schema_version`, `contract_kind`, and a declared payload is accepted.
2. Missing required fields, wrong types, and unknown properties are rejected with a typed `ContractError`.
3. `schema_version` other than the pinned `1.0` is rejected.
4. Validation does not require a database, network, or clock.

## Invalid / adversarial examples (must reject)

- extra property `internal_note` on the envelope
- missing `contract_kind`
- `schema_version: "2.0"`
- non-object instance

## Tests that must fail before implementation

`tests/unit/v4/test_contract_kernel.py`

## Smallest surface

`schemas/v4/envelope-v1.schema.json` plus `caselinker.v4_contracts.validate_instance`.
