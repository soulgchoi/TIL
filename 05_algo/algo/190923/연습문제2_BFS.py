data = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 8 9 8 10 10 11 9 11 11 12 13 14 14 15'
N = list(map(int, data.split()))
edges = [[] for _ in range(16)]
for n in range(0, len(N)-1, 2):
    edges[N[n]].append(N[n+1])

queue = []
visited = [0]*16
front = rear = -1
for v in range(1, 16):
    queue.append(v)
    rear += 1
    while front != rear:
        front += 1
        t = queue[front]
        if not visited[t]:
            visited[t] = 1
            print(t, end=' ')
            for e in edges[t]:
                    queue.append(e)
                    rear += 1
print()
print(front, rear)
