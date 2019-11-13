import sys
sys.stdin = open('1949.txt', 'r')


def mt(x, y, flag, cnt, h):
    global visited, dx, dy, ans

    if cnt > ans:
        ans = cnt

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                if data[nx][ny] < h:
                    visited[nx][ny] = True
                    mt(nx, ny, flag, cnt+1, data[nx][ny])
                    visited[nx][ny] = False
                else:
                    if data[nx][ny] - h < K:
                        if flag:
                            visited[nx][ny] = True
                            mt(nx, ny, False, cnt+1, h-1)
                            visited[nx][ny] = False


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    peak = max(sum(data, []))
    start = []

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for a in range(N):
        for b in range(N):
            if data[a][b] == peak:
                start += [(a, b, 1)]
                if len(start) > 4:
                    break

    ans = 0

    for s in start:
        x, y, z = s
        visited = [[False]*N for _ in range(N)]

        visited[x][y] = True
        mt(x, y, True, 1, data[x][y])
        visited[x][y] = False

    print('#%d %d' % (tc, ans))
