# 540
# flag = False
# while flag == False:
#     n = int(input())
#     if n == -1:
#         flag = True
#     elif n % 3 == 0:
#         print(n // 3)

# 125
# n = int(input())
# for i in range(1, n+1):
#     print(i, end=' ')

# 126
# n = list(map(int, input().split()))
# if 0 in n:
#     n = n[0:n.index(0)]
# odd = 0
# even = 0
# for i in n:
#     if i % 2 == 1:
#         odd += 1
#     else:
#         even += 1
# print('odd : {} \neven : {}'.format(odd, even))

# 128
# n = list(map(int, input().split()))
# if 0 in n:
#     n = n[0:n.index(0)]
#
# count = 0
# for i in n:
#     if i % 3 != 0 and i % 5 != 0:
#         count += 1
# print(count)

# n = list(map(int, input().split()))
# count = 0
# for i in n:
#     if i % 3 != 0 and i % 5 != 0:
#         count += 1
#     if i == 0:
#         break
# print(count)

# 541
# a = input()
# i = 0
# while i < 20:
#     print(a, end='')
#     i += 1

# 544
# n = int(input())
# i = n
# while i < 100:
#     i += 1
#     n += i
# print(n)

# 545
# n = list(map(int, input().split()))
# m3 = 0
# m5 = 0
# for i in n:
#     if i % 3 == 0:
#         m3 += 1
#     if i % 5 == 0:
#         m5 += 1
# print('Multiples of 3 : {} \nMultiples of 5 : {}'.format(m3, m5))

# 547
# for i in range(2, 7):
#     for j in range(5):
#         print(i+j, end=' ')
#     print()

# 131
# n, m = map(int, input().split())
# if n > m:
#     while m <= n:
#         print(m, end=' ')
#         m += 1
# elif n < m:
#     while n <= m:
#         print(n, end=' ')
#         n += 1
# else:
#     print(n)

# 132
# n = int(input())
# m5 = 0
# for i in range(1, n+1):
#     if i % 5 == 0:
#         m5 += i
# print(m5)

# 136
# n = int(input())
# for i in range(1, 11):
#     print(n*i, end=' ')

# 137
# n, m = map(int, input().split())
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i*j, end=' ')
#     print()

# 138
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print((i, j), end=' ')
#     print()

# # 139
# n, m = map(int, input().split())
# if n > m:
#     for j in range(1, 10):
#         for i in range(n - m + 1):
#             if (n-i)*j < 10:
#                 print('{} * {} =  {}'.format(n-i, j, (n-i)*j), end='   ')
#             else:
#                 print('{} * {} = {}'.format(n-i, j, (n-i) * j), end='   ')
#         print()
# else:
#     for j in range(1, 10):
#         for i in range(m - n + 1):
#             if (n+i)*j < 10:
#                 print('{} * {} =  {}'.format(n+i, j, (n+i)*j), end='   ')
#             else:
#                 print('{} * {} = {}'.format(n+i, j, (n+i)*j), end='   ')
#         print()

# 549
# n = int(input())
# odd = 0
# i = 1
# count = 0
# while i < n:
#     if i % 2 == 1:
#         i += i
#         count += 1
#
# print(count, i)