import sys
sys.stdin = open('2630.txt', 'r')


def func(i, M):
	global cnt_w, cnt_b
	temp = []
	temp_w = []
	temp_b = []
	for n in range(M):
		temp += paper[(i+(n*i))+(N*n):(i+(n*i))+(N*n)+M]
		temp_w += p_white[(i+(n*i))+(N*n):(i+(n*i))+(N*n)+M]
		temp_b += p_blue[(i+(n*i))+(N*n):(i+(n*i))+(N*n)+M]
	if temp == temp_w:
		cnt_w += 1
		return
	elif temp == temp_b:
		cnt_b += 1
		return
	else:
		func(i, M//2)
		func(M//2, M//2)
		func(M*M//2, M//2)
		func(M*M//2+(M//2), M//2)


N = int(input())
paper = sum([list(map(int, input().split())) for _ in range(N)], [])
p_white = [0] * N*N
p_blue = [1] * N*N

cnt_w = cnt_b = 0
func(0, N)


print(cnt_w)
print(cnt_b)
