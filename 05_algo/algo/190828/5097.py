import sys
sys.stdin = open('5097.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = list(map(int, input().split()))
    data = list(map(int, input().split())) + [0 for _ in range(M)]
    print(data)
    front = 0
    rear = N

    while front < M:
        data[front], data[rear] = data[rear], data[front]
        front += 1
        rear += 1

    print('#{} {}'.format(tc, data[front]))