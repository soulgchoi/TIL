import sys
sys.stdin = open("2578.txt", "r")


def isBingo(x):
    bingo = 0
    count_3 = 0
    count_4 = 0
    for i in range(len(x)):
        count_1 = 0
        count_2 = 0
        if x[i][i] == 0:
            count_3 += 1
        if x[i][len(x)-1-i] == 0:
            count_4 += 1
        for j in range(len(x[0])):
            if x[i][j] == 0:
                count_1 += 1
            if x[j][i] == 0:
                count_2 += 1
        if count_1 == 5:
            bingo += 1
        if count_2 == 5:
            bingo += 1
    if count_3 == 5:
        bingo += 1
    if count_4 == 5:
        bingo += 1

    return bingo


numbers = [list(map(int, input().split())) for _ in range(5)]

numbers2 = []
for _ in range(5):
    numbers2 += [num2 for num2 in list(map(int, input().split()))]

a = 0
Bingo = 0
while Bingo < 3:
    if a <= len(numbers2):
        a += 1
        for x in range(len(numbers)):
            for y in range(len(numbers[0])):
                if numbers[x][y] == numbers2[a-1]:
                    numbers[x][y] = 0
                    Bingo = isBingo(numbers)
    else:
        break

print(a)
