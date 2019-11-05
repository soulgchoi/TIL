import sys
sys.stdin = open('5176.txt', 'r')

# def func(N):
#     n = 0
#     while n != N:
#         tree[n+1][0] = n+1
#         n += 1
        # tree[n][1] = n+1

#
#
# def func(T, a):
#     if T in None:
#         if not tree[T][0]:
#             tree[T][1] = a
#         else:
#             tree[T][0] = a
#     else:
#         func(tree[T][0])
#         func(tree[T][1])

def func2(T):
    if T:

    func2(tree[T][0])
    tree[T][0] = T




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0]*2 for _ in range(N+1)]

    for n in range(1, N+1):
        func2(n)

    print(tree)
    # print(tree)