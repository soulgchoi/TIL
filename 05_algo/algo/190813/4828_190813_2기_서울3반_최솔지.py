import sys
sys.stdin = open("4828.txt", "r")

# max 와 min 사용
T = int(input())
for t in range(1, T + 1):
    N = input()
    H = list(map(int, input().split()))

    print('#{} {}'.format(t, max(H) - min(H)))


# max 와 min 사용하지 않고
T = int(input())
for t in range(1, T + 1):
    N = input()
    H = list(map(int, input().split()))
    maxnum = minnum = H[0]

    for h in range(1, len(H)):
        if maxnum < H[h]:
            maxnum = H[h]
        if minnum > H[h]:
            minnum = H[h]

    print('#{} {}'.format(t, maxnum - minnum))