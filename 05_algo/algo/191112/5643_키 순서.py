import sys
sys.stdin = open('5643.txt', 'r')


def bfs(start, li):
    global N
    visited = [0] * N
    stack = [start]
    front, rear = -1, 0
    while front != rear:
        front += 1
        s = stack[front]
        visited[s] = 1
        for t in li[s]:
            if not visited[t]:
                stack += [t]
                visited[t] = 1
                rear += 1

    return sum(visited)

T = int(input())
for tc in range(1, T + 1):
    N, M = int(input()), int(input())
    data = [list(map(int, input().split())) for _ in range(M)]

    data1 = [[] for _ in range(N + 1)]
    data2 = [[] for _ in range(N + 1)]

    for d in data:
        a, b = d
        data1[a - 1] += [b - 1]
        data2[b - 1] += [a - 1]

    cnt = 0
    for s in range(N):
        d1 = bfs(s, data1) - 1
        d2 = bfs(s, data2) - 1
        if d1 + d2 == N-1:
            cnt += 1

    print('#%d %d' % (tc, cnt))