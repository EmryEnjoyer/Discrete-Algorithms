# This is from the Wikipedia article on Euclid's Extended Algorithm.
# Link: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def eea(a, b):
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)

    while r != 0:
        quotient = old_r//r
        (old_r, r) = (r, old_r - r * quotient)
        (old_s, s) = (s, old_s - s * quotient)
        (old_t, t) = (t, old_t - t * quotient)

    return (old_s, old_t, old_r)

n = int (input("input first integer: "))
m = int (input("input second integer: "))
inv = eea(n, m)

print(inv)