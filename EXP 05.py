# Hill Cipher Program (Encryption and Decryption)

def text_to_numbers(text):
    return [ord(c) - 65 for c in text]

def numbers_to_text(nums):
    return ''.join(chr((n % 26) + 65) for n in nums)

# Encryption
def encrypt(text, key):
    text = text.upper().replace(" ", "")
    
    if len(text) % 2 != 0:
        text += 'X'

    cipher = ""

    for i in range(0, len(text), 2):
        p = text_to_numbers(text[i:i+2])

        c1 = (key[0][0]*p[0] + key[0][1]*p[1]) % 26
        c2 = (key[1][0]*p[0] + key[1][1]*p[1]) % 26

        cipher += numbers_to_text([c1, c2])

    return cipher


# Decryption
def decrypt(cipher, key):

    det = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26

    # Find modular inverse of determinant
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break

    # Inverse key matrix
    inv_key = [
        [(key[1][1] * det_inv) % 26, (-key[0][1] * det_inv) % 26],
        [(-key[1][0] * det_inv) % 26, (key[0][0] * det_inv) % 26]
    ]

    plain = ""

    for i in range(0, len(cipher), 2):
        c = text_to_numbers(cipher[i:i+2])

        p1 = (inv_key[0][0]*c[0] + inv_key[0][1]*c[1]) % 26
        p2 = (inv_key[1][0]*c[0] + inv_key[1][1]*c[1]) % 26

        plain += numbers_to_text([p1, p2])

    return plain


# Main Program
key = [[3,3],
       [2,5]]

text = input("Enter Plain Text: ")

encrypted = encrypt(text, key)
print("Encrypted Text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Text:", decrypted)