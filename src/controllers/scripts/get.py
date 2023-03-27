from src.controllers.base.get import get
from src.models.Script import Script


def get_scripts(query_filter: list or dict, options: dict) -> list or dict:
    return get(query_filter, options, Script)
