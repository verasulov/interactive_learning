from src.controllers.base.create import create
from src.models.Action import Action


def create_actions(items: list) -> None:
    create(items, Action)
