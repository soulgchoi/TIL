N = int(input())
card = list(range(1, N+1))
i = 0
while i < len(card)-1:
	i += 1
	card += [card[i]]
	i += 1
print(card[-1])