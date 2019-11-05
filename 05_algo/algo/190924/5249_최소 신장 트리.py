import sys
sys.stdin = open('5249.txt', 'r')


def make_set(x):
    parent[x] = x
    rank[x] = 0


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])

    return parent[x]


def union(x, y):
    root1 = find_set(x)
    root2 = find_set(y)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(G, E):
    global ans
    for g in range(G+1):
        make_set(g)

    mst = []

    for e in E:
        weight2, v2, u2 = e

        if find_set(v2) != find_set(u2):
            mst += [e]
            union(v2, u2)
            ans += weight2

    return mst


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        u, v, weight = map(int, input().split())
        edges.append((weight, u, v))

    edges.sort()

    parent = {}
    rank = {}
    ans = 0
    li = (kruskal(V, edges))

    print('#%d %d' % (tc, ans))

    # graph = [[0]*(V+1) for _ in range(V+1)]
    # for l in li:
    #     a, b, c = l
    #     graph[b][c] = a
        # graph[c][b] = a

    # print(graph)


# def MST_PRIM(G, r):
#     key = [inf]*(V+1)
#     pi = [None]*(V+1)
#     visited = [False]*(V+1)
#     key[r] = 0
#
#     for _ in range(V):
#         minidx = -1
#         minimum = inf
#         for i in range(V):
#             if not visited[i] and key[i] < minimum:
#                 minimum = key[i]
#                 minidx = i
#             visited[minidx] = True
#             for v, val in G[minidx].items():
#                 print(v, val)
#                 if not visited[v] and val < key[v]:
#                     key[v] = val
#                     pi[v] = minidx

    # graph = {}
    # for _ in range(E):
    #     i, j, weight = map(int, input().split())
    #     graph[i] = {j: weight}
    #     graph[j] = {i: weight}
    # inf = 9999999


