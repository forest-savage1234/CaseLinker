# Slice C — source lineage and hypotheses

**Requirements:** CONST-006, CONST-007, RESOLVE-001…005  
**Distinctions:** similarity is not identity; derivation is not corroboration; no blind transitivity

## Acceptance contract

1. A source-family derivation record is accepted.
2. Labeling same-family copies as independent corroboration is rejected.
3. An identity hypothesis may be `possibly_same` with positive and negative evidence.
4. `creates_canonical_identity: true` and `inference_method: transitive_closure` are rejected.

## Tests

`tests/unit/v4/test_lineage_hypotheses.py`
