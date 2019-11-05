import sys
sys.stdin = open('5105.txt', 'r')

def findstart(N, data):
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x, y = i, j
                break
    maze(x, y)

def maze(x, y):
    global path_count
    queue = [[x, y]]
    visited = [[x, y]]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while stack:
        x, y = queue[0]
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < N and 0 <= ny < N and [nx, ny] not in visited and (data[nx][ny] == 1 or data[nx][ny] == 3):
                visited.append([nx, ny])
                stack.append([nx, ny])
                path[nx][ny] = path[x][y] + 1
                if data[nx][ny] == 3:
                    path_count = path[nx][ny] - 1
                    return
        else:
            queue.pop()

for tc in range(1, int(input())+1):
    N = int(input())
    data = [[int(d) for d in input()] for _ in range(N)]

    stack = []
    visited = []

    path = [[0]*N for _ in range(N)]
    path_count = 0

    findstart(N, data)
    print('#{} {}'.format(tc, path_count))

