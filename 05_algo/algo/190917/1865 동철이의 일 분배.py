import sys
sys.stdin = open('1865.txt', 'r')


def perm(k, val):
    global ans
    if k == N:
        if val > ans:
            ans = val
    else:
        for i in range(k, N):
            cheol[k], cheol[i] = cheol[i], cheol[k]
            if val * dong[k][cheol[k]] > ans:
                perm(k+1, val * dong[k][cheol[k]])
            cheol[k], cheol[i] = cheol[i], cheol[k]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dong = [input().split() for _ in range(N)]
    for d in dong:
        for i in range(N):
            d[i] = int(d[i])/100

    cheol = [c for c in range(N)]

    ans = 0
    # task()
    perm(0, 1)
    print('#%d %0.6f' % (tc, ans*100))
