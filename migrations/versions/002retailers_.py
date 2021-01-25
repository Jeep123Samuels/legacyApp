"""empty message

Revision ID: 002retailers
Revises: users
Create Date: 2020-12-22 08:40:23.888571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002retailers'
down_revision = '001users'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('retailer', sa.String(length=225), nullable=True),
    sa.Column('slug', sa.String(length=225), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('image_url')
    )
    op.create_index(op.f('ix_products_description'), 'products', ['description'], unique=True)
    op.create_index(op.f('ix_products_slug'), 'products', ['slug'], unique=True)
    op.create_table('retailers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=225), nullable=False),
    sa.Column('location', sa.String(length=225), nullable=True),
    sa.Column('contact_no', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shoplists',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=225), nullable=False),
    sa.Column('status', sa.Enum('active', 'completed', 'inactive', 'incomplete', name='shoplistsstatus'), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_lists_products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Enum('bought', 'not_found', 'searching', name='userproductstatus'), nullable=False),
    sa.Column('products_id', sa.Integer(), nullable=True),
    sa.Column('shoplists_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['shoplists_id'], ['shoplists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_lists_products')
    op.drop_table('shoplists')
    op.drop_table('retailers')
    op.drop_index(op.f('ix_products_slug'), table_name='products')
    op.drop_index(op.f('ix_products_description'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###