import sys
sys.stdin = open('input (2).txt', 'r')


def issquare(x, y):
    return 0 <= x < N and 0 <= y < N and data[x][y] != 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    matrix = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] != 0 and visited[i][j] != 1:
                visited[i][j] = 1
                x, y = i, j

                col = 1
                n = 0
                while issquare(x, y+n):
                    n += 1
                    if data[x][y+n] != 0:
                        visited[x][y+n] = 1
                        col += 1
                x, y = x, y+n-1

                row = 0
                m = 0
                while issquare(x+m, y):
                    if data[x+m][y] != 0:
                        visited[x+m][y] = 1
                        row += 1
                    m += 1
                r2, c2 = x, y = x+m, y

                for r in range(i+1, r2):
                    for c in range(j, c2):
                        visited[r][c] = 1

                matrix.append([row*col, row, col])

    print('#%d %s' % (tc, len(matrix)), end=' ')

    for a in range(len(matrix)-1):
        min_number = a
        for b in range(a+1, len(matrix)):
            if matrix[min_number][0] > matrix[b][0]:
                min_number = b
            elif matrix[min_number][0] == matrix[b][0]:
                if matrix[min_number][1] > matrix[b][1]:
                    min_number = b
        matrix[min_number], matrix[a] = matrix[a], matrix[min_number]

    for ab in range(len(matrix)):
        print(matrix[ab][1], matrix[ab][2], end=' ')
    print()


