from src.controllers.running_scripts.get import get_running_scripts
from src.controllers.running_actions.create import create_running_actions


def set_running_action(running_script_id: int, action_alias: str) -> None:
    running_scripts = get_running_scripts(['=', 'id', running_script_id], {})
    if len(running_scripts) == 0:
        raise Exception('running_script_not_found')
    running_script = running_scripts[0]
    if running_script != 'active':
        raise Exception('running_script_is_not_active')
    action = next((action for action in running_script['actions'] if action['alias'] == action_alias), None)
    if action is None:
        raise Exception('action_alias_not_found')
    create_running_actions([{
        'running_script_id': running_script_id,
        'user_id': running_script['user_id'],
        'action': action
    }])
