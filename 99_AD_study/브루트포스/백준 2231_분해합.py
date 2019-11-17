# N = int(input())
N = 15
x = len(str(N))
if N < 10:
	result = 0
else:
	result = N - 9*x

for i in range(9*x):
	temp = result+i
	for t in str(result+i):
		temp += int(t)
	if temp == N:
		result += i
		break
else:
	result = 0

print(result)

