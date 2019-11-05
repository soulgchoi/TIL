# 143
# n = int(input())
# i = 1
# for _ in range(n-1):
#     i += 2
# for x in range(n):
#     print(' '*x + '*'*i)
#     i -= 2
# i += 4
# for y in range(n-1):
#     print(' '*(n-y-2) + '*'*i)
#     i += 2

# 144
# n = int(input())
# for i in range(n):
#     for _ in range(n*2 - i*2 - 2):
#         print(' ', end='')
#     for _ in range(i*2 + 1):
#         print('*', end='')
#     print()

# 145
# n = int(input())
# for x in range(1, n+1):
#     for _ in range(n-x):
#         print(' ', end=' ')
#     for j in range(1, x+1):
#         print(j, end=' ')
#     print()

# 146
# n = int(input())
# x = 65
# y = 0
# for i in range(n):
#     for _ in range(n-i):
#         print(chr(x), end=' ')
#         x += 1
#     for _ in range(i):
#         print(y, end=' ')
#         y += 1
#     print()

# 147
# n = int(input())
# x = 1
# for i in range(n):
#     for _ in range(i):
#         print(' ', end=' ')
#     for _ in range(n-i):
#         print(x, end=' ')
#         x += 1
#     print()

# 148
# n = int(input())
# for i in range(n):
#     for _ in range(i+1):
#         print('#', end=' ')
#     for _ in range(n-i-1):
#         print(' ', end=' ')
#     print()
# for j in range(n-2, -1, -1):
#     for _ in range(n-j-1):
#         print(' ', end=' ')
#     for _ in range(j+1):
#         print('#', end=' ')
#     print()

# 149
# n = int(input())
# x = 1
# for _ in range(n):
#     for _ in range(n):
#         print(x, end=' ')
#         if x+2 < 10:
#             x += 2
#         else:
#             x = 1
#     print()

# 556
# arr = [n for n in range(1, 11)]
# for a in arr:
#     print(a, end=' ')

# 560
# numbers = list(map(int, input().split()))
# minimum = numbers[0]
# for number in numbers:
#     if minimum > number:
#         minimum = number
# print(minimum)

# 561
# numbers = list(map(int, input().split()))
# big = 9999
# big_count = 0
# small = 1
# small_count = 0
# for number in numbers:
#     if number < 100:
#         small_count += 1
#         if small < number:
#             small = number
#     if number >= 100:
#         big_count += 1
#         if big > number:
#             big = number
#
# if small_count == 0:
#     print(100, end=' ')
# else:
#     print(small, end=' ')
#
# if big_count == 0:
#     print(100)
# else:
#     print(big)

