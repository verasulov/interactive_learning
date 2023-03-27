from bottle import route, static_file, template, request, abort
from src.server import app
import os


@route('/sw.js', method='GET')
def get_favicon():
    static_path = app.config.get('static_path')
    return static_file('sw.js', root='web/%s/static/vendors/js/' % static_path)


@route('/static/<filename:path>', method='GET')
def send_static(filename):
    static_path = app.config.get('static_path')
    path = 'web/%s/static/vendors/%s.gz' % (static_path, filename)
    if os.path.exists(path) and 'gzip' in request.headers.get('Accept-Encoding'):
        filename = '%s.gz' % filename
    return static_file(filename, root='web/%s/static/vendors/' % static_path)


@route('/<url:re:.*>', method='GET')
def index(url):
    if 'api/v' in url or 'static/' in url:
        abort(405, 'Not found')
    return template('web/index.html')
