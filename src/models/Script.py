from sqlalchemy.dialects.postgresql import TIMESTAMP, BIGINT, JSONB, VARCHAR, INTEGER
from src.models.User import User
from sqlalchemy import Column, ForeignKey
from src.helper import Base


class Script(Base):
    __tablename__ = 'scripts'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    name = Column(VARCHAR, nullable=False)
    values = Column(JSONB, server_default='{}', nullable=False)
    version = Column(INTEGER, server_default='1')
    status = Column(VARCHAR, server_default='active')
    creator_id = Column(BIGINT, ForeignKey(User.id))
    updater_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'updater_id_fkey'))
    deleter_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'deleter_id_fkey'))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
