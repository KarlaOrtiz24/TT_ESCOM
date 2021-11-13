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

dirname = os.path.join(os.getcwd(), 'Aprendizaje_Abecedario')
imgpath = dirname + os.sep 
 
images = []
directories = []
dircount = [0]
prevRoot=''
cant=0
 
print("leyendo imagenes de ",imgpath)
 
for root, dirnames, filenames in os.walk(imgpath):
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
            