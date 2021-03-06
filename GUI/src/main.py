from flask import Flask
from flask import render_template
from flask import Response
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
import Routes.Routes as routes
from pathlib import Path

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

@app.route('/test')
def testVideo():
    import VozaLSM
    return redirect('escucha')

@app.route('/escucha')
def escucha():
    return render_template('escucha.html')

@app.route('/ver')
def ver():
    return render_template('ver.html')

@app.route('/menu-principal')
def menuPrincipal():
    return render_template('menu-principal.html')

@app.route('/senar')
def dinamicas():
    import PrediccionAction
    senar()
    return redirect('ver')

@app.route('/traducir', methods=['GET', 'POST'])
def traduccionVoz():
    import mostrarGlosa
    import nlp
    import cv2
    
    if request.method == 'POST':
        data = request.get_data()
        # print(data.decode())
        
        frase = data.decode().split('"')
        if('.' in frase[1]):
            frase = frase[1].split('.')[0]
        elif('¿' in frase[1]):
            frase = frase[1].split('¿')[1]
            frase = frase.split('?')[0]
        
        if(',' in frase):
            frase = frase.split(',')
            frase = frase[0] + frase[1]
        
        print(frase)
        
        glosa = nlp.nlp(str(frase))
        print(glosa)
        
        videos = routes.getArchivosCarpeta(routes.juntarConPadre(__file__, 'BD'))
        # print(videos)
        
        resp = {}
        
        for palabra in glosa:
            if palabra + '.mp4' in videos:
                capture = cv2.VideoCapture(routes.juntarConPadre(__file__, palabra + '.mp4'))
                while (capture.isOpened()):
                    ret, frame = capture.read()
                    if (ret == True):
                        cv2.namedWindow (palabra, cv2.WINDOW_NORMAL)
                        cv2.imshow(palabra, frame)
                        if cv2.waitKey(10) & 0xFF == 27:
                            break
                        else:
                            break

                capture.release()
                cv2.destroyAllWindows()
                    
            resp[palabra] = palabra + '.mp4'
        
        return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=False)
