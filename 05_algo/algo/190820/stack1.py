s = []


def stack_top(s):
    if len(s) == 0:
        return -1
    else:
        return s[-1]


def stack_push(item):
    s.append(item)


def stack_pop(s):
    if len(s) == 0:
        return None

    else:
        return s.pop(-1)

print(s)
print(stack_top(s))
stack_push('choi')
print(s)
print(stack_top(s))
stack_push('sol')
print(s)
print(stack_top(s))
stack_push('ji')
print(s)
print(stack_top(s))
stack_pop(s)
print(s)
print(stack_top(s))