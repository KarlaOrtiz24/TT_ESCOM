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

num_frames = 0
fil = 0
col = 0

lista = []

for frame in bgr.values():
    num_frames += 1
    nombre_frame = 'frame_' + str(num_frames)

    bgr4json.setdefault(nombre_frame, {})
    
    for fila in range(len(frame)):
        nombre_fila = 'fila_' + str(fila)
        
        bgr4json[nombre_frame].setdefault(nombre_fila, {})

        for columna in range(len(frame[fila])):
            nombre_col = 'columna_' + str(columna)
            # print(nombre_frame, nombre_fila, nombre_col)
            
            bgr_valores = dict(zip('bgr', frame[fila][columna].tolist()))
            # print(bgr_valores)
            
            bgr4json[nombre_frame][nombre_fila].setdefault(nombre_col, bgr_valores)


# print(bgr4json)
# print(rgb4json)

with open('tlaxcala.json', 'w') as json_file:
    json.dump(bgr4json, json_file)

# json.dumps(rgb) 