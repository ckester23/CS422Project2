"""
Author:               Scotty Wallace
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/12/2022
Date Last Modified:   11/12/2022

This creates a landing page and an image upload page for our app
"""
import os
from flask import Blueprint, current_app, flash, g, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from .Application.server.src import palette_finder

UPLOAD_FOLDER = current_app.config['UPLOAD_FOLDER'] 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

bp = Blueprint('upload', __name__)

# from https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# landing page
@bp.route('/')
def index():
    return render_template('templates/upload/index.html')

# upload page
@bp.route('/upload', methods=['GET', 'POST'])
def fileUpload():
    if request.method == 'Post':
        if 'file' not in request.files:
            flash('file not in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('no file given')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config[UPLOAD_FOLDER], filename))

    return render_template('templates/upload/upload.html')
