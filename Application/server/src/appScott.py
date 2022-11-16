"""
Author:               Scotty Wallace & Cheyanne Kester
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/12/2022
Date Last Modified:   11/15/2022

Description: This initializes our flask app
"""

import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['UPLOAD_FOLDER'] = '/Application/static/images'


    # manually pushing app context
    with app.app_context():
        from . import upload
        app.register_blueprint(upload.bp)

    app.add_url_rule('/', endpoint='index')

    return app

if __name__ == "__main__":
    create_app().run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))