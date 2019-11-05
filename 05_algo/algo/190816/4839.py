import sys
sys.stdin = open("4839.txt", "r")

# 수로 비교
def find_middle(x, y, z=1, count=0):
    start = z
    end = x
    middle = (x+z) // 2
    if middle == y:
        return count
    elif middle > y:
        count += 1
        return find_middle(middle, y, start, count)
    elif middle < y:
        count += 1
        return find_middle(end, y, middle, count)


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    a = find_middle(P, A)
    b = find_middle(P, B)

    if a < b:
        print('#%d A' % tc)

    elif b < a:
        print('#%d B' % tc)

    elif a == b:
        print('#%d 0' % tc)



# 인덱스로 비교
def find_middle(p, x, y, z=1, count=0):
    start = z
    end = x
    middle = (end+start) // 2
    if p[middle] == y:
        return count
    elif p[middle] > y:
        count += 1
        return find_middle(p, middle, y, start, count)
    elif p[middle] < y:
        count += 1
        return find_middle(p, end, y, middle, count)


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    P_list = list(range(P+1))
    a = find_middle(P_list, P, A)
    b = find_middle(P_list, P, B)

    if a < b:
        print('#%d A' % tc)

    elif b < a:
        print('#%d B' % tc)

    elif a == b:
        print('#%d 0' % tc)
