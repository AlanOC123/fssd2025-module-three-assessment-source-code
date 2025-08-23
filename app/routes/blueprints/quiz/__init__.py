from flask import Blueprint
from app.routes.schema import get_blueprint_schema

bp = Blueprint(name="quiz", import_name=__name__, url_prefix="/quiz")

from . import index

quiz_bp_route = get_blueprint_schema(blueprint=bp)
