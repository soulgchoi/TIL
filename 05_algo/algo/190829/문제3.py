import sys
sys.stdin = open('문제3.txt', 'r')

def isisland(x, y):
    return 0 <= x < N and 0 <= y < N and matrix[x][y] != 0


def findisland():
    global visited
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0 and (i, j) not in visited:
                visited.append((i, j))
                return i, j

def check():
    count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                count += 1
    return count

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    island = 0
    visited = []

    dx = [0, 0, -1, 1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]

    while len(visited) != check():
        x1, y1 = findisland()
        stack = [(x1, y1)]
        while stack:
            x, y = stack[-1]
            n = 0
            while n < 8:
                nx = x + dx[n]
                ny = y + dy[n]
                if isisland(nx, ny) and (nx, ny) not in visited:
                    x, y = nx, ny
                    visited.append((x, y))
                    stack.append((x, y))
                    n = 0
                else:
                    n += 1
            stack.pop()

        island += 1

    print(island)