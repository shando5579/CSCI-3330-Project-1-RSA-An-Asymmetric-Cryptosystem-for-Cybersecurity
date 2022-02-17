<<<<<<< HEAD
"""
@author: Nickolas Paternoster
@project: Algorithms Project 1
@file: encrypt_decrypt.py

This file is used for encrypting/decrypting 
messages given a public and/or private key.

"""
import key_gen

new_n = key_gen.n_perm
new_e = key_gen.e_perm
new_d = key_gen.d_perm


# Used to convert ints to chars and store in array
def convertToChar(message):
    '''Converts a message to proper
    char values according to ASCII'''
    converted = []
    for value in message:
        converted.append(chr(value))
    return converted

=======
import project1_key_gen

global c_perm
new_p = project1_key_gen.p_perm
new_q = project1_key_gen.q_perm
new_n = project1_key_gen.n_perm
new_phiN = project1_key_gen.phiN_perm
new_e = project1_key_gen.e_perm
new_d = project1_key_gen.d_perm
'''
print('nw p is:', new_p)
print('nw q is:', new_q)
print('nw n is:', new_n)
print('nw phiN is:', new_phiN)
print('nw e is:', new_e)
'''
#print('d is:' , new_d)
>>>>>>> 7645c428fa01664e2134a1bd4ee52b3fb3f86615

def encrypt_recursive(m, e, n):
    ''' Returns m^e mod n = c '''
    if e == 0:
        return 1
<<<<<<< HEAD
    if e % 2 == 0:
        t = encrypt_recursive(m, e//2, n)
        return (t*t) % n
    else:
        t = encrypt_recursive(m, e//2, n)
        return m * (t**2 % n) % n


def decrypt_recursive(c, d, n):
    ''' Returns c^d mod n = m '''
=======
    if e%2 == 0:
        t = encrypt_recursive(m, e//2, n)
        return (t*t)%n
    else:
        t = encrypt_recursive(m, e//2, n)
        return m *(t**2%n)%n
global c_perm

#message will go in index 0, new_e will go in 1, and new_n will go in 2
c = encrypt_recursive(19,5,119)
c_perm = c

print(c)

def decrypt_recursive(c, d, n):
    ''' Returns c^d mod n = m '''

>>>>>>> 7645c428fa01664e2134a1bd4ee52b3fb3f86615
    if d == 0:
        return 1
    if d % 2 == 0:
        t = decrypt_recursive(c, d // 2, n)
        return (t * t) % n
    else:
        t = decrypt_recursive(c, d // 2, n)
        return c * (t ** 2 % n) % n

<<<<<<< HEAD
# Takes a string and converts the characters to ascii values, then sends each of those values to the encryption method


def encrypt_string(str, e, n):
    '''Processes and encrypts a string'''
    string = list(str.encode('ascii'))
    encrypt = list()
    for i in string:
        encrypt.append(encrypt_recursive(i, new_e, new_n))
    return encrypt


# runs encrypted ascii values and decrypts them with the private key


def decrypt_string(c, d, n):
    '''Processes and decrypts a string'''
    decrypt = list()
    for i in c:
        decrypt.append(decrypt_recursive(i, new_d, new_n))
    return decrypt

# Used for testing the encryption / decryption on numbers and strings

# message will go in index 0, e will go in 1, and n will go in 2


c = encrypt_string('testing', new_e, new_n)
print('Encrypted message is: ', c)


# c will go in index 0, d will go in 1, and n will go in 2
m = decrypt_string(c, new_d, new_n)
print('Decrypted message is: ', convertToChar(m))
=======
#c_perm will go in index 0, new_d will go in 1, and new_n will go in 2
m = decrypt_recursive(c_perm, 77, 119)
print(m)
>>>>>>> 7645c428fa01664e2134a1bd4ee52b3fb3f86615

