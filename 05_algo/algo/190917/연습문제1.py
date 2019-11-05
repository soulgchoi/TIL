def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min_num = i
        for j in range(i+1, n):
            if A[j] < A[min_num]:
                min_num = j
        A[min_num], A[i] = A[i], A[min_num]


def SelectionSort_recursion(A, n, i=0):
    if i == n-1:
        return
    else:
        min_num = i
        for j in range(i+1, n):
            if A[j] < A[min_num]:
                min_num = j
        A[min_num], A[i] = A[i], A[min_num]
        SelectionSort_recursion(A, n, i+1)


A = [2, 5, 233, 6, 65, 3, 5]
n = len(A)
# SelectionSort(A)
SelectionSort_recursion(A, n)
print(A)