"""
Author:               Scotty Wallace, Cheyanne Kester
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/12/2022
Date Last Modified:   11/29/2022

This creates a landing page and an image upload page for our app
Initializes routes for all pages

NOTE THAT NON ROUTED FUNCTIONS MUST BE DECLARED BEFORE ROUTED FUNCTIONS TO WORK
"""

import os
import palette_finder as pf

from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from static import tempPalettes as tp
from werkzeug.utils import secure_filename


temp_path = None
bp = Blueprint('gbiv', __name__)

"""---non-routed functions---"""
# modified from https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

# gets palette using lib ian wrote
def get_palette(path):
   domColor = pf.color_extractor(path)
   # second index yields dom
   return pf.palette_generator(domColor[1])

# ensures palette data will be presentable
def parsePalette(httpStr):
    colorList = []
    color = ''
    append = False

    for s in httpStr:
        # valid hex chars spaced by anything (assuming get 0-f only)
        if s.isalnum():
            color += s
            append = True
        elif(append):
                colorList.append(str(color))
                color = ''
                # only append after first non-hex char
                append = False

    return colorList 

"""---routed functions---"""
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

# sample palettes page
@bp.route('/samplePalettes')
def samplePalettes():
    palettes = tp.getPalettes()
    return render_template('samplePalettes.html', palList=palettes)
    
# page displaying all palettes generated from uploaded image
@bp.route('/gbived/<palettes> <image>')
def gbived(palettes, image):
    # ensuring valid hex colors

    parsedPalettesList = parsePalette(palettes)
    return render_template('index.html', palettes=str(palettes), pList=parsedPalettesList, t_file=image)  #image not working

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
        # makes sure filename cannot be used to attack website
        filename = secure_filename(file.filename)

        #saves file to web temp storage
        path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        return redirect(url_for('gbiv.gbived', palettes = get_palette(path), image=filename)) 

    return render_template('index.html', palettes=None, image=None)
