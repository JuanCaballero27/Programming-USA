n, m = [int(i) for i in input().split()]
tube = set()
danger = 1

for i in range(m):
    pair = {int(i) for i in input().split()}
    # if not tube.isdisjoint(pair) or len(tube) == 0:
    #     danger *= 2
    
    # tube.update(pair)

print(2**m)