from src.controllers.base.create import create
from src.models.Script import Script


def create_scripts(items: list, with_id: bool = False) -> None or list:
    return create(items, with_id, Script)
