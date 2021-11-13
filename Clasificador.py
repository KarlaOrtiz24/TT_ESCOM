##Clasificador para la red neuronal convolucional del TT##
##Creado el 12/11/2021
##Karla Ortiz Chávez 
##Irvin Yoariht Macedo Cruz 
##Angel Ramón Piñon Cabañero
##Irving Daniel Sanchez Pizano

##Librerias 
import numpy as np 
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

ejemplo_directorio = 'C:/Users/Karla/TT_ESCOM/Aprendizaje_Abecedario' ##Directorio donde se encuentran las imagenes para el aprendizaje
 
images = []
directories = []
dircount = [0]
prevRoot=''
cant=0
 
print("leyendo imagenes de ",ejemplo_directorio)
 
for root, dirnames, filenames in os.walk(ejemplo_directorio):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            cant=cant+1
            filepath = os.path.join(root, filename)
            image = plt.imread(filepath)
            images.append(image)
            b = "Leyendo..." + str(cant)
            print (b, end="\r")
            if prevRoot !=root:
                print(root, cant)
                prevRoot=root
                directories.append(root)
                dircount.append(cant)
                cant=0
dircount.append(cant)
 
if len(dircount) > 1:
    dircount = dircount[1:]
    dircount[0] = dircount[0] + 1

print('Directorios leidos:',len(directories))
print("Imagenes en cada directorio", dircount)
print('suma Total de imagenes en subdirs:',sum(dircount))


##Creacion de etiquetas 

etiquetas = [] 
indice = 0 
for cantidad in dircount: 
    for i in range(cantidad): 
        etiquetas.append(indice)
    indice = indice+1
print("Cantidad de etiquetas creadas: ", len(etiquetas))
Abecedario_fijo=[]
indice = 0
for directorio in directories: 
    name = directorio.split(os.sep)
    print(indice, name[len(name)-1])
    Abecedario_fijo.append(name[len(name)-1])
    indice = indice+1
y = np.array(etiquetas)
x = np.array(images, dtype=np.uint8)

classes = np.unique(y)
nClasses = len(classes)
print('Total de numeros de salidas: ', nClasses)
print('Clases de salidas: ', classes)
