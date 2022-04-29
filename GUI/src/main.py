from flask import Flask
from flask import render_template
from flask import Response
import cv2 as cv 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escucha')
def escucha():
    return render_template('escucha.html')

@app.route('/ver')
def ver():
    return render_template('ver.html')

@app.route('/menu-principal')
def menuPrincipal():
    return render_template('menu-principal.html')

if __name__ == '__main__':
    app.run(debug=True)