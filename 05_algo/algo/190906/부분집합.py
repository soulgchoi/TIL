def powersetlist(s):
    r = [[]]

    for e in s:
        temp = [x+[e] for x in r]
        r += temp
    return r
print(powersetlist([1, 2, 3, 4, 5]))