from src.controllers.base.get import get
from src.models.User import User


def get_users(query_filter: list or dict, options: dict) -> list or dict:
    return get(query_filter, options, User)
