# SafeNestT Migration Plan

## Rule

Do not remove or disable Base44 until the replacement for a domain is implemented, tested, migrated, reconciled, and exercised end-to-end.

## Domain migration contract

For every migrated domain:

1. Inventory the current Base44 behavior and data model.
2. Define the custom API contract.
3. Define the PostgreSQL schema and authorization model.
4. Implement automated unit/integration/security tests.
5. Build migration tooling and reconciliation checks.
6. Connect the existing frontend through an adapter or controlled switch.
7. Verify production-like workflows.
8. Record cutover criteria.
9. Only then retire the Base44 dependency for that domain.

## Initial milestones

- [ ] Foundation and CI
- [ ] PostgreSQL and Alembic
- [ ] Auth
- [ ] Users/roles/tenants
- [ ] Cases + RLS
- [ ] Evidence/files
- [ ] Admin
- [ ] Hermes integration
- [ ] Billing/notifications/integrations
- [ ] Data migration
- [ ] Full E2E/security verification
- [ ] Base44 removal
