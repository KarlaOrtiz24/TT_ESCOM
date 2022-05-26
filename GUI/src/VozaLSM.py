from reconocedorVoz import *
from mostrarGlosa import *
from nlp import *

texto = reconocerVoz()
print ("Fase 1: " + texto)

glosa = nlp(texto)
print ("Fase 2: ")
print (glosa)

Data = []
for x in glosa:
    Data += obtenerData(x)
    
print(Data)
mostrarSeñas(Data)

#La tortilla es grande
#El abuelo está comiendo durazno
#Él está estudiando


