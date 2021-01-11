"""empty message

Revision ID: 2d6b3218f4eb
Revises: 2aeeefa31503
Create Date: 2021-01-11 15:32:27.095792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d6b3218f4eb'
down_revision = '2aeeefa31503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('occurred_on', sa.DateTime(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_storages_description'), 'storages', ['description'], unique=True)
    op.create_table('credit_events',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('occurred_on', sa.DateTime(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('storage_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['storage_id'], ['storages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_credit_events_description'), 'credit_events', ['description'], unique=False)
    op.create_table('debit_events',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('occurred_on', sa.DateTime(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('storage_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['storage_id'], ['storages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_debit_events_description'), 'debit_events', ['description'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_debit_events_description'), table_name='debit_events')
    op.drop_table('debit_events')
    op.drop_index(op.f('ix_credit_events_description'), table_name='credit_events')
    op.drop_table('credit_events')
    op.drop_index(op.f('ix_storages_description'), table_name='storages')
    op.drop_table('storages')
    # ### end Alembic commands ###
