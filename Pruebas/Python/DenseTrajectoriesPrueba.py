from Utilities import Video 
import Routes.Routes as routes
import csv

ruta_destino = routes.juntarConPadre(__file__, 'VideosPrueba')
ruta_csv = routes.juntarConPadre(__file__, 'CSV')

ruta_origen = routes.juntarConPadre(__file__, '..')
ruta_origen = routes.juntarRutas(ruta_origen, 'Aprendizaje_Dinamico')

archivos_ruta_origen = routes.getArchivosCarpeta(ruta_origen)

for archivo in archivos_ruta_origen:
    extension = archivo.split('.')
    
    if extension[1] == 'mp4':
        ruta_video = routes.juntarRutas(ruta_origen, archivo)
        ruta_dataframe_bgr = routes.juntarRutas(ruta_csv, extension[0] + '_bgr.csv')
        ruta_dataframe_rgb = routes.juntarRutas(ruta_csv, extension[0] + '_rgb.csv')
        bgr, rgb = Video.dtVideoJson(ruta_video, ruta_destino, extension[0])
        
        pixeles = []
        frames = 0
        
        for frame in bgr.values():
            nombre_frame = 'frame_' + str(frames)
            
            for fila in range(len(frame)):
                # nombre_fila = 'fila_' + str(fila)
                
                for columna in range(len(frame[fila])):
                    
                    pixeles.clear()
                    for pixel in range(len(frame[fila][columna])):
                        pixeles.append(frame[fila][columna][pixel])
                        
                    pixeles.insert(0, nombre_frame)
                    
                    
                    with open(ruta_dataframe_bgr, 'a', newline='', encoding='utf-8') as archivo:
                        write = csv.writer(archivo)
                        write.writerow(pixeles)
            frames += 1
        
        print('ESCRITURA DE ' + extension[0] + '_bgr.csv COMPLETADA' )
        
    else:
        continue