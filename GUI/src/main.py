from flask import Flask
from flask import render_template
from flask import Response

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
    return render_template('escucha.html')

@app.route('/ver')
def ver():
    return render_template('ver.html')

@app.route('/menu-principal')
def menuPrincipal():
    return render_template('menu-principal.html')

if __name__ == '__main__':
    app.run(debug=False)
    
