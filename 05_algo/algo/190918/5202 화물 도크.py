import sys
sys.stdin = open('5202.txt', 'r')


def func():
    global se
    if len(se) == 0:
        return
    else:
        s = se.pop(0)
        if res[-1][1] <= s[0] and s not in res:
            res.append(s)
        func()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    se = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-1):
        mi = i
        for j in range(i+1, N):
            if se[mi][1] > se[j][1]:
                mi = j
        se[i], se[mi] = se[mi], se[i]

    res = [se[0]]

    func()

    print('#%d %d' % (tc, len(res)))

