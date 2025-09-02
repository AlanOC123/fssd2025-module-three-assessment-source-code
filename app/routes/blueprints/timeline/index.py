from flask import Response, render_template
from . import bp
from app.data.interface import get_timeline, get_decades

@bp.get('/', endpoint='index')
def index() -> Response | str:
    timeline_list = get_timeline()
    decades_list = get_decades()
    print(decades_list)
    timeline_data = []

    for ind in range(len(timeline_list)):
        timeline = timeline_list[ind]
        img = timeline.get("mainImg")
        num_milestones = timeline.get("numMilestones")
        pseudoname = timeline.get("pseudoname")
        decade = decades_list[ind]

        if not img or not num_milestones or not pseudoname or not decade:
            continue

        timeline_data.append({ "img": img, "milestones": num_milestones, "name": pseudoname, "decade": decade })

    return render_template('timeline/views/index.html', timeline_data=timeline_data, decades_list=decades_list)
