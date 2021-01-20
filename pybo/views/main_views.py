from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from pybo.models import Question


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hi')
def re_hi():
    return "hil"


@bp.route('/')
def index():
    print(123)
    return redirect(url_for('question._list'))  # blueprint:question / func:_list
