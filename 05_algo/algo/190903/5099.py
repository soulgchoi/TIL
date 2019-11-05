import sys
sys.stdin = open('5099.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     data = list(map(int, input().split()))
#     pizza = []
#     result = []
#     for idx, val in enumerate(data):
#         pizza.append((idx+1, val))
#     fire = [pizza.pop(0)]
#     while fire:
#         if len(fire) < N and pizza:
#             if len(pizza) > 0:
#                 fire.append(pizza.pop(0))
#         else:
#             for i in range(len(fire)):
#                 p, c = fire[i]
#                 if c // 2 != 0:
#                     fire[i] = (p, c // 2)
#                 else:
#                     result.append(p)
#                     if len(pizza) > 0:
#                         fire[i] = pizza.pop(0)
#                     else:
#                         fire.pop(i)
#                         break
#
#
#     print('#%d %s' % (tc, result[-1]))


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    data = list(map(int, input().split()))
    pizza = []
    for i in range(M):
        pizza.append([i+1, data[i]])

    fire = []
    for i in range(N):
        fire.append(pizza.pop(0))

    p = 0
    while True:
        fire[p][1] //= 2
        if fire[p][1] == 0:
            res = fire[p][0]
            if len(pizza) > 0:
                fire[p] = pizza.pop(0)
        p = (p+1) % N
        if sum(fire[f][1] for f in range(N)) == 0:
            break
    # sum_c = sum(fire[f][1] for f in range(N))
    # print(sum_c)
    print('#%d %d' % (tc, res))

"""
///////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
    #
    # for tc in range(int(input())):
    #     N, M = map(int, input().split())  # N = 화덕의 크기 M = 피자의 갯수
    #     pizza = list(map(int, input().split()))
    #     for i in range(M):
    #         pizza[i] = [i + 1, pizza[i]]  # pizza[i][0]은 피자 순서 pizza[i][1]은 치즈 양
    #     num = N
    #     count = 0
    #     fire = [0] * N
    #     for i in range(N):
    #         if i > M:
    #             fire[i] = [999]
    #         fire[i] = pizza[i]
    #
    #     while count != M - 1:
    #         for i in range(len(fire)):
    #             if fire[i][1] != 0:
    #                 fire[i][1] = int(fire[i][1] // 2)  # 모든 것의 피자를 반으로 줄인다.
    #
    #                 if fire[i][1] == 0:
    #                     count += 1
    #                     if num < M:
    #                         fire[i] = pizza[num]
    #                         num += 1
    #
    #             if count == M - 1:
    #                 break
    #     for i in range(len(fire)):
    #         if fire[i][1] != 0:
    #             a = fire[i][0]
    #     print('#%d %d' % (tc + 1, a))