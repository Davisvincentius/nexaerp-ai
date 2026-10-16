
import sqlalchemy as sa
from alembic import op


revision = "001_core_tables"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # 1. Tabel perusahaan
    op.create_table(
        "companies",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("name", sa.String(150), nullable=False),
        sa.Column(
            "slug",
            sa.String(100),
            nullable=False,
            unique=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    # 2. Tabel pengguna
    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column(
            "email",
            sa.String(255),
            nullable=False,
            unique=True,
        ),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    # 3. Relasi pengguna dengan perusahaan
    op.create_table(
        "company_memberships",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column(
            "company_id",
            sa.Uuid(),
            sa.ForeignKey("companies.id"),
            nullable=False,
        ),
        sa.Column(
            "user_id",
            sa.Uuid(),
            sa.ForeignKey("users.id"),
            nullable=False,
        ),
        sa.Column(
            "role",
            sa.String(30),
            nullable=False,
            server_default="viewer",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.UniqueConstraint(
            "company_id",
            "user_id",
            name="uq_company_membership",
        ),
    )

    # 4. Indeks untuk mempercepat pencarian membership
    op.create_index(
        "ix_company_memberships_company_id",
        "company_memberships",
        ["company_id"],
    )

    op.create_index(
        "ix_company_memberships_user_id",
        "company_memberships",
        ["user_id"],
    )


def downgrade():
    # Hapus indeks terlebih dahulu
    op.drop_index(
        "ix_company_memberships_user_id",
        table_name="company_memberships",
    )
    op.drop_index(
        "ix_company_memberships_company_id",
        table_name="company_memberships",
    )

    # Hapus tabel berdasarkan urutan dependensi
    op.drop_table("company_memberships")
    op.drop_table("users")
    op.drop_table("companies")
