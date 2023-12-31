"""empty message

Revision ID: 3e8b33d501d1
Revises: afa300087a25
Create Date: 2023-11-25 02:05:26.034619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e8b33d501d1'
down_revision: Union[str, None] = 'afa300087a25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sex',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=90), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('athletes', sa.Column('sex_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'athletes', 'sex', ['sex_id'], ['id'], ondelete='SET NULL')
    op.add_column('race_results', sa.Column('athlete_id', sa.Integer(), nullable=False))
    op.add_column('race_results', sa.Column('bib_number', sa.String(length=90), nullable=False))
    op.alter_column('race_results', 'result_place',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('race_results', 'result_points',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('race_results_race_id_fkey', 'race_results', type_='foreignkey')
    op.drop_constraint('race_results_user_id_fkey', 'race_results', type_='foreignkey')
    op.create_foreign_key(None, 'race_results', 'races', ['race_id'], ['id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'race_results', 'athletes', ['athlete_id'], ['id'], ondelete='RESTRICT')
    op.drop_column('race_results', 'user_id')
    op.drop_constraint('races_race_class_id_fkey', 'races', type_='foreignkey')
    op.create_foreign_key(None, 'races', 'race_classes', ['race_class_id'], ['id'], ondelete='RESTRICT')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'races', type_='foreignkey')
    op.create_foreign_key('races_race_class_id_fkey', 'races', 'race_classes', ['race_class_id'], ['id'], ondelete='SET NULL')
    op.add_column('race_results', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'race_results', type_='foreignkey')
    op.drop_constraint(None, 'race_results', type_='foreignkey')
    op.create_foreign_key('race_results_user_id_fkey', 'race_results', 'athletes', ['user_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('race_results_race_id_fkey', 'race_results', 'races', ['race_id'], ['id'], ondelete='SET NULL')
    op.alter_column('race_results', 'result_points',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('race_results', 'result_place',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('race_results', 'bib_number')
    op.drop_column('race_results', 'athlete_id')
    op.drop_constraint(None, 'athletes', type_='foreignkey')
    op.drop_column('athletes', 'sex_id')
    op.drop_table('sex')
    # ### end Alembic commands ###
