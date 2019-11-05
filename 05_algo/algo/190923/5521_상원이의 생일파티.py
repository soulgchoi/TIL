import sys
sys.stdin = open('5521.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     edges = [[] for _ in range(N+1)]
#
#     for _ in range(M):
#         a, b = map(int, input().split())
#         edges[a].append(b)
#         edges[b].append(a)
#
#     print('#%d' % tc, end=' ')
#
#     cnt = 0
#     depth = 0
#
#     queue = [1]
#     visited = [0]*(N+1)
#     while queue:
#         for _ in range(len(queue)):
#             t = queue.pop(0)
#             if not visited[t]:
#                 visited[t] = 1
#                 cnt += 1
#                 for e in edges[t]:
#                     if not visited[e]:
#                         queue.append(e)
#         depth += 1
#         if depth > 2:
#             break
#     print(cnt-1)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        edges[a] += [b]
        edges[b] += [a]

    print('#%d' % tc, end=' ')

    cnt = 0
    depth = 0

    queue = [1]
    visited = [0] * (N + 1)
    front, rear = -1, 0
    while front != rear:
        for _ in range(front, rear):
            front += 1
            t = queue[front]
            if not visited[t]:
                visited[t] = 1
                cnt += 1
                for e in edges[t]:
                    if not visited[e]:
                        queue += [e]
                        rear += 1
        depth += 1
        if depth > 2:
            break
    print(cnt-1)
