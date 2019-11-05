import sys
from itertools import permutations
# import math
sys.stdin = open('17135.txt', 'r')


# def archer(M):
#     arc = [0] * M
#     for a in range(M):
#         for b in range(a+1, M):
#             for c in range(b+1, M):
#                 arc[a] = 2
#                 arc[b] = 2
#                 arc[c] = 2
#                 castle.insert(N, arc)
#                 return
# def a_func(x):
#     arc = combinations(x, 5)


def arrow(N, D, count):
    for i in range(M):
        if castle[-1][i] == 2:
            for x in range(N):
                for y in range(M):
                    if abs(x+y - N+i) <= D:
                        if castle[x][y] == 1:
                            count += 1
                            return

def pull(N):
    castle.pop(N-1)
    castle.insert(0, [0] * N)


T = 6
for tc in range(1, T+1):
    N, M, D = list(map(int, input().split()))
    castle = [list(map(int, input().split())) for _ in range(N)] + [[0] * M]
    count = 0
    archer = [2, 2, 2]
    archer += [0]*(M-3)
    arc = list(set(list(permutations(archer, 5))))

    while arc:
        count = 0
        castle[N] = list(arc.pop(0))
        while sum(sum(castle[:N], [])) != 0:
            arrow(N, D, count)
            pull(N)

        print(count)