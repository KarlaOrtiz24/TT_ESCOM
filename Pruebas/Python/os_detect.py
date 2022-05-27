import sys
import random

my_os = sys.platform

# print(my_os)

pantallas_carga = ['', '1', '2', '3']
eleccion = random.shuffle(pantallas_carga)

print(eleccion)