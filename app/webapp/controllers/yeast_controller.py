from flask import render_template
from webapp import webapp_blueprint as bp
from webapp.forms.yeast_form import YeastForm
from db_engine import db_session_scope

@bp.route('/yeast_matcher')
def yeast_matcher_view():
    form = YeastForm
    return render_template('yeast_matcher.html', yeast_form=form)
