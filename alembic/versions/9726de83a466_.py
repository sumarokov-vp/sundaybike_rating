"""empty message

Revision ID: 9726de83a466
Revises: 55780f7cfca0
Create Date: 2023-11-25 02:27:22.093718

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9726de83a466'
down_revision: Union[str, None] = '55780f7cfca0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('race_classes', sa.Column('multiplier', sa.DECIMAL(precision=10, scale=2), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('race_classes', 'multiplier')
    # ### end Alembic commands ###