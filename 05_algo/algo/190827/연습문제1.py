def createQueue(n):
    return [0] * 3


def enQueue(x):
    global rear
    if rear == len(Q)-1:
        print('Queue_Full')
    else:
        rear += 1
        Q[rear] = x


def deQueue():
    global front
    if front == rear:
        print('Queue_Empty')
    else:
        front += 1
        return Q[front]

Q = createQueue(3)
front = rear = -1
enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
print(Q)
print(deQueue())
print(deQueue())
print(deQueue())
deQueue()