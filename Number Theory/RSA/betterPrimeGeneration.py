# I'll go through and document this sometime with links for further reading. There's a lot of good math that went into this
# from a lot of places.

import random

def generatePrime(bytes):
    primeToTest = random.randint(2**(bytes-1), 2**bytes+1)
    if not primeToTest % 2 == 1:
        primeToTest += 1
    if primeToTest % 5 == 0:
        primeToTest += 2
    while not testIsPrime(primeToTest):
        primeToTest = random.randint(2**(bytes-1), 2**bytes + 1)
    return primeToTest

def testIsPrime(n):
    file = open("primes.txt")
    lastPrime = 1;
    for line in file:
        if(n % int(line) == 0):
            file.close()
            return False;
        lastPrime = int(line)
    file.close()
    if(n < lastPrime):
        return False;

    isPrime = True;
    for i in range(0, 20):
        if not PrimalityTest(n, 20):
            isPrime = False
    return isPrime


# Miller Rabin Test for Primality
def getMaxDivisionsByTwo(a):
    divs = 0
    while(a % 2 == 0):
        a >>= 1
        divs += 1
    return (divs, a)


#k: trials
def PrimalityTest(n, k):
    (pwr, remainder) = getMaxDivisionsByTwo(n-1)
    for i in range(0,k):
        a = random.randint(2, n-2)
        x = fastExponentiation(a, remainder, n)
        if x == 1 or x == n - 1:
            continue
        didPass = False;
        for j in range(0,pwr-1):
            x = fastExponentiation(x, 2, n)
            if x == n-1:
                didPass = True;
                break
        if not didPass:
            return False
        else:
            continue
    return True


def fastExponentiation(base, exponent, mod):
    if(mod == 1):
        return 0;
    result = 1;
    base = base % mod;
    while exponent > 0:
        if(exponent % 2 == 1):
            result = result * base % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result;


def gcd(a, b):
    if(a <b):
        return gcd(b, a)
    while b:
        a, b = b, a%b
    return a;


def generateCoPrime(a):
    print("Finding an integer that is coprime to", a)
    result = random.randint(100000, a)
    while(gcd(result, a) != 1):
        result += 1
    print("The chosen coprime is", result, "\n")
    return result