def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            shifted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            shifted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext

plaintext = str(input("Enter message: "))
key = int(input("Enter key: "))
encrypted_text = caesar_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
decrypted_text = caesar_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
