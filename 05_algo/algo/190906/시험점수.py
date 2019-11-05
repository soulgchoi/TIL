import sys
sys.stdin = open('시험점수.txt', 'r')


def powersetlist(s):
    r = [[]]
    for e in s:
        temp = [x + [e] for x in r]
        r += temp
    return r

# 이 때 s 는 리스트, s 돌리면서 하나씩 리스트 더하기더하기
def powerset(s):
    r = [[]]
    for e in s:
        temp = [x + [e] for x in r]
        r += temp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    test = list(map(int, input().split()))
    score = set()
    powerset = powersetlist(test)
    for p in powerset:
        score.add(sum(p))
    print('#%d %d' % (tc, len(score)))


