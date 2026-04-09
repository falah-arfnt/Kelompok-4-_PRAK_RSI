from logging.config import fileConfig
import sys
import os

from sqlalchemy import engine_from_config, pool
from alembic import context

from sqlmodel import SQLModel

# ======================================================
# ADD PATH supaya src bisa kebaca
# ======================================================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ======================================================
# IMPORT SEMUA MODEL (WAJIB supaya masuk metadata)
# ======================================================
from src.database.schema.user import User
from src.database.schema.event import Event
from src.database.schema.registration import Registration
from src.database.schema.account import Account
from src.database.schema.role import Role
from src.database.schema.log import Log

# ======================================================
# Alembic Config
# ======================================================
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ======================================================
# TARGET METADATA (INI YANG DIPAKAI AUTOGENERATE)
# ======================================================
target_metadata = SQLModel.metadata


# ======================================================
# OFFLINE MIGRATION
# ======================================================
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


# ======================================================
# ONLINE MIGRATION
# ======================================================
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


# ======================================================
# RUN MODE
# ======================================================
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()