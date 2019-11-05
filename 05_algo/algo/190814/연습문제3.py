arr = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]

for n in range(len(arr)):
    for m in range(len(arr)):
        min_number = arr[n][m]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if min_number > arr[i][j]:
                    min_number = arr[i][j]
                    arr[n][m], arr[i][j] = arr[i][j], arr[n][m]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_start = 0
