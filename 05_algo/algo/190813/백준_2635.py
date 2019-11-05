n = 350
i = 1
len_chain = []
list_chain = []
while i < n:
    chain = [n]
    chain.append(n-i)
    i += 1
    m = chain[-1]
    while chain[-2]-chain[-1] >= 0:
        chain.append(chain[-2]-chain[-1])
    len_chain.append(len(chain))
    list_chain.append(chain)

result = len_chain.index(max(len_chain))
result_2 = ' '.join(map(str, list_chain[result]))
print(max(len_chain), result_2)