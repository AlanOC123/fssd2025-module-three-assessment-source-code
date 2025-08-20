from flask import Response, render_template
from app.routes.schema import get_view_schema

def index() -> Response | str:
    return render_template('index.html')

index_route = get_view_schema(rule='/', func=index, endpoint='index', methods=["GET"])
