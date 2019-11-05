import sys
sys.stdin = open("금속막대.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    screws = [data[i:i+2] for i in range(0, len(data)-1, 2)]
    end = []

    for odd in data:
        if data.count(odd) == 1:
            end.append(odd)
    screws_2 = []
    for a in range(len(screws)):
        if screws[a][0] in end:
            screws_2 += screws[a]
            screws.pop(a)
            break

    for _ in range(N):
        for screw in screws:
            if screw[0] == screws_2[-1]:
                screws_2 += screw
                screws.pop(screws.index(screw))

    print('#{} {}'.format(tc, ' '.join(map(str, screws_2))))