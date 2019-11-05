import sys
sys.stdin = open('1242.txt', 'r')

def Bbit_input(i):
    output = ''
    for j in range(3, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    return output


code = {0: [0, 0, 0, 1, 1, 0, 1],
        1: [0, 0, 1, 1, 0, 0, 1],
        2: [0, 0, 1, 0, 0, 1, 1],
        3: [0, 1, 1, 1, 1, 0, 1],
        4: [0, 1, 0, 0, 0, 1, 1],
        5: [0, 1, 1, 0, 0, 0, 1],
        6: [0, 1, 0, 1, 1, 1, 1],
        7: [0, 1, 1, 1, 0, 1, 1],
        8: [0, 1, 1, 0, 1, 1, 1],
        9: [0, 0, 0, 1, 0, 1, 1]}

code2 = {0: [3, 2, 1, 1],
         1: [2, 2, 2, 1],
         2: [2, 1, 2, 2],
         3: [1, 4, 1, 1],
         4: [1, 1, 3, 2],
         5: [1, 2, 3, 1],
         6: [1, 1, 1, 4],
         7: [1, 3, 1, 2],
         8: [1, 2, 1, 3],
         9: [3, 1, 1, 2]}

T = int(input())
for tc in range(1, 10):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    temp = ['0']*M
    code_li = []
    for a in arr:
        if temp != a and a not in code_li:
            code_li.append(a)   # x 는 암호코드가 있는 리스트 한 줄

    print(code_li)
    # 뒤에 있는 0 자르기
    # for i in range(M - 1, -1, -1):
    #     if x2[i] != '0':
    #         x2 = x2[0:i + 1]
    #         x2 = ''.join(x)
    #         break


    # 2진수로 변환하기
    # x2 = ''
    # for y in ??:
    #     if y in 'ABCDEF':
    #         z = Bbit_input(ord(y)-ord('A')+10)
    #         x2 += z
    #     else:
    #         z = Bbit_input(int(y))
    #         x2 += z
    #
    # print(x2)

    # b = ''
    # for i in range(len(x2)-1, -1, -1):
    #     if x2[i] == '1':
    #         b = i
    #         break
    # print(b)

    # count = []
    #
    # b = 0
    # for i in range(len(x2)-1, -1, -1):
    #     if x2[i] == '1':
    #         b = i
    #
    # while b != 0:
    #     while b & 1 ==
    #
    #
    # print(count)


    # j = 3
    # while j != 0:
    #     for i in x2:
    #         while i == 1:
    #             count[j] += 1
    #         j -= 1
    #         while i == 0:
    #             count[j] += 1
    #         j -= 1
    # print(count)

    print()