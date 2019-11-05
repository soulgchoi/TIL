import sys
sys.stdin = open('5250.txt', 'r')

def quickSort(arr, l, r):
    if l < r:
        s = hoare_partition(arr, l, r)
        quickSort(arr, l, s-1)
        if s < N//2:
            quickSort(arr, s+1, r)

def hoare_partition(arr, l, r):
    pivot = l
    i, j = l, r
    while i < j:
        while i < r and arr[i] <= arr[pivot]:
            i += 1
        while j > l and arr[j] >= arr[pivot]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    quickSort(A, 0, N-1)

    print('#%d %d' % (tc, A[N//2]))