import sys
sys.stdin = open('2178.txt', 'r')

# def dfs(r, c, count, stack, v):
# 	global ans, N, M, dx, dy, maze
# 	if (r, c) == ((N-1), (M-1)):
# 		if count < ans:
# 			ans = count
# 	else:
# 		x, y = stack.pop(0)
# 		v[x][y] = True
# 		for i in range(4):
# 			nx, ny = x + dx[i], y + dy[i]
# 			if 0 <= nx < N and 0 <= ny < M:
# 				if maze[nx][ny] == 1 and not v[nx][ny]:
# 					stack += [(nx, ny)]
# 					v[nx][ny] = True
# 					dfs(nx, ny, count+1, stack, v)


for _ in range(4):
	N, M = map(int, input().split())
	maze = [list(map(int, input())) for _ in range(N)]
	dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
	ans = 0
	visited = [[0]*M for _ in range(N)]
	visited[0][0] = 1
	queue = [(0, 0)]
	front, rear = -1, 0
	flag = True
	while front != rear:
		front += 1
		x, y = queue[front]
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < N and 0 <= ny < M:
				if maze[nx][ny] == 1 and not visited[nx][ny]:
					if (nx, ny) == ((N-1), (M-1)):
						ans = visited[x][y] + 1
						flag = False
						break
					else:
						queue += [(nx, ny)]
						rear += 1
						visited[nx][ny] = visited[x][y] + 1
		if not flag:
			break

	print(ans)