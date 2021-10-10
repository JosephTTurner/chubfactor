from flask.templating import render_template
from app import webapp_blueprint as bp


@bp.route("/my_crew")
def my_crew_view():
    return render_template("todo.html")
