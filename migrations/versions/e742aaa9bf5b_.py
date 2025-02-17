"""empty message

Revision ID: e742aaa9bf5b
Revises: fc2a3bd245a3
Create Date: 2023-02-25 14:39:55.158797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e742aaa9bf5b'
down_revision = 'fc2a3bd245a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))
        batch_op.drop_column('pass_word')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pass_word', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###
