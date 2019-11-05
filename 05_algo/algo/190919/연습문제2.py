def power_set(k, n):
    if k == n:
        t2 = sorted(t)
        if sum(t) == 10 and t2 not in res:
            res.append(t2)
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = arr[i]
            visited[i] = 1
            power_set(k+1, n)
            visited[i] = 0


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
visited = [0]*N
res = []
for j in range(1, N):
    t = [0]*j
    power_set(0, j)

print(res)