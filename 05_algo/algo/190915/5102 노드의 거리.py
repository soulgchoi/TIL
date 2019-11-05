import sys
sys.stdin = open('5102.txt', 'r')

def func(queue):
	global front, rear
	count = 0
	while front != rear:
		front += 1
		x = queue[front]
		count += 1
		for i in range(V + 1):
			if matrix[x][i] == 1:
				queue.append(i)
				rear += 1
				matrix[x][i] = 0
				if i == G:
					return count
	return 0


T = int(input())
for tc in range(1, T+1):
	V, E = map(int, input().split())
	node = [tuple(map(int, input().split())) for _ in range(E)]
	S, G = map(int, input().split())  # 출발, 도착지점

	matrix = [[0]*(V+1) for _ in range(V+1)]

	for n in node:
		matrix[n[0]][n[1]] = 1
		matrix[n[1]][n[0]] = 1

	front = rear = -1
	queue = []

	for m in range(len(matrix)):
		if matrix[S][m] == 1:
			queue.append(m)
			rear += 1
			matrix[S][m] = 0

	ans = func(queue)

	print('#%d %d' % (tc, ans))