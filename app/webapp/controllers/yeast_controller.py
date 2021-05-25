from flask import render_template
from webapp import webapp_blueprint as bp
from webapp.forms.yeast_form import YeastCompareForm, YeastForm, set_yeast_choices
from db_engine import db_session_scope
from webapp.models.yeast_model import Yeast

@bp.route('/yeast_matcher')
def yeast_matcher_view():
    set_yeast_choices()
    yeast_form = YeastForm()
    compare_form = YeastCompareForm()

    return render_template('yeast_matcher.html', yeast_form=yeast_form)

@bp.route('/add_yeast', methods=['POST'])
def add_yeast():
    form = YeastForm()
    if form.validate_on_submit():
        data = form.data
        yeast = Yeast(**data)
        with db_session_scope() as db_session:
            # handle near duplicates?
            db_session.add(yeast)

@bp.route('/compare_yeast', method=['POST'])
def compare_yeast():
    form = YeastCompareForm()
    if form.validate_on_submit():
        yeast_one_id = form.data.get('yeast_one')
        yeast_two_id = form.data.get('yeast_two')
        with db_session_scope() as db_session:
            yeast_one = Yeast.get_by_id(int(yeast_one_id))
            yeast_two = Yeast.get_by_id(int(yeast_two_id))
            compare_results = yeast_one.can_ferm_with(yeast_two)
        # process compare results


