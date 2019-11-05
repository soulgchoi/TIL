import sys
sys.stdin = open('암호코드.txt', 'r')


def find():
    for a in arr:
        for i in range(M-1, -1, -1):
            if a[i] == 1:
                password = a[i - 55:i+1]
                return password


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

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    pw = find()
    pw_li = [pw[j:j+7] for j in range(0, len(pw), 7)]

    print(pw)
    print(pw_li)

    numbers = []

    for p in pw_li:
        for key, val in code.items():
            if p == val:
                numbers.append(key)

    # print(numbers)

    check = 0
    for n in range(8):
        if n % 2:
            check += numbers[n]
        else:
            check += numbers[n]*3

    print('#%d' % tc, end=' ')

    if check % 10:
        print(0)
    else:
        print(sum(numbers))

# py = mat[i][::-1].find('1')
# py = 1이 있는 인덱스