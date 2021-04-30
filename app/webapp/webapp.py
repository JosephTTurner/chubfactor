from flask import Blueprint, render_template

webapp_blueprint = Blueprint('webapp_blueprint', __name__, template_folder='templates')

@webapp_blueprint.route('/')
def index():
    return render_template('index.html')
