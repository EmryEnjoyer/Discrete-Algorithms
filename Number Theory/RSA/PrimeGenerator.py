import random

# Find a better prime generation

def generatePrime():
    startingInt = random.randint(2**32, 2**48)
    startingInt = startingInt * 2 + 1

    print("Generating the next prime after", startingInt, "...")
    while not primeTest(startingInt):
        startingInt += 1
        if ((str(startingInt))[-1] == '5'):
            startingInt += 1
    print("The prime that we chose is", startingInt, "\n")
    return startingInt


def gcd(a, b):
    if(b > a):
        return gcd(b, a)
    if(a % b == 0):
        return b
    return gcd(b, a%b)

def primeTest(n):
    for i in range(2, int (n**.5+1)):
        if(n % i == 0):
            return False;
    return True;

def generateCoPrime(a):
    print("Finding an integer that is coprime to", a)
    result = random.randint(100000, a)
    while(gcd(result, a) != 1):
        result += 1
    print("The chosen coprime is", result, "\n")
    return result