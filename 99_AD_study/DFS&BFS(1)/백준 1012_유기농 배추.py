import sys
sys.stdin = open('1012.txt', 'r')

T = int(input())
for _ in range(T):
	M, N, K = map(int, input().split())
	baechu = []  # 배추 위치 저장
	bae = [[0]*N for _ in range(M)]  # 배추밭
	chu = [[0]*N for _ in range(M)]  # 비교할 리스트
	for _ in range(K):  # 배추밭에 배추
		b, c = map(int, input().split())
		bae[b][c] = 1
		baechu += [(b, c)]

	ans = 0
	dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

	while bae != chu:  # visited 안쓰고 배추밭 다 0일 때까지
		for bc in baechu:  # 저장한 배추 위치로 찾기
			b2, c2 = bc
			if bae[b2][c2] == 1:
				ans += 1  # 시작점에서만 count
				queue = [(b2, c2)]  # 아래부터 bfs
				front, rear = -1, 0
				while front != rear:
					front += 1
					x, y = queue[front]
					bae[x][y] = 0
					for i in range(4):
						nx, ny = x + dx[i], y + dy[i]
						if 0 <= nx < M and 0 <= ny < N:
							if bae[nx][ny] == 1:
								bae[nx][ny] = 0
								queue += [(nx, ny)]
								rear += 1
	print(ans)


