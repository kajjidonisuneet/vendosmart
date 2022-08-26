"""vendor data table

Revision ID: 8b7e2ff0f653
Revises: 
Create Date: 2022-08-26 18:32:18.210691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b7e2ff0f653'
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
    sa.Column('skill', sa.String(length=128), nullable=False),
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
