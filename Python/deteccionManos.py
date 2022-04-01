#Detector de manos 
#Creado el 25/11/2021
#Sanchez Pizano Irving Daniel 
#Ortiz Chavez Karla 
#Macedo Cruz Irvin Yoariht 
#Piñon Caballero Angel Ramon
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import os
import pyttsx3
import spacy 
from spacy import displacy
#engine = pyttsx3.init()


#Cargamos el modelo ya guardado
model = load_model(r'C:\Users\Karla\TT_ESCOM\Convolucional.h5')
model.summary()
#Cargamos la direccion de los datos
data_dir = r'C:\Users\Karla\TT_ESCOM\Aprendizaje_Abecedario'
print(data_dir)
#Obtenemos las etiquetas de la carpeta
labels = (os.listdir(data_dir))
#labels[-1] = 'Nothing'

#print(labels)

#Inicializamos la captura de video
cap = cv2.VideoCapture(0)


while(True):
    
    ret, frame = cap.read()
    
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 5) 
    #region of intrest
    roi = frame[100:300, 100:300]
    img = cv2.resize(roi, (60, 60))
    cv2.imshow('roi', roi)
    

    img2 = img/255
    #print('img', img)
    #make predication about the current frame
    prediction = model.predict(img2.reshape(1,60,60,3))
    #print(prediction)
    char_index = np.argmax(prediction)
    #print(char_index,prediction[0,char_index]*100)

    confidence = round(prediction[0,char_index]*100, 1)
    predicted_char = labels[char_index]
  

    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 1
    color = (0,255,255)
    thickness = 2

    #writing the predicted char and its confidence percentage to the frame
    msg = predicted_char +', Conf: ' +str(confidence)+' %'
    cv2.putText(frame, msg, (80, 80), font, fontScale, color, thickness)
    
    cv2.imshow('frame',frame)
    
    #close the camera when press 'q'
    if cv2.waitKey(10) & 0xFF == 27:
        break
        
#release the camera and close all windows
cap.release()
cv2.destroyAllWindows()





