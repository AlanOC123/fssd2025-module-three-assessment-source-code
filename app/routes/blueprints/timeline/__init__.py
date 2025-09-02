from flask import Blueprint
from app.routes.schema import get_blueprint_schema

bp = Blueprint(name='timeline', import_name=__name__, url_prefix='/timeline')

from . import index

compare_bp_route = get_blueprint_schema(bp)
