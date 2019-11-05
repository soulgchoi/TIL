import sys
sys.stdin = open('5102.txt', 'r')

def BFS(queue):
	global count
	if S == G:
		return
	while queue:
		count += 1
		for i in range(len(queue)):
			x = queue.pop(0)
			for j in matrix[x]:
				if visited[j] == 1:
					continue
				visited[j] = 1
				queue.append(j)
			if G in queue:
				return
	count = 0


T = int(input())
for tc in range(1, T+1):
	V, E = list(map(int, input().split()))
	node = [list(map(int, input().split())) for _ in range(E)]
	S, G = list(map(int, input().split()))

	matrix = [[]*(V+1) for _ in range(V+1)]

	for n in node:
		matrix[n[0]].append(n[1])
		matrix[n[1]].append(n[0])

	visited = [0]*(V+1)

	queue = [S]
	visited[S] = 1
	count = 0

	BFS(queue)

	print('#%d %d' % (tc, count))