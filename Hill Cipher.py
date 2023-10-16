import numpy as np

# Function to generate the key matrix
def generate_key_matrix(key):
    key_matrix_size = int(np.sqrt(len(key)))
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape(key_matrix_size, -1)
    return key_matrix

# Function to encrypt the plaintext using Hill cipher
def encrypt(plaintext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = plaintext.upper().replace(" ", "")
    plaintext = [ord(char) - ord('A') for char in plaintext]
    plaintext_size = len(plaintext)

    # Pad the plaintext with 'X' to make its length a multiple of key matrix size
    padding_size = key_matrix.shape[0] - (plaintext_size % key_matrix.shape[0])
    plaintext += [ord('X') - ord('A')] * padding_size

    plaintext_matrix = np.array(plaintext).reshape(-1, key_matrix.shape[0])
    ciphertext_matrix = (np.dot(plaintext_matrix, key_matrix) % 26).flatten()

    # Convert back to letters
    ciphertext = "".join(chr(char + ord('A')) for char in ciphertext_matrix)
    return ciphertext

# Function to calculate the modular inverse of a number
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to decrypt the ciphertext using Hill cipher
def decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = mod_inverse(det, 26)

    if det_inv is None:
        return "Invalid key. The key matrix is not invertible."

    inverse_key_matrix = (np.linalg.inv(key_matrix) * det * det_inv) % 26

    ciphertext = ciphertext.upper().replace(" ", "")
    ciphertext = [ord(char) - ord('A') for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext).reshape(-1, key_matrix.shape[0])
    plaintext_matrix = (np.dot(ciphertext_matrix, inverse_key_matrix) % 26).flatten()

    # Convert back to letters
    plaintext = "".join(chr(char + ord('A')) for char in plaintext_matrix)
    return plaintext

# Example usage
plaintext = input("Enter the plaintext: ")
key = input("Enter the key (e.g., 4 letter key for 2x2 matrix): ")
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)