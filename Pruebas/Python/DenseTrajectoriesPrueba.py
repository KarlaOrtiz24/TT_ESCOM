from Utilities import Video 
import Routes.Routes as routes

ruta_destino = routes.juntarConPadre(__file__, 'VideosPrueba')
nombre_video = 'Prueba'

Video.grabarVideo(ruta_destino, nombre_video)