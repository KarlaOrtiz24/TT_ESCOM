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


# load saved model from PC
model = load_model(r'C:\Users\Karla\TT_ESCOM\ABECEDARIO.h5')
model.summary()
data_dir = r'C:\Users\Karla\TT_ESCOM\Aprendizaje_Abecedario'
#getting the labels form data directory
labels = (os.listdir(data_dir))
print('labels', labels)
#labels[1] = 'Nothing'
#print(labels)

#initiating the video source, 0 for internal camera
cap = cv2.VideoCapture(0)


while(True):
    
    _ , frame = cap.read()
    
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 5) 
    #region of intrest
    roi = frame[50:300, 50:300]
    img = cv2.resize(roi, (60, 60))
    cv2.imshow('roi', roi)
    

    img = img/255

    #make predication about the current frame
    prediction = model.predict(img.reshape(1,60,60,3))
    char_index = np.argmax(prediction)
    #print(char_index,prediction[0,char_index]*100)

    confidence = round(prediction[0,char_index]*100, 1)
    predicted_char = labels[char_index]

    # Initialize the engine 
    engine = pyttsx3.init() 
    #engine.say(predicted_char) 
    engine.runAndWait()

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




