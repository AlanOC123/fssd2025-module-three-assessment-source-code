from flask import Response, render_template
from . import bp

@bp.get('/planet_list', endpoint='planet_list')
def all_planets_view() -> Response | str:
    return render_template('explore/planet_list.html')
