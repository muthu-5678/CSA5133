# Simple DES Demonstration (Binary Output)

def string_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def binary_to_string(binary):
    text = ''
    for i in range(0, len(binary), 8):
        text += chr(int(binary[i:i+8], 2))
    return text

def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

# Encryption
def encrypt(plain, key):
    plain_bin = string_to_binary(plain)
    key_bin = string_to_binary(key)

    key_bin = key_bin[:len(plain_bin)]

    cipher_bin = xor(plain_bin, key_bin)
    return cipher_bin

# Decryption
def decrypt(cipher_bin, key):
    key_bin = string_to_binary(key)
    key_bin = key_bin[:len(cipher_bin)]

    plain_bin = xor(cipher_bin, key_bin)
    return binary_to_string(plain_bin)


# Main Program
plain = input("Enter Plain Text: ")
key = input("Enter Key: ")

cipher = encrypt(plain, key)
print("Encrypted (Binary):", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted Text:", decrypted)