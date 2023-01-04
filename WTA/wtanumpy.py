import numpy as np


def wta(inputs, weights, learning_rate, num_iterations):
    for i in range(num_iterations):
        # Calculate the dot product of the inputs and weights
        dot_product = np.dot(inputs, weights)

        # Find the index of the maximum value in the dot product for each row
        winners = np.argmax(dot_product, axis=1)

        # Set the winning weights to the maximum value in the dot product plus the learning rate
        weights[:, winners] += learning_rate

    # Initialize the output array with all zeros
    output = np.zeros(dot_product.shape)

    # Set the value at the winning index to 1 for each row
    output[np.arange(dot_product.shape[0]), winners] = 1

    return output


# Test the modified WTA function with a 2x2 input array
inputs = np.array([[1, 0], [0, 1]])
weights = np.array([[0.1, 0.2], [0.3, 0.4]])
learning_rate = 0.1
num_iterations = 100

output = wta(inputs, weights, learning_rate, num_iterations)
print(output)  # prints [[0. 1.], [0. 1.]]
