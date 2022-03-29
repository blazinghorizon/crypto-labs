import random

# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

def modPow(x, pow, mod) :
    res = 1 

    # уменьшить x если оно меньше или равно mod
    x = x % mod
     
    if (x == 0) :
        return 0
 
    while (pow > 0) :
         
        # если pow нечетно - res = res * x
        if ((pow & 1) == 1) :
            res = (res * x) % mod
 
        #pow будет четным теперь
        pow //= 2
        x = (x * x) % mod
         
    return res

def generatePQ(n: int):
    p = 0
    q = 0

    while True:
        p = getLowLevelPrime(n)
        if not isMillerRabinPassed(p, 25):
            continue
        else:
            break

    while True:
        q = getLowLevelPrime(n)
        if not isMillerRabinPassed(q, 25):
            continue
        else:
            break

    return p, q

# sqr func
def power_mod(x:int, pow:int, mod:int):
    assert type(x) is int
    assert type(pow) is int and pow >= 0
    assert type(mod) is int

    res = 1
    pow_res = 0
    while pow_res < pow:
        pow_res_1 = 2
        res1 = x
        while pow_res + pow_res_1 <= pow:
            res1 = (res1 * res1) % mod
            pow_res_1 *= 2
        pow_res_1 //= 2
        res = (res * res1) % mod
        pow_res += pow_res_1
        #print(res1, res, pow_res, pow_res_1)
    return res % mod

# gcd func
def gcd(x, y):
    while x != 0 and y != 0:
        if x >= y:
            x %= y
        else:
            y %= x
    return x or y

def gcdExtended(a, b):
    d = gcdExtendedInner(a, b)
    return (d[1] % b + b) % b

def gcdExtendedInner(a, b):
    if a == 0 : 
        return b, 0, 1   

    gcd, x1, y1 = gcdExtendedInner(b%a, a)
    
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd, x, y

# extended euclid algorithm
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
        q = a // m
        t = m
 
        m = a % m
        a = t
        t = y
 
        y = x - q * y
        x = t
 
    if (x < 0):
        x = x + m0
 
    return x
 
def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)
 
def getLowLevelPrime(n):
    while True:
        pc = nBitRandom(n)
 
        for divisor in first_primes_list:
            if pc % divisor == 0:
                break
        else: return pc

def isMillerRabinPassed(num, trials):
    maxDivisionsByTwo = 0
    e = num - 1
    while e % 2 == 0:
        e >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * e == num - 1)
 
    def trialComposite(round_tester):
        if modPow(round_tester, e, num) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if modPow(round_tester, 2**i * e, num) == num-1:
                return False
        return True
 
    for i in range(trials):
        round_tester = random.randrange(2, num)
        if trialComposite(round_tester):
            return False
    return True

# old and unused functions #

def modInverse_naive(a, m):
     
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1

def power(num1, num2):
    if num2 == 0:
        return 1
    elif num2 == 1:
        return num1
    elif num2 % 2 != 0:
        return num1 * power(num1, num2 - 1)
    elif num2 % 2 == 0:
        return power(num1 * num1, num2 / 2)

def power2(base, exp):
    """ Fast power calculation using repeated squaring """
    if exp < 0:
        return 1 / power(base, -exp)
    ans = 1
    while exp:
        if exp & 1:
            ans *= base
        exp >>= 1
        base *= base
    return ans

def power3(a, b, n):
    x = 0

    if (b == 0):
        return 1

    if b % 2 == 0:
        x = power3(a, b/2, n)
        return (x * x) % n

    x = power3(a, (b - 1)/2, n)
    x = (x * x) % n
    return (a * x) % n

    