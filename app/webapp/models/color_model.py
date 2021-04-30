from models.base_model import Base
from sqlalchemy import Column, String

class Shade(Base):
    __tablename__ = 'shades'
    name = Column(String(256), nullable=False)


class Color(Base):
    __tablename__ = 'colors'
    name = Column(String(256), nullable=False)
