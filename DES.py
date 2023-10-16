from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad(text):
    # Add PKCS5 padding to the input text
    padding_length = 8 - (len(text) % 8)
    return text + bytes([padding_length] * padding_length)

def unpad(text):
    # Remove PKCS5 padding from the decrypted text
    padding_length = text[-1]
    return text[:-padding_length]

def generate_key():
    # Generate a random 8-byte (64-bit) key
    return get_random_bytes(8)

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_text)
    return plaintext

if __name__ == "__main__":
    while True:
        # Ask the user to enter the key as a hexadecimal string
        key_input = input("Enter the 64-bit key (in hexadecimal format, e.g., 0123456789ABCDEF): ")
        try:
            key = bytes.fromhex(key_input)
            if len(key) != 8:
                raise ValueError
            break
        except ValueError:
            print("Invalid key format. Please enter a 16-character hexadecimal key.")

    # Ask the user to enter the plaintext as a string
    plaintext = input("Enter the plaintext message: ").encode()
    encrypted_text = des_encrypt(key, plaintext)
    decrypted_text = des_decrypt(key, encrypted_text)

    print("Original: ", plaintext)
    print("Encrypted: ", encrypted_text.hex())
    print("Decrypted: ", decrypted_text.decode())
    while True:
        # Ask the user to enter the key as a hexadecimal string
        key_input = input("Enter the 64-bit key (in hexadecimal format, e.g., 0123456789ABCDEF): ")
        try:
            key = bytes.fromhex(key_input)
            if len(key) != 8:
                raise ValueError
            break
        except ValueError:
            print("Invalid key format. Please enter a 16-character hexadecimal key.")

    # Ask the user to enter the plaintext as a string
    plaintext = input("Enter the plaintext message: ").encode()
    encrypted_text = des_encrypt(key, plaintext)
    decrypted_text = des_decrypt(key, encrypted_text)

    print("Original: ", plaintext)
    print("Encrypted: ", encrypted_text.hex())
    print("Decrypted: ", decrypted_text.decode())
