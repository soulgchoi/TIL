import sys
sys.stdin = open('5207.txt', 'r')

def bin_search(li, x, low, high):
    global check
    if low > high:
        return -1
    else:
        mid = (low+high) // 2
        if x == li[mid]:
            check.append(0)
            return mid
        elif x < li[mid]:
            check.append(1)
            return bin_search(li, x, low, mid-1)
        elif x > li[mid]:
            check.append(2)
            return bin_search(li, x, mid+1, high)


def leftright(li):
    if len(li) <= 2:
        return True
    else:
        for i in range(len(li)-1):
            if li[i] == li[i+1]:
                return False
        return True


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Nl = sorted(list(map(int, input().split())))
    Ml = list(map(int, input().split()))

    cnt = 0
    for m in Ml:
        if m in Nl:
            check = []
            bin_search(Nl, m, 0, len(Nl)-1)
            if leftright(check):
                cnt += 1

    print('#%d %d' % (tc, cnt))
