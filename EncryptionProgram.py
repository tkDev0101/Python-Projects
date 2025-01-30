#Encryption Program

import random
import string
chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"CHARS: {chars}")
# print(f"KEY: {key}")

#ENCRYPT
print("\nEncrypting a Message >>")
plain_text = input("Enter a message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"\nOriginal Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")



#DECRYPT
print("\nDecrypting a Message >>")
cipher_text = input("Enter a message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"\nEncrypted Message: {cipher_text}")
print(f"Original Message: {plain_text}")
