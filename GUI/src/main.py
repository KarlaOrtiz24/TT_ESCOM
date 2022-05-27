from flask import Flask
from flask import render_template
from flask import Response
import random

app = Flask(__name__)

def iniciarCamara():
    from camara import VideoCamara
    cam = VideoCamara()
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n')

def iniciarMicro():
    import reconocedorVoz 
    import mostrarGlosa 
    import nlp 

    cad = ''

    texto = reconocerVoz()
    # print ("Fase 1: " + texto)
    
    cad += '<p>Fase1: ' + texto + '</p>'

    glosa = nlp(texto)
    # print ("Fase 2: ")
    # print (glosa)
    
    cad += '<p>Fase 2: ' + glosa + '</p>'

    Data = []
    for x in glosa:
        Data += obtenerData(x)
        
    # print(Data)
    # mostrarSeñas(Data)
    

@app.route('/camara')
def camara():
    return Response(iniciarCamara(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/microfono')
def micro():
    return Response(iniciarMicro())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escucha')
def escucha():
    return render_template('escucha.html')

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
