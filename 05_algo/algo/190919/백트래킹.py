
def backtrack(a, k, inp):
    if k == inp:
        for i in range(1, k):
            if a[i]:
                print(i)
        return
    else:
        k += 1
        c = [True, False]
        for i in range(2):
            a[k] = c[i]
            backtrack(a, k, inp)

MAXCANDIDATES = 4
NMAX = 4
a = [0] * NMAX
backtrack(a, 0, 3)
