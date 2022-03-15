

import cv2 as cv 
import Routes.Routes as routes
import time

def grabarVideo(ruta_destino, nombre_video):
    # Se coloca un 0 para seleccionar la camara de la laptop
    # si se ocupa otra camara se coloca otro valor
    captura_camara = cv.VideoCapture(0)
    
    # Formato del video
    codecs = cv.VideoWriter_fourcc(*'mp4v')
    
    fps = captura_camara.get(cv.CAP_PROP_FPS)
    
    delay = 1/fps
    
    nombre = routes.juntarRutas(ruta_destino, nombre_video + '.mp4')
    
    # Escritura del video
    salida = cv.VideoWriter(
        nombre,
        codecs,
        30.0,
        (640, 480)
    )
    
    # El ciclo se mantendra mientras la camara este abierta
    while (captura_camara.isOpened()):
        # Se devuelven dos datos ret es un booleano, 
        # True cuando se lee la imagen y False si la imagen aun no se lee
        # Imagen como su nombre lo indica es lo capturado por la camara
        ret, imagen = captura_camara.read()
        
        # Volteamos la imagen verticalmente para que se muestre 
        # en modo espejo
        imagen_volteada = cv.flip(imagen, 1)
        
        if ret == True:
            
            # Se muestra la imagen en una ventana
            cv.imshow('Video', imagen_volteada)
            
            # Se escribe la imagen 
            salida.write(imagen_volteada)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            
            #time.sleep(delay)
    
    # Se limpian las entradas y salidas y se cierran todas las ventanas
    captura_camara.release()
    salida.release()
    cv.destroyAllWindows()
    
# ==================================================================================================

def copiarVideo(ruta_origen, ruta_destino, nombre_video):
    # Se coloca la ruta de donde se leerá el video a copiar
    captura_camara = cv.VideoCapture(ruta_origen)
    
    # Formato del video
    codecs = cv.VideoWriter_fourcc(*'mp4v')
    
    ancho = int(captura_camara.get(cv.CAP_PROP_FRAME_WIDTH))
    alto = int(captura_camara.get(cv.CAP_PROP_FRAME_HEIGHT))
    
    fps = captura_camara.get(cv.CAP_PROP_FPS)
    
    delay = 1/fps
    
    nombre = routes.juntarRutas(ruta_destino, nombre_video + '.mp4')
    
    # Escritura del video
    salida = cv.VideoWriter(
        nombre,
        codecs,
        fps,
        (ancho, alto)
    )
    
    # El ciclo se mantendra mientras la camara este abierta
    while (captura_camara.isOpened()):
        # Se devuelven dos datos ret es un booleano, 
        # True cuando se lee la imagen y False si la imagen aun no se lee
        # Imagen como su nombre lo indica es lo capturado por la camara
        ret, imagen = captura_camara.read()
        
        # Volteamos la imagen verticalmente para que se muestre 
        # en modo espejo
        imagen_volteada = cv.flip(imagen, 1)
        
        
        if ret == True:
            escala = 600
            dimension_maxima = max(imagen_volteada.shape)
            redimension = escala/dimension_maxima
            
            img_real = cv.resize(imagen, None, fx = redimension, fy = redimension)
            
            # Se escribe la imagen 
            salida.write(imagen_volteada)
            
            # Se muestra la imagen en una ventana
            cv.imshow('Video', img_real)
            
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    # Se limpian las entradas y salidas y se cierran todas las ventanas
    captura_camara.release()
    salida.release()
    cv.destroyAllWindows()
    
# ==================================================================================================