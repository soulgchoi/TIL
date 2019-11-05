# 0 <= x + dx < N
# 0 <= y + dy < M

arr = [[1, 2, 3, 4, 5]]*5
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
res = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < len(arr) and 0 <= Y < len(arr[0]):  # 이 부분 함수 선언 가능
                res += abs(arr[x][y]-arr[X][Y])  # 이 부분 함수 선언 가능
            # 반복해서 나타나면 함수 선언하는 게 속도가 빠르다.

print(res)
