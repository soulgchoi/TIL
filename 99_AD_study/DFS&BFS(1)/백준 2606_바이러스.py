import sys
sys.stdin = open('2606.txt', 'r')

C, N = int(input()), int(input())
data = [list(map(int, input().split())) for _ in range(N)]
coms = [[] for _ in range(C+1)]
for d in data:
	coms[d[0]] += [d[1]]
	coms[d[1]] += [d[0]]
visited = [True] * (C+1)
queue = [1]
front, rear = -1, 0
while front != rear:
	front += 1
	v = queue[front]
	if visited[v]:
		visited[v] = False
		for w in coms[v]:
			queue += [w]
			rear += 1
print(len(list(set(queue)))-1)
