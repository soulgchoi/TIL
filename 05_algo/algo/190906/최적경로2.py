import sys
sys.stdin = open('최적경로.txt', 'r')


# def permute(arr):
#     global ans, m
#     result = arr[:]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr):
#         home(arr, result)
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             result = arr[:]
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return


# def home(arr, result):
#     global ans
#     result = [0] + result + [N + 1]
#
#     path = 0
#     x = 0
#     for s in range(N + 1):
#         if ans > path:
#             path += n[result[s]][result[s + 1]]
#         else:
#             break
#
#     if ans > path:
#         ans = path


def perm(arr, k, N):
    if k == N:
        home(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, k+1, N)
            arr[k], arr[i] = arr[i], arr[k]

def home(arr):
    global ans
    arr = [0] + arr + [N + 1]

    path = 0
    x = 0
    for s in range(N + 1):
        if ans > path:
            path += n[arr[s]][arr[s+1]]
        else:
            break

    if ans > path:
        ans = path


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    m = [data[i:i + 2] for i in range(0, (N + 2) * 2, 2)]
    m2 = m.pop(1)
    m.append(m2)
    n = [[0] * (N + 2) for _ in range(N + 2)]

    customer = [n for n in range(1, N + 1)]
    print(customer)
    ans = 9999

    for i in range(N+2):
        for j in range(N+2):
            n[i][j] = abs(m[i][0]-m[j][0]) + abs(m[i][1]-m[j][1])

    # permute(customer)
    perm(customer, 0, N)
    print('#%d %d' % (tc, ans))