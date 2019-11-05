import sys
sys.stdin = open('5203.txt', 'r')


def check_triplet(li):
    tri = 0
    for i in li:
        if li.count(i) >= 3:
            tri = 1
            return tri
    if check_run(li):
        tri = 1
    return tri


def check_run(li):
    for i in li:
        if i+1 in li and i+2 in li:
            return True


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    p1 = []
    p2 = []

    p11 = p22 = 0
    while card:
        p1.append(card.pop(0))
        p2.append(card.pop(0))
        if len(p1) >= 3:
            if check_triplet(p1):
                p11 = 1
                break
            if check_triplet(p2):
                p22 = 1
                break

    print('#%d' % tc, end=' ')

    if p11 == p22:
        print(0)
    elif p11 == 1:
        print(1)
    elif p22 == 1:
        print(2)
