# makeset > union
# 빠진 것까지 총 그룹이 몇개인지
# 그룹 만들어서 bfs, dfs 로 카운팅 가능
import sys
sys.stdin = open('5248.txt', 'r')


# def find_group(x, y):
#     global group
#     if len(group) == 0:
#         group.append([x, y])
#     else:
#         for g in group:
#             if x in g:
#                 g.append(y)
#

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    edges = [[] for _ in range(N+1)]
    for d in range(0, M*2-1, 2):
        edges[data[d]] += [data[d+1]]
        edges[data[d+1]] += [data[d]]

    group = 0
    visited = [0]*(N+1)
    for n in range(1, N+1):
        if not visited[n]:
            group += 1
            queue = [n]
            front, rear = -1, 0
            while front != rear:
                front += 1
                q = queue[front]
                if not visited[q]:
                    visited[q] = 1
                    for e in edges[q]:
                        queue.append(e)
                        rear += 1

    print('#%d %d' % (tc, group))










