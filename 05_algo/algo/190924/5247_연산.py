import sys
sys.stdin = open('5247.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     queue = [N]
#     ans = 0
#     found, check = False, [True]*((10**6)+1)
#     func = [lambda x: x + 1, lambda x: x - 1, lambda x: x * 2, lambda x: x - 10]
#
#     while queue:
#         ans += 1
#         field = {}
#         for val in queue:
#             for f in func:
#                 val2 = f(val)
#
#                 if val2 > 10**6 or val2 < 1:
#                     continue
#
#                 elif val2 == M:
#                     found = True
#                     break
#
#                 else:
#                     if field.get(val2) is None and check[val2]:
#                         field[val2] = True
#                         check[val2] = False
#         if found:
#             break
#         else:
#             queue = list(field.keys())
#
#     print('#%d %d' % (tc, ans))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    queue = [N]
    ans = 0
    front, rear = -1, 0

    found = False
    check = [True] * ((10**6)+1)
    while front != rear:
        ans += 1
        for _ in range(front, rear):
            front += 1
            val = queue[front]
            for i in range(4):
                if i == 0:
                    temp = val + 1
                elif i == 1:
                    temp = val - 1
                elif i == 2:
                    temp = val * 2
                elif i == 3:
                    temp = val - 10

                if temp > 10**6 or temp < 1:
                    continue
                elif temp == M:
                    found = True
                    break
                else:
                    if check[temp]:
                        check[temp] = False
                        queue.append(temp)
                        rear += 1
        if found:
            break

    print('#%d %d' % (tc, ans))