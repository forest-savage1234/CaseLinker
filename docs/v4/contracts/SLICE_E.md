# Slice E — projections, audit/AI provenance, logical Postgres

**Requirements:** CONST-008, CONST-016, CONST-017, AI-001, AI-002, OPS-001  
**Distinctions:** a projection is not a source of truth; AI cannot publish  
**Blocked:** OD-008 infrastructure selection; no executable migration

## Acceptance contract

1. A projection artifact with `authoritative: false` is accepted.
2. `authoritative: true` is rejected.
3. An AI execution record may be `proposed`; `published` is rejected.
4. PostgreSQL work is a markdown logical analysis only.

## Tests

`tests/unit/v4/test_projection_provenance.py`
