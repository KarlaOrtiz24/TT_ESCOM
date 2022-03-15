
import os

#Obtener la ruta del archivo actual, para eso: 
def getRutaActual(archivoActual): #COlocar __file__ <-Con eso se obtiene la ruta del archivo actual 
    return os.path.dirname(archivoActual)

#Función para obtener el directorio padre del directorio de nuestro archivo actual
def getRutaPadre(archivoActual):
    return os.path.join(getRutaActual(archivoActual), '..')

#Llamas a getRutaPadre para obtenerla y el primer argumento es el archivo actual
def juntarConPadre(archivoActual, rutaInteres): #Segundo argumento, con que lo quieres unir
    return os.path.join(getRutaPadre(archivoActual), rutaInteres)

#El argumento es la ruta, devuelve todas las carpetas que estan dentro de esa carpeta
def getCarpetasRuta(ruta):
    carpetas = []
    
    with os.scandir(ruta) as directorios:
        for directorio in directorios:
            carpetas.append(str(directorio).split("'")[1])
            
        return carpetas

#Parecida a JuntarConPadre, aqui se manda la primera ruta y se manda la 
# ruta con la que se quiere unir
def juntarRutas(ruta1, ruta2):
    return os.path.join(ruta1, ruta2)

#Obtienes los archivos de la ruta 
def getArchivosCarpeta(ruta):
    return os.listdir(ruta)