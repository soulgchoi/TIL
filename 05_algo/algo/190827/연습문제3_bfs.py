vertex = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
edges = [vertex[i:i+2] for i in range(0, len(vertex), 2)]
# G = {edge[0]: for edge in edges}
# for edge in edges:
#     G[edge[0]] = [edge[1] for edge in edges]
#
# print(G)

G = [[0] * (len(edges)+1) for _ in range(len(edges)+1)]
for i in range(1, len(edges)+1):
    for j in range(1, len(edges)+1):
        for edge in edges:
            if edge == [i, j]:
                G[i][j] = 1
                G[j][i] = 1


def BFS(G, v, n):
    visited = [0] * n
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            print(t, end=' ')
        for i in range(len(G[t])):
            if G[t][i] == 1 and not visited[i]:
                queue.append(i)
BFS(G, 1, 8)