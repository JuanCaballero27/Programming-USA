from math import gcd, lcm

def reduced_fraction(x, y):
    d = gcd(x, y)

    return x // d, y // d


def steps(a, b, c, d):
    x = gcd(b, d)
    y = gcd(a, c)



t = int(input())

for i in range(t):
    a, b, c, d = [int(k) for k in input().split()]

    if a / b == c / d or (a == 0 and c == 0):
        print(0)
    elif a == 0 or c == 0:
        print(1)
    else:
        a, b = reduced_fraction(a, b)
        c, d = reduced_fraction(c, d)

