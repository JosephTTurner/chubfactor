'''
Form for yeast model
'''

from flask_wtf import FlaskForm
from wtforms.fields.core import IntegerField, SelectField
from wtforms.validators import Required
from wtforms.fields.simple import TextAreaField, TextField

from db_engine import db_session_scope
from webapp.models.yeast_model import Yeast

YEAST_CHOICES = None

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
    max_high_temp = IntegerField(
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

def set_yeast_choices(db_session=None):
    if db_session is None:
        with db_session_scope() as db_session:
          YEAST_CHOICES = db_session.query(Yeast).all()
    else:
        YEAST_CHOICES = db_session.query(Yeast).all()


class YeastCompareForm(FlaskForm):
    # assert YEAST_CHOICES is not None, "Yeasts table or the YEAST_CHOICES variable has not been populated."
    yeast_one = SelectField(
        'Yeast One:',
        choices=YEAST_CHOICES)
    yeast_two = SelectField(
        'Yeast Two:',
        choices=YEAST_CHOICES)
