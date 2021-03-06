# 1.2 lab

import utils

BITS = 1000

print('Alice calculates a, g, p and A...')

p = utils.generateP(BITS)
while True:
    try:
        # https://e-maxx.ru/algo/primitive_root
        g = utils.generateG(p)
    except:
        continue
    else:
        break

a = utils.generateP(BITS)
_a = utils.modPow(g, a, p)

print(f'Alice sends Bob p = {p}, g = {g} and A = {_a};')
print()
print('Bob gets g and p;')
print('Bob calculates b, B and K...')
b = utils.generateP(BITS)
_b = utils.modPow(g, b, p)
k_bob = utils.modPow(_a, b, p)
print(f'Bob sends Alice B = {b}')
print()
print('Alice gets B;')
print('Alice calculates K...')
k_alice = utils.modPow(_b, a, p)
print()
print(f'*** Alice\'s K = {k_alice}; Bob\'s K = {k_bob} ***')
print()
i_value = 12
value = i_value + k_alice
print(f'Alice sends Bob value = {value} (value = real + K)')
print(f'Bob decodes value, gets = {value - k_bob} (real = value - K)')

while True:
    break
    try:
        pass
    except:
        print('invalid input, try again...')
    else:
        print('Calculating...')
        break

'''
while True:
    try:
        e = int(input('e: '))
    except:
        print('invalid input, try again...')
    else:
        print('Calculating...')
        break

# get p, q and phi
while True:
    p, q = utils.generatePQ(BITS)
    phi = (p - 1)*(q - 1)

    if utils.gcd(e, phi) == 1:
        break
    else:
        e += 1

# get n
n = p * q
# get d using Euclid Algorithm
d = utils.gcdExtended(e, phi)

# output calculated parameters
print(f'E = {e}\np = {p}\nq = {q}\nphi = {phi}\nn = {n}\nd = {d}\n')
#print(f'open key - ({e}, {n})\nclosed key - ({d}, {n})')

# encrypt and decrypt message
while True:
    try:
        msg = int(input('Input the message: '))
    except:
        print('invalid input, try again...')
    else:
        break

c = utils.modPow(msg, e, n)
m = utils.modPow(c, d, n)

print("Message data =", msg)
print("Encrypted data =", c)
print("Decrypted data =", m)

'''