import sys
sys.stdin = open('파스칼.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*10 for _ in range(10)]
    for i in range(10):
        arr[i][0] = 1
        arr[i][i] = 1

    for j in range(2, 10):
        for k in range(1, 9):
            arr[j][k] = arr[j-1][k-1] + arr[j-1][k]

    print('#%d' % tc)

    for a in range(N):
        for b in range(N):
            if arr[a][b] != 0:
                print(arr[a][b], end=' ')
            else:
                break
        print()

