c = 9
ch = ord('0') + c

print(type(ch))

n_list = []
number = 123

print(type(ord('9')-48))


def itoa(x):
    sr = ''
    while True:
        r = x % 10
        sr = sr + chr(r + ord('0'))
        x //= 10
        if x == 0:
            break

    s = ''
    for i in range(len(sr) - 1, -1, -1):
        s = s + sr[i]

    return s


print(itoa(number))


def atoi(st):
    value = 0

    for i in range(len(st)):
        if ord('0') <= ord(st[i]) <= ord('9'):
            digit = ord(st[i]) - ord('0')
        else:
            break
        value = (value * 10) + digit
