# def Dijkstra(s, A, D):
#     U = set(s)
#     for v in V:
#         D[v] = A[s][v]

    # while U != V:






data = '1 2 3 1 3 5 2 3 2 3 2 1 2 4 6 3 4 4 3 5 6 5 6 6 4 6 3 4 5 2 5 1 3'
# data = '1 2 3 1 3 4 2 4 5 3 2 1 3 4 4 3 5 5 4 5 3 5 1 3 5 6 5 4 6 4'
N = list(map(int, data.split()))

inf = 999999
matrix = [[inf]*7 for _ in range(7)]
for i in range(0, len(N)-2, 3):
    matrix[N[i]][N[i+1]] = N[i+2]

for j in range(1, 7):
    matrix[j][j] = 0


V = {1, 2, 3, 4, 5, 6}
D = [[inf] for _ in range(7)]

print(matrix)
# Dijkstra(0, matrix, D)
# for v in V:
#     for n_idx, n in enumerate(matrix[v]):
#         if n != 0:
#             distance[v].append((n_idx, n))


# print(matrix)
# print(distance)
