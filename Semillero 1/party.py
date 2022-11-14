def deep(adjacency, x):
    temp = x
    level = 0
    while temp != 0:
        level += 1
        temp = adjacency[temp]

    return level


n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

adjacency = {}

for i in range(n):
    adjacency[i+1] = data[i] if data[i] != -1 else 0

groups = 0
for element in adjacency.keys():
    if groups < deep(adjacency, element):
        groups = deep(adjacency, element)

print(groups)