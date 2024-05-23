def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    pyramid = []
    for line in lines:
        number, word = line.split()
        pyramid.append((int(number), word))

    decoded_message = [word for _, word in sorted(pyramid)]
    return ' '.join(decoded_message)

# Example usage:
message_file = 'encoded_message.txt'
decoded_message = decode(message_file)
print(decoded_message)