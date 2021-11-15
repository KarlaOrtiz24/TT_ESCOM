## Ejemplo sencillo de red neuronal para entender su funcionamiento ##
## La red neuronal aprenderá a pasar de grados celsius a farenheit
## Creado el 12/11/2021
## Karla Ortiz Chávez 
## Irvin Yoariht Macedo Cruz 
## Angel Ramón Piñon Cabañero
## Irving Daniel Sanchez Pizano

##Librerias 
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

## Datos de entrada
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype = float)

## Datos de salida
farenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype = float)

## Se usará keras para facilitar el uso y despliegue de las redes neuronales 
## Se crea una capa densa (las capas densas son las que se conectan a todas las neuronas
## de la siguiente capa) la red neuronal contará con 2 capas solamente y 2 neuronas
## el parametro units hace referencia a las neuronas de la capa (de salida)
## input_shape hace referencia a la entrada de las neuronas

capa = tf.keras.layers.Dense(units = 1, input_shape=[1])

## Se crea un modelo de keras para poder trabajar con las capas
## existen varios tipos de modelos, y el usado aqui sera el secuencial
## y se le indican las capas que tendra en el parametro de entrada

modelo = tf.keras.Sequential([capa])

## Luego se lleva a cabo la compilacion del modelo para iniciar con el proceso de 
## entrenamiento, se le brindaran propiedades para saber como aprender

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

print('Comienzo del entrenamiento')
historial = modelo.fit(celsius, farenheit, epochs = 1000)
print('Modelo entrenado')

plt.xlabel('# Epoca')
plt.ylabel('Magnitud perdida')
plt.plot(historial.history['loss'])
plt.show()

resp = True

print(capa.get_weights())

while resp:
    resp_num = input('Selecciona una opcion:\n1) Convertir de Celsius a Farenheit\n2) Salir\n')
    
    if resp_num == '1':
        grados = input('Ingresa los grados:\t-')
        grados_fl = float(grados)
        
        resultado = modelo.predict([grados_fl])
        print('El resultado es ' + str(resultado) + ' grados Farenheit')
        
    elif resp_num == '2':
        resp = False
    else:
        print('opcion no valida')
        
    print()