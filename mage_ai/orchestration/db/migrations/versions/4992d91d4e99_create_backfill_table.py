"""Create Backfill table

Revision ID: 4992d91d4e99
Revises: 6aecc9bc451c
Create Date: 2023-01-25 00:14:00.643040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4992d91d4e99'
down_revision = '6aecc9bc451c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backfill',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('block_uuid', sa.String(length=255), nullable=True),
    sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('end_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('failed_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('interval_type', sa.Enum('SECOND', 'MINUTE', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR', 'CUSTOM', name='intervaltype'), nullable=True),
    sa.Column('interval_units', sa.Integer(), nullable=True),
    sa.Column('metrics', sa.JSON(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('pipeline_schedule_id', sa.Integer(), nullable=True),
    sa.Column('pipeline_uuid', sa.String(length=255), nullable=True),
    sa.Column('start_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('started_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('status', sa.Enum('INITIAL', 'RUNNING', 'COMPLETED', 'FAILED', 'CANCELLED', name='status'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('variables', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['pipeline_schedule_id'], ['pipeline_schedule.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pipeline_run', sa.Column('backfill_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pipeline_run', 'backfill', ['backfill_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pipeline_run', type_='foreignkey')
    op.drop_column('pipeline_run', 'backfill_id')
    op.drop_table('backfill')
    # ### end Alembic commands ###
