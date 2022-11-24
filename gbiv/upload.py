"""
Author:               Scotty Wallace & Cheyanne Kester
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/12/2022
Date Last Modified:   11/20/2022

This creates a landing page and an image upload page for our app
Initializes routes for all pages
"""
import os
import sys
from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from . import hslStringParser as hsp
from . import palette_finder as pf

UPLOAD_FOLDER = current_app.config['UPLOAD_FOLDER'] 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

bp = Blueprint('upload', __name__)


# from https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
# non routed functions first!
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# gets palette using lib ian wrote
def get_palette(path):
   domColor = pf.color_extractor(path)
   # second index yields dom
   return pf.palette_generator(domColor[1])

# landing page
@bp.route('/')
def index():
    return render_template('index.html', palettes=None)

# about us page
@bp.route('/about')
def about():
    return render_template('about.html')

# color theory page
@bp.route('/colortheory')
def colortheory():
    return render_template('colortheory.html')

@bp.route('/samplePalettes')
def samplePalettes():
    return render_template('samplePalettes.html')
    
# page displaying user's palettes
@bp.route('/uploaded/<palettes>')
def uploaded(palettes):
    parsedPalettesList = hsp.parseListOfPalettes(palettes) #cheyanne
    return render_template('index.html', palettes=str(palettes), pList=parsedPalettesList)  #image not working

# upload page
# code is run after clicking submit button
@bp.route('/', methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.filename == '':
        flash('no file given')
    elif not(allowed_file(file.filename)):
        flash('invalid filetype')
    else: 
        filename = secure_filename(file.filename)
        userImage = file.filename
        path = os.path.join(UPLOAD_FOLDER + filename)
        file.save(path)
        return redirect(url_for('upload.uploaded', palettes = get_palette(path)))

    return render_template('index.html', palettes=None)
