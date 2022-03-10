import os

def getRutaActual(archivoActual):
    return os.path.dirname(archivoActual)

def getRutaPadre(archivoActual):
    return os.path.join(getRutaActual(archivoActual), '..')

def juntarConPadre(archivoActual, rutaInteres):
    return os.path.join(getRutaPadre(archivoActual), rutaInteres)

def getCarpetasRuta(ruta):
    carpetas = []
    
    with os.scandir(ruta) as directorios:
        for directorio in directorios:
            carpetas.append(str(directorio).split("'")[1])
            
        return carpetas
    
def juntarRutas(ruta1, ruta2):
    return os.path.join(ruta1, ruta2)

def getArchivosCarpeta(ruta):
    return os.listdir(ruta)