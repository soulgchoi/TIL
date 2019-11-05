import sys
sys.stdin = open('5188.txt', 'r')

def func(x, y, val):
    global ans

    if x == N-1 and y == N-1:
        # if val < ans:
        ans = val
    else:
        dx, dy = [1, 0], [0, 1]
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if val + arr[nx][ny] < ans:
                    func(nx, ny, val + arr[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    x, y = 0, 0

    val = arr[x][y]
    ans = 999

    func(x, y, val)
    print('#%d %d' % (tc, ans))

