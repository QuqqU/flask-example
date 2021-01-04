from flask import Blueprint, render_template, url_for
from pybo.models import Question
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hi')
def hi(): 
    return "hil"


@bp.route('/')
def index(): 
    return redirect(url_for('question._list')) # blueprint:question / func:_list
