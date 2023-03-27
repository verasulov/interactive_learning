from sqlalchemy.dialects.postgresql import BIGINT, JSONB, TIMESTAMP, VARCHAR
from sqlalchemy import Column
from src.helper import Base

# todo добавить таблицу в автоматическую фиксацию изменных данных
class Log(Base):
    __tablename__ = 'logs'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    operation = Column(VARCHAR, nullable=False)
    table = Column(VARCHAR, nullable=False)
    new_value = Column(JSONB)
    old_value = Column(JSONB)
    created_at = Column(TIMESTAMP, nullable=False)
