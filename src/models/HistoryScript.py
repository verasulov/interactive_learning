from sqlalchemy.dialects.postgresql import TIMESTAMP, BIGINT, JSONB, VARCHAR
from src.models.User import User
from src.models.Script import Script
from sqlalchemy import Column, ForeignKey
from src.helper import Base


class HistoryScript(Base):
    __tablename__ = 'histories_scripts'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    script_id = Column(BIGINT, ForeignKey(Script.id), nullable=False)
    data = Column(JSONB, nullable=False)
    description = Column(VARCHAR, nullable=False)
    creator_id = Column(BIGINT, ForeignKey(User.id))
    created_at = Column(TIMESTAMP, nullable=False)
