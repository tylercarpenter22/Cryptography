'''
Tyler Carpenter
CIS 3362 Guha
This program will take a user inputed affine cypher and use a brutforce 
apporach to decrypt it. It will try every possible a-key(nums coprime with 26)
and every possible b-key(nums between 0 and 25) and print the decrypted text.

The Affine Cipher uses the formula:
E(x)=(ax+b)mod26
'''

#this function takes in the a-key performs inverse mod arithmetic with mod 26
def mod_inverse(a):
  #mod is 26 for letters of alphabet
  for x in range(1, 26):
      if (a * x) % 26 == 1:
          return x
  return None

#this takes in an affine ciphertext and two keys and returns the plaintext
def affine_decrypt(ciphertext, a, b):
  #get mod inverse of a key
  a_inv = mod_inverse(a)
  if a_inv is None:
      return None

  plaintext = ""

  for char in ciphertext:
      if char.isalpha():
          y = ord(char.upper()) - ord('A')  #convert letter to number
          x = (a_inv * (y - b)) % 26
          plaintext += chr(x + ord('A'))  #convert number back to letter
      else:
          plaintext += char  #non-alphabetic characters remain unchanged

  return plaintext


def main():
  #get input
  print("Decrypt a affine cypher")
  ciphertext = input("Enter the ciphertext: ")
  while ciphertext != "-1":
    b = int(input("Enter the b key: "))
    #uses all possible a keys with each b key to decrypt
    possible_a_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    #brute force approach
    for a in possible_a_values:
        decrypted_message = affine_decrypt(ciphertext, a, b)
        if decrypted_message:
            print(f"a = {a} -> Decrypted message: {decrypted_message}")

if __name__ == "__main__":
  main()