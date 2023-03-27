from src.routers.api.v1.scripts.router_path import router_path_v1_scripts
from src.controllers.scripts.get import get_scripts
from bottle import route, response, abort, HTTPError, request
from src.lib.json import json_encode, json_decode
from src.helper import print_exception


@route(router_path_v1_scripts, method='GET')
def router_v1_get_scripts():
    response.headers['Content-Type'] = 'application/json'
    try:
        params = request.params
        if 'filter' not in params:
            abort(400, 'filter_not_found')
        if 'options' not in params:
            abort(400, 'options_not_found')
        query_filter = json_decode(params.getunicode('filter'))
        options = json_decode(params.getunicode('options'))
        scripts = get_scripts(query_filter, options)
        return json_encode([{
            'id': script['id'],
            'name': script['name'],
            'status': script['status'],
            'version': script['version']
        } for script in scripts])
    except HTTPError as e:
        raise e
    except Exception as e:
        print_exception(e)
        abort(500)
