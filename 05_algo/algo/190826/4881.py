import sys
sys.stdin = open('4881.txt', 'r')

# column 번호를 가지고 순열을 만든다.
# 순열 백트래킹 사용

def backtrack():
    for i in range(ncard):
        perm(cand[i]) = 1

        perm(cand[i]) = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(arr)