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

app = Flask(__name__)

# binary secret key
app.secret_key = b'goducks'

# creating upload folder
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)
app.config['UPLOAD_FOLDER'] = upload_folder

# manually pushing app context
with app.app_context():
    import gbiv
    app.register_blueprint(gbiv.bp)
    app.add_url_rule('/', endpoint='index')
