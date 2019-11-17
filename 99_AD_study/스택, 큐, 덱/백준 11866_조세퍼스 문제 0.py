# N, K = 7, 3
N, K = map(int, input().split())
temp = [0]*N
n = list(range(1, N+1))
print('<', end='')
i = 0
res = []
while n != temp:
	cnt = 0
	while cnt < K:
		if i >= N:
			i -= N
		if n[i] != 0:
			cnt += 1
			i += 1
		else:
			i += 1
	i -= 1
	if cnt == K:
		res += [n[i]]
		n[i] = 0
		i += 1
res2 = ', '.join(list(map(str, res)))
print(res2, end='')
print('>')

