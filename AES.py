from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

def generate_key(password):
    # Generate a 256-bit (32 bytes) key using PBKDF2 with 100,000 iterations
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    return key, salt

def aes_encrypt(key, plaintext):
    # Generate a random 16-byte IV (Initialization Vector)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext, iv

def aes_decrypt(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

if __name__ == "__main__":
    # Ask the user to enter a password
    password = input("Enter the password: ")
    key, salt = generate_key(password.encode())

    # Ask the user to enter the plaintext as a string
    plaintext = input("Enter the plaintext message: ").encode()
    encrypted_text, iv = aes_encrypt(key, plaintext)
    decrypted_text = aes_decrypt(key, encrypted_text, iv)

    print("Original: ", plaintext.decode())
    print("Encrypted: ", encrypted_text.hex())
    print("Decrypted: ", decrypted_text.decode())
