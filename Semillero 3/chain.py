t = int(input())

for i in range(t):
    n = int(input())

    permutation = [str(i+1) for i in range(n)]
    print(" ".join(permutation))
    index = 0
    while index < n-1:
        permutation[index], permutation[index+1] = permutation[index+1], permutation[index]
        print(" ".join(permutation))
        index += 1