import sys
sys.stdin = open('문제2.txt', 'r')

def startpoint():
    global point
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            if (i, j) not in point:
                point.append((i, j))
                return i, j

T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    point = []
    square = 0

    for _ in range((N-K+1)*(M-K+1)):
        x, y = startpoint()
        x1, y1 = x, y
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        n = 0
        sum_square = 0
        while n < 4:
            nx = x + dx[n]
            ny = y + dy[n]
            sum_square += matrix[nx][ny]
            x, y = nx, ny
            if x == x1+K-1 and y == y1:
                n += 1
            elif x == x1+K-1 and y == y1+K-1:
                n += 1
            elif x == x1 and y == y1+K-1:
                n += 1
            elif x == x1 and y == y1:
                n += 1
        if square < sum_square:
            square = sum_square
    print('#%d %d' % (tc, square))