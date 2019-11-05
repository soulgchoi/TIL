import sys
sys.stdin = open('5209.txt', 'r')


# def perm(k, val):
#     global ans
#     if k == N:
#         if val < ans:
#             ans = val
#     else:
#         for i in range(k, N):
#             p[k], p[i] = p[i], p[k]
#             if val+arr[k][p[k]] < ans:
#                 perm(k+1, val+arr[k][p[k]])
#             p[k], p[i] = p[i], p[k]

def perm(k, val):
    global ans
    if k == N:
        if val < ans:
            ans = val
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = arr[k][i]
            visited[i] = 1
            if val+arr[k][i] < ans:
                perm(k+1, val+arr[k][i])
            visited[i] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 999
    visited = [0]*N

    # print(arr)
    p = list(range(N))
    t = [0]*N

    perm(0, 0)
    print('#%d %d' % (tc, ans))

