##13/04/2022
#Author Karla Ortiz Chávez 
#Clasificador de red convolucional para la detección de Action detection



##Librerias 
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


def clasificadorAD():
    no_sequences = 20

# Los videos tendran una secuencia de 30 frames
    sequence_length = 20
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


    log_dir = os.path.join('Logs')
    tb_callback = TensorBoard(log_dir=log_dir)
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(20,1662)))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(actions.shape[0], activation='softmax'))
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    model.fit(X_train, y_train, epochs=10, callbacks=[tb_callback])
    model.summary()

    test_eval = model.evaluate(X_test, y_test, verbose=1)
    puntaje = model.evaluate(X_train, y_train, verbose=0)
    print('Precision: {:.1f}%'.format(100*puntaje[1]))
    print(puntaje)
    print('Test loss:', test_eval[0])
    print('Test accuracy:', test_eval[1])

clasificadorAD()