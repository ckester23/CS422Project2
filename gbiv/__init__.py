"""
Author:               Scotty Wallace
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/12/2022
Date Last Modified:   11/12/2022

Description: This initializes our flask app
"""

import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import upload
    app.register_blueprint(upload.bp)
    app.add_url_rule('/', endpoint='index')

    return app
