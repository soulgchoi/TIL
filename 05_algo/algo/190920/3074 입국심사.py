import sys
sys.stdin = open('3074.txt', 'r')

def func(n):
    if n == 0:
        return
    else:
        for t in T:
            if t[0] % n == 0:


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    T = [[int(input()), 1] for _ in range(N)]

    M -= N


    print(N, M)
    print(t)
