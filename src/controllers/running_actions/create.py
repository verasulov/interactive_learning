from src.controllers.base.create import create
from src.models.RunningAction import RunningAction


def create_running_actions(items: list) -> None:
    create(items, RunningAction)
