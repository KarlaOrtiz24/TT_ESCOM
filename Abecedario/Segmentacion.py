import numpy as np
import math
import matplotlib.pyplot as plt
import cv2 as cv
from statistics import mode
from scipy import stats
from PIL import Image, ImageFilter
import collections
from collections import Counter
%matplotlib inline
from PIL import Image
import random

def mediana(img_arr, suavizado):
    #Realizamos una copia del arreglo de pixeles recibido para no modificar al original
    img = img_arr.copy()
    #Convertimos a escala de grises
    img_bn = cv.cvtColor(img_arr, cv.COLOR_BGR2GRAY)
    #Aplicamos el filtro de mediana que implementa la librería de Opencv
    med = cv.medianBlur(img_bn, suavizado)
    
    #retornamos el arreglo que se genera por la función del filtro
    return med

def gaussiano(img_arr, val):
    #Realizamos una copia del arreglo de pixeles recibido para no modificar al original
    img = img_arr.copy()
    #Aplicamos el filtro del suavizado gaussiano
    img2 = img.filter(ImageFilter.GaussianBlur(val))
    
    #retornamos el arreglo generado por el filtro
    return img2

def moda(img_arr, val):
    #Realizamos una copia del arreglo de pixeles recibido para no modificar al original
    img = img_arr.copy()
    #Aplicamos el filtro moda 
    img2 = img.filter(ImageFilter.ModeFilter(val))
    
    #retornamos el arreglo generado por el filtro
    return img2
    
def ObtenerVecinos(copia, i, j):
    #Tenemos una lista vacía que se llenará conforme recorremos los pixeles
    pixel_list = [] 
    #Todos los pixeles a recorrer son los que se encuentran alrededor del pixel que tenemos
    #en copia, donde i y j son sus coordenadas
    try: 
        pixel_list.append(copia.getpixel((i-1, j-1))) 
    except: 
        pixel_list.append((0, 0, 0))
    try: 
        pixel_list.append(copia.getpixel((i, j-1)))
    except: 
        pixel_list.append((0, 0, 0))
    try: 
        pixel_list.append(copia.getpixel((i+1, j-1)))
    except: 
        pixel_list.append((0, 0, 0))
    try: 
        pixel_list.append(copia.getpixel((i-1, j)))
    except: 
        pixel_list.append((0, 0, 0))
    try: 
        pixel_list.append(copia.getpixel((i, j)))
    except: 
        pixel_list.append((0, 0, 0))
    try: 
        pixel_list.append(copia.getpixel((i+1, j)))
    except: 
        pixel_list.append((0, 0, 0))
    try: 
        pixel_list.append(copia.getpixel((i-1, j+1)))
    except: 
        pixel_list.append((0, 0, 0))
    try: 
        pixel_list.append(copia.getpixel((i, j+1)))
    except: 
        pixel_list.append((0, 0, 0))
    try: 
        pixel_list.append(copia.getpixel((i+1, j+1)))
    except: 
        pixel_list.append((0, 0, 0))
        
    #Retornamos la lista llenada con los valores de los pixeles
    return pixel_list

def minimo(img):
    #Creamos una nueva imagen del mismo tamaño que la imagen original
    copia = Image.new('RGB', img.size)
    #Obtenemos los datos de la imagen original
    datosImg = Image.Image.getdata(img)
    #Le agregamos los datos de la original a la copia
    copia.putdata(datosImg)
    #Obtenemos la altura y el ancho de la imagen para comenzar a hacer el proceso de filtrado
    #con los pixeles
    ancho, alto = img.size

    #Recorremos la imagen en anchura y altura
    for i in range(ancho):
        for j in range(alto):
            #obtenemos los valores r,g,b del pixel i,j
            r, g, b = copia.getpixel((i,j))
            #dividimos la suma de los canales entre 3 para convertir a grises
            x = (r + g + b) / 3
            #convertimos a entero el valor del pixel
            intx = int (x)
            #generamos una tupla que será el pixel de la imagen en escala grises
            #de la nueva imagen
            pixel = tuple ([intx, intx, intx])
            #añadimos el pixel a la imagen copia
            copia.putpixel((i,j), pixel)

    #De nuevo recorremos la imagen en ancho y alto
    for i in range(ancho):
        for j in range(alto):
            #Obtenemos los vecinos de cada uno de los pixeles
            vecindades = ObtenerVecinos(img, i, j)
            #Obtenemos los minimos de los valores entre los vecinos
            mini = min(((vecindades[0][0]), (vecindades[1][0]), (vecindades[2][0]), 
                        (vecindades[3][0]), (vecindades[4][0]), (vecindades[5][0]), 
                        (vecindades[6][0]), (vecindades[7][0]), (vecindades[8][0])))
            #Guardamos el valor del mínimo de la vecindad en la variable res
            res = mini
            #generamos una nueva tupla con los valores en rgb del resultado mínimo
            pixel = tuple([res, res, res])
            #añadimos el pixel a la imagen copia
            copia.putpixel((i, j), pixel)
    
    #retornamos la imagen copia
    return copia

