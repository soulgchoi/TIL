import sys
sys.stdin = open('16234.txt', 'r')

# for _ in range(5):
N, L, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ans = 0  # 최종 출력될 값
while True:
	cnt = 0  # 연합 수 셀 것임, 돌 때마다 초기화
	visited = [[False]*N for _ in range(N)]  # visited 돌 때마다 초기화
	for r in range(N):
		for c in range(N):
			if not visited[r][c]:  # 시작점은 visited 가 아닐 때
				queue = [(r, c, array[r][c])]  # 좌표랑 인구를 다 넣음
				visited[r][c] = True
				front, rear = -1, 0  # front/rear 써서 bfs 시작
				while front != rear:
					front += 1
					x, y, z = queue[front]  # (x, y) 좌표 / z 는 인구
					for i in range(4):
						nx, ny = x + dx[i], y + dy[i]
						if 0 <= nx < N and 0 <= ny < N:
							if not visited[nx][ny]:
								nz = array[nx][ny]  # nz 는 옆 인구
								if L <= abs(z - nz) <= R:  # 절댓값 비교
									queue += [(nx, ny, nz)]  # 역시 좌표 + 인구로 queue 에 넣음
									visited[nx][ny] = True
									rear += 1
				if len(queue) > 1:  # 한 번 bfs 다 돌았을 때, queue 길이로 연합 체크
					sum_q = sum(q[2] for q in queue)  # q[2] = 인구 저장 위치
					# sum_q = 연합 내 인구 총합
					for p, q, s in queue:
						array[p][q] = sum_q // len(queue)  # 평균값 다시 넣기
					cnt += 1  # 연합 수 카운트
	if cnt > 0:  # 연합이 1개 이상이면 다시 while 문 돌기
		ans += 1
	else:  # 아닐 때 break
		break
print(ans)












