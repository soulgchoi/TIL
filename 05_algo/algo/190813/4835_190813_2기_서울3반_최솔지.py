import sys
sys.stdin = open("4835.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    nsum = []
    for n in range(N-M+1):
        nsum.append(sum(numbers[n:n+M]))
    print("#%d %d" % (t, max(nsum)-min(nsum)))





maxV = 0
minV = 1000000
for i in range(0, n-m+1):
    #s = sum(v[i:i+M]
    s = 0
    for j in range(i, i+m):
        s += v[j]
    if s > maxV:
        maxV = s
    if s < minV:
        minV = s


# /////////
s = 0
for i in range(0, m):
    s += v[i]
    maxV = s
    minV = s
    for i in range(1, n - m + 1):
        s = s - v[i - 1] + v[i + m - 1]
        if s > maxV:
            maxV = s
        if s < minV:
            minV = s