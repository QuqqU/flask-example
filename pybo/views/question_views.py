from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect
from pybo.models import Question
from pybo.form import QuestionForm, AnswerForm
from pybo import db
from pybo.views.auth_views import login_required

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list')
def _list():
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.create_day.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html',
                           question_list=question_list)


# ? hello
# ! hello
# @param hi
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',
                           question=question,
                           form=form)


@bp.route('/create', methods=('get', 'post'))
@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data,
                            context=form.content.data,
                            create_day=datetime.now(),
                            user=g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('question/question_form.html', form=form)
