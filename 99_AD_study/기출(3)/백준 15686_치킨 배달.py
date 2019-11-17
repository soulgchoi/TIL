import sys
sys.stdin = open('15686.txt', 'r')


def powersetlist(s):
    r = [[]]

    for e in s:
        temp = [x+[e] for x in r]
        r += temp
    return r


# for _ in range(4):
N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []

for r in range(N):
    for c in range(N):
        if array[r][c] == 2:
            chicken += [(r, c)]   # 치킨집 위치
        elif array[r][c] == 1:
            home += [(r, c)]  # 집 위치

# 치킨집마다 치킨 거리 계산해서 넣음
distance = [[] for _ in range(len(chicken))]
for idx, (c, k) in enumerate(chicken):
    for (h, m) in home:
        dis = abs(c-h)+abs(k-m)
        distance[idx] += [dis]

# 길이가 M 인 부분집합 만들기
m = list(range(len(chicken)))
powerset = powersetlist(distance)
comb = []
for p in powerset:
    if len(p) == M:
        comb += [p]

ans = 9999999
for o in comb:
    dd = [2*N] * (len(home))  # 집마다 가장 짧은 치킨거리 넣을 것임
    for oo in o:
        for i, j in enumerate(oo):
            if j < dd[i]:
                dd[i] = j
    if sum(dd) < ans:
        ans = sum(dd)

print(ans)







