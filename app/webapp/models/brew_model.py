from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base

class Brew(Base):
    __tablename__ = 'brews'
    nick_name = Column(String(256))
    keg_day = Column(DateTime(), nullable=True)
    brew_day = Column(DateTime(), nullable=True)
    style_id = Column(Integer(), ForeignKey('styles.id'))
    brewer_id = Column(Integer(), ForeignKey('brewers.id'))
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))
    style = relationship('Style', foreign_keys=[style_id], uselist=False)
    brewer = relationship('Brewer', foreign_keys=[brewer_id], uselist=False)
    recipe = relationship('Recipe', foreign_keys=[recipe_id], uselist=False)

class Style(Base):
    __tablename__ = 'styles'
    name = Column(String(256))
    shade_id = Column(Integer(), ForeignKey('shades.id'), nullable=False)
    color_id = Column(Integer(), ForeignKey('colors.id'), nullable=False)
    parent_id = Column(Integer(), ForeignKey('styles.id'), nullable=True)
    shade = relationship('Shade', foreign_keys=[shade_id])
    color = relationship('Color', foreign_keys=[color_id])
    origins = relationship('Origin', secondary='style_origins', uselist=True) #, back_populates='styles')
    parent = relationship('Style', uselist=False)


class Origin(Base):
    __tablename__ = 'origins'
    name = Column(String(256))
    # styles = relationship('Origin', secondary='style_origins', uselist=True)

class StyleOrigins(Base):
    __tablename__ = 'style_origins'
    style_id = Column(Integer(), ForeignKey('styles.id'), nullable=False)
    origin_id = Column(Integer(), ForeignKey('origins.id'), nullable=False)


