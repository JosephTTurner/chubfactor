'''
A model that builds the values to display for a brew.
'''
from view_models.base_view_model import BaseViewModel
from webapp.models.recipe_model import Ingredient, Recipe

class RecipeViewModel(BaseViewModel):
    def __init__(self, recipe: Recipe, **kwargs):
        super(RecipeViewModel, self).__init__(recipe, **kwargs)

        if recipe is not None:
            self.steps = [BaseViewModel(step) for step in recipe.steps if recipe is not None and recipe.steps is not None]
            self.ingredients = [BaseViewModel(ingredient) for ingredient in recipe.ingredients if recipe is not None and recipe.ingredients is not None]
