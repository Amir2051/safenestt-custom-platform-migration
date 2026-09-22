# SafeNestT Custom Platform Architecture

## Purpose

This document defines the initial architecture for replacing the Base44 backend without changing the existing customer-facing application until each migration stage is verified.

## Boundaries

- `base44-safenest-hermes`: current SafeNestT application and behavioral source of truth.
- `safenestt-custom-platform-migration`: new custom backend, database, authorization, storage abstractions, admin services, billing services, and integration layer.
- `safenestt-ai-agency`: independent Hermes investigation engine.

## Non-negotiables

- Authorization is enforced server-side.
- Tenant isolation is enforced at the database boundary with PostgreSQL RLS where applicable.
- Frontend filtering is never a security boundary.
- Secrets are supplied through environment/secret management.
- Migration proceeds domain-by-domain with automated tests and reconciliation.

## Initial stack

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy 2.x
- Alembic
- Argon2id password hashing
- JWT access/refresh tokens
- Pytest

## First implementation sequence

1. Configuration and CI
2. Database connection and migration framework
3. Users / tenants / roles
4. Authentication and session security
5. Cases and RLS
6. Evidence and storage
7. Hermes API client
8. Remaining product services
