import sys
sys.stdin = open("4865.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    str1_dict = {}
    for n in str1:
        if n not in str1_dict.keys():
            str1_dict[n] = 0

    max_val = 0
    for m in str2:
        if m in str1_dict.keys():
            str1_dict[m] += 1
            if max_val < str1_dict[m]:
                max_val = str1_dict[m]

    print('#{} {}'.format(tc, max_val))
