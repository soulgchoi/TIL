import sys
sys.stdin = open('5208.txt', 'r')


def electric(s, cnt):
    global res
    if s == N-1:
        if cnt < res:
            res = cnt
    for i in range(1, M[s]+1):
        if cnt+1 < res and s+i < len(M):
            electric(s+i, cnt+1)


T = int(input())
for tc in range(1, T+1):
    nm = list(map(int, input().split()))
    N, M = nm[0], nm[1:]+[0]

    res = 9999

    electric(0, -1)
    print('#%d %d' % (tc, res))
