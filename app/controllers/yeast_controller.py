from copy import deepcopy
from flask import render_template, redirect, request
from flask.helpers import url_for

from app import webapp_blueprint as bp
from app.forms.yeast_form import YeastCompareForm, YeastForm
from data.models.yeast_model import TempMatchEnum, Yeast
from app.view_models.yeast_view_model import YeastMatchResultsViewModel
from app.fsa_session import db_session


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
    yeast_one_id = request.form.get("yeast_one")
    yeast_two_id = request.form.get("yeast_two")

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

    yeast_form = YeastForm.build()
    compare_form = YeastCompareForm.build()

    return render_template(
        "yeast_matcher.html",
        yeast_form=yeast_form,
        compare_form=compare_form,
        match_results=match_results,
    )
