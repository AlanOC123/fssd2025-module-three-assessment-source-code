from flask import render_template
from . import bp
from .session_manager import set_in_progress

def get_question_list(id_arr: list) -> list:
    return []

@bp.get('/play', endpoint="play")
def play():
    set_in_progress(True)  
    return render_template('quiz/views/play.html')