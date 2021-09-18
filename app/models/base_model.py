from typing import Type
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.sql.functions import current_timestamp
from datetime import datetime
from db_engine import engine

class MyBase:
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    created_date = Column(DateTime(), nullable=False, server_default=current_timestamp(), default=datetime.utcnow)
    modified_date = Column(DateTime(), nullable=False, server_default=current_timestamp(), default=datetime.utcnow)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    def clone(self):
        return self.__class__(**self.as_dict())

    @classmethod
    def get_by_id(cls, db_session:scoped_session, id_: int) -> 'MyBase':
        '''
        Return the first and only record matching the id.
        '''
        db_session.query(cls).filter_by(id=id_).first()


Base = declarative_base(cls=MyBase)

Base.metadata.create_all(engine)
