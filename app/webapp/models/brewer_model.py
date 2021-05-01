from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import backref, relation, relationship
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base

class Brewer(Base):
    __tablename__ = 'brewers'
    # user_id = Column(Integer(), ForeignKey('users.id'))
    nick_name = Column(String(256))
    started_brewing = Column(DateTime(), nullable=True)
    chub_factor_id = Column(Integer(), ForeignKey('chub_factors.id'))
    brews = relationship('Brew', back_populates='brewer', lazy='joined', uselist=True)
    # user_profile = relationship('User', foreign_keys=[user_id])
    chub_factor = relationship('ChubFactor', foreign_keys=[chub_factor_id], uselist=False, lazy='joined')
    # crew = relationship('Brewer', uselist=True, secondary='brew_crews')

class Crew(Base):
    __tablename__ = 'crews'
    name = Column(String(256))
    slogan = Column(String(256))
    story = Column(String(2048))
    chub_factor_id = Column(Integer(), ForeignKey('chub_factors.id'))
    chub_factor = relationship('ChubFactor', foreign_keys=[chub_factor_id])
    brewers = relationship('Brewer', uselist=True, secondary='brew_crews', lazy='joined', backref=backref('crew'))

class BrewCrew(Base):
    __tablename__ = 'brew_crews'
    crew_id = Column(Integer(), ForeignKey('crews.id'))
    brewer_id = Column(Integer(), ForeignKey('brewers.id'))


