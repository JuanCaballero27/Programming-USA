n, t = [int(i) for i in input().split()]
s = list(input())


def transformation(words: list):
    temp = words[::]
    for index, word in enumerate(words[:len(words)-1]):
        if word == "B" and words[index+1] == "G":
            temp[index], temp[index+1] = "G", "B"

    return temp

for i in range(t):
    s = transformation(s)

print("".join(s))