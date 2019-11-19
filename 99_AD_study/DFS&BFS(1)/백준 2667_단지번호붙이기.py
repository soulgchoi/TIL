import sys
sys.stdin = open('2667.txt', 'r')

def dfs(a, b):
	global dx, dy, data, count
	stack = [(a, b)]
	while stack:
		x, y = stack.pop(0)
		for i in range(4):
			nx, ny = x+dx[i], y+dy[i]
			if 0 <= nx < N and 0 <= ny < N:
				if data[nx][ny] == 1:
					data[nx][ny] = 0
					count += 1
					dfs(nx, ny)

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
home = []
while data != check:
	for r in range(N):
		for c in range(N):
			if data[r][c] == 1:
				data[r][c] = 0
				count = 1
				dfs(r, c)
				home += [count]
print(len(home))
for h in sorted(home):
	print(h)