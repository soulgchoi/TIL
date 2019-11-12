import sys
sys.stdin = open('2383.txt', 'r')


def powersetlist(li):
    r = [[]]

    for l in li:
        temp = [x+[l] for x in r]
        r += temp

    return r


def lunch(li, k, time):
    st = []
    while li:
        time += 1
        for t in range(len(li)):
            if li[t] > 0:
                li[t] -= 1
            else:
                li[t] = -1

        while (0 in li or -1 in li) and len(st) < 3:
            temp = li.pop(0)
            if temp == 0:
                st += [time]
            elif temp == -1:
                st = [time-1]

        for _ in st:
            if time-st[0] >= k:
                st.pop(0)

    while st:
        for _ in st:
            if time-st[0] >= k:
                st.pop(0)
        time += 1

    return time


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    P = []
    S = []

    for a in range(N):
        for b in range(N):
            if data[a][b] != 0:
                if data[a][b] == 1:
                    P += [(a, b)]
                else:
                    S += [(a, b, data[a][b])]

    P_powerset = powersetlist(P)

    min_time = 9999999

    for pset in P_powerset:
        notP = [p for p in P if p not in pset]

        sr1, sc1, k1 = S[0]
        sr2, sc2, k2 = S[1]

        time = 0

        time1 = []
        for pr1, pc1 in pset:
            time1 += [abs(pr1-sr1)+abs(pc1-sc1)]
        time1.sort()

        time2 = []
        for pr2, pc2 in notP:
            time2 += [abs(pr2-sr2)+abs(pc2-sc2)]
        time2.sort()

        t1 = lunch(time1, k1, 0)
        t2 = lunch(time2, k2, 0)

        if t1 < t2:
            time = t2
        else:
            time = t1

        if time < min_time:
            min_time = time

    print('#%d %d' % (tc, min_time))

