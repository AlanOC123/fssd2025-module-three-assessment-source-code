from flask import Response, render_template, session
from app.data.interface import get_planet_by_id
from . import bp

@bp.get('/', endpoint='index')
def index() -> Response | str:
    recently_viewed = session.get("recently_viewed") or ["earth", "mars", "jupiter"]
    planets_viewed = None

    if recently_viewed:
        planets_viewed = [ get_planet_by_id(p)[0] for p in recently_viewed ]

    print(planets_viewed)

    return render_template('explore/views/index.html', recently_viewed=planets_viewed)
