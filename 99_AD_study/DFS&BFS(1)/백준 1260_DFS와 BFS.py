import sys
sys.stdin = open('1260.txt', 'r')

def dfs(v):
	stack = [v]
	while stack:
		v = stack.pop()
		if dfsv[v-1]:
			dfsv[v-1] = False
			print(v, end=' ')
			for w in array[v-1]:
				if dfsv[w-1]:
					dfs(w)

def bfs(v):
	global queue
	front, rear = -1, 0
	while front != rear:
		front += 1
		v = queue[front]
		if bfsv[v-1]:
			print(v, end=' ')
			bfsv[v-1] = False
			for w in array[v-1]:
				queue.append(w)
				rear += 1

N, M, V = map(int, input().split())  # input 받기
data = [list(map(int, input().split())) for _ in range(M)]  # input 받기
array = [[] for _ in range(N)]  # 노드 저장할 리스트
for d in data:
	array[d[0]-1] += [d[1]]
	array[d[1]-1] += [d[0]]
for a in array:  # 작은 숫자부터 dfs/bfs 돌아야 하므로 정렬함
	a.sort()
dfsv = [True] * N  # visited 각각 체크
bfsv = [True] * N
start = V  # 시작점
dfs(start)
print()
queue = [start]
bfs(start)
print()
