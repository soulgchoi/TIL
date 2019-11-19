import sys, pprint
sys.stdin = open('17471.txt', 'r')


def dfs(start, li, cnt, v):
	global N, array
	stack = [start]
	temp = [start]
	cnt += ingu[start]
	while stack:
		s = stack.pop()
		if not v[s]:
			v[s] = True
			for w in array[s]:
				if w in li and not v[w]:
					stack += [w]
					temp += [w]
	return list(set(temp))


for _ in range(8):
	N = int(input())
	ingu = list(map(int, input().split()))
	array = [[] for _ in range(N)]

	for n in range(N):
		data = list(map(int, input().split()))
		for d in range(1, data[0]+1):
			array[n] += [data[d]-1]

	nums = [x for x in range(N)]
	powerset = [[]]
	for e in nums:
		temp = [x + [e] for x in powerset]
		powerset += temp

	min_ingu = 99999
	flag = False
	# 부분집합&차집합으로 찾기
	for pset in powerset[1:-1]:
		notp = [e2 for e2 in nums if e2 not in pset]
		visited = [False] * N
		# print(pset, notp)

		stack1 = dfs(pset[0], pset, 0, visited)
		stack1.sort()  # stack 은 순서대로 들어가는게 아니라 sort 안하니 틀렸음
		stack2 = dfs(notp[0], notp, 0, visited)
		stack2.sort()

		# dfs 로 갈 수 있는 범위가 부분집합과 같다
		# == 선거구를 만들 수 있다
		if pset == stack1 and notp == stack2:
			flag = True  # 한 번이라도 선거구 만들 수 있을 때
			sum1 = 0
			for p1 in pset:
				sum1 += ingu[p1]
			sum2 = 0
			for p2 in notp:
				sum2 += ingu[p2]

			if abs(sum1-sum2) < min_ingu:
				min_ingu = abs(sum1-sum2)
	# 선거구 만들 수 있으면 인구 차이, 없으면 -1 출력
	print(min_ingu) if flag else print(-1)
