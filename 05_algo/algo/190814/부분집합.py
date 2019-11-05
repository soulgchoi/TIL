# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
# for i in range(1<<n):
#     for j in range(n+1):
#         if i & (1<<j):
#             print(arr[j], end=", ")
#     print()
# print()


# arr = [1, 5, -9, 6, -2]
# n = len(arr)
# for i in range(1, 1 << n):  # 0 부터 하면 공집합도 포함
#     subset = []
#
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(arr[j])
#     print(subset)

arr = [5, -9, 6, -2, 3, 6, 7, 1, 5, 4]
n = len(arr)
for i in range(1, 1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    if sum(subset) == 0:
        print(subset)

