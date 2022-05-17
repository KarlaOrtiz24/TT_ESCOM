from flask import Flask
from flask import render_template
from flask import Response
import cv2 as cv 

app = Flask(__name__)
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

def iniciarCamara():
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv.flip(frame, 1)
            (flag, encodedImage) = cv.imencode('.jpg', frame)
            if not flag:
                continue
            
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

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

cap.release()