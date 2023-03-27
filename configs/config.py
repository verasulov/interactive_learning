import os

config = {
    'static_path': os.getenv('WEB_STATIC_PATH', 'src'),
    'server': {
        'host': '0.0.0.0',
        'port': os.getenv('SERVICE_PORT', '8081'),
        'server': 'paste',
        'threadpool_workers': 1000,
        'request_queue_size': 500,
        'quiet': True
    },
    'name': os.getenv('NAME', 'interactive_learning'),
    'database': {
        'type': 'postgresql',
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'port': os.getenv('DB_PORT', '5432'),
        'user': os.getenv('DB_USER', 'rve'),
        'pass': os.getenv('DB_PASS', ''),
        'base': os.getenv('DB_NAME', 'interactive_learning'),
        'app_name': os.getenv('APP_NAME', 'interactive_learning'),
        'charset': 'utf8'
    },
    'oauth2': {
        'client_id': os.getenv('OAUTH_CLIENT_ID', 'OAUTH_CLIENT_ID'),
        'client_secret': os.getenv('OAUTH_CLIENT_SECRET', 'OAUTH_CLIENT_SECRET'),
        'key': os.getenv('OAUTH_KEY', 'OAUTH_KEY'),
        'base_uri': os.getenv('OAUTH_BASE_URI', 'OAUTH_BASE_URI'),
        'redirect_uri': os.getenv('OAUTH_REDIRECT_URI', 'OAUTH_REDIRECT_URI'),
        'auth_uri': os.getenv('OAUTH_AUTH_URI', 'OAUTH_AUTH_URI'),
        'token_uri': os.getenv('OAUTH_TOKEN_URI', 'OAUTH_TOKEN_URI'),
        'resource_uri': os.getenv('OAUTH_RESOURCE_URI', 'OAUTH_RESOURCE_URI'),
        'logout_uri': os.getenv('OAUTH_LOGOUT_URI', 'OAUTH_LOGOUT_URI')
    }
}

try:
    __import__('configs.local')
except ImportError:
    pass
else:
    from configs.local import local_config

    config = {
        **config,
        **local_config
    }
