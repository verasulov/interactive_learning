from sqlalchemy import or_, and_, asc, desc, String, cast
from sqlalchemy.orm import Query
from sqlalchemy import literal_column
sql_alchemy_import = __import__('sqlalchemy')
sql_alchemy_postgresql_import = __import__('sqlalchemy.dialects.postgresql')


def option_builder(models: object or list, query: Query, options: dict) -> tuple:
    counter = False
    if 'count' in options and type(options['count']) is bool and options['count']:
        counter = query.count()
    if 'order' in options and type(options['order']) is list:
        orders = options['order']
        for order in orders:
            if len(order) < 2:
                continue
            key = order[0]
            find_model = models
            if type(models) is list:
                find_model = None
                for model in models:
                    if hasattr(model, key):
                        find_model = model
                        break
            model = find_model
            if model and not hasattr(model, key):
                continue
            order_type = asc if order[1].lower() == 'asc' else desc
            attribute = getattr(model, key) if model else literal_column(key)
            if model and str(attribute.type) == 'JSONB' and len(order) == 3:
                attribute = attribute[order[2]].astext
            if len(order) >= 4:
                if len(order) >= 5:
                    if hasattr(sql_alchemy_postgresql_import, order[4]):
                        attribute = attribute.cast(getattr(sql_alchemy_postgresql_import,
                                                           order[4])).op(order[2])(order[3])
                else:
                    attribute = attribute.op(order[2])(order[3])
            query = query.order_by(order_type(attribute))
    if 'limit' in options and type(options['limit']) is int:
        query = query.limit(options['limit'])
    if 'offset' in options and type(options['offset']) is int:
        query = query.offset(options['offset'])
    return query, counter


def filter_builder(models: object or list, f: list, lvl: int = 0):
    if not f or len(f) == 0:
        return
    comp = str(f[0]).lower()
    key = f[1]
    value = f[2] if len(f) > 2 else None
    query_filter = []
    if comp in ['or', 'and']:
        items = []
        for index, item in enumerate(f):
            if index == 0:
                continue
            r = filter_builder(models, item, lvl + 1)
            if r is not None and type(r) is not list:
                items.append(r)
        method = and_ if comp == 'and' else or_
        if lvl == 0:
            query_filter.append(method(*items))
        else:
            return method(*items)
    else:
        find_model = models
        if type(models) is list:
            find_model = None
            for model in models:
                if hasattr(model, key):
                    find_model = model
                    break
        model = find_model
        if model and not hasattr(model, key):
            raise Exception('Undefined field: ' + key)
        attribute = getattr(model, key) if model else literal_column(key)
        if type(value) is tuple:
            t, v = value
            if t == 'field':
                value = getattr(model, v) if model else literal_column(v)
        type_left = ''
        type_right = ''
        if model and str(attribute.type) == 'JSONB' and len(f) > 3:
            attribute = attribute[f[3]].astext
            if len(f) > 4 and f[4]:
                type_left = f[4]
            if len(f) > 5 and f[5]:
                type_right = f[5]
        else:
            if len(f) > 3 and f[3]:
                type_left = f[3]
            if len(f) > 4 and f[4]:
                type_right = f[4]
        if type_left != '':
            if hasattr(sql_alchemy_import, type_left):
                attribute = attribute.cast(getattr(sql_alchemy_import, type_left))
        if type_right != '':
            if hasattr(sql_alchemy_import, type_right):
                value = cast(value, getattr(sql_alchemy_import, type_right))
        result = False
        if comp == '=':
            result = attribute == value
        elif comp in ['!=', '<>']:
            result = attribute != value
        elif comp == '>':
            result = attribute > value
        elif comp == '<':
            result = attribute < value
        elif comp == '>=':
            result = attribute >= value
        elif comp == '<=':
            result = attribute <= value
        elif comp == 'in':
            result = attribute.in_(value)
        elif comp == 'not in':
            result = ~attribute.in_(value)
        elif comp == 'is null':
            result = attribute.is_(None)
        elif comp == 'is not null':
            result = attribute.isnot(None)
        elif comp == 'like':
            result = attribute.cast(String).like(value)
        elif comp == 'ilike':
            result = attribute.cast(String).ilike(value)
        elif comp == 'contained_by':
            result = attribute.contained_by(value)
        elif comp == 'contains':
            result = attribute.contains(value)
        elif comp == 'has_all':
            result = attribute.has_all(value)
        elif comp == 'has_any':
            result = attribute.has_any(value)
        elif comp == 'has_key':
            result = attribute.has_key(value)
        if result is not False:
            if lvl == 0:
                return [result]
            return result
    return query_filter


def add_to_filter(query_filter: dict or list, additional_filter: dict or list, key: str, base_key: str) -> dict or list:
    if type(query_filter) is list and key != base_key:
        query_filter = {
            base_key: query_filter
        }
    if type(query_filter) is list:
        if len(query_filter) == 0:
            query_filter = additional_filter
        else:
            query_filter = ['AND', query_filter, additional_filter]
    else:
        if key in query_filter:
            query_filter[key] = ['AND', query_filter[key], additional_filter]
        else:
            query_filter[key] = additional_filter
    return query_filter
