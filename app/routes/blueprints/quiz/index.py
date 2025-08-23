from flask import Response, render_template
from . import bp

@bp.get('/', endpoint='index')
def index() -> Response | str:
    return render_template('quiz/views/index.html')
