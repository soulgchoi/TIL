# 518
# a, b, c = map(int, input().split())
# sum_numbers = a + b + c
# avg_numbers = (a+b+c)//3
#
# print(
#     'sum : {}'.format(sum_numbers),
#     'avg : {}'.format(avg_numbers),
#     sep = '\n'
# )

# 519
# a, b = map(int, input().split())
# print('{} {}'.format(a+100, b % 10))

# 522
# a, b = map(int, input().split())
# if a == b:
#     print(1, 0, sep='\n')
# else:
#     print(0, 1, sep='\n')

# 525
# a, b, c = map(int, input().split())
# if a > b and a > c:
#     print(1, end=' ')
# else:
#     print(0, end=' ')
# if a == b == c:
#     print(1)
# else:
#     print(0)

# print(int(a > b and a > c), end=' ')
# print(int(a == b== c))

# 247
# a, b, c = map(int, input().split())
# print(0) if 0 in numbers else print(1)
# print(int(a != 0 and b != 0 and c != 0))

# 528
# n = int(input())
# print(n)
# print('minus') if n < 0 else ''

# 529
# height, weight = map(int, input().split())
# obesity = weight+100 - height
# print(obesity)
# print('Obesity') if obesity > 0 else ''

# 530
# n = int(input())
# print('adult') if n >= 20 else print('{} years later'.format(20-n))

# 531
# n = float(input())
# if n <= 50.80:
#     print('Flyweight')
# elif n <= 61.23:
#     print('Lightweight')
# elif n <= 72.57:
#     print('Middleweight')
# elif n <= 88.45:
#     print('Cruiserweight')
# else:
#     print('Heavyweight')

# 532
# a, b = map(float, input().split())
# if a >= 4.0 and b >= 4.0:
#     print('A')
# elif a >= 3.0 and b >= 3.0:
#     print('B')
# else:
#     print('C')

# 632
# a, b, c = list(map(int, input().split()))
# min_number = numbers[0]
# for i in range(3):
#     if min_number > numbers[i]:
#         min_number = numbers[i]
# print(min_number)

# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b < c:
#         print(b)
#     else:
#         print(c)

# 120
# a, b = map(int, input().split())
# if a > b:
#     print(a - b)
# else:
#     print(b - a)

# 121
# n = int(input())
# if n > 0:
#     print('plus')
# elif n == 0:
#     print('zero')
# else:
#     print('minus')

# 122
# year = int(input())
# if year % 4 == 0 and year % 100:
#     print('leap year')
# else:
#     print('common year')

# 536
# n = 1
# while n <= 15:
#     print(n, end=' ')
#     n += 1

# 537
# x = int(input())
# n = 1
# m = 0
# while n <= x:
#     m += n
#     n += 1
# print(m)