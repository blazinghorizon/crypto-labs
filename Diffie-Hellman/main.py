# 1.2 lab

import numpy
import utils

BITS = 128

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

