import sys
sys.stdin = open('48752.txt', 'r')

def findmaze():
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j

    visited = [[x, y]]
    stack = [[x, y]]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while stack:
        x, y = stack[-1][0], stack[-1][1]

        for n in range(4):
            a = x + dx[n]
            b = y + dy[n]
            if 0 <= x + dx[n] < N and 0 <= y + dy[n] < N and [a, b] not in visited:
                if maze[a][b] == 3:
                    return 1
                if maze[a][b] == 0:
                    visited.append([a, b])
                    stack.append([a, b])
                    break
        else:
            stack.pop()

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[int(i) for i in input()] for _ in range(N)]

    print('#{} {}'.format(tc, findmaze()))





