from flask import Response, render_template
from . import bp

@bp.get('/all-planets', endpoint='all_planets')
def all_planets_view() -> Response | str:
    return render_template('learn/all-planets.html')
