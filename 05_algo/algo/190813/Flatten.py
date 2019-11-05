import sys
sys.stdin = open("flatten.txt", "r")

for tc in range(1, 11):
    dump = int(input())
    block = list(map(int, input().split()))

    while dump != 0:
        m = block.index(max(block))
        n = block.index(min(block))
        block[m] -= 1
        block[n] += 1
        dump -= 1

    print("#%d %d" % (tc, max(block) - min(block)))




    dump = int(input())
    block = sorted(list(map(int, input().split())))
    while dump != 0:
        block[-1] -= 1
        block[0] += 1
        dump -= 1
        block.sort()

    print("#%d %d" % (tc, max(block) - min(block)))



    maxl, minl = find_minmax()
