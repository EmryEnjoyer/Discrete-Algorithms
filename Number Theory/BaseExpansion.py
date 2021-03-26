# From Rosen's book

def expand(n, b):
    num = "";
    start = n;
    while(start != 0):
        num = num + (str) (start % b);
        start = (int) (start/b);
    return (int) (num[::-1]);

n = int (input("Input integer to expand: "))

print(expand(n, 2))