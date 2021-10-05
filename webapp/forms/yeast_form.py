"""
Form for yeast model
"""

from flask_wtf import FlaskForm
from wtforms.fields.core import IntegerField, SelectField
from wtforms.validators import Required
from wtforms.fields.simple import TextAreaField, TextField

from webapp.models.yeast_model import Yeast, YeastType


class YeastForm(FlaskForm):

    @classmethod
    def build(cls):
        default_validators = [Required()]
        cls.name = TextField("Name:", validators=default_validators)
        cls.brand = TextField("Brand:", validators=default_validators)
        cls.ideal_low_temp = IntegerField(
            "Ideal Low Temp:", validators=default_validators
        )
        cls.ideal_high_temp = IntegerField(
            "Ideal High Temp:", validators=default_validators
        )
        cls.min_low_temp = IntegerField("Min Low Temp:", validators=default_validators)
        cls.max_high_temp = IntegerField(
            "Max High Temp:", validators=default_validators
        )
        cls.description = TextAreaField("Description:")
        cls.yeast_type_id = SelectField("Type:", choices=Yeast.choices())

        return cls()


class YeastCompareForm(FlaskForm):

    @classmethod
    def build(cls):
        cls.yeast_one = SelectField("Yeast One:", choices=Yeast.choices())
        cls.yeast_two = SelectField("Yeast Two:", choices=Yeast.choices())

        return cls()
