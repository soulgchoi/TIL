import sys
sys.stdin = open('5201.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    truck = [[t, 0] for t in truck]

    i = j = 0

    while i < N and i < M:
        c = container[i]
        for t in range(j, M):
            if c <= truck[t][0]:
                truck[t][1] = c
                j = t + 1
                break
        i += 1

    res = 0
    for t2 in truck:
        res += t2[1]

    print('#%d %d' % (tc, res))