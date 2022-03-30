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
        pixel = []
        
        info_video = []
        
        frames = 0
        
        for frame in bgr.values():
            nombre_frame = 'frame_' + str(frames)
            
            for fila in range(len(frame)):
                # nombre_fila = 'fila_' + str(fila)
                
                for columna in range(len(frame[fila])):
                    
                    # nombre_columna = 'columna_' + str(columna)
                    
                    pixel.clear()
                    pixel.append(nombre_frame)
                    # pixel.append(nombre_fila)
                    # pixel.append(nombre_columna)
                    
                    for dato in range(len(frame[fila][columna])):
                        pixel.append(int(frame[fila][columna][dato]))
                    
                    # print(pixel)
                    pixeles.append(pixel)
                    
            frames += 1
        
        # for pixel in pixeles:
        #     print(pixel)
        
        print('ESCRITURA DE ' + extension[0] + '_bgr.csv INICIADA' )
        
        
        with open(ruta_dataframe_bgr, 'w', newline='') as File:
            writer = csv.writer(File)
            writer.writerows(pixeles)
        
        print('ESCRITURA DE ' + extension[0] + '_bgr.csv COMPLETADA' )
        
    else:
        continue