import sys
sys.stdin = open("test01.txt", "r")

# 인덱스로 비교
T = 10
for t in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))
    c = [0] * len(H)
    for h in range(2, len(H)-2):
        if H[h] - H[h-2] > 0 and H[h] - H[h-1] > 0 and H[h] - H[h+1] > 0 and H[h] - H[h+2] > 0:
            c[h] += H[h] - max([H[h-2], H[h-1], H[h+1], H[h+2]])

    print("#%d %d" % (t, sum(c)))
    print(c)

# T = 10
# for t in range(1, T+1):
#     N = int(input())
#     H = list(map(int, input().split()))
#     res = 0
#     for h in range(2, len(H)-2):
#         if H[h] - H[h-2] > 0 and H[h] - H[h-1] > 0 and H[h] - H[h+1] > 0 and H[h] - H[h+2] > 0:
#             res += H[h] - max([H[h-2], H[h-1], H[h+1], H[h+2]])
#
#     print("#%d %d" % (t, res))