# Crea tu primer MLP en Keras
import keras as kr
from keras import Sequential
from keras.layers import Dense
import numpy
import os.path
import math
# Fija las semillas aleatorias para la reproducibilidad
from numpy import array
# carga los datos
dataset = numpy.loadtxt("heart_failture.csv", delimiter=",")
# dividido en variables de entrada (X) y salida (Y)
# age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,
# serum_sodium,sex,smoking,time,DEATH_EVENT
X = dataset[:, 0:12]
Y = dataset[:, 12]
p = input('Crear modelo?')
if not os.path.isfile('Menor.h5') or p == 'y' or True:
    # crea el modelo
    model = Sequential()
    model.add(Dense(60, input_dim=12, activation='tanh', name='Data'))
    model.add(Dense(120, activation='tanh'))
    model.add(Dense(60, activation='tanh'))
    model.add(Dense(20, activation='tanh'))
    model.add(Dense(1, activation='tanh', name='predictions'))
    print('La estructura es')
    model.summary()
    # Compila el modelo
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    print('Creado\n')
#else:
    #model = kr.models.load_model('Menor.h5')
    #print('Cargado\n')
# Ajusta el modelo
m = input('Presione n para entrenar\n')
if m == 'n':
    model.fit(X, Y, epochs=2000, batch_size=10)
#model.save('Menor.h5')
