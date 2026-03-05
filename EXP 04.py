# Transposition Cipher (Columnar)

import math

# Encryption
def encrypt_transposition(text, key):
    cipher = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(text):
            cipher[col] += text[pointer]
            pointer += key

    return ''.join(cipher)


# Decryption
def decrypt_transposition(cipher, key):
    num_cols = math.ceil(len(cipher) / key)
    num_rows = key
    num_shaded = (num_cols * num_rows) - len(cipher)

    plain = [''] * num_cols
    col = 0
    row = 0

    for symbol in cipher:
        plain[col] += symbol
        col += 1

        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded):
            col = 0
            row += 1

    return ''.join(plain)


# Main program
text = input("Enter the message: ")
key = int(input("Enter the key (number): "))

encrypted = encrypt_transposition(text, key)
print("Encrypted Text:", encrypted)

decrypted = decrypt_transposition(encrypted, key)
print("Decrypted Text:", decrypted)