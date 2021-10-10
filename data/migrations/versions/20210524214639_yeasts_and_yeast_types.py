"""yeasts and yeast types

Revision ID: 2d53265df36c
Revises: 7e691fd595e3
Create Date: 2021-05-24 21:46:39.369382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2d53265df36c"
down_revision = "7e691fd595e3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "yeast_types",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_date",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "modified_date",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "yeasts",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "created_date",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "modified_date",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column("brand", sa.String(length=256), nullable=True),
        sa.Column("ideal_low_temp", sa.Integer(), nullable=False),
        sa.Column("ideal_high_temp", sa.Integer(), nullable=False),
        sa.Column("min_low_temp", sa.Integer(), nullable=True),
        sa.Column("max_high_temp", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(length=1024), nullable=True),
        sa.Column("yeast_type_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["yeast_type_id"], ["yeast_types.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "ingredient_types",
        sa.Column("table_name", sa.String(length=256), nullable=True),
    )
    op.add_column(
        "ingredient_types",
        sa.Column("class_name", sa.String(length=256), nullable=True),
    )
    op.add_column(
        "ingredients", sa.Column("description", sa.String(length=1024), nullable=True)
    )
    op.add_column("ingredients", sa.Column("class_id", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("ingredients", "class_id")
    op.drop_column("ingredients", "description")
    op.drop_column("ingredient_types", "class_name")
    op.drop_column("ingredient_types", "table_name")
    op.drop_table("yeasts")
    op.drop_table("yeast_types")
    # ### end Alembic commands ###