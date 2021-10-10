from flask import render_template
from app import webapp_blueprint as bp


@bp.route("/calendar")
def calendar_view():
    return render_template("todo.html")
