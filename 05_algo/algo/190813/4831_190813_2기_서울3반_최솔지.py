import sys
sys.stdin = open("4831.txt", "r")

T = int(input())
for t in range(1, T+1):
    # KNM = list(map(int, input().split()))
    # stop = list(map(int, input().split()))
    # K = KNM[0]
    # N = KNM[1]
    #
    # # 값이 0 나오는 경우 먼저 빼기
    # m = []
    # result = 0
    # for idx in range(len(stop) - 1):
    #     m.append(stop[idx + 1] - stop[idx])
    # m.append(N - stop[-1])
    # m.append(stop[0])
    # if max(m) > K:
    #     result = 0
    #
    # # K 만큼 갈 때 충전기가 있는지 체크하기
    # else:
    #     n = 0
    #     while n + K < N:
    #         if n + K in stop:
    #             n += K
    #             result += 1
    #         else:
    #             n -= 1
    #
    # print("#%d %d" % (t, result))

    K, N, M = map(int, input().split())
    stops = [0]+list(map(int, input().split())) + [N]

    last = 0
    cnt = 0
    next = last + K

    for i in range(1, M+2):
        if (stops[i] - stops[i-1]) > K:
            cnt = 0
            break
        if stops[i] > next:
            last = stops[i-1]
            cnt += 1
        next = last + K

    print("#%d %d" % (t, cnt))