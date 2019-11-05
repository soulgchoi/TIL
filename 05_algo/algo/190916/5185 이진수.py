import sys
sys.stdin = open('5185.txt', 'r')

def Bbit_input(i):
    output = ''
    for j in range(3, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    return output

T = int(input())
for tc in range(1, T+1):
    data = input().split()
    N, M = int(data[0]), data[1]

    print('#%d' % tc, end=' ')

    ans = ''
    for m in M:
        if m in 'ABCDEF':
            ans += Bbit_input(ord(m)-ord('A')+10)
        else:
            ans += Bbit_input(int(m))

    print(ans)

# int(뫄뫄, 16)
# 16진수를 int 처리