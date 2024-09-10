'''
Tyler Carpenter
CIS 3362 Guha
This program will take a user plaintext, a-key, and a b-key and encrypt it using affine cypher.

The Affine Cipher uses the formula:
E(x)=(ax+b)mod26
'''

def affine_encrypt(plaintext, a, b):
  m = 26 

  def encrypt_char(c):
      if c.isalpha():
          #convert character to 0-25 index
          convert = ord('A') if c.isupper() else ord('a')
          x = ord(c) - convert
          #encrypt character
          #E(x)=(ax+b)mod26
          encrypted = (a * x + b) % m
          #convert back to character
          return chr(encrypted + convert)
      else:
          #non-alphabetic characters remain unchanged
          return c

  encrypted_message = ''
  for char in plaintext:
      encrypted_message += encrypt_char(char)

  return encrypted_message

print("Encrypt a message using the Affine Cipher")

#get input
a = int(input("Enter key a: "))
b = int(input("Enter key b: "))
plaintext = input("Enter the message: ")

#encrypt and print the message
ciphertext = affine_encrypt(plaintext, a, b)
print(f"Encrypted message: {ciphertext}")
