import sys
sys.stdin = open("solvingclub.txt", "r")


# def start(graph=dict):
#     for key in graph.keys():
#         l_val = []
#         for val in graph.values():
#             l_val += val
#         if key not in l_val and key not in visited:
#             return key
#
# def have_visited(x):
#     for key in graph.keys():
#         if x == key:
#             return True
#         else:
#             return False
#
# def work(x):
#     for i in graph[x]:
#         if i not in visited:
#             visited.append(x)
#             return i


for tc in range(1, 11):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    edges = [data[i:i+2] for i in range(0, E*2, 2)]

    graph = {edge[0]: edge[1] for edge in edges}
    # for edge in edges:
    #     graph[edge[0]] = [edge[1]]

    for key, val in graph.items():
        for edge2 in edges:
            if key == edge2[0]:
                if edge2[1] not in val:
                    val.append(edge2[1])
    #
    # visited = []
    # while visited != V:
    #     start_p = start(graph)
    #     visited.append(start_p)

    print(graph)




