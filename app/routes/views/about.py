from flask import Response, render_template
from app.routes.schema import get_view_schema

def about() -> Response | str:
    return render_template('about.html')

about_route = get_view_schema(rule='/about', func=about, endpoint='about', methods=["GET"])
