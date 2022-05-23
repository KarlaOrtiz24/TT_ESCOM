import cv2 as cv 
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import os
import pyttsx3
import spacy 
from spacy import displacy
import Routes.Routes as routes 

model_dir = routes.getRutaPadre(__file__)
model_dir = routes.juntarRutas(model_dir, '..')
model_dir = routes.juntarRutas(model_dir, 'Convolucional.h5')
model = load_model(model_dir)
model.summary()

data_dir = routes.getRutaPadre(__file__)
data_dir = routes.juntarRutas(data_dir, '..')
data_dir = routes.juntarRutas(data_dir, 'Aprendizaje_Abecedario')
labels = (os.listdir(data_dir))

class VideoCamara:
    def __init__(self):
        self.video = cv.VideoCapture(0, cv.CAP_DSHOW)
    
    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        ret, frame = self.video.read()
        
        cv.rectangle(frame, (100, 100), (300, 300), (255, 0, 0), 2) 
        #region of intrest
        roi = frame[100:300, 100:300]
        img = cv.resize(roi, (60, 60))
        img2 = img/255
        prediction = model.predict(img2.reshape(1,60,60,3))
        char_index = np.argmax(prediction)
        
        confidence = round(prediction[0,char_index]*100, 1)
        predicted_char = labels[char_index]

        font = cv.FONT_HERSHEY_TRIPLEX
        fontScale = 1
        color = (0,255,0)
        thickness = 2

        #writing the predicted char and its confidence percentage to the frame
        msg = predicted_char +', Conf: ' +str(confidence)+' %'
        cv.putText(frame, msg, (80, 80), font, fontScale, color, thickness)
        
        ret, jpeg = cv.imencode('.jpeg', frame)
        
        return jpeg.tobytes()