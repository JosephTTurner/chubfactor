from flask.templating import render_template
from app import webapp_blueprint as bp


@bp.route("/brews")
def brews_view():
    return render_template("todo.html")
