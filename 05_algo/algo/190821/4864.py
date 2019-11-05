import sys
sys.stdin = open("4864.txt", "r")

def BruteForce(key, text):
    i = 0
    j = 0
    t = len(text)
    k = len(key)
    while i < t and j < k:
        if text[i] != key[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == k:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    print('#{} {}'.format(tc, BruteForce(input(), input())))





    # c = 0
    # for i in range(len(text)):
    #     if text[len(key)-1] in key:
    #         key = '0' * skip.index(text[i + len(key)-1]) + key
    #         if key[i] == text[i]:
    #             c += 1
    #         else:
    #             key = ('0'*len(key)) + key
    #             i += len(key)
    #     else:
    #         key = ('0'*len(key)) + key
    #         i += len(key)
    #
    # print(c)
    # i = len(key)-1
    # result = 0
    # while result < len(key) or i < len(text):
    #     if skip[0] != text[i]:
    #         if text[i] in skip:
    #             number = skip.index(text[i])
    #             i += number
    #         else:
    #             i += len(key)
    #     else:
    #         for x, y in zip(range(i, i - len(key), -1), skip):
    #             if y == text[x]:
    #                 result += 1
    #             else:
    #                 result = 0
    #                 i = x
    #                 break
    # print(result)

