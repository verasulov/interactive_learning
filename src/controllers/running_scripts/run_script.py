from src.controllers.running_scripts.create import create_running_scripts
from src.controllers.running_scripts.get import get_running_scripts
from src.controllers.running_actions.create import create_running_actions
from src.controllers.users.get import get_users
from src.controllers.scripts.get import get_scripts
from src.controllers.actions.get import get_actions


def run_script(user_id: int, script_id: int) -> None:
    running_scripts = get_running_scripts([
        'AND',
        ['=', 'user_id', user_id],
        ['=', 'script_id', script_id],
        ['=', 'status', 'active']
    ], {})
    if len(running_scripts) > 0:
        raise Exception('script_already_running')
    check_active_user(user_id)
    script = get_active_script(script_id)
    actions = get_actions(['AND', ['=', 'script_id', script_id], ['=', 'status', 'active']], {})
    first_action = next((action for action in actions if action['start_action']), None)
    if first_action is None:
        raise Exception('start_action_not_found')
    create_running_scripts([{
        'script_name': script['name'],
        'user_id': user_id,
        'script_id': script_id,
        'script': {
            'id': script['id'],
            'name': script['name'],
            'values': script['values'],
            'version': script['version'],
            'status': script['status'],
        },
        'actions': [{
            'id': action['id'],
            'name': action['name'],
            'alias': action['alias'],
            'start_action': action['start_action'],
            'script_id': action['script_id'],
            'values': action['values'],
            'status': action['status']
        } for action in actions]
    }])
    running_scripts = get_running_scripts(['AND', ['=', 'user_id', user_id], ['=', 'script_id', script_id]], {})
    if len(running_scripts) == 0:
        raise Exception('running_script_not_created')
    create_running_actions([{
        'running_script_id': running_scripts[0]['id'],
        'user_id': user_id,
        'action': {
            'id': first_action['id'],
            'name': first_action['name'],
            'alias': first_action['alias'],
            'start_action': first_action['start_action'],
            'script_id': first_action['script_id'],
            'values': first_action['values'],
            'status': first_action['status']
        }
    }])


def check_active_user(user_id: int) -> None:
    users = get_users(['=', 'id', user_id], {})
    if len(users) == 0:
        raise Exception('user_not_found')
    if users[0]['status'] != 'active':
        raise Exception('user_not_active')


def get_active_script(script_id: int) -> dict:
    scripts = get_scripts(['=', 'id', script_id], {})
    if len(scripts) == 0:
        raise Exception('script_not_found')
    script = scripts[0]
    if script['status'] != 'active':
        raise Exception('script_not_active')
    return script
