##Clasificador para la red neuronal convolucional del TT##
##Creado el 12/11/2021
##Karla Ortiz Chávez 
##Irvin Yoariht Macedo Cruz 
##Angel Ramón Piñon Cabañero
##Irving Daniel Sanchez Pizano

##Librerias 
import numpy as np 
import os 
import pathlib
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

actual_path = pathlib.Path(__file__).parent.absolute()

print(actual_path)



# directories = os.listdir(actual_path)



list_dir = []



with os.scandir(actual_path) as directories:

    for directory in directories:

        if directory.is_dir():

            list_dir.append(directory)



image_dir = os.path.join(actual_path, list_dir[2])



list_img_dir = []



with os.scandir(image_dir) as img_directories:

    for img_dir in img_directories:

        list_img_dir.append(img_dir)



list_img_real_dir = []



for img_dir in list_img_dir:

    list_img_real_dir.append(os.path.join(image_dir, img_dir))



files_cant = 0

labels = []
images =[]


for img_dir in list_img_real_dir:

    print('Directorio:', img_dir)

    files = os.listdir(img_dir)

    for file in files:

        print('Archivo leido:', file)
        img = plt.imread(os.path.join(img_dir,file))
        images.append(img)
        files_cant += 1

        labels.append(files_cant)


##Creacion de etiquetas 

for label in labels:

    print('Etiqueta:', label)
print("Cantidad de etiquetas creadas: ", len(labels))


##Clases
Abecedario_fijo=[]
indice=0
for directorio in list_img_real_dir:
    name = directorio.split(os.sep)
    print(indice , name[len(name)-1])
    Abecedario_fijo.append(name[len(name)-1])
    indice=indice+1
 
y = np.array(labels)
for img in images: 
    X = np.array(img, dtype=np.uint8)
    print("SIIII: ", img)
classes = np.unique(y)
nClasses = len(classes)
print('Total de clases : ', nClasses)
print('Lista de clases: ', classes)

##Entrenamiento Test validacion 

train_X, test_X, train_Y, test_Y = train_test_split(X,y, test_size = 0.2)
print('Aprendizaje: ', train_X.shape, train_Y.shape)
print('Test', test_X.shape, test_Y.shape)

train_X = train_X.astype('float32')
test_X = test_X.astype('float32')
train_X = train_X/255
test_X = test_X/255

train_Y_one_hot = to_categorical(train_Y)
test_Y_one_hot  = to_categorical(test_Y)

print('Etiqueta original: ', train_Y[0])
print('Despues de la conversion: ', train_Y_one_hot[0])

train_X, valid_X, train_label, valid_label = train_test_split(train_X, train_Y_one_hot, test_size = 0.2, random_state = 13)
print(train_X.shape, valid_X.shape, train_label.shape, valid_label.shape)
