from src.controllers.base.create import create
from src.models.User import User


def create_users(items: list) -> None:
    create(items, User)
