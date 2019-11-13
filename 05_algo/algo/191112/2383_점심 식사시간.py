import sys
sys.stdin = open('2383.txt', 'r')


def lunch(li, k, time):
    lenP = len(li)
    st = [[] for _ in range(lenP)]
    pcnt = lenP
    scnt = 0
    i = 0
    j = 0
    while pcnt > 0:
        time += 1
        while i < lenP:
            if st[i] and time-st[i][0] == k:
                pcnt -= 1
                scnt -= 1
                i += 1
            else:
                break

        for t in range(j, lenP):
            if li[t] > 0:
                li[t] -= 1
            else:
                li[t] = -1

        while j < lenP and scnt < 3:
            if li[j] == 0 or li[j] == -1:
                temp = li[j]
                if temp == 0:
                    st[j] = [time+1]
                elif temp == -1:
                    st[j] = [time]
                j += 1
                scnt += 1
            else:
                break

    return time

# def lunch(li, k, time):
#     st = []
#     pcnt = len(li)
#     while pcnt > 0:
#         time += 1
#
#         while st:
#             if time - st[0] == k:
#                 st.pop(0)
#                 pcnt -= 1
#             else:
#                 break
#
#         for t in range(len(li)):
#             if li[t] > 0:
#                 li[t] -= 1
#             else:
#                 li[t] = -1
#
#         while li and li[0] == (0 or -1) and len(st) < 3:
#             temp = li.pop(0)
#             if temp == 0:
#                 st += [time + 1]
#             elif temp == -1:
#                 st += [time]
#
#     return time


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

    P_powerset = [[]]
    for y in P:
        temp = [x + [y] for x in P_powerset]
        P_powerset += temp

    min_time = 9999999

    for pset in P_powerset:
        notP = [p for p in P if p not in pset]

        sr1, sc1, k1 = S[0]
        sr2, sc2, k2 = S[1]

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

        time = 0
        if t1 < t2:
            time = t2
        else:
            time = t1

        if time < min_time:
            min_time = time

    print('#%d %d' % (tc, min_time))

