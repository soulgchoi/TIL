import sys
sys.stdin = open("solvingclub.txt", "r")

for _ in range(int(input())):
    tc, N = input().split()
    datas = input().split()
    result = []

    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # for data in datas:
    #     for i in range(len(numbers)):
    #         if data == numbers[i]:
    #             result.append([data, i])
    #
    # for x in range(0, len(result)-1):
    #     minimum = x
    #     for y in range(x+1, len(result)):
    #         if result[minimum][1] > result[y][1]:
    #             minimum = y
    #     result[x], result[minimum] = result[minimum], result[x]
    #
    # print(tc)
    #
    # s = []
    # for res in result:
    #     s.append(res[0])
    # print(' '.join(s))
    # print(result)

    # print(tc)
    #
    # for number in numbers:
    #     result.append(datas.count(number))
    #
    # res = ''
    # for i in range(len(result)):
    #     for j in range(result[i]):
    #         res += numbers[i] +' '
    #
    # print(res)

    print(tc)
    for number in numbers:
        result.append(datas.count(number))

    for i in range(len(result)):
        print((numbers[i]+' ') * result[i], end=' ')
    print()