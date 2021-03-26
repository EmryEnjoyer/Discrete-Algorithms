# This is from Wikipedia's article on the Extended Euclidean Algorithm (EEA)
# More can be found here: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def Inverse(a, b):
    t = 0;
    newt = 1
    r = b;
    newr = a;

    # GCD algorithm, r is the GCD. t is the bezout coefficient we need since we don't care about the bezout coefficeint of the modulus.
    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r-quotient * newr)

    if r > 1:
        #a is not reversible mod b
        return None
    if t < 0:
        t = t + b

    return t

n = int (input("input first integer: "))
m = int (input("input second integer: "))
inv = Inverse(n, m)

print(inv)
print(n * inv % m);