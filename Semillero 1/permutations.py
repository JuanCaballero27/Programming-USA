n = int(input())
planes = [int(i) for i in input().split()]

def cicle(n, collect):
    if collect[collect[collect[n-1]-1]-1] == n:
        return True

    return False


def triangle():
    global planes
    for plane in planes:
        if(cicle(plane, planes)):
            print("YES")

    print("NO")

triangle()