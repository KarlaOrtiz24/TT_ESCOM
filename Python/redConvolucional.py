##Clasificador para la red neuronal convolucional del TT##
##Creado el 12/11/2021
##Karla Ortiz Chávez 
##Irvin Yoariht Macedo Cruz 
##Angel Ramón Piñon Cabañero
##Irving Daniel Sanchez Pizano

##Librerias 
import numpy as np 
import cv2 as cv
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
## Nos situamos en la dirección actual 
actual_path = pathlib.Path(__file__).parent.absolute()
print(actual_path)

list_directorios = [] ##Guarda las lista de directorios
##Checa que lo que este, sean carpetas, si son carpetas lo añade a la lista. 
with os.scandir(actual_path) as directories:
    for directory in directories:
        if directory.is_dir():
            list_directorios.append(directory)
##image_dir es la ruta de las carpetas de las imagenes. 
image_dir = os.path.join(actual_path, list_directorios[2])
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
  ##  print('Directorio:', img_dir)
    files = os.listdir(img_dir)
    dircount.append(len(files))

    for file in files:
        ##print('Archivo leido:', file)
        img = cv.imread(os.path.join(img_dir,file))
        images.append(img)
        img_array = np.asarray(img)
      ##  print("IMG ARRAY", img_array)
        #print(len(img_array))
       # print("IMG", img)
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
X = np.asarray(images) #Se convierten las imagenes a datos numpy 

##print("X", X)
classes = np.unique(y)
nClasses = len(classes)
print('Total de clases : ', nClasses) #imprime el total de las clases, clases 21
print('Lista de clases: ', classes)  #Nos dice las clases

##Entrenamiento Test validacion 

train_X,test_X,train_Y,test_Y = train_test_split(X,y,test_size=0.2)
print('Aprendizaje: ', train_X.shape, train_Y.shape)
print('Entrenamiento : ', test_X.shape, test_Y.shape)

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


##Construccion de la red :O

INIT_LR = 1e-3
epochs = 6
batch_size = 64

ABC_model = Sequential()
ABC_model.add(Conv2D(4, kernel_size=(3, 3),activation='linear',padding='same',input_shape=(28,28,3)))
ABC_model.add(LeakyReLU(alpha=0.01))
ABC_model.add(MaxPooling2D((2, 2),padding='same'))
ABC_model.add(Dropout(0.5))

ABC_model.add(Flatten())
ABC_model.add(Dense(32, activation='linear'))
ABC_model.add(LeakyReLU(alpha=0.01))
ABC_model.add(Dropout(0.5)) 
ABC_model.add(Dense(nClasses, activation='softmax'))

ABC_model.summary()
ABC_model.compile(loss=keras.losses.categorical_crossentropy, optimizer = tensorflow.keras.optimizers.Adagrad(learning_rate=INIT_LR, decay=INIT_LR / 100), metrics=['accuracy'])

##Guardamos la red 

ABC_train_dropout = ABC_model.fit(train_X, train_label, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))

# guardamos la red, para reutilizarla en el futuro, sin tener que volver a entrenar
# ABC_model.save("ABECEDARIO.h5py")


##Test 
test_eval = ABC_model.evaluate(test_X, test_Y_one_hot, verbose=1)

print('Test loss:', test_eval[0])
print('Test accuracy:', test_eval[1])


plt.figure(0)  
plt.plot(ABC_train_dropout.history['accuracy'],'r')  
plt.plot(ABC_train_dropout.history['val_accuracy'],'g')  
# plt.xticks(np.arange(0, 11, 2.0))  
plt.rcParams['figure.figsize'] = (8, 6)  
plt.xlabel("Num of Epochs")  
plt.ylabel("Accuracy")  
plt.title("Training Accuracy vs Validation Accuracy")  
plt.legend(['train','validation'])
plt.figure(1)  
plt.plot(ABC_train_dropout.history['loss'],'r')  
plt.plot(ABC_train_dropout.history['val_loss'],'g')  
plt.xticks(np.arange(0, 11, 2.0))  
plt.rcParams['figure.figsize'] = (8, 6)  
plt.xlabel("Num of Epochs")  
plt.ylabel("Loss")  
plt.title("Training Loss vs Validation Loss")  
plt.legend(['train','validation'])
plt.show()