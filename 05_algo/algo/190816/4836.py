import sys
sys.stdin = open("4836.txt", "r")


T = int(input())
for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    count = 0
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == 0:
                    arr[i][j] = color
                elif arr[i][j] == 1 and color == 2:
                    count += 1
                elif arr[i][j] == 2 and color == 1:
                    count += 1
    print('#%d %d' % (tc, count))