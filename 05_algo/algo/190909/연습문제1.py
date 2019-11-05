N = 13
M = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

def preorder_traverse(T):
    if T:
        print(T, end=' ')
        preorder_traverse(arr[T][0])
        preorder_traverse(arr[T][1])


node = list(map(int, M.split()))
arr = [[0, 0] for _ in range(N+1)]
# for n in range(0, len(node)-1, 2):
#     if not arr[node[n]][0]:
#         arr[node[n]][0] = node[n+1]
#     else:
#         arr[node[n]][1] = node[n+1]




for i in range(len(node)//2):
    parent, child = node[i*2], node[i*2 + 1]
    if not arr[parent][0]:
        arr[parent][0] = child
    else:
        arr[parent][1] = child

print(arr)

preorder_traverse(1)

# def tree(x):
#
#
# print(tree(node))

# def preorder_traverse(t):
#     if t is None:
#         pass
#     else:
#         if t not in arr:
#             arr[t][0] = t
#             x = t
#         else:
#             if t < x:
