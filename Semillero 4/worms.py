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
worms = [int(i) for i in input().split()]
m = int(input())
juicy = [int(i) for i in input().split()]

intervals = []
t = 1

for i in range(len(worms)):
  intervals.append(t)
  t += worms[i]


for element in juicy:
  print(Binary(intervals, element)+1)