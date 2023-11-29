"""empty message

Revision ID: 95cf7d885d75
Revises: bfc6f545fce7
Create Date: 2023-11-28 19:00:40.532963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95cf7d885d75'
down_revision: Union[str, None] = 'bfc6f545fce7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=90), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('athlete_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('athlete_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['athlete_id'], ['athletes.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('result_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('place', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['result_id'], ['race_results.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category_results')
    op.drop_table('athlete_categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
