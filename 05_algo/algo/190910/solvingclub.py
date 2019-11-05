import sys
sys.stdin = open('solvingclub.txt', 'r')

def func(T):
    if T:
        func(tree[T][0])
        func(tree[T][1])
        cal2.append(cal[T])


for tc in range(1, 11):
    N = int(input())
    tree = [[0, 0] for _ in range(N+1)]
    cal = [0] * (N+1)
    for _ in range(N):
        n = list(input().split())
        if len(n) == 2:
            cal[int(n[0])] = int(n[1])
        elif len(n) == 4:
            cal[int(n[0])] = n[1]
            tree[int(n[0])][0] = int(n[2])
            tree[int(n[0])][1] = int(n[3])
    cal2 = []
    func(1)

    cal3 = []
    while cal2:
        c = cal2.pop(0)
        if type(c) == int:
            cal3.append(c)
        else:
            c2 = cal3.pop()
            c1 = cal3.pop()
            if c == '+':
                cal3.append(c1+c2)
            elif c == '-':
                cal3.append(c1-c2)
            elif c == '*':
                cal3.append(c1*c2)
            elif c == '/':
                cal3.append(c1/c2)

    print('#%d %d' % (tc, round(cal3[0])))