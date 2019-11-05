def backtrack(a, k, inp, subset=[]):

	if k == inp:
		return subset
	else:
		subset = []
		k += 1
		c = [True, False]
		for i in range(2):
			a[k] = c[i]
			subset += a
			backtrack(a, k, inp, subset)

MAXCANDIDATES = 4
NMAX = 4
a = [0] * NMAX
print(backtrack(a, 0, 3))
