from flask import Flask, render_template, make_response
import os

app = Flask(__name__)

@app.route('/')
def index():
    
    template = render_template('layout.html')
    response = make_response(template)
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
    return response
#<link rel="stylesheet" href="{{ url_for('static', filename='/Application/static/styleScott.css') }}">

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))