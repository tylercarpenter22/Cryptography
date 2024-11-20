# -----------------------------------------------------------------------------
# Euler Phi and Inverse Mod for RSA
# Written by: Tyler Carpenter
# Date: 11/13/24
# CIS3362-24Fall 0001
# 
# This program calculates the modular inverse of the encryption exponent 'e'
# modulo Euler's Totient function of 'n', denoted as φ(n), for RSA encryption.
# It first computes φ(n) using the sympy library's `totient` function and then
# calculates 'd', which is the modular inverse of 'e' modulo φ(n). This value
# 'd' is crucial for the decryption key in RSA cryptography. The program outputs
# both φ(n) and 'd'.
#
# Dependencies:
# - sympy: A Python library for symbolic mathematics used here to compute
#   Euler's Totient function and the modular inverse.
#
# -----------------------------------------------------------------------------

from sympy import totient
from sympy import mod_inverse

# Main program execution
if __name__ == "__main__":
    # RSA Inputs: n (modulus) and e (encryption exponent)
    n = 576025912082114341909169  # Example large RSA modulus
    e = 395065083027011624330977  # Example encryption exponent
    
    # Calculate and display Euler's Totient function φ(n)
    phi_n = totient(n)
    print(f"φ(n): {phi_n}")

    # Calculate and dipslay the modular inverse d of e modulo φ(n)
    d = mod_inverse(e, phi_n)
    print(f"d: {d}")

    # Checks work for q2 - Result: 19
    # q2 = mod_inverse(139, 660)
    # print(f"q2: {q2}")