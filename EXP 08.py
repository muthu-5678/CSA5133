# RSA Algorithm Program

# Function to find gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

# Input two prime numbers
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

# Choose e
e = int(input("Enter value of e: "))

while gcd(e, phi) != 1:
    print("e must be coprime with phi. Enter again:")
    e = int(input())

# Find d
d = mod_inverse(e, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Message
msg = int(input("Enter message (number): "))

# Encryption
cipher = (msg ** e) % n
print("Encrypted message:", cipher)

# Decryption
plain = (cipher ** d) % n
print("Decrypted message:", plain)