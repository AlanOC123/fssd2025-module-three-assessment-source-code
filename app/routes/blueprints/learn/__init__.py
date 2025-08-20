from flask import Blueprint
from app.routes.schema import get_blueprint_schema

bp = Blueprint(name='learn', import_name=__name__, url_prefix='/learn')

from . import all_planets

learn_bp_route = get_blueprint_schema(bp)
