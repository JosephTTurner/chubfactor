"""
Form for yeast model
"""

from flask_wtf import FlaskForm
from wtforms.fields.core import IntegerField, SelectField
from wtforms.validators import Required
from wtforms.fields.simple import TextAreaField, TextField

from db_engine import db_session_scope
from webapp.models.yeast_model import Yeast, YeastType

YEAST_CHOICES = None
YEAST_TYPES = None


class YeastForm(FlaskForm):
    # yeast_types = YeastType.choices()

    @classmethod
    def build(cls, db_session):
        YEAST_TYPES = YeastType.choices(db_session)

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
        cls.yeast_type_id = SelectField("Type:", choices=YEAST_TYPES)

        return cls()


class YeastCompareForm(FlaskForm):
    # assert YEAST_CHOICES is not None, "Yeasts table or the YEAST_CHOICES variable has not been populated."
    @classmethod
    def build(cls, db_session):
        YEAST_CHOICES = Yeast.choices(db_session)
        cls.yeast_one = SelectField("Yeast One:", choices=YEAST_CHOICES)
        cls.yeast_two = SelectField("Yeast Two:", choices=YEAST_CHOICES)

        return cls()
