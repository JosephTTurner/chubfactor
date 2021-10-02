from flask import render_template, jsonify

from webapp import webapp_blueprint as bp
from webapp.models.brew_model import Brew
from webapp.view_models.brew_table_view_model import BrewTableViewModel
from webapp.view_models.brew_view_model import BrewViewModel
from flask_sa_session import db_session


@bp.route("/")
def index():
    # push view models into table view model

    brew_table_view = BrewTableViewModel()

    return render_template("index.html", table_view=brew_table_view)


@bp.route("/brew_table_data", methods=["GET"])
def brew_table_data():
    # get data
    brews = db_session.query(Brew).all()
    # push data into list of view models
    brew_data = [BrewViewModel(brew).__dict__ for brew in brews]

    return jsonify({"success": True, "data": brew_data})
