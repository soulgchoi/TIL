import sys
sys.stdin = open('1966.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	N, M = map(int, input().split())
	imp = list(map(int, input().split()))
	imp2 = sorted(imp, reverse=True)

	x = imp[M]
	if imp2[0] == x and M == 0:
		print(1)
	else:
		i = 0
		y = M
		cnt = 0
		while imp2:
			if imp2[0] == imp[i]:
				imp2.pop(0)
				N -= 1
				cnt += 1
				if i == y:
					break
				i += 1
			else:
				imp += [imp[i]]
				if i == y:
					y += N
				i += 1

		print(cnt)
