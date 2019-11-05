import sys
sys.stdin = open('solvingclub1.txt', 'r')

# def deck(data):
#     # card = [[0 for _ in range(14)] for _ in range(4)]
#     for d in range(0, len(data)-2, 3):
#         number = int(data[d+1] + data[d+2])
#         if data[d] == 'S':
#             if card[0][number] == 1:
#                 return -1
#             else: card[0][number] += 1
#         elif data[d] == 'D':
#             if card[1][number] == 1:
#                 return -1
#             else: card[1][number] += 1
#         elif data[d] == 'H':
#             if card[2][number] == 1:
#                 return -1
#             else: card[2][number] += 1
#         elif data[d] == 'C':
#             if card[3][number] == 1:
#                 return -1
#             else: card[3][number] += 1
#     return card
#
#
# for tc in range(1, int(input())+1):
#     card = [[0 for _ in range(14)] for _ in range(4)]
#     data = list(input())
#     c = deck(data)
#     if c == -1:
#         print('#{} {}'.format(tc, 'ERROR'))
#     else:
#         result = []
#         for i in range(len(card)):
#             result.append(card[i].count(0)-1)
#         print('#{} {}'.format(tc, ' '.join(map(str, result))))

for tc in range(1, int(input())+1):
    data = list(input())
    card = [data[i:i+3] for i in range(0, len(data)-2, 3)]
    flag = 1
    S = D = H = C = 13
    for i in card:
        if card.count(i) < 2:
            if 'S' in i:
                S -= 1
            elif 'D' in i:
                D -= 1
            elif 'H' in i:
                H -= 1
            elif 'C' in i:
                C -= 1
        else:
            flag = 0
            break
    if flag == 1:
        print('#{} {} {} {} {}'.format(tc, S, D, H, C))
    else:
        print('#{} {}'.format(tc, 'ERROR'))

