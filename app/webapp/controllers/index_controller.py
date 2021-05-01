from flask import render_template
from webapp import webapp_blueprint as bp


@bp.route('/')
def index():
    return render_template('index.html')
