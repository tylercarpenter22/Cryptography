'''
Tyler Carpenter
CIS 3362 Guha
This program will take a user inputed plaintext cypher and a shift key
and return the text with the shift key applied.
'''

#get input
print("Decrypt a shift cypher - Enter -1 to end")
plaintext = input("Enter the ciphertext: ")
while plaintext != "-1":
    shift_key = int(input("Enter the shift key: "))

    decrypted_text = ""

    #loop through each character in the ciphertext
    for char in plaintext:
        if char.isalpha():  # check if the character is a letter
            shift_amount = ord('a') if char.islower() else ord('A')
            #apply shift
            decrypted_char = chr((ord(char) - shift_amount - shift_key) % 26 + shift_amount)
            decrypted_text += decrypted_char
        else:
            #if it's not a letter, add it to the decrypted text unchanged
            decrypted_text += char

    #print the decrypted message
    print("Decrypted message:", decrypted_text)
