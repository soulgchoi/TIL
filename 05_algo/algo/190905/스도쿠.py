import sys
sys.stdin = open('스도쿠.txt', 'r')


def sudoku1(i, j):
    c = []
    for x in range(i, i+3):
        for y in range(j, j+3):
            c.append(data[x][y])
    return check(c)


def sudoku2(i):
    c = []
    for a in range(9):
        c.append(data[i][a])
    return check(c)


def sudoku3(i):
    c = []
    for a in range(9):
        c.append(data[a][i])
    return check(c)


def check(c):
    for n in range(1, 10):
        if n not in c:
            return False

    return True

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    for i1 in range(0, 7, 3):
        for j1 in range(0, 7, 3):
            if sudoku1(i1, j1):
                pass
            else:
                result = 0

    for i2 in range(9):
        if sudoku2(i2) and sudoku3(i2):
                pass
        else:
            result = 0

    print('#%d %d' % (tc, result))