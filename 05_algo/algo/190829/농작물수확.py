import sys
sys.stdin = open('농작물수확.txt', 'r')

def long(r, c):
	global harvest
	dx = [-1, 1]
	dy = [1, 1]
	x, y = r, c
	for i in range(N // 2 + 1):
		for j in range(N // 2 +1):
			if 0 <= x < N and 0 <= y < N:
				harvest += farm[x][y]
				x = x + dx[0]
				y = y + dy[0]
		x = r + i + dx[1]
		y = c + i + dy[1]

def short(r, c):
	global harvest
	dx = [-1, 1]
	dy = [1, 1]
	x, y = r, c
	for i in range(N // 2):
		for j in range(N // 2):
			if 0 <= x < N and 0 <= y < N:
				harvest += farm[x][y]
				x = x + dx[0]
				y = y + dy[0]
		x = r + i + dx[1]
		y = c + i + dy[1]

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	farm = [list(map(int, input())) for _ in range(N)]
	harvest = 0
	r1, c1 = N//2, 0
	r2, c2 = r1, c1+1

	long(r1, c1)
	short(r2, c2)

	print('#%d %d' % (tc, harvest))