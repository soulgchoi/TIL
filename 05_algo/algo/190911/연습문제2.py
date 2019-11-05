N = '01D06079861D79F99F'
M = '0F97A3'

def Bbit_input(i):
    output = ''
    for j in range(3, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    return output


number = ''
for n in N:
    if n in 'ABCDEF':
        m = ord(n)-ord('A') + 10
        number += Bbit_input(m)
    else:
        m = ord(n)-ord('0')
        number += Bbit_input(m)


data = [list(map(int, list(number[i:i+7]))) for i in range(0, len(number), 7)]

for d in data:
    ans = 0
    for j in range(len(d)):
        ans += 2**(len(d)-1-j) * d[j]
    print(ans, end=' ')

