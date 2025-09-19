from flask import Response, render_template, session
from app.data.interface import get_planet_by_id, get_planet_main_data
from . import bp

@bp.get('/', endpoint='index')
def index() -> Response | str:
    recently_viewed = session.get("recently_viewed") or ["earth"]
    planets_viewed = []

    if recently_viewed:
        planets_viewed = [ get_planet_by_id(p) for p in recently_viewed]

    core_data = [get_planet_main_data(p) for p in planets_viewed]

    return render_template('explore/views/index.html', recently_viewed=core_data)
