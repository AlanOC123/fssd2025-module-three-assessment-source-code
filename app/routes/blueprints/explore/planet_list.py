from flask import Response, render_template
from . import bp
from app.data.interface import get_planets

@bp.get('/planet_list/<string:filter_key>', endpoint='planet_list')
def planet_list(filter_key: str | None) -> Response | str:
    planets_list = get_planets(filter_key)
    return render_template('explore/views/planet-list.html', planets=planets_list)
