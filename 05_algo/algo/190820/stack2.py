import sys
sys.stdin = open("stack2.txt", "r")


def check(N):
    stack = []
    S = []
    for n in N:
        if n == '(' or n == ')' or n == '{' or n == '}':
            S.append(n)


    for s in S:
        if s == '(' or s == '{':
            stack.append(s)
        elif s == ')':
            # len 0인지 체크
            if stack.pop(len(stack)-1) == '(':

        elif s == '}':
            if stack.pop(len(stack)-1) == '{':





T = int(input())
for tc in range(1, T + 1):
    print('#{} {}'.format(tc, check(input())))
