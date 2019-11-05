import sys
sys.stdin = open('4366.txt', 'r')


def func(x, li):
    ans = 0
    for i in range(len(li)):
        ans += int(li[i]) * x**(len(li)-1-i)
    return ans


T = int(input())
for tc in range(1, T+1):
    N2 = list(input())
    N3 = list(input())

    n2 = []
    n3 = []

    n2.append(func(2, ''.join(N2)))
    for m in range(len(N2)):
        if N2[m] == '1':
            N2[m] = '0'
            n2.append(func(2, ''.join(N2)))
            N2[m] = '1'
        else:
            N2[m] = '1'
            n2.append(func(2, ''.join(N2)))
            N2[m] = '0'

    n3.append(func(3, ''.join(N3)))
    for n in range(len(N3)):
        if N3[n] == '1':
            N3[n] = '2'
            n3.append(func(3, ''.join(N3)))
            N3[n] = '0'
            n3.append(func(3, ''.join(N3)))
            N3[n] = '1'
        elif N3[n] == '2':
            N3[n] = '0'
            n3.append(func(3, ''.join(N3)))
            N3[n] = '1'
            n3.append(func(3, ''.join(N3)))
            N3[n] = '2'
        else:
            N3[n] = '1'
            n3.append(func(3, ''.join(N3)))
            N3[n] = '2'
            n3.append(func(3, ''.join(N3)))
            N3[n] = '0'

    for a in n2:
        if a in n3:
            print('#%d %d' % (tc, a))
