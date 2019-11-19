import sys
sys.stdin = open('1018.txt', 'r')

for _ in range(2):
	M, N = map(int, input().split())
	input_data = [list(input().split()) for _ in range(M)]
	arr = []
	for data in input_data:
		arr.append(list(d for d in data))

	ans = 0
	print(arr)