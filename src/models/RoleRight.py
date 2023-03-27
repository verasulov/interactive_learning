from sqlalchemy import Column, ForeignKey, Index
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, TIMESTAMP
from src.models.Right import Right
from src.models.Role import Role
from src.models.User import User
from src.helper import Base


class RoleRight(Base):
    __tablename__ = 'roles_rights'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    role_id = Column(BIGINT, ForeignKey(Role.id), nullable=False)
    right_id = Column(VARCHAR, ForeignKey(Right.id), nullable=False)
    status = Column(VARCHAR, server_default='active')
    creator_id = Column(BIGINT, ForeignKey(User.id))
    updater_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'updater_id_fkey'))
    deleter_id = Column(BIGINT, ForeignKey(User.id, name=__tablename__ + 'deleter_id_fkey'))
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
    __table_args__ = (
        Index('unique_roles_rights_pare_id', right_id, role_id, unique=True,
              postgresql_where=(status == 'active')),
    )
