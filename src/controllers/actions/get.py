from src.controllers.base.get import get
from src.models.Action import Action


def get_actions(query_filter: list or dict, options: dict) -> list or dict:
    return get(query_filter, options, Action)
