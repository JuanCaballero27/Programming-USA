integers = [int(i) for i in input().split()]
a, b, c = integers

temp = integers[:]
o1, o2, o3 = 0, 0, 0
n1 = [max(temp), integers.index(max(temp))]
temp.remove(n1[0])
n2 = [max(temp), integers.index(max(temp))]
temp.remove(n2[0])
n3 = [max(temp), integers.index(max(temp))]

difference = n1[0] - n2[0]
if(n2[1] == n1[1]):
    n2[1] += [index for index, k in enumerate(integers) if index != n1[1] and k == n2[0]][0]

if (sum(integers) < 2 * max(integers) or (n3[0]-difference) % 2 == 1):
    print("Impossible")

elif(sum(integers) == 2 * max(integers)):
    index = integers.index(max(integers))
    result = [0, 0, 0]
    for i in range(3):
        if(i == index+1 or i == (index+1)%3):
            result[i] = "0"
        else:
            result[i] = str(max(integers) - integers[i-1])

    print(" ".join(result))

else:
    left = int((n3[0]- difference)/2)
    o3 += difference
    o3 += left
    o2 += left
    o1 += n1[0] - difference - left

    result = [0, 0, 0]
    if(abs(n1[1] - n2[1]) == 1 or abs(n1[1] - n2[1]) == 0):
        result[min(n1[1], n2[1])] = o1

        if(abs(n1[1] - n3[1]) == 1):
            result[min(n2[1], n3[1])] = o3
            result[2] = o2
        else:
            result[2] = o3
            result[min(n2[1], n3[1])] = o2
    else:
        result[2] = o1
        if(abs(n1[1] - n3[1]) == 1):
            result[min(n1[1], n3[1])] = o3
            result[[k for k in range(2) if k != min(n1[1], n3[1])][0]] = o2
        else:
            result[[k for k in range(2) if k != min(n1[1], n3[1])][0]] = o3
            result[min(n1[1], n3[1])] = o2

    print(" ".join([str(k) for k in result]))