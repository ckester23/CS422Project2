# [Gbiv](http://skumperdump.pythonanywhere.com/)


Gbiv is a web application with the goal of making color theory more accessible to the world and inspiring the designer in all of us. The title above is clickable and leads to our website.


## Contents of Repository


### docs folder

This folder contains the documentation for the Gbiv application including the proposal, the SRS, the SDS, user docs, and developer's manual.

### gbiv folder

This folder contains the flask code for running our app


## Running our app locally


### setting up a python virtual environment

How to setup a virtual environment with python [https://docs.python.org/3/library/venv.html#module-venv]

### installing requirements 

Activate your virtual environment then run `python3 -m pip install -r requirements.txt`

### running flask app

From the main project directory run `flask --app gbiv/gbivApp.py --debug run`
