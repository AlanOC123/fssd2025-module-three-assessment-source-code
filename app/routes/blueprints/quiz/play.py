from flask import render_template, request
from . import bp
from .session_manager import set_in_progress, restart

@bp.get('/play', endpoint="play")
def play():
    if request.args.get("retry", default=False) in { "true", "y", "True", "1" }:
        restart()

    set_in_progress(True)  
    return render_template('quiz/views/play.html')