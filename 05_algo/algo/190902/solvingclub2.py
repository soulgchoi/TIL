import sys
sys.stdin = open('solvingclub2.txt', 'r')


for tc in range(1, 11):
    V, E = list(map(int, input().split()))
    data = list(map(int, input().split()))
    edge = [[0] * (V + 1) for _ in range(V + 1)]
    count = [0] * (V + 1)

    for i in range(len(data) // 2):
        edge[data[2 * i]][data[2 * i + 1]] = 1
    for j in range(E):
        count[data[2 * j + 1]] += 1

    queue = []
    visited = [0] * (V + 1)
    front = rear = -1
    for a in range(1, V + 1):
        if count[a] == 0:
            queue.append(a)
            rear += 1
            visited[a] = 1
    while front != rear:
        front += 1
        x = queue[front]
        for n in range(V + 1):
            if edge[x][n] == 1:
                count[n] -= 1
            if edge[x][n] == 1 and visited[n] == 0 and count[n] == 0:
                queue.append(n)
                rear += 1
                visited[n] = 1
                count[n] -= 1

    print('#%d %s' % (tc, ' '.join(map(str, queue))))
