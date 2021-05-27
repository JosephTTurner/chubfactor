from flask import render_template, redirect
from flask.helpers import url_for
from webapp import webapp_blueprint as bp
from webapp.forms.yeast_form import YeastCompareForm, YeastForm, set_yeast_choices
from db_engine import db_session_scope
from webapp.models.yeast_model import Yeast
from webapp.view_models.yeast_view_model import YeastMatchResultsViewModel

@bp.route('/yeast_matcher')
def yeast_matcher_view():
    set_yeast_choices()
    yeast_form = YeastForm()
    compare_form = YeastCompareForm()

    return render_template(
        'yeast_matcher.html',
        yeast_form=yeast_form,
        compare_form=compare_form,
        match_results=None)

@bp.route('/add_yeast', methods=['POST'])
def add_yeast():
    form = YeastForm()
    if form.validate_on_submit():
        data = form.data
        yeast = Yeast(**data)
        with db_session_scope() as db_session:
            # handle near duplicates?
            db_session.add(yeast)

@bp.route('/compare_yeast', methods=['POST'])
def compare_yeast():
    form = YeastCompareForm()
    if form.validate_on_submit():
        yeast_one_id = form.data.get('yeast_one')
        yeast_two_id = form.data.get('yeast_two')
        with db_session_scope() as db_session:
            yeast_one = Yeast.get_by_id(db_session, int(yeast_one_id))
            yeast_two = Yeast.get_by_id(db_session, int(yeast_two_id))
            match_enum, min_temp, max_temp = yeast_one.check_temp_match(yeast_two)

            match_results = YeastMatchResultsViewModel(
                match_enum=match_enum,
                min_temp=min_temp,
                max_temp=max_temp
            )

        set_yeast_choices()
        yeast_form = YeastForm()
        compare_form = YeastCompareForm()

        return render_template(
            'yeast_matcher.html',
            yeast_form=yeast_form,
            compare_form=compare_form,
            match_results=match_results)

    else:
        return redirect(url_for('webapp_blueprint.yeast_matcher_view'))


