import sys
sys.stdin = open('덩치.txt', 'r')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

res = [0]*N
for d in range(N):
	temp = d
	cnt = 0
	for e in range(N):
		if e != d:
			if data[e][0] > data[d][0] and data[e][1] > data[d][1]:
				cnt += 1
	res[d] = cnt+1

for r in res:
	print(r, end=' ')

