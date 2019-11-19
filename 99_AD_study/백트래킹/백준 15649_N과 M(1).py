input1 = '3 1'
input2 = '4 2'

def func(k, n):
	if k == n:
		print(' '.join(t))
	else:
		for i in range(N):
			if visited[i]:
				continue
			t[k] = str(arr[i])
			visited[i] = 1
			func(k+1, n)
			visited[i] = 0


N, M = map(int, input().split())
arr = [a for a in range(1, N+1)]
visited = [0]*N

t = [0]*M
func(0, M)
