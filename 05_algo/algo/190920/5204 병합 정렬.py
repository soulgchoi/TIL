import sys
sys.stdin = open('5204.txt', 'r')

def partition(n):
    if len(n) == 1:
        return n

    left = partition(n[0:len(n)//2])
    right = partition(n[len(n)//2:len(n)])

    return merge(left, right)

def merge(l, r):
    global cnt
    result = [0]*(len(l)+len(r))
    i, j, k = 0, 0, 0
    if l[-1] > r[-1]:
        cnt += 1
    while len(l) > i and len(r) > j:
        if l[i] <= r[j]:
            result[k] = l[i]
            i += 1
        else:
            result[k] = r[j]
            j += 1
        k += 1
    if i == len(l):
        while j < len(r):
            result[k] = r[j]
            j += 1
            k += 1
    elif j == len(r):
        while i < len(l):
            result[k] = l[i]
            i += 1
            k += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Na = list(map(int, input().split()))
    cnt = 0
    res = partition(Na)

    print('#%d %d %d' % (tc, res[N//2], cnt))