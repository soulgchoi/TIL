import sys
sys.stdin = open('solvingclub.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    C2 = [0] * P

    for b in bus:
        for i in range(b[0], b[1]+1):
            for c in range(len(C)):
                if i == C[c]:
                    C2[c] += 1

    print('#%d %s' % (tc, ' '.join(map(str, C2))))