def func(k, n):
    if k == n:
        print(' '.join(t))
    else:
        for i in range(N):
            t[k] = str(arr[i])
            func(k+1, n)


N, M = map(int, input().split())
arr = [a for a in range(1, N+1)]

t = [0]*M
func(0, M)