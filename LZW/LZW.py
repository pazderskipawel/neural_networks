def compress(data):
    dictionary = {}
    max_code = 256
    for i in range(max_code):
        dictionary[chr(i)] = i
    w = ""
    result = []
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = max_code
            max_code += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result

def decompress(data):
    dictionary = {}
    max_code = 256
    for i in range(max_code):
        dictionary[i] = chr(i)
    result = []
    w = chr(data.pop(0))
    result.append(w)
    for code in data:
        if code in dictionary:
            entry = dictionary[code]
        elif code == max_code:
            entry = w + w[0]
        else:
            raise ValueError("Bad compression code: %d" % code)
        result.append(entry)
        dictionary[max_code] = w + entry[0]
        max_code += 1
        w = entry
    return "".join(result)


if __name__ == '__main__':
    # Example usage
    original_data = "hello world"
    compressed_codes = compress(original_data)
    print("Compressed codes:", compressed_codes)
    decompressed_data = decompress(compressed_codes)
    print("Decompressed data:", decompressed_data)

    # Read data from a file
    with open('input.txt', 'r') as f:
        original_data = f.read()
    compressed_codes = compress(original_data)
    with open('output.bin', 'wb') as f:
        f.write(bytes(compressed_codes))

    # Read compressed data from a file
    with open('output.bin', 'rb') as f:
        compressed_codes = list(f.read())
    decompressed_data = decompress(compressed_codes)
    with open('output.txt', 'w') as f:
        f.write(decompressed_data)
