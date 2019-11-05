def Bbit_input(i):
    output = ''
    for j in range(3, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    return output


pattern = [
    '001101',
    '010011',
    '111011',
    '110001',
    '100011',
    '110111',
    '001011',
    '111101',
    '011001',
    '101111',
]

N = '0269FAC9A0'

number = []
for n in N:
    if ord(n)-ord('A') + 10 >= 10:
        m = ord(n)-ord('A') + 10
        number += Bbit_input(m)
    else:
        number += Bbit_input(int(n))

# print(number)

while number:
    num = number.pop()
    check = ''
    if num == '1':
        check += num
        for _ in range(5):
            temp = number.pop()
            check += temp
    c = check[::-1]
    if c in pattern:
        print(pattern.index(c), end=' ')