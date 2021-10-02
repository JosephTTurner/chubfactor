from copy import deepcopy
from flask import render_template, redirect, request
from flask.helpers import url_for

from webapp import webapp_blueprint as bp
from webapp.forms.yeast_form import YeastCompareForm, YeastForm
from webapp.models.yeast_model import TempMatchEnum, Yeast
from webapp.view_models.yeast_view_model import YeastMatchResultsViewModel
from flask_sa_session import db_session


@bp.route("/yeast_matcher")
def yeast_matcher_view():
    yeast_form = YeastForm.build()
    compare_form = YeastCompareForm.build()

    return render_template(
        "yeast_matcher.html",
        yeast_form=yeast_form,
        compare_form=compare_form,
        match_results=None,
    )


@bp.route("/add_yeast", methods=["POST"])
def add_yeast():
    data = dict(deepcopy(request.form))
    del data["csrf_token"]
    yeast = Yeast(**data)
    # handle near duplicates?
    db_session.add(yeast)

    return redirect(url_for("webapp_blueprint.yeast_matcher_view"))


@bp.route("/compare_yeast", methods=["POST"])
def compare_yeast():
    # if form.validate_on_submit():
    yeast_one_id = request.form.get("yeast_one")
    yeast_two_id = request.form.get("yeast_two")

    # yeast_one = Yeast.get_by_id(db_session, int(yeast_one_id))
    yeast_one = db_session.query(Yeast).filter_by(id=int(yeast_one_id)).first()
    yeast_two = db_session.query(Yeast).filter_by(id=int(yeast_two_id)).first()
    match_enum, min_temp, max_temp = yeast_one.check_temp_match(yeast_two)
    match_description = TempMatchEnum.get_name(match_enum)
    match_results = YeastMatchResultsViewModel(
        match_enum=match_enum,
        match_description=match_description,
        min_temp=min_temp,
        max_temp=max_temp,
    )

    yeast_form = YeastForm.build(db_session)
    compare_form = YeastCompareForm.build(db_session)

    return render_template(
        "yeast_matcher.html",
        yeast_form=yeast_form,
        compare_form=compare_form,
        match_results=match_results,
    )
