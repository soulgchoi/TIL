def func(r, N):
	global ans, col, left, right
	if r == N:
		ans += 1
	for c in range(N):
		if col[c] and left[r - c + N - 1] and right[r + c]:
			col[c] = 0
			left[r - c + N - 1] = 0
			right[r + c] = 0
			func(r + 1, N)
			col[c] = 1
			left[r - c + N - 1] = 1
			right[r + c] = 1


N = int(input())
col = [1] * N
left = [1] * (2 * N - 1)
right = [1] * (2 * N - 1)
ans = 0

func(0, N)
print(ans)