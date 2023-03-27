from sqlalchemy.ext.declarative import declarative_base
from functools import lru_cache
from sqlalchemy.engine import Engine, create_engine
from sqlalchemy import inspect
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, session
from configs.config import config as server_config
from datetime import datetime
import logging

Base = declarative_base()


@lru_cache(maxsize=None)
def get_pg_engine(user: str, password: str, host: str, port: str, base: str, app_name: str,
                  type_engine: str, pool_recycle: int) -> Engine:
    dsn = type_engine + '://' + user + ':' + password + '@' + host + ':' + '' + str(port) + '/' + base
    if type_engine == 'mysql+pymysql':
        dsn += '?charset=utf8'
        return create_engine(dsn, pool_recycle=pool_recycle)
    if type_engine == 'postgresql':
        dsn += '?application_name=' + app_name
        return create_engine(dsn, connect_args={'application_name': app_name})
    return create_engine(dsn)


def get_connection_config(name: str = 'database') -> dict:
    return server_config.get(name, {})


@contextmanager
def get_session(config: dict = None) -> session:
    if config is None:
        config = get_connection_config()
    engine = get_pg_engine(
        user=config['user'],
        password=config['pass'],
        host=config['host'],
        port=config['port'],
        base=config['base'],
        app_name=config['app_name'],
        type_engine=config['type'],
        pool_recycle=config['pool_recycle'] if 'pool_recycle' in config else None
    )
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    yield s
    s.close()


def object_as_dict(obj) -> dict:
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


def get_dsn_connect(config: dict = None) -> str:
    if config is None:
        config = get_connection_config()
    user = config['user']
    password = config['pass']
    host = config['host']
    port = config['port']
    base = config['base']
    app_name = config['app_name']
    type_engine = config['type']
    dsn = type_engine + '://' + user + ':' + password + '@' + host + ':' + str(port) + '/' + base
    if type_engine == 'mysql+pymysql':
        dsn += '?charset=utf8'
    if type_engine == 'postgresql':
        dsn += '?application_name=' + app_name
    return dsn


def print_exception(exception: Exception, function_name: str = ''):
    text = str(datetime.now()) + '\tException service method\t' + function_name
    root_logger = logging.getLogger()
    root_logger.error(text, exc_info=exception)
