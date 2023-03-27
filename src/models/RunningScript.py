from sqlalchemy.dialects.postgresql import TIMESTAMP, BIGINT, JSONB, VARCHAR
from src.models.User import User
from src.models.Script import Script
from sqlalchemy import Column, ForeignKey, Index
from src.helper import Base


class RunningScript(Base):
    __tablename__ = 'running_scripts'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    script_name = Column(VARCHAR, nullable=False)
    user_id = Column(BIGINT, ForeignKey(User.id), nullable=False)
    script_id = Column(BIGINT, ForeignKey(Script.id), nullable=False)
    script = Column(JSONB, nullable=False)
    actions = Column(JSONB, nullable=False)
    values = Column(JSONB, server_default='{}', nullable=False)
    status = Column(VARCHAR, server_default='active')
    creator_id = Column(BIGINT, ForeignKey(User.id))
    updater_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'updater_id_fkey'))
    deleter_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'deleter_id_fkey'))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
    __table_args__ = (
        Index('unique_running_script_user_status', user_id, status, unique=True,
              postgresql_where=(status == 'active')),
    )
