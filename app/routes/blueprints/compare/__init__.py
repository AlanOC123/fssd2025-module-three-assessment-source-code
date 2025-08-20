from flask import Blueprint
from app.routes.schema import get_blueprint_schema

bp = Blueprint(name='compare', import_name=__name__, url_prefix='/compare')

from . import select

compare_bp_route = get_blueprint_schema(bp)
