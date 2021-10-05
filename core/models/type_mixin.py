"""
Mixin for data classes that represent types / options that are often enumerated.
May prefer a solution that explicitly extends an enum class either from SA or Python.
"""

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from core.db_engine import db_session

class TypeMixin:
    id = Column(Integer(), primary_key=True)
    name = Column(String(256), nullable=False)

    @classmethod
    def choices(cls):
        return [
            (record.id, record.name) for record in db_session.query(cls).all()
        ]
