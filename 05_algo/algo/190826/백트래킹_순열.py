def backtrack(a, k, inp):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == inp:
        for i in range(1, k+1):
            print(a[i], end=' ')
        print()

    else:
        k += 1
        ncandidates = construct_candidates(a, k, inp, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, inp)

def construct_candidates(a, k, inp, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, inp+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

MAXCANDIDATES = 4
NMAX = 4
a = [0] * NMAX
backtrack(a, 0, 3)