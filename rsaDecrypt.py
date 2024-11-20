# -----------------------------------------------------------------------------
# RSA Message Decryption with Modular Inverse
# Written by: Tyler Carpenter
# Date: 11/13/24
# CIS3362-24Fall 0001
# 
# This program demonstrates how to decrypt RSA-encrypted messages using the
# private key 'd' and modulus 'n'. It leverages modular exponentiation to
# decrypt ciphertexts and convert them back into readable text (messages).
# The program uses helper functions to calculate modular exponentiation, 
# convert the decrypted integer back to characters, and process multiple ciphertexts.
#
# -----------------------------------------------------------------------------


def fastmodexpo(base, exp, mod):
    
    if exp == 0:
        return 1
    if exp % 2 == 0:
        tmp = fastmodexpo(base, exp // 2, mod)
        return (tmp * tmp) % mod
    return (base * fastmodexpo(base, exp - 1, mod)) % mod

def getBlockSize(n):
   
    res = 0
    mult = 1

    # Calculate block size based on the modulus n, assuming the message is encoded
    # in base 26 (A-Z).
    while 26 * mult <= n:
        res += 1
        mult *= 26

    return res

def convertBack(msg, blocksize):

    res = ""
    # Convert an integer message back to letters, assuming base 26 encoding (A-Z)
    for i in range(blocksize):
        let = chr(msg % 26 + ord('A'))
        res = let + res
        msg = msg // 26
    return res

def decode_messages(d, n, ciphertexts, blocksize):

    for cipher in ciphertexts:
        decrypted_block = fastmodexpo(cipher, d, n)  # Decrypt the ciphertext
        plaintext = convertBack(decrypted_block, blocksize)  # Convert to readable text
        print(plaintext)


if __name__ == "__main__":
    # Private key (d) and public modulus (n) for RSA decryption
    d = 344532366002717868017953  # Example private key
    n = 576025912082114341909169  # Example RSA modulus
    
    # List of ciphertexts (encrypted messages) to be decrypted
    ciphertexts = [
        488798928261625380184161,
        533946500611718831345802,
        411942882720703143384960,
        20068354290376977207914,
        252864055600177840617225,
        144565738643838496733483,
        98121155489099542089269,
        377474600037914621137040
    ]
    
    # The block size is determined based on the modulus n
    blocksize = getBlockSize(n)
    
    # Decode and print the messages
    decode_messages(d, n, ciphertexts, blocksize)
