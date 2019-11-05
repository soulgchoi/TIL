# 반복문으로 부분함수 만들기
# def powerset_1():
#     bit = [0, 0, 0]
#     for i in range(2):
#         bit[0] = i
#         for j in range(2):
#             bit[1] = j
#             for k in range(2):
#                 bit[2] = k
#                 print(bit)
#
# powerset_1()

def func(k, n, j):
    if k == n:
        print(' '.join(t))
    else:
        for i in range(j, N):
            if visited[i]:
                continue
            t[k] = str(arr[i])
            visited[i] = 1
            func(k+1, n, i)
            visited[i] = 0


N, M = map(int, input().split())
arr = [a for a in range(1, N+1)]
visited = [0]*N

t = [0]*M
res = []
func(0, M, 0)