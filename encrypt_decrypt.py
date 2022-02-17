"""
@author: Nickolas Paternoster
@project: Algorithms Project 1
@file: encrypt_decrypt.py

This file is used for encrypting/decrypting 
messages given a public and/or private key.

"""

import key_gen

# Used to convert chars to ints and store in array
def convertToInt(message):
    '''Converts a message to proper 
    int values according to ASCII'''
    converted = []

    for char in message:
        converted.append(ord(char))

    return converted

# Used to convert ints to chars and store in array
def convertToChar(message):
    '''Converts a message to proper 
    char values according to ASCII'''
    converted = []

    for value in message:
        converted.append(chr(value))

    return converted

def encrypt_recursive(m, e, n):
    ''' Returns m^e mod n = c '''

    if e == 0:
        return 1
    if e % 2 == 0:
        t = encrypt_recursive(m, e//2, n)
        return (t*t) % n
    else:
        t = encrypt_recursive(m, e//2, n)
        return m * (t**2 % n) % n


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


def encrypt_string(str, e, n):
    '''Processes and encrypts a string'''

    # Converts current string to int values from ASCII table
    converted_str = convertToInt(str)
    encrypted_str = []

    # Processes and encrypts each value in converted_str
    for value in converted_str:
        encrypted_str.append(encrypt_recursive(value, e, n))

    return encrypted_str

def decrypt_string(c, d, n):
    '''Processes and decrypts a string'''

    # Decrypts values from encrypted values c
    decrypted_str = []
    for value in c:
        decrypted_str.append(decrypt_recursive(value, d, n))

    # Converts current decrypted string to char values from ASCII table
    converted_str = convertToChar(decrypted_str)

    return converted_str

# Used for testing the encryption / decryption on numbers and strings

# message will go in index 0, e will go in 1, and n will go in 2
'''
c = encrypt_string('19', 5, 119)
print('c is: ', c)

c2 = encrypt_recursive(19, 5, 119)
print('c2 is: ', c2)

# c will go in index 0, d will go in 1, and n will go in 2
m = decrypt_string(c, 77, 119)
print('m is: ', m)

m2 = decrypt_recursive(c2, 77, 119)
print('m2 is: ', m2)
'''