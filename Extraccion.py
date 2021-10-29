from matplotlib import pyplot as plt
from scipy import ndimage 
from skimage.color import rgb2gray
from skimage import io
import xlsxwriter
import numpy as np
import pandas as pd
import cv2 
from PIL import Image
from skimage import io 

def Umbralizacion(ruta,x):
    imagen=cv2.imread(ruta)
    gray = cv2.medianBlur(imagen, 5)

    _, dst1 = cv2.threshold(gray, int(x), 255, cv2.THRESH_BINARY)
    cv2.imwrite('umbral.jpg', dst1)#para guardarla
    cv2.imshow('umbral fijo', dst1)
    cv2.waitKey(0)
def Mediana(valor,ruta):
    imagen = cv2.imread(ruta)
    img2 = cv2.medianBlur(imagen, valor)
    cv2.imshow("Mediana", img2)
    cv2.waitKey(0)
    cv2.imwrite ('Mediana.jpg', img2)

def Minimo(n,ruta):
    img = cv2.imread(ruta)

      #Crea la forma del kernel
    tam = (int(n), int(n))
    forma = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(forma, tam)

      # Aplica el filtro minimo
    imgResult = cv2.erode(img, kernel)

      #Muestra el resultado
    cv2.namedWindow('Resultado con n ' + str(n), cv2.WINDOW_NORMAL)
    cv2.imshow('Resultado con n ' + str(n), imgResult)
    cv2.waitKey(0)

def Maximo(n,ruta):
    img = cv2.imread(ruta)

      # Crea la forma del kernel
    tam = (int(n),int(n))
    forma = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(forma, tam)

      #Aplica el filtro
    imgResult = cv2.dilate(img, kernel)

      #Muestra el resultado
    cv2.namedWindow('Result with n ' + str(n), cv2.WINDOW_NORMAL) 
    cv2.imshow('Result with n ' + str(n), imgResult)
    cv2.waitKey(0)

imagen = cv2.imread(r'/A.png')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen', gris)
cv2.waitKey(50)
cv2.imwrite('gris.jpg', gris)#para guardarla
continuar=False
while continuar==False:
    print("Inserte el valor para el filtro mediano")
    y=input()
    Mediana(int(y),'gris.jpg')
    print("Inserte el valor del filtro para realizar la umbralización")
    x=input()
    Umbralizacion('Mediana.jpg',x)
    print("Inserte el valor para el filtro Maximo, de preferencia un número entre 1 y 10")
    n=input()
    Maximo(n,'umbral.jpg')
    print("Inserte el valor para el filtro Minimo, de preferencia un número entre 1 y 10")
    m=input()
    Minimo(m,'umbral.jpg')
    BN = cv2.imread('umbral.jpg')
    print("Esta satisfecho con el resultado?")
    respuesta=input()
    if respuesta=="Y":
        continuar=True
    else:
        continuar=False
h,w=gris.shape
imagen2='bosque.jpg'
imagen3='CS.jpg'

imagen4=cv2.imread('umbral.jpg')
OR=cv2.bitwise_or(imagen,imagen4)
cv2.imshow('OR',OR)
cv2.imwrite(imagen2,OR)
mask_inv=cv2.bitwise_not(imagen4)
cv2.imshow('NOT',mask_inv)
OR2=cv2.bitwise_or(imagen,mask_inv)
cv2.imshow('OR2',OR2)
cv2.imwrite(imagen3,OR2)
imagenOR=cv2.imread('bosque.jpg')
lw=[255,255,255]
df=pd.DataFrame({'R','G','B'})
rl=[]
gl=[]
bl=[]

for i in range(h):
    for j in range(w):
        if list(imagenOR[i,j])!=lw:
            b=imagenOR[i,j][0]
            g=imagenOR[i,j][1]
            r=imagenOR[i,j][2]
            if r<240 and g<240 and b < 240:
                rl.append(r)
                gl.append(g)
                bl.append(b)
df=pd.DataFrame({'R':rl,'G':gl,'B':bl})
writer1=pd.ExcelWriter('Bosque.xlsx',engine='xlsxwriter')
df.to_excel(writer1,sheet_name='Hoja1',index=False)
writer1.save()
rl2=[]
gl2=[]
bl2=[]
rl3=[]
gl3=[]
bl3=[]
imagenOR2=cv2.imread('CS.jpg')
for i in range(h):
    for j in range(w):
        if list(imagenOR[i,j])!=lw:
            b=imagenOR2[i,j][0]
            g=imagenOR2[i,j][1]
            r=imagenOR2[i,j][2]
            if b>r:
                rl2.append(r)
                gl2.append(g)
                bl2.append(b)
            elif r<240 and g<240 and b < 240:
                rl3.append(r)
                gl3.append(g)
                bl3.append(b)
df2=pd.DataFrame({'R':rl2,'G':gl2,'B':bl2})
writer2=pd.ExcelWriter('Cielo.xlsx',engine='xlsxwriter')
df2.to_excel(writer2,sheet_name='Hoja1',index=False)
df3=pd.DataFrame({'R':rl3,'G':gl3,'B':bl3})
writer3=pd.ExcelWriter('Suelo.xlsx',engine='xlsxwriter')
df3.to_excel(writer3,sheet_name='Hoja1',index=False)
writer2.save()
writer3.save()
while(1):
    cv2.imshow("image",imagen4)
    if cv2.waitKey(0):
        cv2.destroyAllWindows()