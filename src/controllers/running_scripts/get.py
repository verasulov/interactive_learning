from src.controllers.base.get import get
from src.models.RunningScript import RunningScript


def get_running_scripts(query_filter: list or dict, options: dict) -> list or dict:
    return get(query_filter, options, RunningScript)
