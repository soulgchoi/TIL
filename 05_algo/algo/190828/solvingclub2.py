import sys
sys.stdin = open('solvingclub2.txt', 'r')

def cal1(data):
    stack = []
    opr = []
    token = '()+*'
    for d in data:
        if d in token:
            if not stack:
                stack.append(d)
            else:
                if d == '+':
                    if stack[-1] == '*' or stack[-1] == '+':
                        opr.append(stack.pop())
                        stack.append(d)
                    else:
                        stack.append(d)
                elif d == '(':
                    stack.append(d)
                elif d == '*':
                    if stack[-1] == '*':
                        opr.append(stack.pop())
                        stack.append(d)
                    else:
                        stack.append(d)
                elif d == ')':
                    while stack[-1] != '(':
                        opr.append(stack.pop())
                    stack.pop()
        else:
            opr.append(d)

    while stack:
        opr.append(stack.pop())

    return opr

def cal2(opr):
    stack2 = []
    while opr:
        o = opr.pop(0)
        try:
            stack2.append(int(o))
        except ValueError:
            s2 = stack2.pop()
            s1 = stack2.pop()
            if o == '+':
                stack2.append(s1 + s2)
            elif o == '*':
                stack2.append(s1 * s2)
    return stack2

for tc in range(1, 11):
    N = int(input())
    data = input()
    c = cal1(data)
    result = cal2(c)[0]

    print('#{} {}'.format(tc, result))