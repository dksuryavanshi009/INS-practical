class PolyalphabeticCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        ciphertext = ''
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                key = ord(self.key[key_index % len(self.key)].upper()) - ord('A')
                encrypted_char = chr((ord(char) - base + key) % 26 + base)
                ciphertext += encrypted_char
                key_index += 1
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                key_index += 1
            else:
                plaintext += char
        return plaintext

key = 'KEY'
cipher = PolyalphabeticCipher(key)
plaintext = 'Message'
encrypted_text = cipher.encrypt(plaintext)
decrypted_text = cipher.decrypt(encrypted_text)

print('Plaintext:', plaintext)
print('Encrypted text:', encrypted_text)
print('Decrypted text:', decrypted_text)
