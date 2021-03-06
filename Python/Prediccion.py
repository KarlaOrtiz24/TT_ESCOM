import cv2
import mediapipe as mp
import os
import numpy as np
from keras_preprocessing.image import load_img, img_to_array
from keras.models import load_model
import spacy
from spacy import displacy
import Routes.Routes as routes

#model = load_model(r'C:\Users\Karla\TT_ESCOM\ABECEDARIO.h5')
#model.summary()
#dir_img = 'C:/Users/Karla/TT_ESCOM/Aprendizaje_Abecedario'
#getting the labels form data directory
#labels = (os.listdir(data_dir))
#print('labels', labels)
#labels[-1] = 'Nothing'
#print(labels)
# Lectura de la camara

modelo = routes.juntarConPadre(__file__, 'Convolucional.h5')
# modelo = 'C:/Users/Karla/TT_ESCOM/Convolucional.h5'
cnn = load_model(modelo)

# direccion = r'C:/Users/Karla/TT_ESCOM/Aprendizaje_Abecedario'
direccion = routes.juntarConPadre(__file__, 'Aprendizaje_Abecedario')
print('Direccion',direccion)
dir_img =os.listdir(direccion)
print('Nombres', dir_img)
aux = 0
for i in dir_img:
    print(aux, "=", i)
    aux = aux + 1

cap = cv2.VideoCapture(0)

# Creacion de objeto para la deteccion y el seguimiento de las manos
clase_manos = mp.solutions.hands
manos = clase_manos.Hands(
    static_image_mode = False,
    max_num_hands = 2,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
)

# Dibujo de las manos
dibujo = mp.solutions.drawing_utils



while (1):
    cont_letras = 0
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    copia = frame.copy()
    resultado = manos.process(color)
    posiciones = []
    frase = ""
    letra = ""
    if resultado.multi_hand_landmarks:
        for mano in resultado.multi_hand_landmarks:
            for id, lm in enumerate(mano.landmark):
                alto, ancho, c = frame.shape
                corx, cory = int(lm.x * ancho), int(lm.y * alto)
                posiciones.append([id, corx, cory])
                dibujo.draw_landmarks(frame, mano, clase_manos.HAND_CONNECTIONS)
            if len(posiciones) != 0:
                punto_i1 = posiciones[3]
                punto_i2 = posiciones[17]
                punto_i3 = posiciones[10]
                punto_i4 = posiciones[0]
                punto_i5 = posiciones[9]
                x1, y1 = (punto_i4[1] - 50), (punto_i4[2] - 50)
                ancho, alto = (x1 + 100), (y1 + 100)
                x2, y2 = x1 + ancho, y1 + alto
            dedos_reg = copia[y1:y2, x1:x2]
            dedos_reg = cv2.resize(dedos_reg, (60, 60))
            x = img_to_array(dedos_reg)  # Convertir la imagen a una matriz
            x = np.expand_dims(x, axis=0)  # Se agrega un nuevo eje
            vector = cnn.predict(x)  # Va a ser un arreglo de 2 dimensiones
            resultado = vector[0]
            respuesta = np.argmax(resultado)  # Entrega el indice del valor m??s alto 0 | 1
            if respuesta == 0:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[0]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "a"
                print("a")
            elif respuesta == 1:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[1]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "b"
                print("b")
            elif respuesta == 2:
                #    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                    cv2.putText(frame, '{}'.format(dir_img[2]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                    letra = "c"
                    print("c")
            elif respuesta == 3:
                 #   cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[3]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "d"
                print("d")               
            elif respuesta == 4:
              #  cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[4]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "e"
                print("e")

            elif respuesta == 5:
               # cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[5]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "f"
                print("f")
            elif respuesta == 6:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[6]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "g"
                print("g")

            elif respuesta == 7:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[7]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "h"
                print("h")
            elif respuesta == 8:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[8]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "i"
                print("i")

            elif respuesta == 9:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[9]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "l"
                print("l")
            elif respuesta == 10:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[10]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "m"
                print("m")

            elif respuesta == 11:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[11]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "n"
                print("n")
            elif respuesta == 12:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[12]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "o"
                print("o")
            elif respuesta == 13:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[13]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "p"
                print("p")
            elif respuesta == 14:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[14]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "r"
                print("r")
            
            elif respuesta == 15:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[15]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "s"
                print("s")
            elif respuesta == 16:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[16]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "t"
                print("t")
            elif respuesta == 17:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[17]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "u"
                print("u")
            elif respuesta == 18:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[18]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "v"
                print("v")
            elif respuesta == 19:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[19]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "w"
                print("w")
            elif respuesta == 20:
                #cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                cv2.putText(frame, '{}'.format(dir_img[20]), (x1, y1 - 5), 1, 1.3, (255, 0, 0), 1, cv2.LINE_AA)
                letra = "y"
                print("y")
            else:
                cv2.putText(frame, 'LETRA_DESCONOCIDA', (x1, y1 - 5), 1, 1.3, (0, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("Proyecto Final", cv2.flip(frame, 1))
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()