import sys
sys.stdin = open('5102.txt', 'r')


def node_path(queue, G):
    global path
    while queue:
        x = queue.pop(0)
        for n in node:
            if n[0] == x[1]:
                queue.append(n)
                path[n[0]] = path[x[0]] + 1
                if n[1] == G:
                    return path[n[0]]
            if n[1] == x[1]:
                queue.append(n)
                path[n[1]] = path[x[1]] + 1
                if n[1] == G:
                    return path[n[1]]



T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    nodes = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))

    path = [0]*V

    queue = []
    for i in range(E):
        if node[i][0] == S:
            queue.append(node[i])
            path[node[i][0]] = 1

    matrix = [[0] * (V+1) for _ in range(V+1)]
    for i in range(V + 1):
        for j in range(V + 1):
            for node in nodes:
                if [i, j] == node:
                    matrix[i][j] = 1
                    matrix[j][i] = 1

    visited = [[0] * (V+1) for _ in range(V+1)]

    queue = []
    for e in range(E):
        if nodes[e][0] == S:
            queue.append(node[e])

    while queue:
        x, y = queue.pop(0)
        visited[x][y] = 1
        visited[y][x] = 1
        if

    # stack = ['start']
    # s = S
    # while stack:
    #     if s == G:
    #         break
    #     if s not in visited:
    #         visited.append(s)
    #     x = 0
    #     while x < V:
    #         if matrix[s - 1][x] == 1 and x + 1 not in visited:
    #             stack.append(s)
    #             s = x + 1
    #             break
    #         else:
    #             x += 1
    #     else:
    #         s = stack.pop()
    #
    #
    # print(S, G)
    # print('#%d %d' % (tc, node_path(queue, G)))
