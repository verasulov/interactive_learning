from sqlalchemy import Column, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, TIMESTAMP
from src.models.User import User
from src.models.Script import Script
from src.helper import Base


class ScriptUser(Base):
    __tablename__ = 'scripts_users'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    user_id = Column(BIGINT, ForeignKey(User.id), nullable=False)
    script_id = Column(BIGINT, ForeignKey(Script.id), nullable=False)
    status = Column(VARCHAR, server_default='active')
    creator_id = Column(BIGINT, ForeignKey(User.id))
    updater_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'updater_id_fkey'))
    deleter_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'deleter_id_fkey'))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
    __table_args__ = (
        Index('unique_scripts_users_pare_id', user_id, script_id, unique=True,
              postgresql_where=(status == 'active')),
    )
