def stringEncryption(text, key):
    cipherText = ""
    cipher = []
    for i in range(len(key)):
        cipher.append(ord(text[i]) - ord('A') + ord(key[i]) - ord('A'))
    for i in range(len(key)):
        if cipher[i] > 25:
            cipher[i] = cipher[i] - 26
    for i in range(len(key)):
        x = cipher[i] + ord('A')
        cipherText += chr(x)
    return cipherText

def stringDecryption(s, key):
    plainText = ""
    plain = []
    for i in range(len(key)):
        plain.append(ord(s[i]) - ord('A') - (ord(key[i]) - ord('A')))
    for i in range(len(key)):
        if plain[i] < 0:
            plain[i] = plain[i] + 26
    for i in range(len(key)):
        x = plain[i] + ord('A')
        plainText += chr(x)
    return plainText
    for i in range(len(key)):
        if plain[i] < 0:
            plain[i] = plain[i] + 26
    for i in range(len(key)):
        x = plain[i] + ord('A')
        plainText += chr(x)
    return plainText

plainText = "Hello"
key = "MONEY"
encryptedText = stringEncryption(plainText.upper(), key.upper())
print("plain text - " + plainText)
print("encryption - " + encryptedText)
print("decryption - " + stringDecryption(encryptedText, key.upper()))
