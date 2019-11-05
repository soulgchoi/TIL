import sys
sys.stdin = open("4837.txt", "r")

T = int(input())
for tc in range(1, T+1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a = len(A)
    N, K = map(int, input().split())
    count = 0

    for i in range(1, 1 << a):
        subset_sum = 0
        subset = []
        for j in range(a):
            if i & (1 << j):
                subset_sum += A[j]
                subset.append(A[j])

        if len(subset) == N and subset_sum == K:
            count += 1

    print('#%d %d' % (tc, count))

