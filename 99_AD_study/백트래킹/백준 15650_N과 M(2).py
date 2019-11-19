input1 = '3 1'
input2 = '4 2'

def func(k, n):
	if k == n:
		t2 = sorted(t)
		if t2 not in res:
			res.append(t2)
			print(' '.join(t2))
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
res = []
func(0, M)
