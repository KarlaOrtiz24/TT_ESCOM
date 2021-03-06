#04/04/2022
#Karla Ortiz Chavez 
#TT_Escom, Obtención de videos en npy para clasificador de detección de acciones
from cProfile import label
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report
from scipy import stats

import pandas as pd 
import seaborn as sn 

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

DATA_PATH = os.path.join(r'C:\Users\Karla\TT_ESCOM\Aprendizaje_Dinamico_AD') 

# Acciones que guardaremos
actions = np.array(['Abril', 'Adios', 'Agosto', 'Ahi', 'Ahora', 'Alegre', 'Alla', 'Amiga', 'Amigo',
'Amistad', 'Amor', 'Ante', 'Año', 'Arriba', 'Ayer', 'Bajo', 'Bien', 'Buenas Noches', 'Buenas tardes',
'Bueno', 'Buenos dias', 'Como', 'Como estas', 'Compromiso', 'Con_Preposicion', 'Contra', 'Convivencia', 'Cual',
'Cuando', 'Cultura', 'De nada', 'Desde', 'Dia', 'Diciembre', 'Domingo', 'Donde', 'Él', 'Ella', 'Ellas','Ellos',
'En', 'Enero', 'Enojado', 'Entre', 'Esa, ese, es', 'Escribir', 'Estar','Estudiar', 'Familia', 'Febrero', 'Femenino', 'Gracias', 'Hablar','Hola', 'Honestidad', 'J', 'Jueves',
'Jugar', 'Julio', 'Junio', 'Justicia', 'K', 'Ll','Lunes', 'mal', 'Mamá', 'Martes', 'Marzo', 'Mayo', 'Mes', 'no', 'Ñ', 'Octubre', 'Papá', 'Platicar', 'Por', 'Por que', 'Pregunta',
'Profesor', 'Proteger', 'Q', 'Que', 'Que pasa', 'Quien', 'Respeto', 'Responsabilidad', 'Rr', 'Sabado', 'Semana', 'Septiembre', 'si', 'Solidaridad', 'Tolerancia', 'Tú', 'Ustedes', 
'Valores', 'Viernes', 'X', 'Yo', 'Z'])

# Veinte videos por valor de datos, ejemplo: 30 videos correspondientes a Abril, en un futuro... Dataset
no_sequences = 20

# Los videos tendran una secuencia de 30 frames
sequence_length = 20

# Se comienza por el folder 0. 0 a 29
start_folder = 0
for action in actions: 
    for sequence in range(no_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass

'''
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

'''
##Iniciando etiquetado de datos

label_map = {label:num for num, label in enumerate(actions)}
print('labelMap', label_map)
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
#print(X.shape)
y = to_categorical(labels).astype(int)
y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
y_test.shape



#Red neuronal 
#El modelo es secuencial, 3 capas LSTM  y 3 capas densas con distintas neuronas en cada una. 
log_dir = os.path.join('Logs3')
tb_callback = TensorBoard(log_dir=log_dir)
model = Sequential()
model.add(LSTM(100, return_sequences=True, activation='relu', input_shape=(20,1662)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(1000, activation='relu'))
model.add(Dense(800, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))
model.compile(optimizer='Adam', loss='categorical_crossentropy', 
metrics=['categorical_accuracy'])
ABC_model= model.fit(X_train, y_train, epochs=100, callbacks=[tb_callback])
model.summary()

print(X_test[0].shape)

test_eval = model.evaluate(X_test, y_test, verbose=1)
puntaje = model.evaluate(X_train, y_train, verbose=0)
print('Precision: {:.1f}%'.format(100*puntaje[1]))
print(puntaje)
print('Test loss:', test_eval[0])
print('Test accuracy:', test_eval[1])

res = model.predict(X_test)
actions[np.argmax(res[4])]
actions[np.argmax(y_test[4])]

#Modelo y pesos guardados
model.save('action3.h5') #No correr, Action 2 es red funcional con porcentaje de 96, para correr
#y guardar otra CAMBIAR el NOMBRE
#del model
model.load_weights('action3.h5')

#Matriz de confusión
yhat = model.predict(X_test)
ytrue = np.argmax(y_test, axis=1).tolist()
yhat = np.argmax(yhat, axis=1).tolist()
print(multilabel_confusion_matrix(ytrue, yhat))



""""
colors = [(245,117,16), (117,245,16), (16,117,245)]
def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        #cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors[num], -1)
        cv2.putText(output_frame, actions[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
    return output_frame
#plt.figure(figsize=(18,18))
#plt.imshow(prob_viz(res, actions, image, colors))




sequence = []
sentence = []
predictions = []
threshold = 0.5

cap = cv2.VideoCapture(0)
# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        print(results)
        
        # Draw landmarks
        draw_styled_landmarks(image, results)
        
        # 2. Prediction logic
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-20:]
        
        if len(sequence) == 20:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            print(actions[np.argmax(res)])
            predictions.append(np.argmax(res))
            
            
        #3. Viz logic
            if np.unique(predictions[-10:])[0]==np.argmax(res): 
                if res[np.argmax(res)] > threshold: 
                    
                    if len(sentence) > 0: 
                        if actions[np.argmax(res)] != sentence[-1]:
                            sentence.append(actions[np.argmax(res)])
                    else:
                        sentence.append(actions[np.argmax(res)])

            if len(sentence) > 5: 
                sentence = sentence[-5:]

            # Viz probabilities
            image = prob_viz(res, actions, image, colors)
            
        cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
        cv2.putText(image, ' '.join(sentence), (3,30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Show to screen
 
        cv2.imshow('OpenCV Feed', image)

        # Break gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
"""