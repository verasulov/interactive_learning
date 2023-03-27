"""sessions beaker storage

Revision ID: 6171e0b5bc5f
Revises: d00f4c492448
Create Date: 2022-05-09 13:14:07.837197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6171e0b5bc5f'
down_revision = 'd00f4c492448'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""create schema sessions;""")


def downgrade():
    op.execute("""drop schema sessions;""")
