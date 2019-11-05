import sys
sys.stdin = open('solvingclub.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    code = [list(input()) for _ in range(N)]

    print(code)