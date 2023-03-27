from bottle import default_app, debug, BaseRequest
from configs.config import config
from beaker.middleware import SessionMiddleware
from src.helper import get_dsn_connect

BaseRequest.MEMFILE_MAX = 1024 * 1024
debug(config.get('debug', False))

app = default_app()
app.config.load_dict(config, make_namespaces=True)

session_opts = {
    'session.type': 'ext:database',
    'session.url': get_dsn_connect(),
    'session.schema_name': 'sessions',
    'session.cookie_expires': 4 * 60 * 60,
    'session.path': '/'
}
middleware_app = SessionMiddleware(app, session_opts)
