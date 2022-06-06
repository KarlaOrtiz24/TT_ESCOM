from flask import Flask
from flask import render_template
from flask import Response
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
import Routes.Routes as routes
from pathlib import Path
import io
import wave
import numpy as np
import scipy.io.wavfile
import soundfile as sf
from scipy.io.wavfile import write

app = Flask(__name__)

def iniciarCamara():
    from camara import VideoCamara
    cam = VideoCamara()
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')
        
def iniciarSenas():
    from senar import CamaraSenas
    cam = CamaraSenas()
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')

@app.route('/camara')
def camara():
    return Response(iniciarCamara(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/senas')
def senar():
    return Response(iniciarSenas(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escucha')
def escucha():
    return render_template('escucha.html', data = 'Voz convertida a texto')

@app.route('/ver')
def ver():
    return render_template('ver.html')

@app.route('/menu-principal')
def menuPrincipal():
    return render_template('menu-principal.html')

@app.route('/traducir', methods=['GET', 'POST'])
def traduccionVoz():
    import reconocedorVoz 
    import mostrarGlosa
    import nlp
    
    if request.method == 'POST':
        file = request.files.get('file')
        file_bytes = request.files['file'].read()
        ruta = routes.juntarRutas(routes.getRutaActual(__file__), 'audioTraducir.mp3')
        ruta_wav = routes.juntarRutas(routes.getRutaActual(__file__), 'audioTraducir.wav')
        
        
        
        resp = {}
        return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=False)
