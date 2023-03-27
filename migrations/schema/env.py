from __future__ import with_statement
from alembic import context
from logging.config import fileConfig
import sys
sys.path.append('../')

from migrations.schema.version_table_name import version_table_name

# import models for databeses
from src.models.Action import Action
from src.models.HistoryScript import HistoryScript
from src.models.Log import Log
from src.models.Organization import Organization
from src.models.Right import Right
from src.models.Role import Role
from src.models.RoleRight import RoleRight
from src.models.RunningAction import RunningAction
from src.models.RunningScript import RunningScript
from src.models.Script import Script
from src.models.ScriptOrganization import ScriptOrganization
from src.models.ScriptUser import ScriptUser
from src.models.User import User
from src.models.UserOrganization import UserOrganization
from src.models.UserRole import UserRole

models = [
    Action.__tablename__,
    HistoryScript.__tablename__,
    Log.__tablename__,
    Organization.__tablename__,
    Right.__tablename__,
    Role.__tablename__,
    RoleRight.__tablename__,
    RunningAction.__tablename__,
    RunningScript.__tablename__,
    Script.__tablename__,
    ScriptOrganization.__tablename__,
    ScriptUser.__tablename__,
    User.__tablename__,
    UserOrganization.__tablename__,
    UserRole.__tablename__
]

from configs.config import config as my_config
from src.helper import get_pg_engine, Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata


target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
# Для ислючений нескольких миграций


def include_name(name, type_, parent_names):
    if type_ == 'table':
        return name not in [] and name in models
    return True


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, version_table=version_table_name)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    pg_config = my_config['database']
    connectable = get_pg_engine(
        user=pg_config['user'],
        password=pg_config['pass'],
        host=pg_config['host'],
        port=pg_config['port'],
        base=pg_config['base'],
        app_name=pg_config['app_name'],
        type_engine=pg_config['type'],
        pool_recycle=None
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table=version_table_name,
            include_name=include_name
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
