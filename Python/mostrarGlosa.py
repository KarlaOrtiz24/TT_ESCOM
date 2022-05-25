import cv2
import pymongo
from tkinter import *

cliente = pymongo.MongoClient( "mongodb://localhost:27017")
db = cliente["KAYI"]
senas = db["LSM"]


def mostrarVideo(Data):
    #url = "../BD/" + palabra + ".mp4"
    #capture = cv2.VideoCapture(url)
    
    capture = cv2.VideoCapture(Data)
    
    while (capture.isOpened()):
        ret, frame = capture.read()
        if (ret == True):
            cv2.namedWindow (Data, cv2.WINDOW_NORMAL)
            cv2.imshow(Data, frame)
            if (cv2.waitKey(30) == ord('s')):
                break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()

def mostrarSeñas(arrayData):
    for x in arrayData:
        mostrarVideo(x)

def obtenerData(palabra):
    consulta = {"Nombre": palabra}
    doc = senas.find_one(consulta)

    if (doc is None):
        consulta = {"Femenino": palabra}
        doc = senas.find_one(consulta)
        if (doc is not None):
            res = [doc['Data'], "../BD/mujer.mp4"]
            return res

    if (doc is None):
        consulta = {"Atributo": palabra}
        doc = senas.find_one(consulta)
        if (doc is not None):
            res = [doc['Data'], "../BD/así.mp4"]
            return res
    
    if (doc is None):
        return deletrear(palabra)

    return [doc['Data']]

def deletrear(palabra):
    arreglo = ['../BD/deletrear.mp4']
    
    for x in palabra:
        consulta = {"Nombre": x}
        doc = senas.find_one(consulta)
        # Data = doc['Data']
        Data = "../BD/" + x + ".mp4"
        arreglo.append(Data)

    return arreglo
