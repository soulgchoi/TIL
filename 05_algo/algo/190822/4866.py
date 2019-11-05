import sys
sys.stdin = open("4866.txt", "r")

def check(data):

    N = [')', '}']
    stack = []

    while data:
        if data[-1] in N:
            stack.append(data.pop())
        else:
            if data[-1] == '(':
                if not stack:
                    return -1
                else:
                    if stack.pop() == ')':
                        pass
                    else:
                        return -1
            if data[-1] == '{':
                if not stack:
                    return -1
                else:
                    if stack.pop() == '}':
                        pass
                    else:
                        return -1
            data.pop()
    if stack:
        return -1
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    data = [char for char in input()]

    if check(data) == -1:
        print('#{} {}'.format(tc, 0))
    elif check(data) == 1:
        print('#{} {}'.format(tc, 1))