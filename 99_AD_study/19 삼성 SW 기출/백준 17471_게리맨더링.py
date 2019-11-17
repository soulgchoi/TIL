import sys
sys.stdin = open('17471.txt', 'r')


def powersetlist(s):
	r = [[]]

	for e in s:
		temp = [x+[e] for x in r]
		r += temp
	return r


for _ in range(4):
	N = int(input())
	ingu = list(map(int, input().split()))
	node = [[] for _ in range(N)]
	for n in range(N):
		temp = list(map(int, input().split()))
		node[n] += temp[1:]
	# print(node)

	numbers = list(range(N))
	powerset = powersetlist(numbers)
	# print(powerset)

	for i in range(len(powerset)):
		ls1 = powerset[i]
		ls2 = [item for item in numbers if item not in powerset[i]]
		visited1 = [False] * len(ls1)
		visited2 = [False] * len(ls2)
		# dfs 검증 필요



