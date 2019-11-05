# 562
# numbers = list(map(int, input().split()))
# odd = []
# even = []
# count = 0
# for idx, n in enumerate(numbers):
#     if idx % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)
#         count += 1
# print('sum : {}'.format(sum(odd)))
# print('avg : {}'.format(sum(even)/count))

#563
# numbers = list(map(int, input().split()))
# numbers.sort()
# numbers.reverse()
# print(' '.join(map(str, numbers)))

#151
# numbers = list(map(int, input().split()))
# num = 0
# for idx, n in enumerate(numbers):
#     if idx in [0, 2, 4]:
#         num += n
# print(num)

#152
# numbers = list(map(int, input().split()))
# odd = 0
# even = 0
# for n in range(len(numbers)):
#     if n % 2:
#         even += numbers[n]
#     else:
#         odd += numbers[n]
# print('odd : {}'.format(odd))
# print('even : {}'.format(even))

#153
# n = [0] * 100
# n = list(map(int, input().split()))
#
# flag = 0
# for i in range(100):
#     if n[i] == -1:
#         flag = i
#         break
#
# for j in range(3, 0, -1):
#     if flag-j < 0:
#         continue
#     else:
#         print(n[flag-j], end=' ')

#156
# numbers = list(map(int, input().split()))
# for number in numbers:
#     if number == 999:
#         numbers2 = numbers[:numbers.index(999)]
# print('max : {}'.format(max(numbers2)))
# print('min : {}'.format(min(numbers2)))

#157
# numbers = list(map(int, input().split()))
# for number in numbers:
#     if number == 0:
#         numbers2 = numbers[:numbers.index(0)]
#
# count = 0
# result = 0
# for num2 in numbers2:
#     if num2 % 5 == 0:
#         count += 1
#         result += num2
# print('Multiples of 5 : {}'.format(count))
# print('sum : {}'.format(result))
# print('avg : {}'.format(round(result/count, 1)))

#159
# n = int(input())
# numbers = list(reversed(sorted(list(map(int, input().split())))))
# for num in numbers:
#     print(num)

#565
# numbers = list(map(int, input().split()))
# numbers2 = [0] * 10
# for i in range(len(numbers)):
#     if numbers[i] == 0:
#         break
#     numbers2[numbers[i] // 10] += 1
#
# for idx, num in enumerate(numbers2):
#     if num != 0:
#         print('{} : {}'.format(idx, num))

# 565
# n = int(input())
# num = [100, n]
# while num[-1] >= 0:
#     x = num[-2]
#     y = num[-1]
#     num.append(x-y)
#
# print(' '.join(map(str, num)))

#569
# score = [list(map(int, input().split())) for _ in range(5)]
# count = 0
# for sc in score:
#     if sum(sc)/len(sc) >= 80:
#         print('pass')
#         count += 1
#     else:
#         print('fail')
# print('Successful : {}'.format(count))

#570
# arr = [[1 for _ in range(5)] for _ in range(5)]
# for i in range(1, len(arr)):
#     for j in range(1, len(arr)):
#         arr[i][j] = arr[i][j-1] + arr[i-1][j]
# for ar in arr:
#     print(' '.join(map(str, ar)))

#160
# n = list(map(int, input().split()))
# dice = [[0] for _ in range(7)]
# # print(dice)
# for i in n:
#     dice[i][0] += 1
# for j in range(1, 7):
#     print('{} : {}'.format(j, dice[j][0]))

#161
# score = list(map(int, input().split()))
# score2 = [0] * 11
# for sc in score:
#     if sc == 0:
#         break
#     score2[sc//10] += 1
# for idx in range(len(score2)-1, -1, -1):
#     if score2[idx] != 0:
#         print('{} : {} person'.format(idx*10, score2[idx]))

#162
# n = list(map(int, input().split()))
# while len(n) < 10:
#     n.append((n[-1]+n[-2]) % 10)
# print(' '.join(map(str, n)))

#163
# arr = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
# sum_arr = 0
# for a in arr:
#     print(' '.join(map(str, a)))
#     sum_arr += sum(a)
# print(sum_arr)

#167
# arr = [list(map(int, input().split())) for _ in range(4)]
# for a in arr:
#     print(sum(a)//len(a), end=' ')
# print()
# for x in range(len(arr[0])):
#     col = 0
#     for y in range(len(arr)):
#         col += arr[y][x]
#     print(col//len(arr), end=' ')
# print()
# print(sum(sum(arr, []))//len(sum(arr, [])))

#168
arr = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    arr[i][0] = 1
    arr[i][i] = 1
for a in range(2, 10):
    for b in range(1, 9):
        arr[a][b] = arr[a-1][b-1] + arr[a-1][b]

n = int(input())
for x in range(n-1, -1, -1):
    for y in arr[x]:
        if y == 0:
            break
        else:
            print(y, end=' ')
    print()

#573
# def problem(x):
#     for i in range(x):
#         for j in range(1, x+1):
#             print(i*x + j, end=' ')
#         print()
# n = int(input())
# problem(n)








