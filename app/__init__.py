from flask import Blueprint

webapp_blueprint = Blueprint("webapp_blueprint", __name__, template_folder="templates")

from app.controllers import (
    index_controller,
    calendar_controller,
    brew_controller,
    crew_controller,
    yeast_controller,
)


