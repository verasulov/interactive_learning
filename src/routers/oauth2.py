from bottle import route, response, request, HTTPResponse, redirect, abort
from src.lib.json import json_decode
from datetime import datetime
from src.server import app
from src.controllers.users.get import get_users
from src.controllers.users.create import create_users
import requests
import base64


@route('/oauth2/logout', method='GET')
def oauth2_logout(redirect_page: str = None):
    beaker_session = request.environ.get('beaker.session')
    oauth2_data = beaker_session['oauth2_data'] if 'oauth2_data' in beaker_session else None
    if oauth2_data is not None and oauth2_data:
        params = '?access_token=' + oauth2_data['access_token'] + '&refresh_token=' + oauth2_data['refresh_token']
        logout_uri = app.config.get('oauth2.logout_uri', '') + params
        requests.get(logout_uri, allow_redirects=False, timeout=5)
    beaker_session.delete()
    if redirect_page:
        redirect('/oauth2/login?redirect_page=%s' % redirect_page)
    redirect('/oauth2/login')

# todo вернуть авторизацию
@route('/oauth2/login', method='GET')
def oauth2_login():
    # code = request.query.get('code')
    # redirect_uri = app.config.get('oauth2.redirect_uri')
    # client_id = app.config.get('oauth2.client_id')
    # client_secret = app.config.get('oauth2.client_secret')
    # my_state = ''
    # params = request.params
    # if 'redirect_page' in params:
    #     my_state = base64.b64encode(params.getunicode('redirect_page', '/').encode('ascii')).decode('ascii')
    # if not code:
    #     get_code(client_id, client_secret, redirect_uri, my_state)
    # oauth2_data = get_access_token(code, client_id, redirect_uri, client_secret)
    # user_data = get_user_data(oauth2_data)
    # user_id = user_data['id'] if 'id' in user_data else -1
    # user = get_user(user_id)
    user = get_user(14500)
    # if user is None:
    #     abort(401, 'user_not_found')
    oauth2_redirect_page = '/'
    # state = request.query.get('state')
    # if state:
    #     oauth2_redirect_page = base64.b64decode(state.encode('ascii')).decode('ascii')
    beaker_session = request.environ.get('beaker.session')
    beaker_session.invalidate()
    # beaker_session['oauth2_data'] = oauth2_data
    # beaker_session['user'] = user_data
    beaker_session['user'] = user
    beaker_session['user_data'] = user
    beaker_session['date_update_user'] = datetime.now().timestamp()
    beaker_session['date_auth_user'] = datetime.now().timestamp()
    beaker_session.save()
    redirect(oauth2_redirect_page)


def get_code(client_id: str, client_secret: str, redirect_uri: str, state: str = ''):
    get_params = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': redirect_uri
    }
    auth_uri = app.config.get('oauth2.auth_uri', '') + '?state=%s' % state
    for param in get_params:
        auth_uri += '&' + param + '=' + get_params[param]
    my_redirect(auth_uri)


def get_access_token(code: str, client_id: str, redirect_uri: str, client_secret: str) -> dict:
    token_uri = app.config.get('oauth2.token_uri', '')
    my_response = requests.post(token_uri, data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    })
    if my_response.status_code != 200:
        redirect('/oauth2/token_error')
    return json_decode(my_response.text)


def get_user_data(oauth2_data: dict) -> dict:
    resource_uri = app.config.get('oauth2.resource_uri', '')
    my_response = requests.get(resource_uri, headers={
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': oauth2_data['token_type'] + ' ' + oauth2_data['access_token']
    })
    if my_response.status_code != 200:
        redirect('/oauth2/resource_error')
    return json_decode(my_response.text)


def my_redirect(uri: str):
    code = 303 if request.get('SERVER_PROTOCOL') == 'HTTP/1.1' else 302
    res = response.copy(cls=HTTPResponse)
    res.status = code
    res.body = ''
    res.set_header('Location', uri)
    raise res


def get_user(user_id: int) -> dict or None:
    users = get_users(['=', 'id', user_id], {})

    if len(users) == 0:
        create_users([{
            'id': user_id
        }])
        users = get_users(['=', 'id', user_id], {})
    return users[0]
