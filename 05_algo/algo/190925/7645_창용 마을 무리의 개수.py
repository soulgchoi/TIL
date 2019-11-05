import sys
sys.stdin = open('7645.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(M)]
    edges = [[] for _ in range(N+1)]

    for d in data:
        a, b = d
        edges[b] += [a]
        edges[a] += [b]

    visited = [True]*(N+1)
    group = 0
    for i in range(1, N+1):
        if not visited[i]:
            continue
        queue = [i]
        front, rear = -1, 0
        group += 1
        while front != rear:
            front += 1
            s = queue[front]
            for e in edges[s]:
                if visited[e]:
                    queue.append(e)
                    rear += 1
                    visited[e] = False

    print('#%d %d' % (tc, group))
