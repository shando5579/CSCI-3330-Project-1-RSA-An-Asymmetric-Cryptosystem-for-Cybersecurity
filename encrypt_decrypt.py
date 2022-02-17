"""
@author: Nickolas Paternoster
@project: Algorithms Project 1
@file: encrypt_decrypt.py

This file is used for encrypting/decrypting 
messages given a public and/or private key.

"""

import key_gen

def encrypt_recursive(m, e, n):
    ''' Returns m^e mod n = c '''

    if e == 0:
        return 1
    if e%2 == 0:
        t = encrypt_recursive(m, e//2, n)
        return (t*t)%n
    else:
        t = encrypt_recursive(m, e//2, n)
        return m *(t**2%n)%n

def decrypt_recursive(c, d, n):
    ''' Returns c^d mod n = m '''

    if d == 0:
        return 1
    if d % 2 == 0:
        t = decrypt_recursive(c, d // 2, n)
        return (t * t) % n
    else:
        t = decrypt_recursive(c, d // 2, n)
        return c * (t ** 2 % n) % n


# message will go in index 0, e will go in 1, and n will go in 2
c = encrypt_recursive('Hello',5,119)

# c_perm will go in index 0, d will go in 1, and n will go in 2
m = decrypt_recursive(c, 77, 119)

print('c is: ', c)
print('m is: ', m)
