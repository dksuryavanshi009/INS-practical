# Get the shared prime number (publicly known) as user input
p = int(input("Enter the shared prime number (p):"))

# Get the shared base (publicly known) as user input
g = int(input("Enter the shared base (g):"))

# Get Alice's private key (secret) from user input
a_private = int(input("Enter Alice's private key:"))

# Get Bob's private key (secret) from user input
b_private = int(input("Enter Bob's private key:"))

# Calculate public keys for Alice and Bob
a_public = (g ** a_private) % p
b_public = (g ** b_private) % p

# Exchange public keys over the insecure channel

# Calculate the shared secret for Alice and Bob
shared_secret_alice = (b_public ** a_private) % p
shared_secret_bob = (a_public ** b_private) % p

# Both Alice and Bob now have the same shared secret
print("Shared Secret (Alice):", shared_secret_alice)
print("Shared Secret (Bob):", shared_secret_bob)
