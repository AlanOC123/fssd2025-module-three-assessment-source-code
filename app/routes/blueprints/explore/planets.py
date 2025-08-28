from flask import render_template, redirect, url_for, Response, session, request, abort
from . import bp
from app.data.interface import get_planet_by_id, get_planet_data, get_planets

def update_recents(planet_id: str, limit: int = 3) -> None:
    recents = list(session.get("recently_viewed", []))

    if planet_id in recents:
        recents.remove(planet_id)
    recents.insert(0, planet_id)

    session["recently_viewed"] = recents[:limit]

def _get_valid_planet_or_404(planet_id: str):
    planet = get_planet_by_id(planet_id)

    if not planet:
        abort(404)
    return planet

def _get_page_payload(curr_planet_id: str):
    all_planets = get_planets()
    curr_planet = _get_valid_planet_or_404(curr_planet_id)
    return { "curr_planet": curr_planet, "all_planets": all_planets }


@bp.get('/planets', endpoint='planets_default')
def planets_default():
    # get the last visted planet from the session as a back up with a default to earth. Always hydrates
    last_visited_planet = session.get('last_visited') or 'earth'

    # get the planet data or fail a 404
    planet_data = _get_page_payload(last_visited_planet)

    return render_template('explore/views/planets.html', planet_data=planet_data)

@bp.get('/planets/<string:planet_id>', endpoint='planet_selected')
def planet_selected(planet_id: str):
    # gather the data up into an object so its easier to work with in the JS
    planet_data = _get_page_payload(planet_id)

    # add the valid id to the session data
    session['last_visited'] = planet_id

    # update the session recents for the index page if a new planet was viewed for a quick select
    update_recents(planet_id=planet_id)

    # render the page with the planet data
    return render_template('explore/views/planets.html', planet_data=planet_data)
