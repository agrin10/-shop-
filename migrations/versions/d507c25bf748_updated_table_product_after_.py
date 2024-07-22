"""updated table product after disconnection

Revision ID: d507c25bf748
Revises: 
Create Date: 2024-07-21 16:40:55.902597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd507c25bf748'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.String(length=225), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),  # Remove the length parameter
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image_path', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###