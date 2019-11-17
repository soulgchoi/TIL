import sys
sys.stdin = open('1541.txt', 'r')

data = input().split('-')
print(data)
res = sum(map(int, data.pop(0).split('+')))
print(res)
if data:
	for d in data:
		if '+' in d:
			res -= sum(map(int, d.split('+')))
		else:
			res -= int(d)
print(res)
