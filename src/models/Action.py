from sqlalchemy.dialects.postgresql import TIMESTAMP, BIGINT, JSONB, VARCHAR, BOOLEAN
from src.models.User import User
from src.models.Script import Script
from sqlalchemy import Column, ForeignKey
from src.helper import Base


class Action(Base):
    __tablename__ = 'actions'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    name = Column(VARCHAR, nullable=False)
    alias = Column(VARCHAR, nullable=False)
    start_action = Column(BOOLEAN, server_default='false', nullable=False)
    script_id = Column(BIGINT, ForeignKey(Script.id), nullable=False)
    values = Column(JSONB, server_default='{}', nullable=False)
    status = Column(VARCHAR, server_default='active')
    creator_id = Column(BIGINT, ForeignKey(User.id))
    updater_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'updater_id_fkey'))
    deleter_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'deleter_id_fkey'))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
