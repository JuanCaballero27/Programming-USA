def diagonal(r1, c1, r2, c2):
    for i in range(1, 9):
        if (c1 + i == c2 and r1+i == r2) or (c2 + i == c1 and r2+i == r1) or (c1 - i == c2 and r1+i == r2) or (c1+i == c2 and r1-i == r2):
            return True

    return False


def rook_moves(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2:
        return 1
    else:
        return 2

def bishop_moves(r1, c1, r2, c2):
    if (r1+c1) % 2 != (r2+c2) % 2:
        return 0
    
    if diagonal(r1, c1, r2, c2):
        return 1
    else:
        return 2

def king_moves(r1, c1, r2, c2):
    if(diagonal(r1, c1, r2, c2)):
        return abs(r1-r2)

    elif(r1 == r2):
        return abs(c1 - c2)

    elif(c1 == c2):
        return abs(r1 - r2)

    else:
        return abs(r1-r2) + abs(c1-c2) - min(abs(r1 - r2),  abs(c1 - c2))

r1, c1, r2, c2 = [int(i) for i in input().split()]

print(rook_moves(r1, c1, r2, c2), bishop_moves(r1, c1, r2, c2), king_moves(r1, c1, r2, c2))