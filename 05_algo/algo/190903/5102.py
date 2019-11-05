import sys
sys.stdin = open('5102.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	V, E = list(map(int, input().split()))
	matrix = [[0]*V for _ in range(V)]
	for _ in range(E):
		x, y = list(map(int, input().split()))
		matrix[x-1][y-1] = 1
		matrix[y-1][x-1] = 1
	S, G = list(map(int, input().split()))

	print(matrix)

