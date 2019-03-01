"""empty message

Revision ID: cdad2e31c9dd
Revises: c17c7bb33627
Create Date: 2019-02-28 19:16:17.123770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdad2e31c9dd'
down_revision = 'c17c7bb33627'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctor', sa.Column('email', sa.String(length=250), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doctor', 'email')
    # ### end Alembic commands ###
