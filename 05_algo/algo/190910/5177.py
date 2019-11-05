import sys
sys.stdin = open('5177.txt', 'r')

def func(t, n):
    if not tree[t]:
        tree[t] = n
    elif not tree[2*t]:
        func(2*t, n)
        # if tree[t] > n:
        #     tree[2*t], tree[t] = tree[t], tree[2*t]
        func3(t)
    elif not tree[2*t+1]:
        func(2*t+1, n)
        # if tree[t] > n:
        #     tree[2*t+1], tree[t] = tree[t], tree[2*t+1]
        func3(t)
    else:
        t += 1
        func(t, n)

def func2(x):
    global ans
    if x:
        ans += tree[x//2]
        n = x//2
        func2(n)


def func3(t):
    if t > 0 and tree[t]:
        if tree[t] < tree[t//2]:
            tree[t//2], tree[t] = tree[t], tree[t//2]
            func3(t//2)
        if tree[t] < tree[t//2]:
            tree[t//2+1], tree[t] = tree[t], tree[t//2+1]
            func3(t//2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    tree = [0]*(N+1)

    for n in data:
        func(1, n)

    print(tree)
    # for _ in range(N):
    #     func3(1)
    #
    # print(tree)

    ans = 0
    func2(N)

    print('#%d %d' % (tc, ans))
