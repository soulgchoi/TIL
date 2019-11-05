import sys
sys.stdin = open('연습문제2.txt', 'r')


def run(x):
    if x[1] == x[0]+1 and x[2] == x[0]+2:
        return True
    # else:
    #     return False


def triplet(x):
    if x[0] == x[1] == x[2]:
        return True
    # else:
    #     return False


def perm(arr, k, n):
    global check
    if k == n:
        x, y = arr[0:3], arr[3:6]
        if (run(x) or triplet(x)) and (run(y) or triplet(y)):
            check = 1
            return
        else:
            return

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, k+1, n)
            arr[k], arr[i] = arr[i], arr[k]


for t in range(1, 5):
    arr = list(map(int, input()))
    n = len(arr)

    print('#%d' % t, end=' ')

    check = 0
    perm(arr, 0, n)
    if check:
        print('Baby-gin')
    else:
        print(-1)
