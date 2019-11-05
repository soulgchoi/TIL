import sys
sys.stdin = open('5099.txt', 'r')

"""
def cheese(fire):
    for i in range(len(fire)):
        fire.insert(i+1, (0, 0))
        p, c = fire.pop(i)
        if c // 2 != 0:
            fire[i] = (p, c // 2)
        else:
            result.append(p)
            if len(pizza) > 0:
                fire[i] = pizza.pop(0)
            else:
                fire.pop(i)
                break


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    data = list(map(int, input().split()))
    pizza = []
    result = []
    for idx, val in enumerate(data):
        pizza.append((idx+1, val))
    fire = [pizza.pop(0)]
    while fire:
        if len(fire) < N and pizza:
            if len(pizza) > 0:
                fire.append(pizza.pop(0))
        else:
            cheese(fire)

<<<<<<< HEAD
    print('#%d %s' % (tc, result[-1]+1))
"""

=======
    print('#%d %s' % (tc, result[-1]))
>>>>>>> 1cee19a8f02b44a22a18717ffb119fb351916700
