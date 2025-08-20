from flask import Response, render_template
from . import bp

@bp.get('/select', endpoint='select')
def planet_list_view() -> Response | str:
    return render_template('compare/select.html')
