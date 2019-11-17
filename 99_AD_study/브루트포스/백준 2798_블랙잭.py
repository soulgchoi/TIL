import sys
sys.stdin = open('백준 2798', 'r')


def comb(k, val, j):
	global ans
	if k == 3:
		if ans < val <= M:
			ans = val
	else:
		for i in range(j, N):
			comb(k+1, val+card[i], j+1)


N, M = map(int, input().split())
card = list(map(int, input().split()))

ans = 0
# for a in range(N):
# 	val = card[a]
# 	for b in range(N):
# 		if a != b:
# 			val += card[b]
# 			for c in range(N):
# 				if c != a and c != b:
# 					val += card[c]
# 					if ans < val <= M:
# 						ans = val
# 					val -= card[c]
# 			val -= card[b]
# 	val -= card[a]

comb(0, 0, 0)
print(ans)
