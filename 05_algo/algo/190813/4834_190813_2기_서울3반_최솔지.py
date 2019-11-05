import sys
sys.stdin = open("4834.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = input()
    a = input()
    numbers = {}
    for i in a:
        numbers[i] = a.count(i)

    count = max(numbers.values())
    card = 0
    for j in numbers.keys():
        if numbers[j] == count:
            if card < int(j):
                card = int(j)

    print("#%d %d %d" % (t, card, count))