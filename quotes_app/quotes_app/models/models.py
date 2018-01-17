from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    Text,
    Date,
    Time
    )

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class SessionLogModel(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    session_uid = Column(Text)
    session_url = Column(Text)
    date = Column(Date, default=datetime.now().date())
    time = Column(Time, default=datetime.now().time())

    def __init__(self, session_uid, session_url):
        self.session_uid = session_uid
        self.session_url = session_url

    def to_json(self):
        dict_ = {
            s.key: getattr(self, s.key) for s in inspect(self).mapper.column_attrs
        }
        return dict_
