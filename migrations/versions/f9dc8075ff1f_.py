"""empty message

Revision ID: f9dc8075ff1f
Revises: b220a2fa7f3f
Create Date: 2016-10-13 15:37:25.763753

"""

# revision identifiers, used by Alembic.
revision = 'f9dc8075ff1f'
down_revision = 'b220a2fa7f3f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###
