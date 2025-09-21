from flask import render_template, flash, redirect, url_for
from app.data.interface import get_timeline_data
from . import bp

@bp.get('/history/<string:timeline_id>', endpoint="history")
def history_timeline(timeline_id):
    if not timeline_id:
        flash("Timeline not found")
        return redirect(url_for('timeline.index'))

    timeline_data = get_timeline_data(timeline_id)
    return render_template('timeline/views/history-timeline.html', timeline_data=timeline_data)
