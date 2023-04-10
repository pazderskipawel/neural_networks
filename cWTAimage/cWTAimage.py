import os
import numpy as np
from PIL import Image

class cWTA:
    def __init__(self, num_neurons, learning_rate, num_epochs):
        self.num_neurons = num_neurons
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs

        # Initialize weights randomly
        self.weights = np.random.rand(num_neurons, 3)

    def train(self, X):
        for epoch in range(self.num_epochs):
            print(f"Training (epoch {epoch+1})...")
            # Loop over each input in the training data
            for i in range(X.shape[0]):
                # Find the neuron in the network with weights closest to the input
                distances = np.sum((self.weights - X[i])**2, axis=1)
                closest_neuron_idx = np.argmin(distances)

                # Update the weights of the winning neuron and its neighbors
                for j in range(self.num_neurons):
                    if j == closest_neuron_idx:
                        # If the neuron is the winner, update its weights to move closer to the input
                        # using the learning rate parameter to control the magnitude of the change
                        self.weights[j] += self.learning_rate * (X[i] - self.weights[j])
                    elif abs(j - closest_neuron_idx) <= 2:
                        # If the neuron is a neighbor of the winner, update its weights to move closer
                        # to the input as well, but with a smaller magnitude of change
                        self.weights[j] += self.learning_rate * 0.5 * (X[i] - self.weights[j])
            print(f"Weights of winning neurons {self.weights[j]}")

    def compress(self, X):
        print("Compressing...")
        compressed_X = np.zeros((X.shape[0], self.num_neurons))
        for i in range(X.shape[0]):
            # Find the closest neuron to the input and set its index to 1 in the compressed representation
            distances = np.sum((self.weights - X[i])**2, axis=1)
            closest_neuron_idx = np.argmin(distances)
            compressed_X[i, closest_neuron_idx] = 1

        return compressed_X

    def decompress(self, compressed_X):
        print("Decompressing...")
        decompressed_X = np.zeros((compressed_X.shape[0], 3))
        for i in range(compressed_X.shape[0]):
            # Reconstruct the original input using the weights of the winning neurons in the compressed representation
            winning_neuron_idx = np.argmax(compressed_X[i])
            decompressed_X[i] = self.weights[winning_neuron_idx]

        return decompressed_X


if __name__ == '__main__':
    # Load the image and convert it to a numpy array
    img = Image.open("image.jpg")
    if img.mode == 'L':
        img = img.convert('RGB')
    width, height = img.size
    X = np.array(img).reshape(-1, 3) / 255.0

    # Create and train the cWTA neural network
    num_neurons = 64
    learning_rate = 0.1
    num_epochs = 10
    network = cWTA(num_neurons, learning_rate, num_epochs)
    network.train(X)

    # Compress and decompress the image
    compressed_X = network.compress(X)
    decompressed_X = network.decompress(compressed_X)

    # Convert the decompressed array back to an image and save it
    decompressed_img = Image.fromarray((decompressed_X * 255.0).astype(np.uint8).reshape(height, width, 3))
    decompressed_img.save("image_decompressed.jpg")

    orig_size = os.path.getsize("image.jpg")
    comp_size = os.path.getsize("image_decompressed.jpg")
    print("Original image size: ", orig_size, "bytes")
    print("Compressed image size: ", comp_size, "bytes")
    print(f"Compression rate: {(comp_size / orig_size) * 100}% of the original file")
