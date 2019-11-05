import sys
sys.stdin = open('숫자회전.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print('#', tc, sep='')

    for i in range(N):
        for j in range(N):
            print(matrix[N-1-j][i], end='')
        print(end=' ')
        for k in range(N):
            print(matrix[N-1-i][N-1-k], end='')
        print(end=' ')
        for l in range(N):
            print(matrix[l][N-1-i], end='')
        print(end=' ')
        print()
    # for x in range(N):
    #     for y in range(3):
    #         print(''.join(map(str, result[y][N*x:N*x+N])), end=' ')
    #     print()

    # for i in range(N):
    #     for j in range(N):
    #         result[0].append(matrix[N-1-j][i])
    #
    #     for k in range(N):
    #         result[1].append(matrix[N-1-i][N-1-k])
    #
    #     for l in range(N):
    #         result[2].append(matrix[l][N-1-i])
    #
    # for x in range(N):
    #     for y in range(3):
    #         print(''.join(map(str, result[y][N*x:N*x+N])), end=' ')
    #     print()

    #

    # for i in range(N):
    #     for j in range(N-1, -1, -1):
    #         result[0].append(matrix[j][i])
    #
    # for i in range(N-1, -1, -1):
    #     for j in range(N):
    #         result[2].append(matrix[j][i])
    #
    #     for k in range(N-1, -1, -1):
    #         result[1].append(matrix[i][k])
    #
    # for x in range(N):
    #     for y in range(3):
    #         print(''.join(map(str, result[y][N*x:N*x+N])), end=' ')
    #     print()