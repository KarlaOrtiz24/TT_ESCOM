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

# Treinta videos por valor de datos, ejemplo: 30 videos correspondientes a Abril, en un futuro... Dataset
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
X.shape
y = to_categorical(labels).astype(int)
y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
y_test.shape
'''
 ## Nos situamos en la dirección actual 
actual_path = os.path.join(os.path.dirname(__file__), '..')

list_directorios = [] ##Guarda las lista de directorios
    ##Checa que lo que este, sean carpetas, si son carpetas lo añade a la lista. 
with os.scandir(actual_path) as directories:
    for directory in directories:
        if directory.is_dir():
            list_directorios.append(directory)

##image_dir es la ruta de las carpetas de las imagenes. 
image_dir = os.path.join(actual_path, list_directorios[4])
print(image_dir)

##print("IMAGE DIR", image_dir)
list_img_dir = [] ##Son las carpetas
with os.scandir(image_dir) as img_directories:
    for img_dir in img_directories:
        list_img_dir.append(img_dir)

list_img_real_directorio = [] ##Lista de directorios de las imagenes 
clases = []
for img_dir in list_img_dir:
    clases.append(img_dir.name)
    list_img_real_directorio.append(os.path.join(image_dir, img_dir))
##print("LIST", clases)
files_cant = 0

labels = [] #Lista de etiquetas
dircount = []
images =[] #Lista de imagenes

for img_dir in list_img_real_directorio:
    #  print('Directorio:', img_dir)
    files = os.listdir(img_dir)
    dircount.append(len(files))

    for file in files:
        ##print('Archivo leido:', file)
        img = cv2.imread(os.path.join(img_dir,file))
        images.append(img)
        img_array = np.asarray(img)
        ##print("IMG ARRAY", img_array)
        #print(len(img_array))
        #print("IMG", img)
        files_cant += 1

##Creacion de etiquetas, etiquetado de todos los datos. 
indice = 0 
for cant in dircount: 
    for i in range(cant): 
        labels.append(indice)
    indice+=1
print("Etiquetas: ",len(labels))

    ##Clases, asignacion de las clases con un índice, EJEMPLO CLASE A índice 0. 
Abecedario_fijo=[]
indice=0
for directorio in list_img_real_directorio:
    name = directorio.split(os.sep)
    print(indice , name[len(name)-1])
    Abecedario_fijo.append(name[len(name)-1])
    indice=indice+1

y = np.array(labels)
X = np.array(images) #Se convierten las imagenes a datos numpy 

    ##print("X", X)
classes = np.unique(y)
nClasses = len(classes)
print('Total de clases : ', nClasses) #imprime el total de las clases, clases 21
print('Lista de clases: ', classes)  #Nos dice las clases




train_X,test_X,train_Y,test_Y = train_test_split(X,y,test_size=0.2)
print('Aprendizaje:', train_X.shape, train_Y.shape)#80% aprendizaje
print('Recuperación:', test_X.shape, test_Y.shape)#20% recuperación

train_X = train_X.astype('float32')
test_X = test_X.astype('float32')
train_X = train_X/255
test_X = test_X/255 #Normalizarlo, 0, 1 

train_Y_one_hot = to_categorical(train_Y)
test_Y_one_hot  = to_categorical(test_Y)

print('Etiqueta original: ', train_Y[0])
print('Despues de la conversion: ', train_Y_one_hot[0]) #A(1, 0,0,0,0,0,0,0,0,0)

train_X, valid_X, train_label, valid_label = train_test_split(train_X, train_Y_one_hot, test_size = 0.2, random_state = 4)

    # el método shape da la cantidad de datos que contiene un arreglo

    # print('train_X: ', train_X.shape)
    # print('valid_X: ', valid_X.shape)

    # print('train_label:', train_label.shape)
    # print('valid_label:', valid_label.shape)


print(train_X.shape,valid_X.shape,train_label.shape,valid_label.shape)
'''



log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)
model = Sequential()
model.add(LSTM(100, return_sequences=True, activation='relu', input_shape=(20,1662)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(1000, activation='relu'))
model.add(Dense(800, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.fit(X_train, y_train, epochs=100, callbacks=[tb_callback])
model.summary()


test_eval = model.evaluate(X_test, y_test, verbose=1)
puntaje = model.evaluate(X_train, y_train, verbose=0)
print('Precision: {:.1f}%'.format(100*puntaje[1]))
print(puntaje)
print('Test loss:', test_eval[0])
print('Test accuracy:', test_eval[1])