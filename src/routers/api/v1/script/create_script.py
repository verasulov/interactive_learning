from src.routers.api.v1.script.router_path import router_path_v1_script
from bottle import route, response, abort, HTTPError, request
from src.controllers.scripts.create import create_scripts
from src.lib.json import json_encode, json_decode
from src.helper import print_exception


@route(router_path_v1_script, method='POST')
def router_v1_create_script():
    response.headers['Content-Type'] = 'application/json'
    try:
        data_script = json_decode(request.body.read())
        if 'name' not in data_script or 'nodes' not in data_script or 'edges' not in data_script or 'description' not in data_script:
            abort(400, 'not_enough_params')
        created_scripts = create_scripts([{
            'name': data_script['name'],
            'values': {
                'description': data_script['description'],
                'nodes': data_script['nodes'],
                'edges': data_script['edges']
            }
        }], True)
        if len(created_scripts) == 0:
            abort(500, 'error_script_not_created')
        return json_encode(created_scripts[0])
    except HTTPError as e:
        raise e
    except Exception as e:
        print_exception(e)
        abort(500)
