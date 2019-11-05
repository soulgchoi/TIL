import sys
sys.stdin = open('2048.txt', 'r')

def up():
    for i in range(0, N-1):
        for j in range(0, N):
            if tiles[i][j] != 0:
                for k in range(i+1, N):
                    if tiles[k][j] == tiles[i][j]:
                        tiles[i][j] = tiles[k][j] * 2
                        tiles[k][j] = 0
                        break
                    elif tiles[k][j] != tiles[i][j] and tiles[k][j] != 0:
                        break
            else:
                n = 0
                for k in range(i+1, N):
                    if tiles[k][j] != 0:
                        tiles[i][j] = tiles[k][j]
                        tiles[k][j] = 0
                        n = k
                        break
                for l in range(n+1, N):
                    if tiles[l][j] != 0:
                        if tiles[i][j] == tiles[l][j]:
                            tiles[i][j] = tiles[l][j] * 2
                            tiles[l][j] = 0
                            break
                        else:
                            break

def down():
    for i in range(N-1, 0, -1):
        for j in range(N-1, -1, -1):
            if tiles[i][j] != 0:
                for k in range(i-1, -1, -1):
                    if tiles[k][j] == tiles[i][j]:
                        tiles[i][j] = tiles[k][j] * 2
                        tiles[k][j] = 0
                        break
                    elif tiles[k][j] != tiles[i][j] and tiles[k][j] != 0:
                        break
            else:
                n = 0
                for k in range(i-1, -1, -1):
                    if tiles[k][j] != 0:
                        tiles[i][j] = tiles[k][j]
                        tiles[k][j] = 0
                        n = k
                        break
                for l in range(n-1, -1, -1):
                    if tiles[l][j] != 0:
                        if tiles[i][j] == tiles[l][j]:
                            tiles[i][j] = tiles[l][j] * 2
                            tiles[l][j] = 0
                            break
                        else:
                            break


def right():
    for i in range(0, N):
        for j in range(N-1, 0, -1):
            if tiles[i][j] != 0:
                for k in range(j-1, -1, -1):
                    if tiles[i][k] == tiles[i][j]:
                        tiles[i][j] = tiles[i][k] * 2
                        tiles[i][k] = 0
                        break
                    elif tiles[i][k] != tiles[i][j] and tiles[i][k] != 0:
                        break
            else:
                n = 0
                for k in range(j-1, -1, -1):
                    if tiles[i][k] != 0:
                        tiles[i][j] = tiles[i][k]
                        tiles[i][k] = 0
                        n = k
                        break
                for l in range(n-1, -1, -1):
                    if tiles[i][l] != 0:
                        if tiles[i][j] == tiles[i][l]:
                            tiles[i][j] = tiles[i][l] * 2
                            tiles[i][l] = 0
                            break
                        else:
                            break

def left():
    for i in range(0, N):
        for j in range(0, N-1):
            if tiles[i][j] != 0:
                for k in range(j+1, N):
                    if tiles[i][k] == tiles[i][j]:
                        tiles[i][j] = tiles[i][k] * 2
                        tiles[i][k] = 0
                        break
                    elif tiles[i][k] != tiles[i][j] and tiles[i][k] != 0:
                        break
            else:
                n = 0
                for k in range(j+1, N):
                    if tiles[i][k] != 0:
                        tiles[i][j] = tiles[i][k]
                        tiles[i][k] = 0
                        n = k
                        break
                for l in range(n+1, N):
                    if tiles[i][l] != 0:
                        if tiles[i][j] == tiles[i][l]:
                            tiles[i][j] = tiles[i][l] * 2
                            tiles[i][l] = 0
                            break
                        else:
                            break


T = int(input())
for tc in range(1, T+1):
    n, S = list(map(str, input().split()))
    N = int(n)
    tiles = [list(map(int, input().split())) for _ in range(N)]

    print('#%d' % tc)

    if S == 'up':
        up()
    if S == 'down':
        down()
    if S == 'right':
        right()
    if S == 'left':
        left()

    for tile in tiles:
        t = map(str, tile)
        print(' '.join(t))
