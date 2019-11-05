import sys
sys.stdin = open('3074.txt', 'r')


def bin_search(low, high):
    global N, M, res
    mid = (low + high) // 2
    p = 0

    if low >= mid:
        res = low
        return

    for i in range(N):
        p += mid//li_t[i]
        if p >= M:
            break

    if p >= M:
        return bin_search(low, mid)
    else:
        return bin_search(mid, high)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li_t = [int(input()) for _ in range(N)]

    min_time = 1
    max_time = max(li_t)*M

    res = 0

    bin_search(min_time, max_time)

    print('#%d %d' % (tc, res+1))

