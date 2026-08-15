# Wave 1 contract layer map

**Label:** proposal. Not a running system.

| Concern | Where it lives | Not here |
|---|---|---|
| Shape, required fields, unknown properties | `schemas/v4/*.schema.json` | UI |
| Bitemporal / hypothesis / disclosure invariants | `x-caselinker-invariants` in those schemas | Policy text |
| Fail-closed evaluation | `caselinker.v4_contracts.validate_instance` | Repositories, HTTP |
| Transaction grain | `POSTGRES_LOGICAL_MODEL.md` (logical) | Applied migrations |
| Policy content, IdP, tenancy choice | blocked OD-003/005/007 | These contracts |
