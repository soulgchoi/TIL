def enQueue(x):
    global rear
    if rear == len(Q)-1:
        print('Queue_Full')
    else:
        rear += 1
        Q[rear] = x
        if x in P.keys():
            P[x] += 1
            print(P, Chu)
        else:
            P[x] = 1
            print(P, Chu)


def deQueue():
    global front, Chu
    if front == rear:
        print('Queue_Empty')
    else:
        front += 1
        Chu -= P[Q[front]]
        print(P, Q[front], Chu)
        return Q[front]


Q = [0] * 20
front = rear = -1
Chu = 20
P = {}

i = j = 1
while Chu > 0:
    enQueue(i)
    deQueue()
    


