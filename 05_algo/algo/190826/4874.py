import sys
sys.stdin = open('4874.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = input().split()

    stack = []
    n = 0
    while N[n] != '.':
        try:
            stack.append(int(N[n]))
        except ValueError:
            if stack:
                try:
                    y = stack.pop()
                    x = stack.pop()
                    if N[n] == '+':
                        stack.append(x+y)
                    if N[n] == '-':
                        stack.append(x-y)
                    if N[n] == '*':
                        stack.append(x*y)
                    if N[n] == '/':
                        stack.append(x//y)
                except IndexError:
                    break
        n += 1

    if len(stack) == 1:
        if stack[0] in N and N[N.index(stack[0])+1] == '.':
            print('#{} {}'.format(tc, 'error'))
        else:
            print('#{} {}'.format(tc, stack[0]))
    else:
        print('#{} {}'.format(tc, 'error'))

