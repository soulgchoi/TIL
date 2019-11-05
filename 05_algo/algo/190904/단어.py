import sys
sys.stdin = open('단어.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [[0 for _ in range(N+1)]] + [[0] + list(map(int, input().split())) for _ in range(N)]

    count = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                if arr[i][j-1] != 1:
                    n = 1
                    nj = j + 1
                    while 1 <= nj < N+1:
                        if arr[i][nj] == 0:
                            break
                        if arr[i][nj] == 1:
                            n += 1
                        nj = nj + 1
                    if n == K:
                        count += 1

                if arr[i-1][j] != 1:
                    m = 1
                    ni = i + 1
                    while 1 <= ni < N+1:
                        if arr[ni][j] == 0:
                            break
                        if arr[ni][j] == 1:
                            m += 1
                        ni = ni + 1
                    if m == K:
                        count += 1

    print('#%d %d' % (tc, count))