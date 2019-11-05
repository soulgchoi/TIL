import sys
sys.stdin = open("2669.txt", "r")

N = [list(map(int, input().split())) for _ in range(4)]
area = []

for n in N:
    r1, c1, r2, c2 = n[0], n[1], n[2], n[3]
    for r in range(r1, r2):
        for c in range(c1, c2):
            area.append((r, c))

print(len(list(set(area))))