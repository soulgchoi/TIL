import sys
sys.stdin = open("금속막대.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    end = []
    for odd in data:
        if data.count(odd) == 1:
            end.append(odd)

    screws = [data[i:i + 2] for i in range(0, len(data) - 1, 2)]

    for a in range(0, len(screws)):
        if screws[a][0] in end:
            screws[0], screws[a] = screws[a], screws[0]
        if screws[a][1] in end:
            screws[-1], screws[a] = screws[a], screws[-1]


    print(screws)