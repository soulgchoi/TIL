import sys
sys.stdin = open("solvingclub_2.txt", "r")

for _ in range(10):
    tc = int(input())
    # 2차원 배열 입력받기
    arr = [list(map(int, input().split())) for _ in range(100)]

    num_list = []
    r_sum = 0
    l_sum = 0
    for x in range(len(arr)):
        row_sum = 0
        col_sum = 0
        r_sum += arr[x][x]
        l_sum += arr[x][99 - x]
        for y in range(len(arr[0])):
            row_sum += arr[x][y]
            col_sum += arr[y][x]

        num_list.append(row_sum)
        num_list.append(col_sum)
    num_list += [r_sum, l_sum]

    print('#%d %d' % (tc, max(num_list)))
