def Binary(array: list, x: int):
    lower = 0
    upper = len(array) - 1

    while lower < upper:
        index = (lower + upper) // 2
        if array[index] <= x:
            if array[index+1] > x:
              return index
            else:
              lower = index+1
        
        else:
            upper = index-1

    if array[lower] <= x:
        return lower
    
    return -1

n = int(input())
prices = [int(i) for i in input().split()]
prices.sort()
q = int(input())

for i in range(q):
    m = int(input())
    print(Binary(prices, m) + 1)