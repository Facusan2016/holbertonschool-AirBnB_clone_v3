#!/usr/bin/python
"""App module using Flask"""
from flask import Flask, jsonify, Response
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    """Main function of Flask app"""
    app.run(host=os.getenv('HBNB_API_HOTS', '0.0.0.0'),
            port=os.getenv('HBNH_API_PORT', '5000'),
            threaded=True)
