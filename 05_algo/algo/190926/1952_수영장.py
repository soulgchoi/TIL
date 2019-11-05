import sys
sys.stdin = open('1952.txt', 'r')


def func(m, val):
    global charge, swim, min_c

    if m > 11:
        if val < min_c:
            min_c = val
            return

    if swim[m] == 0:
        func(m+1, val)

    if swim[m]:
        if val + charge[0]*swim[m] < min_c:
            func(m+1, val + charge[0]*swim[m])
        if val + charge[1] < min_c:
            func(m+1, val + charge[1])
        if val + charge[2] < min_c:
            func(m+3, val + charge[2])


T = int(input())
for tc in range(1, T+1):
    charge = list(map(int, input().split()))
    swim = list(map(int, input().split()))

    min_c = charge[3]

    func(0, 0)

    print('#%d %d' % (tc, min_c))
