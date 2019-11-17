import sys
sys.stdin = open('2217.txt', 'r')

N = int(input())
rope = sorted(list(int(input()) for _ in range(N)))
res = rope[0]
for i in range(N):
	weight = rope[i]*(N-i)
	if weight > res:
		res = weight
print(res)