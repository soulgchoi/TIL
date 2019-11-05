import sys
sys.stdin = open("4873.txt", "r")

def peek(x):
    if stack == []:
        return False
    if stack[-1] == x:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    string = input()
    stack = []

    for s in string:
        if not peek(s):
            stack.append(s)
        else:
            stack.pop()

    print('#{} {}'.format(tc, len(stack)))


