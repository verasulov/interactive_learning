from src.routers.api.v1.script.router_path import router_path_v1_script
from src.controllers.scripts.get import get_scripts
from bottle import route, response, abort, HTTPError
from src.lib.json import json_encode
from src.helper import print_exception


@route(router_path_v1_script + '/<script_id:int>', method='GET')
def router_v1_get_script(script_id: int):
    response.headers['Content-Type'] = 'application/json'
    try:
        scripts = get_scripts(['=', 'id', script_id], {})
        if len(scripts) == 0:
            abort(404, 'empty_data')
        script = scripts[0]
        return json_encode({
            'id': script['id'],
            'name': script['name'],
            'status': script['status'],
            'version': script['version'],
            'nodes': script['values']['nodes'],
            'edges': script['values']['edges']
        })
    except HTTPError as e:
        raise e
    except Exception as e:
        print_exception(e)
        abort(500)
