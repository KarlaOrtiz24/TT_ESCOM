from Utilities import Video 
import Routes.Routes as routes
import json

ruta_destino = routes.juntarConPadre(__file__, 'VideosPrueba')
ruta_json = routes.juntarConPadre(__file__, 'JSON')

ruta_origen = routes.juntarConPadre(__file__, '..')
ruta_origen = routes.juntarRutas(ruta_origen, 'Aprendizaje_Dinamico')

archivos_ruta_origen = routes.getArchivosCarpeta(ruta_origen)

for archivo in archivos_ruta_origen:
    extension = archivo.split('.')
    
    if extension[1] == 'mp4':
        ruta_video = routes.juntarRutas(ruta_origen, archivo)
        bgr, rgb = Video.dtVideoJson(ruta_video, ruta_destino, extension[0])
    else:
        continue
