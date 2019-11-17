import sys
sys.stdin = open('15683.txt', 'r')

for _ in range(6):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    print(array)
