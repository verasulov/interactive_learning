from src.lib.filter_builder import filter_builder, option_builder
from src.helper import get_session, object_as_dict


def get(query_filter: list or dict, options: dict, orm_model) -> list or dict:
    result = []
    with get_session() as session:
        query = session.query(orm_model)
        if len(query_filter) > 0:
            query = query.filter(*filter_builder(orm_model, query_filter))
        query_option, counter = option_builder(orm_model, query, options)
        rows = query_option.all()
        for row in rows:
            result.append(object_as_dict(row))
    if type(counter) is int:
        return {
            'total': counter,
            'rows': result
        }
    return result

