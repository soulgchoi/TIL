def dfs_recur1(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(8):
        if visited[w] != 1 and matrix[v][w]:
            dfs_recur1(w)
    # for w in edges[v]:
    #     if not visited[w]:
    #         dfs_recur1(w)


def dfs_recur2(v):
    stack = []
    stack.append(v)
    while stack:
        v = stack.pop()
        if not visited2[v]:
            visited2[v] = 1
            print(v, end=' ')
            for w in edges[v]:
                if not visited2[w]:
                    stack.append(w)



data = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
N = list(map(int, data.split()))
matrix = [[0]*8 for _ in range(8)]
for i in range(0, len(N)-1, 2):
    matrix[N[i]][N[i+1]] = 1
    matrix[N[i+1]][N[i]] = 1

edges = [[] for _ in range(8)]
for n in range(0, len(N)-1, 2):
    edges[N[n]].append(N[n+1])

print(edges)

visited = [0]*8
visited2 = [0]*8


dfs_recur1(1)
print()
dfs_recur2(1)

