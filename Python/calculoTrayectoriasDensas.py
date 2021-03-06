#Obtencion de frames de videos 
#Creado el 12/11/2021 
#Piñon Caballero Angel Ramón 
#Ortiz Chávez Karla 
#Macedo Cruz Irvin Yoariht 
#Sanchez Pizano Irving Daniel 
import numpy as np
import cv2
import csv
import time

def dibujarFlujo(img, flow, step=16): #Dibuja el flujo real 

    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T

    lines = np.vstack([x, y, x-fx, y-fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)

    img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(img_bgr, lines, 0, (0, 255, 0))

    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)

    return img_bgr

archivo =r'C:\Users\Karla\TT_ESCOM\Abecedario\paises-estados\Toluca.mp4'
def calculoTrayectoriasDensas (archivo):
    cap = cv2.VideoCapture(archivo)                             #Abrimos el video que se analizara

    suc, prev = cap.read()                                      #Cargamos el primer fotograma
    prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)           
    aux = True
    a = []

    while aux:
        try:
            suc, img = cap.read()                               #Leemos un fotograma
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #Convertimos en grises

            start = time.time()

            flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            #prevgray = gray
            #print(prevgray)
            print(flow)
            flow2 = cv2.cvtColor(flow, cv2.COLOR_BGR2GRAY)
            print('flow2', flow2)
            end = time.time()
            fps = 1 / (end-start)                               #Calculo de los FPS

            print(f"{fps:.2f} FPS")

            #cv2.imshow('flow', dibujarFlujo(gray, flow))           #Se muestra el flujo

            a.append(prevgray)
        except:
            aux = False

    #tabla = archivo[:-3] + 'csv'
        
    #with open(tabla, 'w', newline='', encoding='utf-8') as csvfile:     #Se crea el archivo .csv
    #    writer = csv.writer(csvfile)
    #    writer.writerows(a)

    cap.release()
    cv2.destroyAllWindows() 
calculoTrayectoriasDensas(archivo)