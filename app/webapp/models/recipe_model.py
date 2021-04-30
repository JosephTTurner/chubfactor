from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base

class Recipe(Base):
    __tablename__ = 'recipes'
    name = Column(String(256), nullable=False, unique=True, server_default='Dumbass Didn\'t Name It')
    recipe_type_id = Column(Integer(), ForeignKey('recipe_types.id'))
    chub_factor_id = Column(Integer(), ForeignKey('chub_factors.id'))
    recipe_ingredients = relationship('RecipeIngredient', lazy='joined', uselist=True)
    recipe_steps = relationship('Step', secondary='RecipeSteps', lazy='joined', uselist=True)
    recipe_type = relationship('RecipeType', lazy='joined', foreign_keys=[recipe_type_id])
    chub_factor = relationship('ChubFactor', foreign_keys=[chub_factor_id])

class RecipeType(Base):
    __tablename__ = 'recipe_types'
    name = Column(String(256))

class Ingredient(Base):
    __tablename__ = 'ingredients'
    name = Column(String(256), nullable=False, server_default='Mystery Ingredient')
    ingredient_type_id = Column(Integer(), ForeignKey('ingredient_types.id'), nullable=False)
    chub_factor_id = Column(Integer(), ForeignKey('chub_factors.id'))
    ingredient_type = relationship('IngredientType', foreign_keys=[ingredient_type_id], uselist=False)
    chub_factor = relationship('ChubFactor', foreign_keys=[chub_factor_id])

class IngredientType(Base):
    __tablename__ = 'ingredient_types'
    name = Column(String(256))

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'
    recipe_id = Column(Integer(), ForeignKey('recipes.id'), nullable=False)
    ingredient_id = Column(Integer(), ForeignKey('ingredients.id'), nullable=False)
    unit_id = Column(Integer(), ForeignKey('units.id'), nullable=False)
    amount = Column(Float(), nullable=False)
    recipe = relationship('Recipe', foreign_keys=[recipe_id], lazy='joined', uselist=False)
    ingredient = relationship('Ingredient', foreign_keys=[ingredient_id], lazy='joined', uselist=False)
    unit = relationship('Unit', foreign_keys=[unit_id], lazy='joined', uselist=False)

class Step(Base):
    __tablename__ = 'steps'
    text = Column(String(1024), nullable=False)
    order = Column(Integer(), nullable=False)

class RecipeStep(Base):
    __tablename__ = 'recipe_steps'
    step_id = Column(Integer(), ForeignKey('steps.id'))
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))

class Unit(Base):
    __tablename__ = 'units'
    name = Column(String(256), nullable=False)
