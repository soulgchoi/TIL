import sys
sys.stdin = open('5174.txt', 'r')

def func(T):
    global cnt
    if T:
        cnt += 1
        func(tree[T][0])
        func(tree[T][1])



T = int(input())
for tc in range(1, T+1):
    E, N = list(map(int, input().split()))
    node = list(map(int, input().split()))
    tree = [[0]*2 for _ in range(E+2)]

    for i in range(E):
        parent, child = node[i*2], node[i*2 + 1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    print(tree)

    cnt = 0
    func(N)

    print('#%d %d' % (tc, cnt))