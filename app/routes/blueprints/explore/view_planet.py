from flask import render_template, redirect, url_for, Response, session
from . import bp
from app.data.interface import get_planet_by_id

def update_recents(planet_id: str, limit: int = 3) -> None:
    recents = list(session.get("recently_viewed", []))

    if planet_id in recents:
        recents.remove(planet_id)
    recents.insert(0, planet_id)
    print(recents)
    session["recently_viewed"] = recents[:limit]

@bp.get('/view/<string:planet_id>', endpoint='view_planet')
def view_planet(planet_id: str | None):
    if not planet_id:
        return redirect(url_for("explore.planet_list", filter_key='all'))
    update_recents(planet_id=planet_id)
    planet = get_planet_by_id(planet_id)[0]
    if not planet:
        return redirect(url_for("explore.planet_list", filter_key='all'))
    print(planet)
    return render_template('explore/views/view-planet.html', planet=planet)
