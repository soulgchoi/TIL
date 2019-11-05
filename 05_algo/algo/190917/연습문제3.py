def powerset(li):
    r = [[]]

    for e in li:
        temp = [x + [e] for x in r]
        for t in temp:
            if sum(t) == 0:
                print(t)
        r += temp


def comb(n, r):
    if r == 0:
        tr2 = tr
        print(tr2)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)



an = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# powerset(an)
#
# print('/////////////////////////////')

n = len(an)
for r in range(n):
    tr = [0] * r
    comb(n, r)
