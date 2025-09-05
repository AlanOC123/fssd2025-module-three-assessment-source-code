from flask import render_template, abort
from app.data.interface import get_timeline_data
from . import bp

@bp.get('/history/<string:timeline_id>', endpoint="history")
def history_timeline(timeline_id):
    if not timeline_id:
        abort(404)
        raise ValueError("no timeline given")

    timeline_data = get_timeline_data(timeline_id)
    print(timeline_data)
    return render_template('timeline/views/history-timeline.html', timeline_data=timeline_data)
