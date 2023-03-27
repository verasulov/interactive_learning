import json
from datetime import datetime
from enum import Enum


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return str(o)
        if isinstance(o, Enum):
            return o.value
        return json.JSONEncoder.default(self, o)


def json_encode(data: any) -> str:
    return json.dumps(data, cls=DateTimeEncoder)


def json_decode(data: str) -> any:
    return json.loads(data)
