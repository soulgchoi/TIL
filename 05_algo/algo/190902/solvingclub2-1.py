import sys
sys.stdin = open('solvingclub2.txt', 'r')


# def BFS(G, V, n):
#     global result
#     visited = [0] * n
#     queue = []
#     for v in range(1, len(V)):
#         if V[v] == 0:
#             queue.append(v)
#             while queue:
#                 t = queue.pop(0)
#                 if not visited[t] and V[t] == 0:
#                     visited[t] = True
#                     result.append(t)
#                 for j in range(len(G[t])):
#                     if G[t][j] == 1 and not visited[j]:
#                         queue.append(j)
#                         V[]


for tc in range(1, 11):
    V, E = list(map(int, input().split()))
    data = list(map(int, input().split()))
    edge = [[0]*(V+1) for _ in range(V+1)]
    # edge2 = [[0] * (V + 1) for _ in range(V + 1)]
    count = [0] * (V+1)

    for i in range(len(data)//2):
        edge[data[2*i]][data[2*i+1]] = 1
        # edge2[data[2*i+1]][data[2*i]] = 1

    for j in range(E):
        count[data[2*j+1]] += 1

    queue = []
    visited = [0] * (V+1)
    front = rear = -1
    for a in range(1, V+1):
        if count[a] == 0:
            queue.append(a)
            rear += 1
            visited[a] = 1
    while front != rear:
        front += 1
        x = queue[front]
        for n in range(V+1):
            if edge[x][n] == 1:
                count[n] -= 1
            if edge[x][n] == 1 and visited[n] == 0 and count[n] == 0:
                queue.append(n)
                rear += 1
                visited[n] = 1
                count[n] -= 1

    # stack = []
    # while len(visited) < len(set(data)):
    #     for i in range(1, V+1):
    #         if sum(edge2[i]) == 0:
    #             stack.append(i)
    #             visited.append(i)
    #         else:

    print('#%d %s' % (tc, ' '.join(map(str, queue))))
    # print(visited)

    # result = []
    # BFS(edge1, count, V+1)
    # print(result)
    # print('#%d %s' % (tc, ' '.join(map(str, result[1:]))))
