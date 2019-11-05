import sys
sys.stdin = open('1244.txt', 'r')

# def perm(k):
#     global cnt, ans
#     if k == cnt:
#         val = int(''.join(map(str, numbers)))
#         if val > ans:
#             ans = val
#         return
#     else:
#         for i in range(len(numbers)-1, k-1, -1):
#             numbers[i], numbers[k] = numbers[k], numbers[i]
#             # if numbers[k] >= numbers[i]:
#             perm(k+1)
#             numbers[i], numbers[k] = numbers[k], numbers[i]
#
#
T = int(input())
for tc in range(1, T+1):
    data, C = input().split()
    C = int(C)

    # ans = int(data)
    numbers = [int(d) for d in data]
    max_number = max(numbers)

    # perm(0)
    # print(ans)
    m_numbers = sorted(numbers, reverse=True)

    # ans = []
    # i = 0
    # temp = numbers[::]
    # while i != C:
    #     if not temp:
    #         break
    #     m_temp = max(temp)
    #     for t in range(len(temp)-1, -1, -1):
    #         if temp[t] == m_temp:
    #             m_idx = t
    #             if m_idx != 0:
    #                 temp[0], temp[m_idx] = temp[m_idx], temp[0]
    #                 ans += [temp.pop(0)]
    #                 i += 1
    #                 break
    #             else:
    #                 ans += [temp.pop(0)]
    #                 break

    i = 0
    cnt = 0
    while cnt != C and i < len(numbers):
        m_temp = m_numbers[i]
        for t in range(i, len(numbers)):
            if numbers[t] == m_temp:
                m_idx = t
                if m_idx != i:
                    numbers[i], numbers[m_idx] = numbers[m_idx], numbers[i]
                    i += 1
                    cnt += 1
                    break
                else:
                    i += 1
                    break

    if (C-cnt) % 2 == 1:
            numbers[-2], numbers[-1] = numbers[-1], numbers[-2]



    #
    # m_cnt = numbers.count(max_number)
    # if m_cnt > 1:
    #     else_cnt = m_cnt-i+1
    #     while m_cnt != 0:
    #


    # ans += temp
    #
    # if i < C:
    #     while i != C:
    #         ans[-2], ans[-1] = ans[-1], ans[-2]
    #         i += 1

    print('#%d %s' % (tc, ''.join(map(str, numbers))))
    # print('#%d %s' % (tc, ''.join(map(str, ans))))

