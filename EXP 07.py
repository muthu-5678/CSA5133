# Diffie-Hellman Key Exchange Program

# Public values
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

# Private keys
a = int(input("Enter private key of User A: "))
b = int(input("Enter private key of User B: "))

# Public keys
A = (g ** a) % p
B = (g ** b) % p

print("Public Key of User A:", A)
print("Public Key of User B:", B)

# Shared secret keys
key_A = (B ** a) % p
key_B = (A ** b) % p

print("Secret Key for User A:", key_A)
print("Secret Key for User B:", key_B)