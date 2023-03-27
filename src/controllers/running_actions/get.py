from src.controllers.base.get import get
from src.models.RunningAction import RunningAction


def get_running_actions(query_filter: list or dict, options: dict) -> list or dict:
    return get(query_filter, options, RunningAction)
