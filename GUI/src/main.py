from flask import Flask
from flask import render_template
from flask import Response
from flask import request
from flask import jsonify
import random

app = Flask(__name__)

def iniciarCamara():
    from camara import VideoCamara
    cam = VideoCamara()
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')

@app.route('/camara')
def camara():
    return Response(iniciarCamara(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escucha')
def escucha():
    return render_template('escucha.html', data = 'Voz convertida a texto')

@app.route('/ver')
def ver():
    return render_template('ver.html')

@app.route('/carga')
def carga():
    pantallas_carga = ['', '1', '2', '3']
    eleccion = random.randint(0, 3)
    pantalla = 'loading' + pantallas_carga[eleccion] + '.html'
    
    return render_template(pantalla)

@app.route('/menu-principal')
def menuPrincipal():
    return render_template('menu-principal.html')

if __name__ == '__main__':
    app.run(debug=False)
