from bottle import hook, request, abort
from src.lib.json import json_decode
from datetime import datetime
from src.server import app
from src.routers.oauth2 import oauth2_logout, get_user
import requests


@hook('before_request')
def before_request():
    print(request.path)
    beaker_session = request.environ.get('beaker.session')
    authorization = request.headers.get('Authorization', None)
    if authorization and '/api/app/v' in request.path:
        if 'Token' not in authorization:
            abort(401, 'Unauthorized')
        split_authorization = authorization.split(' ')
        if len(split_authorization) != 2:
            abort(401, 'Unauthorized')
        if app.config.get('api_app_token') != split_authorization[1]:
            abort(401, 'Unauthorized')
        return
    if authorization and '/api/v' in request.path:
        if 'Bearer' not in authorization:
            abort(401, 'Unauthorized')
        return
    not_oauth_paths = [
        '/oauth2/'
    ]
    user = beaker_session['user'] if 'user' in beaker_session else None
    not_oauth = True
    for not_oauth_path in not_oauth_paths:
        if not_oauth_path in request.path:
            not_oauth = False
            break
    if not not_oauth:
        return
    if user is None:
        if '/api/' in request.path or '/static/' in request.path:
            abort(401, 'Unauthorized')
        oauth2_logout(request.path or '/')
    else:
        now = datetime.now().timestamp()
        last_update = beaker_session['date_update_user'] if 'date_update_user' in beaker_session else 0
        date_auth_user = beaker_session['date_auth_user'] if 'date_auth_user' in beaker_session else 0
        if now - date_auth_user > 4 * 60 * 60 and now - last_update > 60 * 60:
            if '/api/' in request.path or '/static/' in request.path or '/favicon.ico' in request.path:
                abort(401, 'Unauthorized')
            oauth2_logout()
        if 'user_data' not in beaker_session:
            oauth2_logout()
        app.config['user'] = beaker_session['user_data']
    if 'user' in app.config and 'status' in app.config['user'] and app.config['user']['status'] != 'active':
        status = app.config['user']['status']
        if status == 'blocked':
            abort(403, 'user is blocked')
        elif status == 'deleted':
            abort(403, 'user is deleted')
        oauth2_logout()

