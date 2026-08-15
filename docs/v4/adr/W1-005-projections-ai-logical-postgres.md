# W1-005: Projections, AI provenance, logical PostgreSQL analysis

- **Status:** Proposed
- **Scope:** CaseLinker v4 research-network proposal only
- **Upstream:** not accepted
- **Unresolved authorities:** OD-008 (infrastructure, RPO/RTO, hosting)

## Decision

Projection artifacts are content-addressed and non-authoritative. AI execution records cannot have disposition `published`. PostgreSQL is described only as a logical constraint/transaction note in `docs/v4/architecture/POSTGRES_LOGICAL_MODEL.md`. No migration, driver usage, or vendor selection is authorized by this ADR.
