def Bbig_print(i):
    output = ''
    for j in range(7, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    print(output)


for i in range(-7, 8):
    print('%3d = ' % i, end=' ')
    Bbig_print(i)

