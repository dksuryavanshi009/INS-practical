def encrypt(message, key):
    encrypted_message = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            encrypted_message[col] += message[pointer]
            pointer += key
    return ''.join(encrypted_message)

def decrypt(encrypted_message, key):
    decrypted_message = [''] * ((len(encrypted_message) // key) + 1)
    row, col = 0, 0
    for symbol in encrypted_message:
        decrypted_message[row] += symbol
        row += 1
        if row == (len(encrypted_message) // key) + 1 or (row == (len(encrypted_message) // key) and col >= (len(encrypted_message) % key)):
            row = 0
            col += 1
    return ''.join(decrypted_message)

plaintext = "MESSAGE"
key = 4
encrypted_text = encrypt(plaintext, key)
print("Encrypted message:", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted message:", decrypted_text)
