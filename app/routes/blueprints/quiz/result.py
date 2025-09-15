from flask import render_template, session
from datetime import datetime, timezone
from . import bp

@bp.get("/result", endpoint="result")
def result():
    return '<h1>End</h1>'