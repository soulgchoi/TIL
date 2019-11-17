import sys
sys.stdin = open('11399.txt', 'r')

# def perm(k, val):
# 	global res
# 	if k == N:
# 		if res > val:
# 			res = val
# 		return
# 	else:
# 		for i in range(k, N):
# 			atm[k], atm[i] = atm[i], atm[k]
# 			temp = val
# 			for t2 in range(k+1):
# 				temp += atm[t2]
# 			if temp < res:
# 				perm(k+1, temp)
# 			atm[k], atm[i] = atm[i], atm[k]


N = int(input())
atm = list(map(int, input().split()))
# res = 9999
# perm(0, 0)
atm.sort()
a = 0
res = 0
while a < N:
	for b in range(a+1):
		res += atm[b]
	a += 1

print(res)