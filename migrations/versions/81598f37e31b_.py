"""empty message

Revision ID: 81598f37e31b
Revises: 
Create Date: 2019-02-22 01:51:41.791658

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '81598f37e31b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('card_number', sa.String(length=250), nullable=False),
    sa.Column('birth_day', sa.DateTime(), nullable=False),
    sa.Column('gender', sa.String(length=250), nullable=False),
    sa.Column('phone_number', sa.String(length=250), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('card_number')
    )
    op.drop_table('t1')
    op.drop_table('eglen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eglen',
    sa.Column('id', mysql.INTEGER(display_width=11, unsigned=True), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('t1',
    sa.Column('jdoc', mysql.JSON(), nullable=True),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('patient')
    # ### end Alembic commands ###
