t = int(input())

def perfect_square(x):
    root = int(x**0.5)
    return root**2 == x



for i in range(t):
    n = int(input())

    if perfect_square(n):
        print("0 " + " ".join([str(n - i) for i in range(1, n)]))