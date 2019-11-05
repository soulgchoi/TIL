# def killfly(M):
#     global result
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             if (i, j) not in point:
#                 point.append((i, j))
#                 sum_fly = 0
#                 for r in range(i, M+i):
#                     for c in range(j, M+j):
#                         sum_fly += data[r][c]
#                 if result < sum_fly:
#                     result = sum_fly
import sys
sys.stdin = open('파리.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_f = 0
            for r in range(i, M + i):
                for c in range(j, M + j):
                    sum_f += data[r][c]
            if result < sum_f:
                result = sum_f

    print('#%d %d' % (tc, result))