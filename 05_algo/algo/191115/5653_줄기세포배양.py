import sys
sys.stdin = open('5653.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        data[r] = [0]*(K+1) + data[r] + [0]*(K+1)

    data = [[0]*len(data[0]) for _ in range(K+1)] + data + [[0]*len(data[0]) for _ in range(K+1)]

    length1 = len(data)
    length2 = len(data[0])

    check = [[0]*length2 for _ in range(length1)]
    visited = [[False]*length2 for _ in range(length1)]

    da, db = [0, 0, -1, 1], [1, -1, 0, 0]

    k = 0
    while k < K+1:
        for a in range(length1):
            for b in range(length2):
                if data[a][b] != 0 and check[a][b] != 0:
                    c, d, t = check[a][b]
                    if c == 1 and k-t == d:
                        check[a][b] = (2, d, k)
                    elif c == 2 and k-t == 1:
                        for i in range(4):
                            na, nb = a + da[i], b + db[i]
                            if not visited[na][nb]:
                                if data[na][nb] < d:
                                    data[na][nb] = d
                        if d == 1:
                            check[a][b] = (-1, 0, 0)
                    elif c == 2 and k-t == d:
                        check[a][b] = (-1, 0, 0)

        for a2 in range(length1):
            for b2 in range(length2):
                if data[a2][b2] != 0 and not visited[a2][b2]:
                    check[a2][b2] = (1, data[a2][b2], k)
                    visited[a2][b2] = True

        k += 1

    cnt = 0
    for r in range(length1):
        for c in range(length2):
            if check[r][c] != 0:
                r2, c2, temp = check[r][c]
                if r2 == 1 or r2 == 2:
                    cnt += 1

    print('#%d %d' % (tc, cnt))
