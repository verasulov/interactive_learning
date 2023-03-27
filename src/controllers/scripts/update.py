from src.controllers.base.update import update
from src.models.Script import Script


def update_scripts(items: list) -> None:
    update(items, Script)
