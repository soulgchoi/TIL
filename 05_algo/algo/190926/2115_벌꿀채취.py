import sys
sys.stdin = open('2115.txt', 'r')


def power_set(li):
    r = [[]]

    for e in li:
        temp = [x + [e] for x in r]
        r += temp

    return r


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    bee = [list(map(int, input().split())) for _ in range(N)]
    honey = [[0]*N for _ in range(N)]

    max_honey = (0, 0, 0)
    for i in range(N):
        for j in range(N-M+1):
            temp = bee[i][j:j+M]
            if sum(temp) <= C:
                h = sum(t**2 for t in temp)
                honey[i][j] = h
            else:
                P = power_set(temp)
                h = 0
                for p in P:
                    if sum(p) <= C:
                        temp2 = sum([p2 ** 2 for p2 in p])
                        if temp2 > h:
                            h = temp2
            honey[i][j] = h
            if h >= max_honey[2]:
                max_honey = i, j, h

    res1 = max_honey[2]
    for x in range(max_honey[1], max_honey[1] + M):
        honey[max_honey[0]][x] = 0
        honey[max_honey[0]][x-M+1] = 0

    res2 = 0
    for a in honey:
        if max(a) > res2:
            res2 = max(a)

    print('#%d %d' % (tc, res1 + res2))

