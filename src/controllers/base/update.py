from src.helper import get_session
from src.lib.filter_builder import filter_builder
from datetime import datetime
from src.server import app


def update(items: list, orm_model: object) -> None:
    with get_session() as session:
        for field in items:
            if 'filter' not in field or 'values' not in field:
                continue
            field_filter = field['filter']
            field_values = field['values']
            if len(field_filter) == 0:
                continue
            build_filter = filter_builder(orm_model, field_filter)
            date_time = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
            user_id = app.config['user']['id'] if 'user' in app.config else None
            if 'status' in field_values and field_values['status'] == 'deleted':
                if 'deleted_at' not in field and hasattr(orm_model, 'deleted_at'):
                    field_values['deleted_at'] = date_time
                if 'deleter_id' not in field and hasattr(orm_model, 'deleter_id') and user_id:
                    field_values['deleter_id'] = user_id
            else:
                if 'updated_at' not in field and hasattr(orm_model, 'updated_at'):
                    field_values['updated_at'] = date_time
                if 'updater_id' not in field and hasattr(orm_model, 'updater_id') and user_id:
                    field_values['updater_id'] = user_id
            session.query(orm_model).filter(*build_filter).update(field_values, synchronize_session='fetch')
        session.commit()
