from Utilities import Video 
import Routes.Routes as routes

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
cant = Video.dtVideoJson(ruta_origen, ruta_destino, nombre_video2)
print(cant)