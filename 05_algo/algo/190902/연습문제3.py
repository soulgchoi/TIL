from collections import deque

# data = deque([1, 5, 2, 4, 3])
queue = deque()
#
# for d in data:
#     if queue:
#         if queue[-1] > d:
#             queue.insert(queue.index(queue[-1]), d)
#
#     else:
#         queue.append(d)
#
# print(queue)

def enQueue(x, d):
    if len(d) == 0:
        queue.append(x)
    elif len(d) == 1:
        if x < d[0]:
            d.appendleft(x)
        else:
            d.append(x)
    else:
        for q in range(len(d)):
            if x <= d[q]:
                d.insert(q, x)
                break
        else:
            d.append(x)


for i in [1, 5, 2, 4, 3]:
    enQueue(i, queue)
# enQueue(1, queue)
# enQueue(3, queue)
# enQueue(2, queue)
# enQueue(4, queue)
# enQueue(5, queue)
print(queue)
while queue:
    print(queue.popleft(), end=' ')