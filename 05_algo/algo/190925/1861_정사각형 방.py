import sys
sys.stdin = open('1861.txt', 'r')


def check(arr, na, nb, a, b):
    if na < 0 or nb < 0 or na >= N or nb >= N:
        return False
    else:
        if arr[na][nb] != arr[a][b] + 1:
            return False
        else:
            return True


# def check1(a, b):
#     if a < 0 or b < 0 or a >= N or b >= N:
#         return False
#     else:
#         return True
#
#
# def check2(arr, na, nb, a, b):
#     if arr[na][nb] != arr[a][b] + 1:
#         return False
#     else:
#         return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visited = [[True]*N for _ in range(N)]

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    ans = [0, 0]
    for i in range(N):
        for j in range(N):
            x, y = i, j
            if not visited[x][y]:
                continue
            cnt = 1
            s = room[x][y]
            visited[x][y] = False
            # while True:
            n = 0
            while n < 4:
                nx = x + dx[n]
                ny = y + dy[n]
                if check(room, nx, ny, x, y):
                    cnt += 1
                    x, y = nx, ny
                    visited[x][y] = False
                    n = 0
                else:
                    n += 1
                # break
            if cnt > ans[1]:
                ans = [s, cnt]
            elif cnt == ans[1]:
                if s < ans[0]:
                    ans = [s, cnt]

    print('#%d %d %d' % (tc, ans[0], ans[1]))
