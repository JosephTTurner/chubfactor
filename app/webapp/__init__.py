from flask import Blueprint

webapp_blueprint = Blueprint('webapp_blueprint', __name__, template_folder='templates')

from webapp.controllers import index_controller
