import string

a = string.ascii_letters

text = input("Please enter your ciphered text: ")

Rot = input("Please enter your ROT number: ")

Decipher = ""

for char in text:
    if char.isalpha():
        Decipher += a[(string.ascii_letters.index(char) + int(Rot)) % 26]
    else:
        Decipher += char

print(f"Your Message is: {Decipher}")