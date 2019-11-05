import sys
sys.stdin = open('2589.txt', 'r')


def BFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    path = [[0] * row for _ in range(col)]
    path[x][y] = 1

    path_count = 0

    queue = []
    queue.append((x, y))
    while queue:
        x, y = queue.pop(0)
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < col and 0 <= ny < row and jido[nx][ny] == 'L' and not path[nx][ny]:
                path[nx][ny] = path[x][y] + 1
                queue.append([nx, ny])

        path_c = path[x][y] - 1

        if path_count < path_c:
            path_count = path_c

    return path_count

ans = 0
col, row = list(map(int, input().split()))
jido = [[char for char in input()] for _ in range(col)]
for i in range(col):
    for j in range(row):
        if jido[i][j] == 'L':
            ans = max(ans, BFS(i, j))

print(ans)





# long_path = []
# queue = []
# path_count = 0
# for i in range(col):
#     for j in range(row):
#         if jido[i][j] == 'L':
#             path_c = 0
#             queue.append([i, j])
#             path = [[0] * row for _ in range(col)]
#             while queue:
#                 x, y = queue.pop(0)
#                 for n in range(4):
#                     nx = x + dx[n]
#                     ny = y + dy[n]
#                     if ispath(nx, ny) and path[nx][ny] == 0:
#                         path[nx][ny] = path[x][y] + 1
#                         queue.append([nx, ny])
#                         break
#
#                 path_c = path[x][y] - 1
#
#             if path_count < path_c:
#                 path_count = path_c
#                 long_path.append((i, j))
#
# print(path_count)
# print(long_path)