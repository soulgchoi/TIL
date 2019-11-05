import sys
sys.stdin = open('오셀로.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    board = [[0]*(N+1) for _ in range(N+1)]

    board[N//2][N//2+1] = board[N//2+1][N//2] = 1
    board[N//2][N//2] = board[N//2+1][N//2+1] = 2
    color = [2, 2]

    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    for _ in range(M):
        r, c, x = list(map(int, input().split()))
        board[r][c] = x
        color[x-1] += 1
        for n in range(8):
            nr = r + dr[n]
            nc = c + dc[n]
            if nr < 0 or nc < 0 or nr >= N+1 or nc >= N+1:
                continue
            if board[nr][nc] != 0 and board[nr][nc] != x:
                cnt = 0
                while board[nr][nc] != x:
                    cnt += 1
                    nr = nr + dr[n]
                    nc = nc + dc[n]
                    if nr < 0 or nc < 0 or nr >= N+1 or nc >= N+1 or board[nr][nc] == 0:
                        cnt = 0
                        break
                nr = r + dr[n]
                nc = c + dc[n]

                while cnt != 0:
                    board[nr][nc] = x
                    nr = nr + dr[n]
                    nc = nc + dc[n]
                    cnt -= 1

                    color[x-1] += 1
                    color[x-2] -= 1

    print('#%d %d %d' % (tc, color[0], color[1]))

