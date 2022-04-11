import cv2
from pymongo import MongoClient
from tkinter import *

cliente = MongoClient('localhost')
db = cliente['KAYI']
senas = db['LSM']

def obtenerData(palabra):
    consulta = {"Nombre": palabra}
    doc = senas.find_one(consulta)

    return doc['Data']

def mostrarVideo(palabra):
    capture = cv2.VideoCapture(obtenerData(palabra))

    while (capture.isOpened()):
        ret, frame = capture.read()
        if (ret == True):
            cv2.namedWindow (palabra, cv2.WINDOW_NORMAL)
            cv2.imshow(palabra, frame)
            if (cv2.waitKey(30) == ord('s')):
                break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()

def deletrear(palabra):
    arreglo = []
    arreglo.extend(palabra)
    
    for x in arreglo:
        mostrarVideo(x)

def mostrarSeñas(frase):
    for x in frase:
        mostrarVideo(x)
