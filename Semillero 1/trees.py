def groups(distances):
    counter = 0
    checked = set()
    for index, element in enumerate(distances):
        if checked.isdisjoint(element) and checked.isdisjoint(element.union(distances[index+1])):
            counter += 1
            checked.update(element)

    return counter


n = int(input())
distances = [{int(i), index+1} for index, i in enumerate(input().split())]

print(groups(distances))