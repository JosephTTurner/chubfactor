"""
A silly way of rating things
"""
from core.models.base_model import Base
from sqlalchemy import Column, String, Integer


class ChubFactor(Base):
    __tablename__ = "chub_factors"
    rank = Column(Integer(), nullable=False)
    name = Column(String(256), nullable=False)
