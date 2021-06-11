# Crea tu primer MLP en Keras
import os

from keras import models
from keras.models import Sequential
from keras.layers import Dense
import numpy

# Fija las semillas aleatorias para la reproducibilidad
numpy.random.seed(7)
# carga los datos
dataset = numpy.loadtxt("diabetes.csv", delimiter=",")
# dividido en variables de entrada (X) y salida (Y)
X = dataset[:, 1:8]
Y = dataset[:, 8]
p = input('Crear modelo?')
if not os.path.isfile('Menor.h5') or p == 'y':
    # crea el modelo
    model = Sequential()
    model.add(Dense(12, input_dim=7, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compila el modelo
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    print('Creado\n')
else:
    model = models.load_model('Menor.h5')
    print('Cargado\n')
print('La estructura es')
model.summary()
m = input('Presione n para entrenar\n')
if m == 'n':
    # Ajusta el modelo
    model.fit(X, Y, epochs=1500, batch_size=40)
# evalua el modelo
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
model.save('Menor.h5')
