from flask import Blueprint
from app.routes.schema import get_blueprint_schema

bp = Blueprint(name='explore', import_name=__name__, url_prefix='/explore')

from . import index
from . import planets

explore_bp_route = get_blueprint_schema(bp)
