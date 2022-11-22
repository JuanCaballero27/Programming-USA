t = int(input())

for i in range(t):
    x, y = (char for char in input())
    result = (ord(x) - 97) * 26 + (ord(y) - 97)
    result -= result // 27
    print(result)