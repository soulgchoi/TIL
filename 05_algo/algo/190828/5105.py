import sys
sys.stdin = open('5105.txt', 'r')


def ispath(x, y):
    return 0 <= x < N and 0 <= y < N and (data[x][y] == 0 or data[x][y] == 3)


def findmaze(N, data):
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x, y, = i, j
                break
    maze(x, y)


def maze(x, y):
    queue.append((x, y))
    visited.append((x, y))
    while queue:
        global path_count
        x, y = queue.pop(0)
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if ispath(nx, ny) and (nx, ny) not in visited:
                visited.append((nx, ny))
                queue.append((nx, ny))
                path[nx][ny] = path[x][y] + 1
                if data[nx][ny] == 3:
                    path_count = path[nx][ny] - 1
                    return

for tc in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    path = [[0]*N for _ in range(N)]
    path_count = 0
    queue = []
    visited = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    findmaze(N, data)
    print('#{} {}'.format(tc, path_count))

