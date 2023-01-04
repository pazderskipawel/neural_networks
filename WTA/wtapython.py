def wta(inputs, weights, learning_rate, num_iterations):
    batch_size = len(inputs)
    input_size = len(inputs[0])
    output_size = len(weights[0])

    dot_product = [[0] * output_size for _ in range(batch_size)]
    winners = [0] * batch_size
    output = [[0] * output_size for _ in range(batch_size)]

    for i in range(num_iterations):
        for b in range(batch_size):
            for o in range(output_size):
                dot_product[b][o] = sum(inputs[b][j] * weights[j][o] for j in range(input_size))
            winners[b] = dot_product[b].index(max(dot_product[b]))
            for j in range(input_size):
                weights[j][winners[b]] += learning_rate

    for b in range(batch_size):
        output[b][winners[b]] = 1

    return output


# Test the modified WTA function with a 2x2 input array
inputs = [[1, 2], [3, 4]]
weights = [[0.1, 0.2], [0.3, 0.4]]
learning_rate = 0.1
num_iterations = 100

output = wta(inputs, weights, learning_rate, num_iterations)
print(output)  # prints [[0, 1], [0, 1]]
