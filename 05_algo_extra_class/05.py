
'''
1
9
CXXXXXXXC
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
CXCXXXXXC
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N = N + 6
    arr = [['0'] * N for i in range(N)]

    for i in range(3, N - 3):
        s = list(input())
        arr[i][3:N - 3] = s[:]

    ans = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                arr[i][j-1] = 'X'
                arr[i][j+1] = 'X'
                arr[i-1][j] = 'X'
                arr[i+1][j] = 'X'

            if arr[i][j] == 'B':
                arr[i][j-1] = 'X'
                arr[i][j+1] = 'X'
                arr[i-1][j] = 'X'
                arr[i+1][j] = 'X'
                arr[i][j-2] = 'X'
                arr[i][j+2] = 'X'
                arr[i-2][j] = 'X'
                arr[i+2][j] = 'X'

            if arr[i][j] == 'C':
                arr[i][j-1] = 'X'
                arr[i][j+1] = 'X'
                arr[i-1][j] = 'X'
                arr[i+1][j] = 'X'
                arr[i][j-2] = 'X'
                arr[i][j+2] = 'X'
                arr[i-2][j] = 'X'
                arr[i+2][j] = 'X'
                arr[i][j-3] = 'X'
                arr[i][j+3] = 'X'
                arr[i-3][j] = 'X'
                arr[i+3][j] = 'X'


    ans = sum(arr, []).count('H')
    =
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                ans += 1

    print("#%d %d"%(tc, ans))

    # print("#%d %d" % (tc, sum(arr, []).count('H')))



############## 전치 행렬 만들기
A = [[1,2,3], [4,5,6],[7,8,9]]
AT = list(zip(*A))  ### 튜플