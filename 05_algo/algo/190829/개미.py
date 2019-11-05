import sys
sys.stdin = open('개미.txt', 'r')


def wall(n):
    global dx, dy
    if dx == 1 and dy == 0:
        if n == 1:
            dx, dy = 0, -1
        elif n == 2:
            dx, dy = 0, 1
    elif dx == -1 and dy == 0:
        if n == 1:
            dx, dy = 0, 1
        elif n == 2:
            dx, dy = 0, -1
    elif dx == 0 and dy == 1:
        if n == 1:
            dx, dy = -1, 0
        elif n == 2:
            dx, dy = 1, 0
    elif dx == 0 and dy == -1:
        if n == 1:
            dx, dy = 1, 0
        elif n == 2:
            dx, dy = -1, 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    step = 0
    x = y = nx = ny = 0
    dx, dy = 0, 1

    while matrix:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            step += 1
            x = nx
            y = ny
            if matrix[nx][ny] != 0:
                wall(matrix[nx][ny])
        else:
            break

    print('#%d %d' % (tc, step))