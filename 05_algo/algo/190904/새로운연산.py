import sys
sys.stdin = open('새로운연산.txt', 'r')

# arr = [[0 for _ in range(101)] for _ in range(101)]
# arr[0][1] = 1
# for a1 in range(1, 101):
#     arr[1][a1] = arr[1][a1-1] + (arr[1][a1-1]-arr[1][a1-2]+1)
#
# for i in range(2, 101):
#     arr[i][1] = arr[i-1][1] + (arr[i-1][1] - arr[i-2][1] + 1)
#     for j in range(2, 101):
#         arr[i][j] = arr[i][j-1] + (arr[i][j-1]-arr[i-1][j-1]+2)
# print(arr)


def func(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return n + func(n-1)


def func2(x):
    n = 0
    while func(n) < x:
        n += 1
    return n


T = int(input())
for tc in range(1, T+1):
    p, q = list(map(int, input().split()))

    pn = func2(p)
    p1 = pn - (func(pn) - p)
    p2 = pn - p1 + 1

    qn = func2(q)
    q1 = qn - (func(qn) - q)
    q2 = qn - q1 + 1

    x, y = p1+q1, p2+q2
    xy = x + y - 1
    print('#%d %d' % (tc, func(xy)-y+1))