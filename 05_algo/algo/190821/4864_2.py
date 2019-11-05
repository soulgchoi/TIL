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

