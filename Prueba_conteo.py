import numpy as np 
import pathlib
import os 
import re 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report
import keras 
##from keras.utils import to_categorical 
from tensorflow.keras.utils import to_categorical
##from tensorflow.keras.models import Sequential, Input, Model
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input 
from tensorflow.keras import Model
##from keras.models import sequential, Input, Model 
from keras.layers import Dense, Dropout, Flatten 
from keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import (
    BatchNormalization, SeparableConv2D, MaxPooling2D, Activation, Flatten, Dropout, Dense
)
##from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU

cant=0

ejemplo_directorio = 'C:/Users/Karla/TT_ESCOM/Aprendizaje_Abecedario'
for nombre_directorio, direcciones, ficheros in os.walk(ejemplo_directorio):
    for nombre_fichero in ficheros:
        print(nombre_fichero)
    print(nombre_directorio)
