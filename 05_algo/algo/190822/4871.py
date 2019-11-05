import sys
sys.stdin = open("4871.txt", "r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    matrix = [[0] * V for _ in range(V)]
    for i in range(V+1):
        for j in range(V+1):
            for node in nodes:
                if [i, j] == node:
                    matrix[i-1][j-1] = 1

    visited = []
    stack = ['start']
    s = S
    while stack:
        if s == G:
            break
        if s not in visited:
            visited.append(s)
        x = 0
        while x < V:
            if matrix[s-1][x] == 1 and x + 1 not in visited:
                stack.append(s)
                s = x + 1
                break
            else:
                x += 1
        else:
            s = stack.pop()

    if s == G:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

