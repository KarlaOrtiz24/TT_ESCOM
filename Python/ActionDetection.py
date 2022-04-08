#04/04/2022
#Karla Ortiz Chavez 
#TT_Escom, Obtención de videos en npy para clasificador de detección de acciones
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

mp_holistic = mp.solutions.holistic # Modelo Holistico
mp_drawing = mp.solutions.drawing_utils # Dibuja puntos

#Funcion de deteccion de mediapipe

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Conversion de color BGR2RGB
    image.flags.writeable = False                  
    results = model.process(image)                 # Hacemos una prediccion 
    image.flags.writeable = True                   # La imagen es escriible
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # Conversion de color RGB to BGR
    return image, results

#Funcion para dibujar las lineas
def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION) # Conexion en la cara
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Dibujo en poses
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Dibuja la izquierda
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Dibuja conexiones derechas

#Funcion para darle estilo a las uniones
def draw_styled_landmarks(image, results):
    # Draw face connections
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                             mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), 
                             mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                             ) 
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             ) 
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             ) 
    # Draw right hand connections  
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             ) 

#Captura de video de prueba                              
cap = cv2.VideoCapture(0)
# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()

        # Haciendo detecciones
        image, results = mediapipe_detection(frame, holistic)
        print(results)
        
        # Dibujando puntos de referencia
        draw_styled_landmarks(image, results)

        # Se muestra en pantalla
        cv2.imshow('Prueba', image)

        # Se cierra
        if cv2.waitKey(10) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
draw_landmarks(frame, results)
plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) 

#len(results.left_hand_landmarks.landmark)
pose = [] #Guardará las poses obtenidas
#Ciclo for para res en el resultado obtenido de los puntos de referencia
for res in results.pose_landmarks.landmark:
    test = np.array([res.x, res.y, res.z, res.visibility])
    pose.append(test)
pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(132)
face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(1404)
lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() 
if results.face_landmarks:
  print('..') 
else: 
    np.zeros(1404)

#Función para extraer los puntos, a partir de esta funcion obtenemos los puntos que necesitamos
#o son puntos de referencia para nuestra utilidad, de aceurdo a la pose, la cara, la mano derecha 
#la mano izquierda, en coordenadas x, y z que nos devuelve una concatenacion de estos 4.
def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, face, lh, rh])

#Variable result_test donde se guardan los valores que se extraen
result_test = extract_keypoints(results)
result_test

#Donde se guardaran los test, archivos npy que son archivos binarios
np.save('0', result_test)
np.load('0.npy')


# Direccion donde serán guardados los puntos obtenidos de cada palabra

DATA_PATH = os.path.join(r'C:\Users\Karla\TT_ESCOM\Aprendizaje_1to1') 

# Acciones que guardaremos
actions = np.array(['Domingo', 'Él', 'Ella'])
'''Ahi', 'Ahora', 'Alegre', 'Alla', 'Amiga', 'Amigo', 'Amistad', 'Amor', 'Año', 
            'Arriba', 'Ayer', 'Bien', 'Buenas Noches', 'Buenas tardes', 'Bueno', 'Buenos dias', 'Compromiso', 'Convivencia',
            'Cultura', 'Dia', 'Diciembre', 'Domingo', 'Él', 'Ella', 'Ellos', 'Ellas', 'En', 'Enero', 'Enojado', 'Entre', 'Esa, ese, eso',
            'Escribir', 'Estar', 'Estudiar', 'Familia', 'Febrero', 'Femenino', 'Hablar', 'Honestidad', 'J', 'Jueves', 'Jugar', 'Julio', 
            'Junio', 'Justicia', 'K', 'Ll', 'Lunes', 'Martes', 'Marzo', 'Mayo', 'Mes', 'Miercoles', 'Nosotros', 'Noviembre'
            'Ñ', 'Octubre', 'Platicar', 'Por', 'Proteger', 'Q', 'Respeto', 'Responsabilidad', 'Rr','Sabado', 'Semana', 'Septiembre', 
            'Solidaridad', 'Tolerancia', 'Tú', 'Ustedes', 'Valores', 'Viernes', 'X', 'Yo', 'Z'])
'''
# Treinta videos por valor de datos, ejemplo: 30 videos correspondientes a Abril, en un futuro... Dataset
no_sequences = 30

# Los videos tendran una secuencia de 30 frames
sequence_length = 30

# Se comienza por el folder 0. 0 a 29
start_folder = 0
for action in actions: 
    for sequence in range(no_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass


#Captura de video para comenzar el guardado de los videos 
cap = cv2.VideoCapture(0)
# Modelo mediapipe
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    

    
    # Loop en acciones
    for action in actions:
        # For en secuencia de videos
        for sequence in range(start_folder, start_folder+no_sequences):
            # Loop through video length aka sequence length
            for frame_num in range(sequence_length):

                # Lectura
                ret, frame = cap.read()

                # Haciendo detecciones
                image, results = mediapipe_detection(frame, holistic)

                # Dibujando puntos de referencia
                draw_styled_landmarks(image, results)
                
                # Aplicamos una espera 
                if frame_num == 0: 
                    cv2.putText(image, 'EMPEZANDO COLECCION', (120,200), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, 'Colleccionando frames desde el {} Video numero {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Mostrando en pantalla
                    cv2.imshow('Opencv Videos', image)
                    cv2.waitKey(500)
                else: 
                    cv2.putText(image, 'Colleccionando framdes desde el {} Video numero {}'.format(action, sequence), (15,12), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Mostrando en pantalla
                    cv2.imshow('OpenCV Videos', image)
                
                # Exportacion de puntos clave
                keypoints = extract_keypoints(results)
                npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
                np.save(npy_path, keypoints)

                # Final
                if cv2.waitKey(10) & 0xFF == 27:
                    break
                    
    cap.release()
    cv2.destroyAllWindows()


##Iniciando etiquetado de datos
''''
label_map = {label:num for num, label in enumerate(actions)}
label_map
sequences, labels = [], []
for action in actions:
    for sequence in range(no_sequences):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])
np.array(sequences).shape
np.array(labels).shape
X = np.array(sequences)
X.shape
y = to_categorical(labels).astype(int)
y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
y_test.shape'''