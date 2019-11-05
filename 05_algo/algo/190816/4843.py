import sys
sys.stdin = open("4843.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = [0]*10

    for i in range(0, len(numbers)-1):
        max_number = i
        for j in range(i+1, len(numbers)):
            if numbers[max_number] < numbers[j]:
                max_number = j
        numbers[i], numbers[max_number] = numbers[max_number], numbers[i]

    for k in range(5):
        result[k*2] = numbers[k]
        result[k*2 + 1] = numbers[-1-k]

    print('#{} {}'.format(tc, ' '.join(map(str, result))))
