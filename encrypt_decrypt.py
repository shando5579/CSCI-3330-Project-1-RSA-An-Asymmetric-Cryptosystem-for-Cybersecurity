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
global c_perm

#message will go in index 0, new_e will go in 1, and new_n will go in 2
c = encrypt_recursive(19,5,119)
c_perm = c

print(c)

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

#c_perm will go in index 0, new_d will go in 1, and new_n will go in 2
m = decrypt_recursive(c_perm, 77, 119)
print(m)

