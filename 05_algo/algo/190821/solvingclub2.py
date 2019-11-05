import sys
sys.stdin = open('solvingclub2.txt', 'r')

for _ in range(10):
    tc = int(input())
    data = [[char for char in input()] for _ in range(100)]

    long = []
    row = 0
    while row < 100:
        # 가로 회문
        for i in range(len(data)-len(long)):
            for j in range(len(long), len(data)-len(long)):
                row_list = data[row][i:i+j]
                if row_list == row_list[::-1]:
                    if len(long) < len(row_list):
                        long = row_list
        row += 1


    #
    #     # 세로 회문
    #     col_list = []
    #     for col in range(len(data)):
    #         col_list += data[col][row]
    #     for x in range(len(col_list)-len(long)):
    #         for y in range(len(long), len(data)-len(long)):
    #             col_list2 = col_list[x:x+y]
    #             if col_list2 == col_list2[::-1]:
    #                 if len(long) <= len(col_list2):
    #                     long = col_list2
    #                 else:
    #                     break
    #
    #     row += 1
    #
    # print('#{} {}'.format(tc, len(long)))

    # long = []
    # row = 0
    # while row < len(data):
    #     i = 0
    #     col_list = []
    #     for col in range(len(data)):
    #         col_list += data[col][row]
    #     while i < len(data):
    #         j = len(long)
    #         while i+j < len(data):
    #             row_list = data[row][i:i+j+1]
    #             col_list2 = col_list[i:i+j+1]
    #             if row_list == row_list[::-1]:
    #                 if len(long) < len(row_list):
    #                     long = row_list
    #             if col_list2 == col_list2[::-1]:
    #                 if len(long) < len(col_list2):
    #                     long = col_list2
    #
    #             j += 1
    #         i += 1
    #     row += 1


            # for x in range(len(col_list)-len(long)):
            #     for y in range(len(long), len(data)-len(long)):
            #         col_list2 = col_list[x:x+y]
            #         if col_list2 == col_list2[::-1]:
            #             if len(long) <= len(col_list2):
            #                 long = col_list2
            #

    # 세로 회문
    # for col in range(len(data)):
    #     for x in range(len(data)):
    #         col_list2 = []
    #         for y in range(len(long), len(data)-x):
    #             col_list2.append(data[x+y][col])
    #         if col_list2 == col_list2[::-1]:
    #             if len(long) < len(col_list2):
    #                 long = col_list2

    print('#{} {}'.format(tc, len(long)))