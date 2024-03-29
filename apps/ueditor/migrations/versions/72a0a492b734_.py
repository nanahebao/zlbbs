"""empty message

Revision ID: 72a0a492b734
Revises: 750e2e17dc28
Create Date: 2020-04-10 20:11:03.374389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72a0a492b734'
down_revision = '750e2e17dc28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('highlight_post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('highlight_post')
    # ### end Alembic commands ###
