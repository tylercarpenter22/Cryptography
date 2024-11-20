
#Tyler Carpenter
#CIS3362-24Fall 0001 Arup Guha
#This program encrypts n amount of plaintext + key with playfair cipher


alphabet = "abcdefghiklmnopqrstuvwxyz"  # 'j' = 'i'


# Prepares a key so that it is in a format that can create a Playfair square
# Takes in a key and returns a processed version of the key
def prepare_key(key):
    key = key.lower().replace(" ", "").replace("j", "i")
    # Remove duplicate letters
    return "".join(dict.fromkeys(key))


# Prepares a plaintext to be enciphered with the playfair square
# Takes in a plaintext and returns a processed version of the plaintext
def prepare_plaintext(plaintext):
    plaintext = plaintext.lower().replace(" ", "").replace("j", "i")
    return padding(plaintext)


# Pads the plaintext with 'x' or 'q' if needed
def padding(plaintext):
    padded_text = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1:
            # If it's the last character, pad with 'x'
            padded_text.append(plaintext[i] + 'x')
            i += 1
        elif plaintext[i] == plaintext[i + 1]:
            # Handle double letters; 'xx' gets padded with 'q', others with 'x'
            if plaintext[i] == 'x':
                padded_text.append(plaintext[i] + 'q')
            else:
                padded_text.append(plaintext[i] + 'x')
            i += 1
        else:
            padded_text.append(plaintext[i:i + 2])
            i += 2
    return padded_text


# Creates the playfair square with a 5x5 matrix.
def playfair_square(key):
    matrix = list(prepare_key(key))
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


# Helper function to find the position of a character in the Playfair square.
def find_position(char, square):
    for row_idx, row in enumerate(square):
        if char in row:
            return row_idx, row.index(char)
    return None, None


# Encrypts the plaintext using the Playfair square.
def playfair_encrypt(plaintext, square):
    ciphertext = []
    for pair in plaintext:
        row1, col1 = find_position(pair[0], square)
        row2, col2 = find_position(pair[1], square)

        if row1 == row2:  # Same row
            ciphertext.append(square[row1][(col1 + 1) % 5] + square[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            ciphertext.append(square[(row1 + 1) % 5][col1] + square[(row2 + 1) % 5][col2])
        else:  # Rectangle case
            ciphertext.append(square[row1][col2] + square[row2][col1])

    return "".join(ciphertext)


# Main function to handle input/output
if __name__ == "__main__":
    n = int(input().strip())  # Read number of test cases
    encrypted_texts = []

    for _ in range(n):
        key = input().strip()  # Read the key for the test case
        plaintext = input().strip()  # Read the plaintext for the test case

        # Prepare the key, plaintext, and playfair square
        matrix = playfair_square(key)
        adjusted_plaintext = prepare_plaintext(plaintext)

        # Encrypt the plaintext and collect the result
        encrypted_text = playfair_encrypt(adjusted_plaintext, matrix)
        encrypted_texts.append(encrypted_text)

    # Print encrypted ciphertexts, one per line
    for text in encrypted_texts:
        print(text)
