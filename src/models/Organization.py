from sqlalchemy.dialects.postgresql import TIMESTAMP, VARCHAR, BIGINT
from sqlalchemy import Column, ForeignKey
from src.helper import Base
from src.models.User import User


class Organization(Base):
    __tablename__ = 'organizations'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    name = Column(VARCHAR, nullable=False)
    status = Column(VARCHAR, server_default='active')
    creator_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'creator_id_fkey'))
    updater_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'updater_id_fkey'))
    deleter_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'deleter_id_fkey'))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
