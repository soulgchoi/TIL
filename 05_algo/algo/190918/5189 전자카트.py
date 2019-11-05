import sys
sys.stdin = open('5189.txt', 'r')

def perm(k, n):
    global ans, p, val
    if k == n:
        val = 0
        p2 = [0] + p + [0]
        for j in range(len(p2)-1):
            val += arr[p2[j]][p2[j+1]]
        if val < ans:
            ans = val
    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(k+1, n)
            p[k], p[i] = p[i], p[k]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 9999
    p = [a for a in range(1, N)]
    n = N-1
    perm(0, n)
    print('#%d %d' % (tc, ans))