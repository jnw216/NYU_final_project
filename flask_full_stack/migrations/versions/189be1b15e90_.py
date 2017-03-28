"""empty message

Revision ID: 189be1b15e90
Revises: e899251fc6de
Create Date: 2017-03-27 20:54:43.222976

"""

# revision identifiers, used by Alembic.
revision = '189be1b15e90'
down_revision = 'e899251fc6de'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('active_connections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('active_connections', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entry', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ip_analytics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip_address', sa.String(), nullable=True),
    sa.Column('page_views', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('page_views',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('page_views', sa.Integer(), nullable=True),
    sa.Column('page_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visit_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('visit_time', sa.Float(), nullable=True),
    sa.Column('page_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('visit_time_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'visit_time', ['visit_time_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'visit_time_id')
    op.drop_table('visit_time')
    op.drop_table('page_views')
    op.drop_table('ip_analytics')
    op.drop_table('blog_entry')
    op.drop_table('active_connections')
    ### end Alembic commands ###
