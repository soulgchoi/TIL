import sys
sys.stdin = open('5178.txt', 'r')

# def func(t):
#     if t < N+1:
#         if tree[t]:
#             return tree[t]
#         else:
#             if t == N//2 and t % 2:
#                 tree[t] = func(2*t)
#                 return tree[t]
#             else:
#                 tree[t] = func(2*t) + func(2*t+1)
#                 return tree[t]


def func(t):
    if t == 1:
        return
    elif t % 2:
        tree[t//2] = tree[t] + tree[t-1]
        func(t-2)
    else:
        tree[t//2] = tree[t]
        func(t-1)


T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    tree = [0] * (N+1)
    for _ in range(M):
        x, y = list(map(int, input().split()))
        tree[x] = y

    func(N)
    print('#%d %d' % (tc, tree[L]))