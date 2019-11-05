def process_solution(a, k):
    sumnum = 0
    for i in range(1, 11):
        if a[i] == True:
            sumnum += i
    if sumnum == 10:
        for i in range(1, 11):
            if a[i] == True:
                print(i, end=' ')
        print()

def backtrack(a, k, inp):
    if k == inp:
        # for i in range(1, k+1):
        #     print(a[i], end=' ')
        # print()
        return process_solution(a, k)

    else:
        k += 1
        c = [True, False]
        for i in range(2):
            a[k] = c[i]
            backtrack(a, k, inp)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(backtrack(a, 0, 10))