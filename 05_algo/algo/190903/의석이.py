import sys
sys.stdin = open('의석이.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    words = [input() for _ in range(5)]

    print('#%d' % tc, end=' ')
    for i in range(15):
        for w in words:
            try:
                print(w[i], end='')
            except IndexError:
                pass
    print()