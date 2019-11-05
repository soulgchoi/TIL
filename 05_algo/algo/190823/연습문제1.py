string = '2+3*4/5'
stack = []
result = []
token = '()+-*/'
for s in string:
    if s not in token:
        print(s, end=' ')
    else:
        stack += s

while stack:
    print(stack.pop(), end=' ')
