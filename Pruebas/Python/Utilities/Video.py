import cv2 as cv 
import Routes.Routes as routes

def grabarVideo(ruta_destino, nombre_video):
    # Se coloca un 0 para seleccionar la camara de la laptop
    # si se ocupa otra camara se coloca otro valor
    captura_camara = cv.VideoCapture(0)
    
    # Formato del video
    codecs = cv.VideoWriter_fourcc(*'MP4V')
    
    nombre = routes.juntarRutas(ruta_destino, nombre_video + '.mp4')
    
    # Escritura del video
    salida = cv.VideoWriter(
        nombre,
        codecs,
        60.0,
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
    
    # Se limpian las entradas y salidas y se cierran todas las ventanas
    captura_camara.release()
    salida.release()
    cv.destroyAllWindows()