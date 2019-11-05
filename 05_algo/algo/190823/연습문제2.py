def backtrack(a, k, b_input, sum_subset):
    # global MAXCANDIDATES
    # c = [0] * MAXCANDIDATES
    # c = [True, False]
    if k == b_input:
        # for i in range(1, len(a)):
        #     if a[i]:
        #         subset.append(powerset[i-1])
        if sum(subset) == 10:
            return True

    else:
        k += 1
        if sum(subset)+a[k] < 10:
            subset.append(a[k])
            backtrack(a, k, b_input, sum(subset)+a[k])
            subset.pop()
        backtrack(a, k, b_input, sum_subset)

# def construct_candidates(a, k, b_input, c):
#     c[0] = True
#     c[1] = False
#     return 2

MAXCANDIDATES = 10
NMAX = 11
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subset = []
print(backtrack(a, 0, 10, 0))
