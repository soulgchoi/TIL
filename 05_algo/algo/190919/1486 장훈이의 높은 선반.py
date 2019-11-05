import sys, itertools
sys.stdin = open('1486.txt', 'r')

def power_set(x, t):
    global res, H, top
    if t > res:
        return
    if t >= B:
        res = t
        return
    else:
        for i in range(x, N):
            if visited[i]:
                continue
            visited[i] = 1
            power_set(i, t + H[i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    # H.sort(reverse=True)

    res = 99999
    visited = [0]*N
    top = 0

    power_set(0, top)

    print('#%d %d' % (tc, res-B))