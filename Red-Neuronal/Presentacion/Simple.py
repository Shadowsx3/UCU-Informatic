from keras import models
from keras.models import Sequential
from keras.layers import Dense
import numpy

# Carga los datos
dataset = numpy.loadtxt("diabetes.csv", delimiter=",")
# dividido en variables de entrada (X) y salida (Y)
X = dataset[:, 0:7]
Y = dataset[:, 7]
#Creamos el modelo
model = Sequential()
model.add(Dense(12, input_dim=7, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#Lo entrenamos
model.fit(X, Y, epochs=150, batch_size=10)
#Mostramos resultado
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
