# image compression using cWTA

cWTA (competitive winner-takes-all) is a technique used in neural networks to ensure that only one neuron in a layer is activated at a time, meaning it outputs the highest value among its neighbors. In the case of the SOM (Self-Organizing Map) algorithm, the competition is between neurons that represent different regions of the input space.

During the training process, the SOM learns to create a low-dimensional map of the high-dimensional input space by associating each input vector to a neuron in the map. The neuron with the closest weight vector to the input is selected as the winner, and its weight vector is updated to move closer to the input.

cWTA is implemented by selecting the neuron with the minimum Euclidean distance to the input as the winner, and setting all other neurons to zero. This ensures that only the winning neuron is activated, which makes the SOM more effective at capturing the structure of the input space.

## Implementation:
## cWTA class: 

### \_\_init__() function:
- initialize variables
- initialize random weights

### train() function:

- Loops input data (X) through the number of epochs for training the network.
- Within each epoch, the method loops through each input in X and finds the index of the neuron that is closest to it using Euclidean distance.
- The weights of the winning neuron and its neighbors are then updated using the learning rate and the difference between the input and the weights of the neurons.
- This process continues until the specified number of epochs is reached, and the weights of the neurons are adjusted to better represent the input data.

### compress() function:

- Take the original image data (X).
- Initialize an array compressed_X with the shape (X.shape[0], self.num_neurons), where self.num_neurons is the number of neurons in the SOM.
- Iterate over each input in X.
- Find the closest neuron to it using Euclidean distance. 
- Set the corresponding index in compressed_X to 1.
- Return the compressed representation (compressed_X).

### decompress() function:

- This function takes in the compressed representation (compressed_X).
- Initialize an array decompressed_X with the shape (compressed_X.shape[0], 3), where 3 is the number of color channels in the original image.
- Iterate over each row in compressed_X. 
- Find the winning neuron (i.e., the neuron with the highest value).
- Use found weights to reconstruct the original input.
- Add reconstructed input to (decompressed_X).
- Finally, decompressed_X is returned.