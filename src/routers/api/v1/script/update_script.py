from src.routers.api.v1.script.router_path import router_path_v1_script
from src.controllers.scripts.update import update_scripts
from src.controllers.scripts.get import get_scripts
from bottle import route, response, abort, HTTPError, request
from src.lib.json import json_encode, json_decode
from src.helper import print_exception


@route(router_path_v1_script + '/<script_id:int>', method='PUT')
def router_v1_update_script(script_id: int):
    response.headers['Content-Type'] = 'application/json'
    try:
        scripts = get_scripts(['=', 'id', script_id], {})
        if len(scripts) == 0:
            abort(404, 'empty_data')
        script = scripts[0]
        version = script['version'] + 1
        data_script = json_decode(request.body.read())
        update_data = {}
        update_data_values = {}
        if 'name' in data_script:
            update_data['name'] = data_script['name']
        if 'description' in data_script:
            update_data_values['description'] = data_script['description']
        if 'nodes' in data_script:
            update_data_values['nodes'] = data_script['nodes']
        if 'edges' in data_script:
            update_data_values['edges'] = data_script['edges']
        if len(update_data_values.keys()) > 0:
            update_data['values'] = {
                **script['values'],
                **update_data_values
            }
        if len(update_data.keys()) == 0:
            abort(400, 'not_params_for_update')
        update_data['version'] = version
        update_scripts([{
            'filter': ['=', 'id', script_id],
            'values': update_data
        }])
        return json_encode({
            'id': script_id,
            'version': version
        })
    except HTTPError as e:
        raise e
    except Exception as e:
        print_exception(e)
        abort(500)
