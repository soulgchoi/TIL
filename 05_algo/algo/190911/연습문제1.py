input_ = '000000100011010000000111100000011000000111100110000110000111100111100111111001100111'

data = [list(map(int, list(input_)[i:i+7])) for i in range(0, len(input_), 7)]
print(data)

for d in data:
    ans = 0
    for j in range(7):
        ans += 2**(6-j) * d[j]
    print(ans)

    