def maximo(img):
    #Creamos una nueva imagen del mismo tamaño que la imagen original
    copia = Image.new('RGB', img.size)
    #Obtenemos los datos de la imagen original
    datosImg = Image.Image.getdata(img)
    #Le agregamos los datos de la original a la copia
    copia.putdata(datosImg)
    #Obtenemos la altura y el ancho de la imagen para comenzar a hacer el proceso de filtrado
    #con los pixeles
    ancho, alto = img.size
    
    #Recorremos la imagen en anchura y altura
    for i in range(ancho):
        for j in range(alto):
            #obtenemos los valores r,g,b del pixel i,j
            r, g, b = copia.getpixel((i,j))
            #dividimos la suma de los canales entre 3 para convertir a grises
            x = (r + g + b) / 3
            #convertimos a entero el valor del pixel
            intx = int (x)
            #generamos una tupla que será el pixel de la imagen en escala grises
            #de la nueva imagen
            pixel = tuple ([intx, intx, intx])
            #añadimos el pixel a la imagen copia
            copia.putpixel((i,j), pixel)

    #De nuevo recorremos la imagen en ancho y alto
    for i in range(ancho):
        for j in range(alto):
            #Obtenemos los vecinos de cada uno de los pixeles
            vecindades = ObtenerVecinos(img, i, j)
            #Obtenemos los maximos de los valores entre los vecinos
            maxi = max(((vecindades[0][0]), (vecindades[1][0]), (vecindades[2][0]), 
                        (vecindades[3][0]), (vecindades[4][0]), (vecindades[5][0]), 
                        (vecindades[6][0]), (vecindades[7][0]), (vecindades[8][0])))
            #Guardamos el valor del máximo de la vecindad en la variable res
            res = maxi
            #generamos una nueva tupla con los valores en rgb del resultado mínimo
            pixel = tuple([res, res, res])
            #añadimos el pixel a la imagen copia
            copia.putpixel((i, j), pixel)
    
    return copia

def canny(image):
    #Aplicamos el filtro gaussiano para poder suavizar la imagen
    blurred = cv.GaussianBlur(image, (3,3), 0)
    
    #Convertimos la imagen en escala de grises
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    
    # Encontramos el gradiente en la dirección X
    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    
    # Encontramos el gradiente en la dirección y
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    
    # Convertimos el valor del gradiente a 8 bits
    x_grad = cv.convertScaleAbs(grad_x)
    y_grad = cv.convertScaleAbs(grad_y)
    
    # Combina dos gradientes
    src1 = cv.addWeighted(x_grad, 0.5, y_grad, 0.5, 0)
    
    # Combinamos gradientes con algoritmo canny, donde 50 y 100 son umbrales 
    edge = cv.Canny(src1, 50, 100)
    edge1 = cv.Canny(grad_x, grad_y, 10, 100)
    
    # Usamos el borde como una máscara para realizar operaciones bit a bit y bit a bit
    edge2 = cv.bitwise_and(image, image, mask=edge1)
    
    return edge2

def canny1(image):
    blurred = cv.GaussianBlur(image, (3,3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    
    # Encuentra el gradiente en la dirección X
    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    
    # Encuentra el gradiente en la dirección y
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    
    # Convertir el valor del gradiente a 8 bits
    x_grad = cv.convertScaleAbs(grad_x)
    y_grad = cv.convertScaleAbs(grad_y)
    
    # Combina dos gradientes
    src1 = cv.addWeighted(x_grad, 0.5, y_grad, 0.5, 0)
    
    # Combine gradientes con algoritmo canny, donde 50 y 100 son umbrales 
    edge = cv.Canny(src1, 50, 100)
    edge1 = cv.Canny(grad_x, grad_y, 10, 100)
    
    return edge1