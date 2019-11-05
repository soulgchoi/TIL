import sys
sys.stdin = open('격자판.txt', 'r')

def func(i, j, cnt, number = ''):
    global numbers
    x, y = i, j
    number += str(matrix[x][y])

    if cnt == 7:
        numbers.add(number)
        return
    else:
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < 4 and 0 <= ny < 4:
                func(nx, ny, cnt+1, number)

T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(4)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    numbers = set()

    for i in range(4):
        for j in range(4):
            func(i, j, 1)

    print('#%d %d' % (tc, len(numbers)))