from src.controllers.base.create import create
from src.models.RunningScript import RunningScript


def create_running_scripts(items: list) -> None:
    create(items, RunningScript)
