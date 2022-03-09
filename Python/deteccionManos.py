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
#from Clasificador import clasificador
from keras.models import load_model
modelo =os.path.join(os.path.join(os.path.dirname(__file__),'..'),'ABECEDARIO.h5')
print('modelo', modelo)
rbc= load_model(modelo)
carpeta =os.path.join(os.path.join(os.path.dirname(__file__),'..'),'Aprendizaje_Abecedario')
print(carpeta)
direccion= os.listdir(carpeta)
posiciones =[]

def deteccionManos():
    # print('Retorno del clasificador ', neural_network)
    clase_manos = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils    ##Dibujo     #ayuda a dibujar los 21 puntos y sus conexiones
    manos = clase_manos.Hands()             ##Manos    #Se emplea solución hands
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)        #Leemos la camara
    while(1): 
        ret, frame = cap.read()
        color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Se cambia de BGR a RGB ya que las detecciones se hacen con RGB
        copia = frame.copy()
        resultado=manos.process(color)
        posiciones =[]
        if resultado.multi_hand_landmarks: #Se configura que los puntos aparezcan siempre y cuando esten manos enfrente de la camara
            for manos in resultado.multi_hand_landmarks: 
                for id, lm in enumerate(manos.landmark):
                    alto, ancho, c = frame.shape
                    cordenadax, cordenaday = int(lm.x*ancho), int(lm.y*alto)
                    posiciones.append([id, cordenadax, cordenaday])
                    mp_drawing.draw_landmarks(frame, manos, clase_manos.HAND_CONNECTIONS)
                if len(posiciones)!=0: 
                    punto1= posiciones[3] 
                    punto2 = posiciones[20] #Aun no estoy segura
                    punto3 = posiciones[9] #Lo mismo
                    punto4 = posiciones[17] #D
                    punto5 = posiciones[17] #E
                    punto6 = posiciones[19] #F
                    punto7 = posiciones[10] #G
                    punto8 = posiciones[14] #H
                    punto9 = posiciones[10] #I
                    punto10 = posiciones[15] #L
                    punto11 = posiciones[14] #M
                    punto12 = posiciones[12] #N
                    punto13 = posiciones[6] #O
                    punto14 = posiciones[13] #P
                    punto15 = posiciones[19] #R
                    punto16 = posiciones[13]#S
                    punto17 = posiciones[12]#T
                    punto18 = posiciones[17]#U
                    punto19 = posiciones[17] #V
                    punto20 = posiciones[19] #W
                    punto21 = posiciones[13]#Y
                    x1, y1 = (punto18[1]-100, punto18[2]-100)
                    ancho, alto = (x1 +28),(y1 + 28)
                    x2, y2 = x1 +ancho, y1 + alto 
                    dedos_reg = copia[y1:y2, x1:x2]
                    dedos_reg = cv2.resize(dedos_reg, (28,28), interpolation=cv2.INTER_CUBIC)
                    x = img_to_array(dedos_reg)
                    x = np.expand_dims(x, axis=0)
                    vector = rbc.predict(x)
                    resultado = vector[0]
                    respuesta = np.argmax(resultado)
                    if respuesta == 0: 
                        print('Resultado', resultado)
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 3)
                        cv2.putText(frame, '{}'.format(direccion[0]), (x1, y1 - 5), 1, 1.3, (0, 255,0), 1, cv2.LINE_AA)
                    elif respuesta == 1: 
                        print('Resultado', resultado)
                        cv2.rectangle(frame, (x1,y1),(x2,y2), (0,0, 255), 3)
                        cv2.putText(frame, '{}'.format(direccion[1]), (x1,y1-5), 1, 1.3,(0,0,255), 1, cv2.LINE_AA)
                    elif respuesta == 2: 
                        print('Resultado', resultado)
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(255,0,0), 1, cv2.LINE_AA)
                    elif respuesta == 3: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(255,0,255), 1, cv2.LINE_AA)
                    elif respuesta == 4: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 5: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 6: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 7: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 8: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 9: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 10: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 11: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 12: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 13: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 14: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 15: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 16: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 17: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 18: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 19: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    elif respuesta == 20: 
                        print('Resultado', resultado) 
                        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,255),3 )
                        cv2.putText(frame, '{}'.format(direccion[2]), (x1,y1-5), 1, 1.3,(0,255,255), 1, cv2.LINE_AA)
                    
                    else: 
                        cv2.putText(frame, 'Letra desconocida', (x1, y1 -5), 1, 1.3, (0,255,255), 1, cv2.LINE_AA)
        cv2.imshow('Video', frame)
        k = cv2.waitKey(1)
        if k == 27: 
            break
    cap.realese()
    cv2.destroyAllWindows()  
deteccionManos()





'''with manos.Hands(                            #Opciones de Configuracion
    static_image_mode=False,                    #False porque no estamos tomando como entrada una imagen
    max_num_hands=2,                            #Numero maximo de manos por detectar
    min_detection_confidence=0.5) as hands:     #Valor mínimo de confianza del modelo de detección de manos
       while True:
        if ret == False:
            break
            height, width, _ = frame.shape
            
            
        frame = cv2.flip(frame, 1)
            results = hands.process(color)  #se obtinenen las detecciones mediante las salidas multi_handedness y multi_hand_landmarks.
            
            # Dibujando los puntos y las conexiones mediante mp_drawing
                for hand_landmarks in results.multi_hand_landmarks:# usamos un for para obtener cada grupo de 21 puntos por cada mano detectada.
                    mp_drawing.draw_landmarks( # dibujamos los puntos y conexiones con ayuda del propio mediaPipe
                        frame, hand_landmarks, manos.HAND_CONNECTIONS, #se dibujan las conexiones entre los puntos.
                        mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=3, circle_radius=5), #color, grosor de línea y radio de cada punto
                        mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=4, circle_radius=5)) #color, grosor de línea y radio de cada conexion
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()'''

'''neural_return = clasificador()
deteccionManos(neural_return) '''
