import sys
sys.stdin = open("solvingclub.txt", "r")

for _ in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    Y = 0
    for i in range(len(data)):
        if data[len(data)-1][i] == 2:
            Y = i
            break

    x, y = 0, 0
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    X = len(data) - 2

    visited = []

    while X != 0:
        for j in range(len(dx)):
            x = X + dx[j]
            y = Y + dy[j]
            if 0 <= x < len(data) and 0 <= y < len(data) and [x, y] not in visited:
                if data[x][y] == 1:
                    X = x
                    Y = y
                    visited.append([x, y])

    print('#{} {}'.format(tc, Y))
