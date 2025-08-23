from flask import Response, render_template
from app.routes.schema import get_view_schema

def index() -> Response | str:
    pg_name = "index"
    return render_template('app/views/index.html', pg_name=pg_name)

index_route = get_view_schema(rule='/', func=index, endpoint='index', methods=["GET"])
