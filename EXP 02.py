# Monoalphabetic Cipher Program

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"   # substitution key

def encrypt(plain_text):
    plain_text = plain_text.upper()
    cipher_text = ""

    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter

    return cipher_text


def decrypt(cipher_text):
    cipher_text = cipher_text.upper()
    plain_text = ""

    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += alphabet[index]
        else:
            plain_text += letter

    return plain_text


# Main program
message = input("Enter message: ")

encrypted = encrypt(message)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted message:", decrypted)