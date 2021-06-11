nn = NeuralNetwork([2, 3, 2], activation='tanh')
X = np.array([[0, 0],  # sin obstaculos
              [0, 1],  # sin obstaculos
              [0, -1],  # sin obstaculos
              [0.5, 1],  # obstaculo detectado a derecha
              [0.5, -1],  # obstaculo a izq
              [1, 1],  # demasiado cerca a derecha
              [1, -1]])  # demasiado cerca a izq

y = np.array([[0, 1],  # avanzar
              [0, 1],  # avanzar
              [0, 1],  # avanzar
              [-1, 1],  # giro izquierda
              [1, 1],  # giro derecha
              [0, -1],  # retroceder
              [0, -1]])  # retroceder
nn.fit(X, y, learning_rate=0.03, epochs=15001)

index = 0
for e in X:
    print("X:", e, "y:", y[index], "Network:", nn.predict(e))
    index = index + 1