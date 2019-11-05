# 549
# n = int(input())
# odd = 0
# i = 1
# count = 0
# while odd < n:
#     if i % 2 == 1:
#         count += 1
#         odd += i
#         i += 2
# print(count, odd)

# 634
# n = int(input())
# i = 1
# while i <= n:
#     print('*'*i)
#     i += 1

# 550
# n = int(input())
# i = n
# count = 0
# while count < n*2:
#     if count < n:
#         print('*'*i)
#         i -= 1
#         count += 1
#     else:
#         i += 1
#         print('*' * i)
#         count += 1

# 551
# n = int(input())
# i = n
# while i != 0:
#     print(' '*(n-i) + '*'*i)
#     i -= 1

# 552
# n = int(input())
# i = 1
# for _ in range(n-1):
#     i += 2
# for j in range(n):
#     print(' '*j + '*'*i + ' '*j)
#     i -= 2

# 553:
# n = int(input())
# i = 65
# for j in range(n, 0, -1):
#     for _ in range(j):
#         print(chr(i), end='')
#         i += 1
#     print()

# 554
# n = int(input())
# i = j = 65
# for x in range(n, 0, -1):
#     for y in range(x):
#         print(i - 64, end=' ')
#         i += 1
#     for x in range(n+1 - x):
#         print(chr(j), end=' ')
#         j += 1
#     print()

# 140
# n = list(map(int, input().split()))
# i = 0
# n_sum = 0
# while i < len(n):
#     if n[i] == 0:
#         break
#     else:
#         n_sum += n[i]
#         i += 1
# print(n_sum, n_sum//i)

# 141
# n = int(input())
# i = 1
# while n*i < 100:
#     print(n*i, end=' ')
#     if (n*i) % 10 != 0:
#         i += 1
#     else:
#         break

# 142
# n = int(input())
# i = 1
# for i in range(1, n+1):
#     print('*'*i)
# for j in range(n-1, 0, -1):
#     print('*'*j)

