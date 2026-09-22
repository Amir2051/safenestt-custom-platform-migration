# SafeNestT Custom Platform Migration

This repository is the **dedicated migration and replacement platform for SafeNestT's current Base44 backend**.

It is intentionally separate from the existing SafeNestT application and the Hermes investigation engine so the migration can be developed, tested, and hardened without destabilizing either system.

## Repository roles

| Repository | Purpose |
|---|---|
| `base44-safenest-hermes` | Current SafeNestT customer-facing application. Base44 remains in place here during migration. |
| `safenestt-ai-agency` | SafeNestT AI Agency / Hermes Investigation Engine. Remains an independent investigation service. |
| `safenestt-custom-platform-migration` | This repository. Builds the custom SafeNestT backend/platform that will eventually replace Base44. |

## Migration goal

Build a **fully custom SafeNestT platform** with no dependency on Base44 for:

- Database
- Authentication
- Authorization and permissions
- Row-level security / tenant isolation
- Backend business logic
- File and evidence storage
- Admin operations
- Billing and subscription logic
- Notifications
- Application integrations
- AI/investigation orchestration

The existing frontend will initially remain usable while backend capabilities are migrated underneath it. Base44 will only be removed after the replacement has passed functional, security, data-integrity, and end-to-end verification.

## Target architecture

```
SafeNestT React Frontend
        |
        v
Custom SafeNestT Platform
        |
        +-- Authentication
        +-- Users / Roles / Tenants
        +-- PostgreSQL
        +-- RLS / Tenant Isolation
        +-- Cases
        +-- Evidence / Files
        +-- Admin
        +-- Billing
        +-- Notifications
        |
        v
Hermes / AI Agency
(Amir2051/safenestt-ai-agency)
```

## Core engineering principles

1. **Isolation first** — this repository must not destabilize the current production application.
2. **Server-side authorization** — permissions and case ownership must never depend on frontend filtering.
3. **Tenant isolation by design** — users must only be able to access data authorized for their tenant/account.
4. **Incremental migration** — replace capabilities one domain at a time.
5. **Backward compatibility during transition** — Base44 remains available until its replacement is verified.
6. **No secrets in source control** — credentials belong in environment/secret-management systems.
7. **Test before cutover** — every migrated domain needs automated tests plus end-to-end verification.
8. **Auditability** — migration decisions, schema changes, security controls, and cutover steps are documented.

## Planned migration phases

### Phase 1 — Foundation
- Repository structure
- Application configuration
- API foundation
- Development/test environment
- CI

### Phase 2 — Database
- PostgreSQL schema
- SQLAlchemy models
- Alembic migrations
- Indexes and constraints
- Audit fields

### Phase 3 — Authentication
- User registration/login
- Access and refresh tokens
- Password hashing
- Session/token revocation
- Authentication tests

### Phase 4 — Users, roles, and tenants
- User profiles
- Organizations/tenants
- Roles
- Permissions
- Memberships
- Server-side authorization

### Phase 5 — Cases and security isolation
- Cases
- Case ownership
- Case status
- Case metadata
- PostgreSQL RLS
- Direct-object access tests
- Cross-user and cross-tenant isolation tests

### Phase 6 — Evidence and storage
- Evidence records
- File metadata
- Secure object storage abstraction
- Evidence access control
- Case timeline

### Phase 7 — Administration
- Admin APIs
- User administration
- Case administration
- Audit logs
- Operational controls

### Phase 8 — Hermes integration
- Hermes API client
- Investigation creation/start/status
- Findings
- Reports
- Callback handling
- Authentication and signature verification
- Failure/retry behavior

### Phase 9 — Product services
- Billing/subscriptions
- Notifications
- External integrations
- Additional SafeNestT services

### Phase 10 — Data migration
- Base44 data inventory
- Field mapping
- Data transformation
- Migration tooling
- Reconciliation
- Import verification

### Phase 11 — End-to-end verification
- Frontend integration
- Authentication flows
- Case workflows
- Evidence workflows
- Admin workflows
- Hermes investigations
- Security/RLS tests
- Regression tests
- Production readiness review

### Phase 12 — Cutover
- Freeze/migration window
- Final data reconciliation
- Frontend backend switch
- Production monitoring
- Base44 dependency removal
- Decommissioning plan

## Security requirements

SafeNestT handles sensitive case and investigation information. The custom platform therefore treats authorization as a backend/database responsibility.

At minimum, the platform must defend against:

- Reading another user's case by ID
- Searching for another user's cases
- Guessing or enumerating object identifiers
- Accessing another tenant's records
- Unauthorized evidence access
- Unauthorized timeline/notes access
- Privilege escalation
- Admin endpoint abuse
- Token/session misuse

RLS and application-layer authorization must work together rather than relying on frontend visibility rules.

## Hermes relationship

Hermes is **not being rebuilt here**.

The Hermes / AI Agency repository remains an independent service:

`Amir2051/safenestt-ai-agency`

This repository will integrate with Hermes through a documented API boundary. That separation allows the investigation engine to continue evolving independently while SafeNestT's main platform is migrated away from Base44.

## Current status

**Migration repository created.**

The next implementation work will establish the backend foundation, database architecture, authentication model, and tenant/RLS model before feature-by-feature migration begins.

## Important boundary

Do **not** treat this repository as a copy of the current Base44 application.

The current application is the source of truth for existing product behavior and requirements. This repository is the source of truth for the **new custom implementation**.

Changes here should not require modifying or deleting the existing Base44 integration until a migration phase is explicitly ready for verification.

## License

Private project code for SafeNestT.