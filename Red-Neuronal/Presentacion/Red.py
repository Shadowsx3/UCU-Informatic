from numpy import exp, array, random, dot


class NeuralNetwork:
    def __init__(self):
        random.seed(1)
        self.synaptic_weights = 2 * random.random((4, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_input, training_set_output, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_input)
            error = training_set_output - output
            adjustment = dot(training_set_input.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    def think(self, inputs):
        # Pasar las entradas a través de nuestra red neuronal (una neurona)
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":
    #Iniciar la red
    neural_network = NeuralNetwork()
    #Ejemplos de entrada
    training_set_inputs = array([[0, 0, 2, 0], [0, 1, 0, 1], [1, 1, 0, 1]])
    #Salida para cada ejemplo
    training_set_outputs = array([[0, 1, 1]]).T
    #Entrenamos con 1000 iteraciones
    neural_network.train(training_set_inputs, training_set_outputs, 10000)
    #Verificamos si funciona para los ejemplos
    print("Considering situations")
    a = []
    for iteration in training_set_inputs:
        a.append(neural_network.think(iteration))
    #Comparamos resultados
    print(a)
    print(training_set_outputs)
