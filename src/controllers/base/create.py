from src.helper import get_session, object_as_dict
from datetime import datetime
from src.server import app


def create(items: list, with_id: bool, orm_model) -> None or list:
    models = []
    result = []
    with get_session() as session:
        for field in items:
            date_time = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            user_id = app.config['user']['id'] if 'user' in app.config else None
            if 'created_at' not in field and hasattr(orm_model, 'created_at'):
                field['created_at'] = date_time
            if 'creator_id' not in field and hasattr(orm_model, 'creator_id') and user_id:
                field['creator_id'] = user_id
            add_field = orm_model(**field)
            session.add(add_field)
            if with_id:
                models.append(add_field)
        session.commit()
        if with_id:
            for model in models:
                result.append(object_as_dict(model))
            return result
