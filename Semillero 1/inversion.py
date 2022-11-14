def connected(i, j, permutation):
    return permutation[i] > permutation[j]

def components(permutation: list, n: int):
    times = 0
    visited = set()
    for element in range(1, n+1):
        if element not in visited:
            degree = {k+1 for k in range(element, n) if connected(element-1, k, permutation)}
            if visited.isdisjoint(degree):
                times += 1    
            visited.update(degree)

    print(times)


tests = int(input())

for i in range(tests):
    n = int(input())
    permutation = [int(i) for i in input().split()]
    components(permutation, n)