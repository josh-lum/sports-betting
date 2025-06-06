from flask import render_template, Blueprint
from core.rule_engine import suggest_bets

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    bets = suggest_bets()
    return render_template('index.html', bets=bets)
