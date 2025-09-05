from flask import Response, render_template
from . import bp
from app.data.interface import get_timeline, get_decades

@bp.get('/', endpoint='index')
def index() -> Response | str:
    timeline_list = get_timeline()
    print(timeline_list[0]["id"])

    return render_template('timeline/views/index.html', timeline_data=timeline_list)
