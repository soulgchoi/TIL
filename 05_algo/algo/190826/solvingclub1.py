import sys
sys.stdin = open('solvingclub1.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    y = 0
    while y < N:
        x = 0
        count_1 = []
        count_2 = []
        while x < N:
            if matrix[x][y] == 1:
                if x < 10:
                    count_1.append('0'+str(x))
                    count_1.append('n ')
                else:
                    count_1.append(str(x))
                    count_1.append('n ')
            if matrix[x][y] == 2:
                if x < 10:
                    count_2.append('0'+str(x))
                    count_2.append('s ')
                else:
                    count_2.append(str(x))
                    count_2.append('s ')
            x += 1
        y += 1

        check = ''.join(sorted(''.join(count_1).split() + ''.join(count_2).split()))
        stack = []
        for c in check:
            if c == 'n' and not stack:
                stack.append(c)
            if stack and stack[-1] == 'n' and c == 's':
                count += 1
                stack.pop()

    print('#{} {}'.format(tc, count))
