from sqlalchemy.dialects.postgresql import TIMESTAMP, BIGINT, JSONB, VARCHAR
from src.models.User import User
from sqlalchemy import Column, ForeignKey
from src.helper import Base


class Role(Base):
    __tablename__ = 'roles'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    name = Column(VARCHAR, nullable=False)
    values = Column(JSONB, server_default='{}', nullable=False)
    status = Column(VARCHAR, server_default='active')
    creator_id = Column(BIGINT, ForeignKey(User.id))
    updater_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'updater_id_fkey'))
    deleter_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'deleter_id_fkey'))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
