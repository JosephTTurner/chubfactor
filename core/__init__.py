from flask.blueprints import Blueprint

core_blueprint = Blueprint("core", __name__, template_folder="templates")
