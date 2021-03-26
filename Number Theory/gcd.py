# From 
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

n = int (input("input first integer: "))
m = int (input("input second integer: "))

print(gcd(n, m))