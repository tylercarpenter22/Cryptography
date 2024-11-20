# -----------------------------------------------------------------------------
# El Gamal Decryption with Optimized Baby-step Giant-step Algorithm
# Written by: Tyler Carpenter
# Date: 11/13/24
# CIS3362-24Fall 0001
# 
# This program demonstrates how to decrypt messages encrypted with the El Gamal
# cryptosystem using the Baby-step Giant-step method to solve the discrete 
# logarithm problem for finding the private key. It then decrypts each ciphertext
# pair using modular arithmetic and recovers the original plaintext message.
#
# Dependencies:
# - sympy: A Python library for efficient computation of modular inverses.
#
# -----------------------------------------------------------------------------

from sympy import mod_inverse

def optimized_babystep_giantstep(base, target, modulus):
    """
    This function solves the discrete logarithm problem base^a = target (mod modulus)
    using the Baby-step Giant-step method, which reduces the time complexity to O(sqrt(modulus)).
    """
    steps = int(modulus**0.5) + 1
    lookup_table = {}

    # Baby-step: Precompute base^j mod modulus for j = 0 to steps-1
    current_value = 1
    for j in range(steps):
        lookup_table[current_value] = j
        current_value = (current_value * base) % modulus

    # Calculate base^(-steps) using Fermat's Little Theorem for efficient backward steps
    inverse_step = pow(base, steps * (modulus - 2), modulus)

    # Giant-step: Search for the matching pair using precomputed values
    search_value = target
    for i in range(steps):
        if search_value in lookup_table:
            # Return the result as i * steps + j
            return i * steps + lookup_table[search_value]
        search_value = (search_value * inverse_step) % modulus

    return None  # No solution found

def decrypt_elgamal(ciphertext, base, public_key, modulus):
    """
    Decrypts a list of ciphertext pairs (C1, C2) using the El Gamal cryptosystem.
    The private key is found using the Baby-step Giant-step method.
    """
    private_key = optimized_babystep_giantstep(base, public_key, modulus)
    print("Private key (a):", private_key)
    
    if private_key is None:
        raise ValueError("Failed to find the private key using discrete logarithm.")

    decrypted_message = []

    for C1, C2 in ciphertext:
        # Step 1: Calculate K = C1^a % modulus
        K = pow(C1, private_key, modulus)

        # Step 2: Compute modular inverse of K
        K_inv = mod_inverse(K, modulus)

        # Step 3: Decrypt the plaintext block P = K_inv * C2 % modulus
        plaintext_value = (K_inv * C2) % modulus

        # Convert the plaintext numeric value back to text (using base 26 encoding)
        decoded_text = ""
        for _ in range(6):  # Assuming 6 character blocks
            decoded_text = chr((plaintext_value % 26) + ord('a')) + decoded_text
            plaintext_value //= 26
        decrypted_message.append(decoded_text)

    return "".join(decrypted_message)

# Example values (to be replaced with actual cryptographic parameters and ciphertext)
g = 52216224  # Generator value
Ya = 32298658  # Public key (g^a mod q)
q = 310000037  # Modulus

# Example ciphertext pairs (replace with actual ciphertext pairs)
ciphertext_pairs = [
    (56495539, 72767212),
    (62083516, 76971521),
    (181398440, 263421160),
    (149867850, 72743477),
    (14826439, 190288780),
    (113953407, 197793189),
    (117331466, 185360595),
    (291767686, 140312582),
    (97578813, 288144131),
    (66782213, 277003739)
]

# Perform decryption
decrypted_message = decrypt_elgamal(ciphertext_pairs, g, Ya, q)
print("Decrypted message:", decrypted_message)
