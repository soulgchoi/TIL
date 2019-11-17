import sys
sys.stdin = open('1021.txt', 'r')

import collections
T = int(input())
for _ in range(T):
	N, M = map(int, input().split())
	K = collections.deque(map(int, input().split()))
	L = collections.deque(range(1, N+1))
	print(L)
	cnt = 0
	while K:
		if L[0] == K[0]:
			L.popleft()
			K.popleft()
		else:
			if len(L)//2 >= L.index(K[0]):
				L.rotate(-1)
				cnt += 1
			else:
				L.rotate(1)
				cnt +=1
	print(cnt)
