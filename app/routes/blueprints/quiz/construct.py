from flask import Response, render_template
from . import bp

@bp.get('/construct', endpoint='construct')
def construct_view() -> Response | str:
    return render_template('quiz/construct.html')
