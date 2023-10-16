def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa_keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    d = mod_inverse(e, phi)
    return (n, e, d)

def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def rsa_encrypt(plaintext, n, e):
    encrypted = [mod_pow(ord(char), e, n) for char in plaintext]
    return encrypted

def rsa_decrypt(ciphertext, n, d):
    decrypted = [chr(mod_pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted)

# User input
p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))
message = input("Enter the message you want to encrypt: ")
n, e, d = rsa_keygen(p, q)
encrypted_message = rsa_encrypt(message, n, e)
decrypted_message = rsa_decrypt(encrypted_message, n, d)
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
