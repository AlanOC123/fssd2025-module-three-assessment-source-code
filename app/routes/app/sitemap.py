from flask import Response, render_template
from app.routes.schema import get_view_schema

def sitemap() -> Response | str:
    return render_template('app/views/sitemap.html')

sitemap_route = get_view_schema(rule='/sitemap', func=sitemap, endpoint='sitemap', methods=["GET"])
