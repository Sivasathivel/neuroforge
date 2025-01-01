import numpy as np

class Layers:
    def __init__(self, input_dim:int, output_dim: int, activations=None):
        """
        Base class for all layers.

        :param input_size: Number of input neurons.
        :param output_size: Number of output neurons.
        :param activation: Activation function (e.g., sigmoid, ReLU, etc.).
        """
        self.input_size = input_dim
        self.output_size = output_dim
        self.activation = activations
        self.weights = np.random.randn(input_dim, output_dim) * 0.01  # Weight initialization
        self.biases = np.zeros((1, output_dim))  # Bias initialization

    def forward(self, X):
        """
        Forward pass (to be implemented by subclasses).

        :param X: Input data.
        :return: Output of the layer.
        """
        raise NotImplementedError("Forward method must be implemented in subclasses.")
    

    def backward(self, dA, learning_rate):
        """
        Backward pass (to be implemented by subclasses).

        :param dA: Gradient of loss w.r.t. layer output.
        :param learning_rate: Learning rate for gradient descent.
        :return: Gradient of loss w.r.t. layer input.
        """
        raise NotImplementedError("Backward method must be implemented in subclasses.")
    
    