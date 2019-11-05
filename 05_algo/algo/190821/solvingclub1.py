import sys
sys.stdin = open("solvingclub1.txt", "r")

for tc in range(1, 11):
    N = int(input())
    data = [[char for char in input()] for _ in range(8)]  # 2차원 배열 형태

    count = 0  # 회문 개수

    # 가로에서 회문 찾기
    for row in range(len(data)):
        for i in range(len(data)-N+1):
            rev = data[row][i:i+N]
            if data[row][i:i+N] == rev[::-1]:
                count += 1

        # 세로에서 회문 찾기
        # for col in range(len(data)-N+1):
        #     col_list = []
        #     for n in range(N):
        #         col_list += data[col+n][row]
        #     if col_list == col_list[::-1]:
        #         count += 1

    print('#{} {}'.format(tc, count))