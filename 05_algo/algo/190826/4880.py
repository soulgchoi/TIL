import sys
sys.stdin = open('4880.txt', 'r')

# 분할정복
# 이진검색 참고
# aps 응용 merge sort 참고
# 병합 과정 필요
def find(l, r):
    if l == r:
        return 1
    else:
        r1 = find(l, (l+r)//2)
        r2 = find((1+r)//2 + 1, r)
        if card[r1] == card[r2]:
            return r1
        else:

def game(start, end):
    if start == end:
        return start
    if start+1 == end:
        return whoWin(start, end)

    half = (start + end)//2
    win1 = game(start, half)
    win2 = game(half+1, end)
    return whoWin(win1, win2)


def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while a[L]<a[pivot] and L<R:
            L += 1
        while a[R]>=a[pivot] and L<R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
                a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split()))
    print(partition(students, 0, N-1))