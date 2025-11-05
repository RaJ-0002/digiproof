# backend/app/db/alembic/env.py

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# 1) this line lets Alembic read the values in alembic.ini
config = context.config  

# 2) optional: set up Python logging based on Alembic’s fileConfig
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 3) import your models so they get registered into SQLModel.metadata
from sqlmodel import SQLModel
from backend.app.models.user import User
# (and similarly import Project, AIProfile, etc. here)

# 4) hook up your models’ metadata
target_metadata = SQLModel.metadata

def run_migrations_offline():
    """Generate SQL scripts without connecting to the database."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, 
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations by connecting to the live database."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# 5) choose online or offline based on how Alembic was invoked
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
