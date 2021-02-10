from flask import Blueprint, current_app

bp = Blueprint('hello', __name__)

@bp.route('/')
def hello() -> str:
    # return f"Backend is {current_app.config['STORAGE_BACKEND']}"
    return f"<html>Welcome! This web provides the service for finding wikidata properties.</html>"
