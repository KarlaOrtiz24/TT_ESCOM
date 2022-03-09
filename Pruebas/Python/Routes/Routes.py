import os

def getRutaActual(file):
    return os.path.dirname(file)

def getRutaPadre(file):
    return os.path.join(getRutaActual(file), '..')

