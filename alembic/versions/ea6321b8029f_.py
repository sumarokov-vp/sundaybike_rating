"""empty message

Revision ID: ea6321b8029f
Revises: 24a4b6c82df6
Create Date: 2023-12-07 13:38:59.645244

"""
# Standard Library
from typing import (
    Sequence,
    Union,
)

# Third Party Stuff
import sqlalchemy as sa

# My Stuff
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ea6321b8029f"
down_revision: Union[str, None] = "24a4b6c82df6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "athletes",
        sa.Column(
            "category_id", sa.Integer(), server_default=sa.text("3"), nullable=False
        ),
    )
    op.create_foreign_key(
        None, "athletes", "categories", ["category_id"], ["id"], ondelete="RESTRICT"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "athletes", type_="foreignkey")
    op.drop_column("athletes", "category_id")
    # ### end Alembic commands ###