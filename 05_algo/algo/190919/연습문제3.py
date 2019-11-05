def pre_traverse(T):
    if tree[T]:
        print(T, end=' ')
        pre_traverse(tree[T][0])
        if len(tree[T]) >= 2:
            pre_traverse(tree[T][1])
    else:
        print(T, end=' ')


def in_traverse(T):
    if tree[T]:
        in_traverse(tree[T][0])
        print(T, end=' ')
        if len(tree[T]) >= 2:
            in_traverse(tree[T][1])
    else:
        print(T, end=' ')


def post_traverse(T):
    if tree[T]:
        post_traverse(tree[T][0])
        if len(tree[T]) >= 2:
            post_traverse(tree[T][1])
        print(T, end=' ')
    else:
        print(T, end=' ')


N = 12
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
tree = [[] for _ in range(N+2)]


for a in range(0, len(arr)-1, 2):
    tree[arr[a]].append(arr[a+1])

print(tree)

print('preorder  | ', end='')
pre_traverse(1)
print()
print('inorder   | ', end='')
in_traverse(1)
print()
print('postorder | ', end='')
post_traverse(1)
