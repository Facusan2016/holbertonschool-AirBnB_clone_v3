#!/usr/bin/python3
"""App module using Flask"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def statusRoute():
    """Status Route"""
    return jsonify({
        "status": "OK"
    })
