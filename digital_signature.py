"""
@author: Shandon Probst
@project: Algorithms Project 1
@file: digital_signature.py
This file is used for signing and
authenticating digital signatures.
"""

def fastExpo_recursive(a, p, n):
    ''' Returns a^p mod n '''
    if p == 0:
        return 1
    if p%2 == 0:
        t = fastExpo_recursive(a, p//2, n)
        return (t*t)%n
    else:
        t = fastExpo_recursive(a, p//2, n)
        return a *(t**2%n)%n

def sign(m, n, d):
    s = fastExpo_recursive(m, d, n)
    return s

def authenticate(s, n, e):
    m = fastExpo_recursive(s, e, n)
    return m