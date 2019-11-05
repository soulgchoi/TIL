import sys
sys.stdin = open('연습문제1.txt', 'r')

def quickSort(N, l, r):
    if l < r:
        # s = hoare_partition(N, l, r)
        s = lomuto_partition(N, l, r)
        quickSort(N, l, s-1)
        quickSort(N, s+1, r)


def hoare_partition(N, l, r):
    # i, j = l, r-1
    # while True:
    #     while N[i] <= N[r] and i < j:
    #         i += 1
    #     while N[j] >= N[r] and i < j:
    #         j -= 1
    #     if i == j:
    #         if N[i] <= N[r]:
    #             i += 1
    #         N[i], N[r] = N[r], N[i]
    #         return i
    #     else:
    #         N[i], N[j] = N[j], N[i]

    pivot = l
    i, j = l, r
    while i < j:
        while i < r and N[i] <= N[pivot]:
            i += 1
        while j > l and N[j] >= N[pivot]:
            j -= 1
        if i < j:
            N[i], N[j] = N[j], N[i]
    N[pivot], N[j] = N[j], N[pivot]
    return j

def lomuto_partition(arr, p, r):
    x = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i+1


for t in range(1, 4):
    N = list(map(int, input().split()))
    l = 0
    r = len(N)-1

    quickSort(N, l, r)
    print(N)