from flask import Blueprint
from app.routes.schema import get_blueprint_schema

bp = Blueprint(name='explore', import_name=__name__, url_prefix='/explore')

from . import planet_list
from . import index
from . import view_planet

explore_bp_route = get_blueprint_schema(bp)
