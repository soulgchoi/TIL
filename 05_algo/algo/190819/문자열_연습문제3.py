text = 'a pattern matching algorithm'
key = 'rithm'
t = len(text)
k = len(key)

# for i in range(t):
#     for j in range(k):
#         if text[i] == key[j]:
#             count += 1
#         if count == k:
#             print(i - k)


def BruteForce(text, key):
    i = 0
    j = 0
    while i < t and j < k:
        if text[i] != key[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == k:
        return i - k
    else:
        return -1

print(BruteForce(text, key))
