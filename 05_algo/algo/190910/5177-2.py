import sys
sys.stdin = open('5177.txt', 'r')


def func(t, n):
    if not tree[t]:
        tree[t] = n
    elif not tree[2*t]:
        # func(2*t, n)
        tree[2*t] = n
        func3(2*t)
    elif not tree[2*t+1]:
        # func(2*t+1, n)
        tree[2*t+1] = n
        func3(2*t+1)
    else:
        # t += 1
        func(t+1, n)

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
        else:
            return   # 언제 리턴하는지 확인하기
        # if tree[t] < tree[t//2]:
        #     tree[t//2+1], tree[t] = tree[t], tree[t//2+1]
        #     func3(t//2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    tree = [0]*(N+1)

    for n in data:
        func(1, n)

    print(tree)

    ans = 0
    func2(N)

    print('#%d %d' % (tc, ans))