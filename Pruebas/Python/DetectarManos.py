import Routes.Routes as routes

ruta_vocales = routes.juntarConPadre(__file__, 'Vocales')
nombre_carpetas_vocales = routes.getCarpetasRuta(ruta_vocales)
listas_archivos = []

for vocal in nombre_carpetas_vocales:
    listas_archivos.append(routes.getArchivosCarpeta(routes.juntarRutas(ruta_vocales, vocal)))

for lista in listas_archivos:
    for archivo in lista:
        print(archivo)
        print(type(archivo))

