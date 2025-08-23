from flask import Response, render_template, session
from . import bp

@bp.get('/', endpoint='index')
def index() -> Response | str:
    recently_viewed = session.get("recently_viewed")
    return render_template('explore/views/index.html')
