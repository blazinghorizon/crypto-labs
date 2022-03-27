# 1.2 lab

from turtle import xcor
import numpy
import utils

def generate_p_q():
    p = 0
    q = 0
    n = 100

    while True:
        p = utils.getLowLevelPrime(n)
        if not utils.isMillerRabinPassed(p):
            continue
        else:
           # print(n, "bit prime is: \n", p)
            break

    while True:
        q = utils.getLowLevelPrime(n)
        if not utils.isMillerRabinPassed(q):
            continue
        else:
         #   print(n, "bit prime is: \n", q)
            break

    return p, q

#print(utils.power(2, 20))
#print(utils.modInverse(3, 26))
#print(utils.modInverse2(3, 26))

e = int(input('input e'))

while True:
    p, q = generate_p_q()
    phi = (p-1)*(q-1)

    if utils.gcd(e, phi) == 1:
        break
    else:
        e += 1

#print(utils.power3(2,3))

_n = p*q
d = utils.modInverse2(e, phi)
print(f'E = {e}, p = {p}, q = {q}, phi = {phi}, n = {_n}, d = {d}\n')

print(f'open key - ({e}, {_n}), closed key - ({d}, {_n})')

msg = 20

print("Message data = ", msg)

c = utils.power(msg, e) % _n

print("\nEncrypted data = ", c)

m = utils.power_mod(c, d, _n)

print("\nOriginal Message Sent = ", m)


'''
while True:
        n = 1024
        p = utils.getLowLevelPrime(n)
        print('p')
        q = utils.getLowLevelPrime(n)
        print(utils.isMillerRabinPassed(p))
        print(utils.isMillerRabinPassed(q))
        break
       # if not utils.isMillerRabinPassed(p):
          #  continue
      #  if not utils.isMillerRabinPassed(q):
           # continue
        else:
            print('xx')
            phi = (p-1)*(q-1)

            if utils.gcd(e, phi) == 1:
                print(f"{n} bit prime 1st is: {p}\n prime 2nd is: {q}")
                break
            else:
                continue

_n = p*q
#d = utils.modInverse2(e, phi)
#print(f'E = {e}, p = {p}, q = {q}, phi = {phi}, n = {_n}, d = {d}\n')


'''
