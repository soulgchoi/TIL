import sys
sys.stdin = open('토끼.txt', 'r')

def iswall(x, y):
    return 0 <= x < 10 and 0 <= y < 10

def find_hunter():
    global hunter
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3 and (i, j) not in hunter:
                x, y = i, j
                hunter.append((x, y))
                return x, y


matrix = [list(map(int, input().split())) for _ in range(10)]
hunter = []

c_hunter = 0
for ni in range(10):
    for nj in range(10):
        if matrix[ni][nj] == 3:
            c_hunter += 1

rabbit = []
for _ in range(c_hunter):
    dx = [0, 1, 0, -1, -1, 1, 1, -1]
    dy = [-1, 0, 1, 0, -1, -1, 1, 1]
    a = b = 0
    x, y = find_hunter()
    xx, yy = x, y
    for n in range(8):
        while iswall(x, y) and matrix[x][y] != 2:
            a = x + dx[n]
            b = y + dy[n]
            x, y = a, b
            if 0 <= x < 10 and 0 <= y < 10:
                if matrix[x][y] == 1:
                    rabbit.append((x, y))
            else:
                break
        x, y = xx, yy

print(len(set(rabbit)))