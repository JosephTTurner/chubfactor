from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from core.models.base_model import Base
from data.models.yeast_model import Yeast

# string to class dictionary for getting records from ingredient type tables
ingredient_class_dict = {
    "Yeast": Yeast,
    # grain
    # etc.
}


class Recipe(Base):
    __tablename__ = "recipes"
    name = Column(
        String(256),
        nullable=False,
        unique=True,
        server_default="Dumbass Didn't Name It",
    )
    recipe_type_id = Column(Integer(), ForeignKey("recipe_types.id"))
    chub_factor_id = Column(Integer(), ForeignKey("chub_factors.id"))
    ingredients = relationship(
        "RecipeIngredient", lazy="joined", uselist=True
    )  # , backref=backref('recipe'))
    steps = relationship("Step", secondary="recipe_steps", lazy="joined", uselist=True)
    recipe_type = relationship(
        "RecipeType", lazy="joined", foreign_keys=[recipe_type_id]
    )
    chub_factor = relationship("ChubFactor", foreign_keys=[chub_factor_id])


class RecipeType(Base):
    __tablename__ = "recipe_types"
    name = Column(String(256))


class Ingredient(Base):
    __tablename__ = "ingredients"
    name = Column(String(256), nullable=False, server_default="Mystery Ingredient")
    ingredient_type_id = Column(
        Integer(), ForeignKey("ingredient_types.id"), nullable=False
    )
    chub_factor_id = Column(Integer(), ForeignKey("chub_factors.id"))
    description = Column(String(1024), nullable=True)
    ingredient_type = relationship(
        "IngredientType", foreign_keys=[ingredient_type_id], uselist=False
    )
    chub_factor = relationship("ChubFactor", foreign_keys=[chub_factor_id])

    # What to call this?
    # Id of record on table for ingredient type.
    class_id = Column(Integer, nullable=True)

    def class_record(self, db_session):
        """
        Get the record from the table for this type of ingredient
        """
        if self.ingredient_type is None or self.class_id is None:
            return None

        if self.ingredient_type.class_name is None:
            return None

        class_ = ingredient_class_dict.get(self.ingredient_type.class_name)

        if class_ is None:
            return None

        return db_session.query(class_).filter_by(id=self.class_id).first()


class IngredientType(Base):
    __tablename__ = "ingredient_types"
    name = Column(String(256))
    table_name = Column(String(256), nullable=True)
    class_name = Column(String(256), nullable=True)


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"
    recipe_id = Column(Integer(), ForeignKey("recipes.id"), nullable=False)
    ingredient_id = Column(Integer(), ForeignKey("ingredients.id"), nullable=False)
    unit_id = Column(Integer(), ForeignKey("units.id"), nullable=False)
    amount = Column(Float(), nullable=False)
    # recipe = relationship('Recipe', foreign_keys=[recipe_id], lazy='joined', uselist=False)
    ingredient = relationship(
        "Ingredient", foreign_keys=[ingredient_id], lazy="joined", uselist=False
    )
    unit = relationship("Unit", foreign_keys=[unit_id], lazy="joined", uselist=False)


class Step(Base):
    __tablename__ = "steps"
    text = Column(String(1024), nullable=False)
    order = Column(Integer(), nullable=False)


class RecipeStep(Base):
    __tablename__ = "recipe_steps"
    step_id = Column(Integer(), ForeignKey("steps.id"))
    recipe_id = Column(Integer(), ForeignKey("recipes.id"))


class Unit(Base):
    __tablename__ = "units"
    name = Column(String(256), nullable=False)
