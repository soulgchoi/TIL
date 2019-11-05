dfs_ex = 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

# 정점, 간선 각각 리스트로 만들기
dfs = list(dfs_ex)
edges = [dfs[i:i+2] for i in range(0, len(dfs), 2)]
vertex = []
for number in dfs:
    if number not in vertex:
        vertex.append(number)

# 인접행렬 만들기
adjacency = [[0] * len(vertex) for _ in range(len(vertex))]
for i in vertex:
    for j in vertex:
        for edge in edges:
            if [i, j] == edge:
                adjacency[i-1][j-1] = 1
                adjacency[j-1][i-1] = 1

# DFS
visited = []
stack = ['start']
v = vertex[0]

while stack:
    if v not in visited:
        visited.append(v)

    y = 0
    while y < len(adjacency):
        if adjacency[v - 1][y] == 1 and y + 1 not in visited:
            stack.append(v)
            v = y + 1
            break
        else:
            y += 1

    else:
        n = stack.pop()
        v = n

print('-'.join(map(str, visited)))
