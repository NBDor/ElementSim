"""Initial schema

Revision ID: 001
Revises: 
Create Date: 2024-04-27

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Elements table
    op.create_table('elements',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('type', sa.String(), nullable=True),
        sa.Column('properties', sa.JSON(), nullable=True),
        sa.Column('rarity', sa.Float(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('discovery_year', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_elements_id'), 'elements', ['id'], unique=False)
    op.create_index(op.f('ix_elements_name'), 'elements', ['name'], unique=True)
    
    # Recipes table
    op.create_table('recipes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('process_type', sa.String(), nullable=True),
        sa.Column('difficulty', sa.Integer(), nullable=True),
        sa.Column('ingredients', sa.JSON(), nullable=True),
        sa.Column('result_element_id', sa.Integer(), nullable=True),
        sa.Column('result_quantity', sa.Float(), nullable=True),
        sa.Column('processing_time', sa.Integer(), nullable=True),
        sa.Column('tools_required', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('temperature_required', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['result_element_id'], ['elements.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recipes_id'), 'recipes', ['id'], unique=False)
    op.create_index(op.f('ix_recipes_name'), 'recipes', ['name'], unique=True)
    
    # Processes table
    op.create_table('processes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('tools', sa.ARRAY(sa.String()), nullable=True),
        sa.Column('effects', sa.JSON(), nullable=True),
        sa.Column('discovery_year', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_processes_id'), 'processes', ['id'], unique=False)
    op.create_index(op.f('ix_processes_name'), 'processes', ['name'], unique=True)
    
    # Inventories table
    op.create_table('inventories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('items', sa.JSON(), nullable=True),
        sa.Column('last_updated', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventories_id'), 'inventories', ['id'], unique=False)
    op.create_index(op.f('ix_inventories_user_id'), 'inventories', ['user_id'], unique=True)


def downgrade() -> None:
    op.drop_table('inventories')
    op.drop_table('processes')
    op.drop_table('recipes')
    op.drop_table('elements')
