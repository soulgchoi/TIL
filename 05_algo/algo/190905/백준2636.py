import sys
sys.stdin = open('2636.txt', 'r')

for _ in range(int(input())):
    col, row = list(map(int, input().split()))
    cheese = [list(map(int, input().split())) for _ in range(col)]
    s = [[0] * row for _ in range(col)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    ans = 0
    queue = []
    count = 0
    while cheese != s:
        v = [[0] * row for _ in range(col)]
        ans = 0
        queue.append((0, 0))
        v[0][0] = 1
        while queue:
            x, y = queue.pop(0)
            for n in range(4):
                nx = x + dx[n]
                ny = y + dy[n]
                if 0 <= nx < col and 0 <= ny < row and cheese[nx][ny] == 0 and not v[nx][ny]:
                    queue.append((nx, ny))
                    v[nx][ny] = 1
                elif 0 <= nx < col and 0 <= ny < row and cheese[nx][ny] == 1 and not v[nx][ny]:
                    v[nx][ny] = 1
                    cheese[nx][ny] = 0
                    ans += 1
        count += 1

    print(count)
    print(ans)
