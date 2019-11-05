import sys
sys.stdin = open('5186.txt', 'r')

# 재귀함수
def func(i, output=''):
    if i == 0:
            print(output)
    else:
        i = i*2
        if i >= 1:
            output += '1'
            i -= 1
            if len(output) < 13:
                func(i, output)
            else:
                print('overflow')
        else:
            output += '0'
            if len(output) < 13:
                func(i, output)
            else:
                print('overflow')


T = int(input())
for tc in range(1, T+1):
    N = float(input())

    print('#%d' % tc, end=' ')

    func(N)


# while
# def func(i):
#     output = ''
#     while i != 0:
#         i = i*2
#         if i >= 1:
#             output += '1'
#             i -= 1
#         else:
#             output += '0'
#     return output
#
# T = int(input())
# for tc in range(1, T+1):
#     N = float(input())
#
#     print('#%d' % tc, end=' ')
#
#     n = func(N)
#     if len(n) < 13:
#         print(n)
#     else:
#         print('overflow')
