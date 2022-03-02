#Detector de manos 
#Creado el 25/11/2021
#Sanchez Pizano Irving Daniel 
#Ortiz Chavez Karla 
#Macedo Cruz Irvin Yoariht 
#Piñon Caballero Angel Ramon
import cv2 
import mediapipe as mp
from Clasificador import clasificador

def deteccionManos(neural_network):
    print('Retorno del clasificador ', neural_network)
    mp_drawing = mp.solutions.drawing_utils         #ayuda a dibujar los 21 puntos y sus conexiones
    mp_hands = mp.solutions.hands                   #Se emplea solución hands
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)        #Leemos la camara
    with mp_hands.Hands(                            #Opciones de Configuracion
        static_image_mode=False,                    #False porque no estamos tomando como entrada una imagen
        max_num_hands=2,                            #Numero maximo de manos por detectar
        min_detection_confidence=0.5) as hands:     #Valor mínimo de confianza del modelo de detección de manos
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            height, width, _ = frame.shape
            
            
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Se cambia de BGR a RGB ya que las detecciones se hacen con RGB
            results = hands.process(frame_rgb)  #se obtinenen las detecciones mediante las salidas multi_handedness y multi_hand_landmarks.
            
            if results.multi_hand_landmarks is not None: #Se configura que los puntos aparezcan siempre y cuando esten manos enfrente de la camara
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
    cv2.destroyAllWindows()

neural_return = clasificador()
deteccionManos(neural_return) 