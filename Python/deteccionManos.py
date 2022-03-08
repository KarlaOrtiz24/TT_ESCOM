#Detector de manos 
#Creado el 25/11/2021
#Sanchez Pizano Irving Daniel 
#Ortiz Chavez Karla 
#Macedo Cruz Irvin Yoariht 
#Piñon Caballero Angel Ramon
import os
from unittest import result

import cv2
import mediapipe as mp
import numpy as np
from matplotlib.pyplot import axis
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from Clasificador import clasificador
from keras.models import load_model
modelo =r' C:\Users\Karla\TT_ESCOM'
rbc= load_model(modelo)
carpeta = r' C:\Users\Karla\TT_ESCOM\Aprendizaje_Abecedario'
direccion= os.listdir(carpeta)
posiciones =[]
def deteccionManos(neural_network):
    print('Retorno del clasificador ', neural_network)
    mp_drawing = mp.solutions.drawing_utils    ##Dibujo     #ayuda a dibujar los 21 puntos y sus conexiones
    mp_hands = mp.solutions.hands               ##Manos    #Se emplea solución hands
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)        #Leemos la camara
    while(1): 
        ret, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Se cambia de BGR a RGB ya que las detecciones se hacen con RGB
        copia = frame.copy
        resultado=mp_hands.process(frame_rgb)
        posiciones =[]
        if resultado.multi_hand_landmarks: #Se configura que los puntos aparezcan siempre y cuando esten manos enfrente de la camara
            for mp_hands in resultado.multi_hand_landmarks: 
                for id, lm in enumerate(mp_hands.landmark):
                    alto, ancho, c = frame.shape
                    cordenadax, cordenaday = int(lm.x*ancho), int(lm.y*alto)
                    posiciones.append([id, cordenadax, cordenaday])
                    mp_drawing.draw_landmarks(frame, mp_hands, mp_drawing.HAND_CONECTIONS)
                if len(posiciones)!=0: 
                    punto1= posiciones[3] 
                    #punto2 = posiciones[8] #Aun no estoy segura
                    #punto3 = posiciones[3] #Lo mismo
                    #punto4 = posiciones[9]
                    punto5 = posiciones[17]
                    #punto6 = posiciones[5]
                    #punto7 = posiciones[10]
                    #punto8 = posiciones[4]
                    punto9 = posiciones[10]
                    #punto10 = posiciones[2]
                    #punto11 = posiciones[2]
                    #punto12 = posiciones[2]
                    punto13 = posiciones[0]
                    #punto14 = posiciones[2]
                    #punto15 = posiciones[2]
                    #punto16 = posiciones[2]
                    #punto17 = posiciones[2]
                    punto18 = posiciones[9]
                    #punto19 = posiciones[2]
                    #punto20 = posiciones[2]
                    punto21 = posiciones[2]
                    x1, y1 = (punto18[1]-100, punto18[2]-100)
                    ancho, alto = (x1 +200)(y1 + 200)
                    x2, y2 = x1 +ancho, y1 + alto 
                    dedos_reg = copia[y1:y2, x1:x2]
                    dedos_reg = cv2.resize(dedos_reg, (200,200), interpolation=cv2.INTER_CUBIC)
                    x = img_to_array(dedos_reg)
                    x = np.expand_dims(x, axis=0)
                    vector = rbc.predict(x)
                    resultado = vector[0]
                    respuesta = np.argmax(resultado)
                    if respuesta == 0: 
                        print('Resultado', resultado)
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 3)
                        cv2.putText(frame, '{}'.format(direccion[0], x1, y1 - 5), 1, 1.3, (0, 255,0), 1, cv2.LINE_AA)
                    elif respuesta == 1: 
                        print('Resultado', resultado)
                        cv2.rectangle(frame, (x1,y1),(x2,y2) (0,0, 255), 3)
                        cv2.putText(frame, '{}'.format(direccion[1]), (x1,y1)-5, 1, 1.3,(0,0,255), 1, cv2.LINE_AA)
                    elif respuesta == 2: 
                        print('Resultado', resultado)
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1)-5, 1, 1.3,(255,0,0), 1, cv2.LINE_AA)
                    elif respuesta == 3: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1)-5, 1, 1.3,(255,0,255), 1, cv2.LINE_AA)
                    elif respuesta == 4: 
                       print('Resultado', resultado) 
                       cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                       cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1)-5, 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    else: 
                        cv2.putText(frame, 'Letra desconocida', x1, y1-5, 1, 1.3, (0,255,255), 1, cv2.LINE_AA)
        cv2.imshow('Video', frame)
        k = cv2.waitKey(1)
        if k == 27: 
            break
    cap.realese()
    cv2.destroyAllWindows()  







'''with mp_hands.Hands(                            #Opciones de Configuracion
    static_image_mode=False,                    #False porque no estamos tomando como entrada una imagen
    max_num_hands=2,                            #Numero maximo de manos por detectar
    min_detection_confidence=0.5) as hands:     #Valor mínimo de confianza del modelo de detección de manos
       while True:
        if ret == False:
            break
            height, width, _ = frame.shape
            
            
        frame = cv2.flip(frame, 1)
            results = hands.process(frame_rgb)  #se obtinenen las detecciones mediante las salidas multi_handedness y multi_hand_landmarks.
            
            # Dibujando los puntos y las conexiones mediante mp_drawing
                for hand_landmarks in results.multi_hand_landmarks:# usamos un for para obtener cada grupo de 21 puntos por cada mano detectada.
                    mp_drawing.draw_landmarks( # dibujamos los puntos y conexiones con ayuda del propio mediaPipe
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, #se dibujan las conexiones entre los puntos.
                        mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=3, circle_radius=5), #color, grosor de línea y radio de cada punto
                        mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=4, circle_radius=5)) #color, grosor de línea y radio de cada conexion
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()'''

'''neural_return = clasificador()
deteccionManos(neural_return) '''
