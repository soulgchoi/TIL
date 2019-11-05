import sys
import itertools
sys.stdin = open('최적경로.txt', 'r')

#
# def construct_candidates(a, k, b, c):
#     in_perm = [False] * 5
#
#     for i in range(k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for i in range(b):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates
# def cal_path():
#
#
#
#
# def perm(a, k, b):
#     global ans
#     c = [0] * 5
#     if k == b:
#         c_list = []
#         for i in range(1, k+1):
#             c_list.append(a[i])
#         return c_list
#
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, b, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             perm(a, k, b)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     data = list(map(int, input().split()))
#
#     m = [data[i:i+2] for i in range(0, (N+2)*2, 2)]
#     m2 = m.pop(1)
#     m.append(m2)
#     # n = [[0]*(N+2) for _ in range(N+2)]
#     ans = 9999

    # for i in range(N+2):
    #     for j in range(N+2):
    #         n[i][j] = abs(m[i][0]-m[j][0]) + abs(m[i][1]-m[j][1])
N = 5
cus = [1, 2, 3, 4, 5]
permute = list(map(list, itertools.permutations(cus, N)))
# itertools.combinations()
print(permute)
    #
    # for p in permute:
    #     path = 0
    #     x = 0
    #     while p:
    #         if ans > path:
    #             path += abs(m[x][0]-m[p[0]][0]) + abs(m[x][1]-m[p[0]][1])
    #             x = p[0]
    #             p.pop(0)
    #         else:
    #             break
    #     path += abs(m[x][0]-m[N+1][0]) + abs(m[x][1]-m[N+1][1])
    #     if ans > path:
    #         ans = path
    # print('#%d %d' % (tc, ans))

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result = arr[:]
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

# def perm(k, r):




# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     data = list(map(int, input().split()))
#
#     m = [data[i:i+2] for i in range(0, (N+2)*2, 2)]
#     m2 = m.pop(1)
#     m.append(m2)
#     n = [[0]*(N+2) for _ in range(N+2)]

    # for i in range(N+2):
    #     for j in range(N+2):
    #         n[i][j] = abs(m[i][0]-m[j][0]) + abs(m[i][1]-m[j][1])
#
#     cust = [n for n in range(1, N+1)]
#     ans = 9999
#     c_list = permute(cust)
#     for c in c_list:
#         c = [0] + c + [N+1]
#         path = 0
#         for s in range(N+1):
#             if ans > path:
#                 path += abs(m[c[s]][0] - m[c[s+1]][0]) + abs(m[c[s]][1] - m[c[s+1]][1])
#                 # path += n[c[s]][c[s+1]]
#             else:
#                 break
#         if ans > path:
#             ans = path
#
#     print('#%d %d' % (tc, ans))

    # v = [[0] * (N + 2) for _ in range(N + 2)]
    # queue = [(0, 0)]
    #
    # path = [[0] * (N + 2) for _ in range(N + 2)]
    # o_x = 0
    # while queue:
    #     x, y = queue.pop(0)
    #
    #     for s in range(N + 1):
    #         # v[x][0] = 1
    #         if n[x][s] != 0 and v[x][s] == 0:
    #             queue.append((s, x))
    #             v[x][s] = v[x][y] + 1
    #             v[s][x] = v[y][x] + 1
    #             path[x][s] = n[s][x] + path[x][y]
    #             path[s][x] = n[x][s] + path[y][x]
    #             o_x, o_y = s, x
                # for xx in range(N+2):
                #     v[xx][x] = 1
                # path[o_x][s] += n[x][s]
                # path[s][o_x] += n[s][x]

                    # path += n[x][y]

        # res = path
        # path = 0


    # print(m)
    # print(n)
    #
    # v = [[0]*(N+2) for _ in range(N+2)]
    # stack = [(0, 0)]
    # res = 9999
    # path = 0
    # x, y = 0, 0
    # # x, y = stack.pop()
    # while stack:
    #     for y in range(N+2):
    #         # v[x][0] = 1
    #         if n[x][y] != 0 and v[x][y] == 0:
    #             stack.append((x, y))
    #             v[x][y] = 1
    #             v[y][x] = 1
    #             # for xx in range(N+2):
    #             #     v[xx][x] = 1
    #             if res < path:
    #                 pass
    #             else:
    #                 path += n[x][y]
    #             if stack:
    #                 y, x = stack.pop()
    #     res = path
    #     path = 0
    #     x, x = stack.pop()
    # print(res)
    # # for x2 in range(N+1):
    # #     if n[x][x2] != 0 and v[x][x2] == 0:
    # #         stack.append((x, x2))
    # #         v[x][x2] = 1
    # #         v[x2][x] = 1
    # #         path += n[x][x2]
    # #         x = x2
    # #         break
    # print(path)
    # print(res)
    # # print(x, y)
