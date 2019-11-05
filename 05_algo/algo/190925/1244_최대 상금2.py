import sys
sys.stdin = open('1244.txt', 'r')

def perm(k):
    if k == cnt:
        return
    if k == N:
        return
    if arr == m_numbers:
        return
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k+1)


T = int(input())
for tc in range(1, T+1):
    data1, data2 = input().split()
    cnt = int(data2)
    numbers = [int(d) for d in data1]
    N = len(numbers)
    m_numbers = sorted(numbers, reverse=True)

    arr = numbers[::]

