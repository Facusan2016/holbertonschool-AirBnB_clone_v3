#!/usr/bin/python3
"""App module using Flask"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def statusRoute():
    """Status Route"""
    return jsonify({
        "status": "OK"
    })

@app_views.route('/stats')
def count():
    """ Count objects """
    dictob = {}
    clss = {
        "Amenity": "amenities",
        "Place": "places",
        "State": "states",
        "City": "cities",
        "Review": "reviews",
        "User": "users"
    }

    for cls in clss:
        count = storage.coun(cls)
        dictob[clss.get(cls)] = count
    return jsonify(dictob)
