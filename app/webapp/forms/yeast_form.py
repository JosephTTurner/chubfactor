'''
Form for yeast model
'''

from flask_wtf import FlaskForm
from wtforms.fields.core import IntegerField, SelectField
from wtforms.validators import Required
from wtforms.fields.simple import TextAreaField, TextField

from webapp.models.yeast_model import YeastType


class YeastForm(FlaskForm):
    default_validators = [Required()]
    # yeast_types = YeastType.choices()

    name = TextField(
        'Name:',
        validators=default_validators)
    brand = TextField(
        'Brand:',
        validators=default_validators)
    ideal_low_temp = IntegerField(
        'Ideal Low Temp:',
        validators=default_validators,
    )
    ideal_high_temp = IntegerField(
        'Ideal High Temp:',
        validators=default_validators,
    )
    min_low_temp = IntegerField(
        'Min Low Temp:',
        validators=default_validators,
    )
    max_low_temp = IntegerField(
        'Max Low Temp:',
        validators=default_validators,
    )
    description = TextAreaField(
        'Description:',
    )
    # yeast_type_id = SelectField(
    #     'Type:',
    #     choices=yeast_types
    # )
