##13/04/2022
#Author Karla Ortiz Chávez 
#Clasificador de red convolucional para la detección de Action detection



##Librerias 
from abc import ABC
import numpy as np 
import cv2 as cv
import cv2 
from tkinter import filedialog
import tkinter as tk
import os 
import pathlib
import re 
import matplotlib.pyplot as plt
from numpy.core.numeric import indices 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report
import tensorflow
import keras 
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input 
from tensorflow.keras import Model
from tensorflow.keras import optimizers
from keras.layers import Dense, Dropout, Flatten 
from keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import (
    BatchNormalization, SeparableConv2D, MaxPooling2D, Activation, Flatten, Dropout, Dense
)
from keras.layers.advanced_activations import LeakyReLU
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd 
import seaborn as sn 
from sklearn.utils import compute_class_weight


def clasificador():
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
            img = cv.imread(os.path.join(img_dir,file))
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
