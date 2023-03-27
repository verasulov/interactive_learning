from sqlalchemy import Column, ForeignKeyConstraint
from sqlalchemy.dialects.postgresql import TIMESTAMP, BIGINT, JSONB, VARCHAR
from src.helper import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    first_name = Column(VARCHAR, server_default='Без имени', nullable=False)
    middle_name = Column(VARCHAR, server_default='', nullable=False)
    last_name = Column(VARCHAR, server_default='', nullable=False)
    fio = Column(VARCHAR)
    gender = Column(VARCHAR)
    birth_date = Column(TIMESTAMP)
    status = Column(VARCHAR, server_default='active')
    values = Column(JSONB, server_default='{}', nullable=False)
    creator_id = Column(BIGINT)
    updater_id = Column(BIGINT)
    deleter_id = Column(BIGINT)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)


ForeignKeyConstraint([User.creator_id], [User.id])
ForeignKeyConstraint([User.updater_id], [User.id], name=User.__tablename__ + 'updater_id_fkey')
ForeignKeyConstraint([User.deleter_id], [User.id], name=User.__tablename__ + 'deleter_id_fkey')
