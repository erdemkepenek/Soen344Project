"""empty message

Revision ID: aafceb3e7794
Revises: 
Create Date: 2019-04-03 22:24:26.367215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aafceb3e7794'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nurse',
    sa.Column('access_id', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('last_name', sa.String(length=250), nullable=False),
    sa.Column('first_name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('clinic_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['clinic_id'], ['clinics.clinic_id'], ),
    sa.PrimaryKeyConstraint('access_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nurse')
    # ### end Alembic commands ###