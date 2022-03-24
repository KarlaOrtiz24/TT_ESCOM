from Utilities import Video 
import Routes.Routes as routes
import json

ruta_destino = routes.juntarConPadre(__file__, 'VideosPrueba')
ruta_json = routes.juntarConPadre(__file__, 'JSON')
nombre_video = 'Prueba'
nombre_video1 = 'Video_Copia1'
nombre_video2 = 'Video_DT'

ruta_origen = routes.juntarConPadre(__file__, '..')
ruta_origen = routes.juntarRutas(ruta_origen, 'Abecedario')
ruta_origen = routes.juntarRutas(ruta_origen, 'paises-estados')
ruta_origen = routes.juntarRutas(ruta_origen, 'tlaxcala.mp4')

ruta_origen1 = routes.juntarRutas(ruta_destino, nombre_video1)

# Video.grabarVideo(ruta_destino, nombre_video)
# Video.copiarVideo(ruta_origen, ruta_destino, nombre_video1)
bgr, rgb = Video.dtVideoJson(ruta_origen, ruta_destino, nombre_video2)
bgr4json = {}
rgb4json = {}

for frame in bgr:
    bgr4json[frame] = bgr[frame].tolist()

for frame in rgb:
    rgb4json[frame] = rgb[frame].tolist()
    

print(bgr4json)
print(rgb4json)

# json.dumps(bgr)
# json.dumps(rgb)