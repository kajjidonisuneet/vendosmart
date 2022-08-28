"""craeting table

Revision ID: 500aaef0a7aa
Revises: 
Create Date: 2022-08-26 20:52:33.925431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '500aaef0a7aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vendor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('location', sa.String(length=128), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('skills', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vendor_location'), 'vendor', ['location'], unique=False)
    op.create_index(op.f('ix_vendor_name'), 'vendor', ['name'], unique=False)
    op.create_index(op.f('ix_vendor_rating'), 'vendor', ['rating'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vendor_rating'), table_name='vendor')
    op.drop_index(op.f('ix_vendor_name'), table_name='vendor')
    op.drop_index(op.f('ix_vendor_location'), table_name='vendor')
    op.drop_table('vendor')
    # ### end Alembic commands ###