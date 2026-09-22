from app.db.models import Membership, Tenant, User


def test_identity_models_have_expected_tables() -> None:
    assert Tenant.__tablename__ == "tenants"
    assert User.__tablename__ == "users"
    assert Membership.__tablename__ == "memberships"
    assert "uq_memberships_tenant_user" in {c.name for c in Membership.__table__.constraints if c.name}
