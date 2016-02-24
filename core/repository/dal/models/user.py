import datetime
from uuid import uuid4
from sqlalchemy import UniqueConstraint, Boolean, Column, DateTime, Integer, ForeignKey, Unicode, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from core.repository.dal.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    first_name = Column(Unicode(120))
    last_name = Column(Unicode(120))
    middle_name = Column(Unicode(120))
    blocked = Column(Boolean, default=False, nullable=False)
    blockedTill = Column(DateTime)
    deleted = Column(Boolean, default=False, nullable=False)

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 middle_name=None,
                 blocked=None,
                 blocked_till=None):
            self.id = str(uuid4())
            self.first_name = first_name
            self.last_name = last_name
            self.middle_name = middle_name
            self.blocked = blocked
            self.blockedTill = blocked_till

    def __repr__(self):

        return "<User('id': %s, 'first_name': %s, 'last_name': %s)>" % \
            (self.id, self.first_name, self.last_name)
