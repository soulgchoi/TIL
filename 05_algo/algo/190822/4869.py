# import sys
# sys.stdin = open("4869.txt", "r")


def square(x):
	if x == N:
		return 1
	if x > N:
		return 0
	return square(x+10) + square(x+20)*2


T = int(input())
for tc in range(1, T+1):
	N = int(input())
	print('#{} {}'.format(tc, square(0)))
