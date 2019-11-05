import sys
sys.stdin = open('2001_파리퇴치.txt', 'r')

def killfly(M):
    global result
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            if (i, j) not in point:
                point.append((i, j))
                sum_fly = 0
                for r in range(i, M+i):
                    for c in range(j, M+j):
                        sum_fly += data[r][c]
                if result < sum_fly:
                    result = sum_fly


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]
    point = []
    result = 0

    for _ in range((N-M+1)**2):
        killfly(M)

    print('#%d %d' % (tc, result))

