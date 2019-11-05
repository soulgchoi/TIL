def func(t):
    if t > N:
        return 0
    else:
        if tree[t]:
            return tree[t]
        else:
            a = func(2 * t)
            b = func(2 * t + 1)
            tree[t] = a + b
        return tree[t]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = list(map(int, input().split()))
    tree = [0] * (N + 1)
    for _ in range(M):
        x, y = list(map(int, input().split()))
        tree[x] = y

    func(1)

    print('#%d %d' % (tc, tree[L]))