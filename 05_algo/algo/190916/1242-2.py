import sys
sys.stdin = open('1242.txt', 'r')

pCode = [[[""] * 5 for _ in range(5)] for _ in range(5)]
pCode[2][1][1] = 0
pCode[2][2][1] = 1
pCode[1][2][2] = 2
pCode[4][1][1] = 3
pCode[1][3][2] = 4
pCode[2][3][1] = 5
pCode[1][1][4] = 6
pCode[3][1][2] = 7
pCode[2][1][3] = 8
pCode[1][1][2] = 9

hex2bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


def chkPwd(arr):
    sumChk = (arr[0] + arr[2] + arr[4] + arr[6]) * 3 + arr[1] + arr[3] + arr[5] + arr[7]

    if (sumChk % 10) > 0:
        return 0
    else:
        return (arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7])


def getPwd(inStr, endPos):
    sum = 0
    pos = endPos

    num = hex2bin[inStr[pos]]

    pwd = [0] * 8
    pIdx = 7
    bitIdx = 3

    while num[bitIdx] == '0': bitIdx -= 1
    nSaved = num[:bitIdx]

    while pos > -1 and pIdx > -1:

        cntBin = [0] * 4
        cntIdx = 3

        while cntIdx > -1 and pos > -1:

            if pIdx == 0 and cntIdx == 0:
                break

            if int(num[bitIdx]) & 1 == cntIdx & 1:
                cntBin[cntIdx] += 1
                bitIdx -= 1

                if bitIdx < 0:
                    pos -= 1
                    num = hex2bin[inStr[pos]]
                    bitIdx = 3

            else:
                cntIdx -= 1

        minVal = min(cntBin[1], cntBin[2], cntBin[3])
        temp = pCode[cntBin[1] // minVal][cntBin[2] // minVal][cntBin[3] // minVal]

        if temp == "":
            pos = endPos
            num = nSaved
            bitIdx = len(num)
            while num[bitIdx] == '0' and bitIdx > -1: bitIdx -= 1
            if bitIdx < 0 and pos > -1:
                pos -= 1
                num = hex2bin[inStr[pos]]
            pIdx = 7
            continue

        else:
            pwd[pIdx] = temp
            pIdx -= 1

    if pIdx < 0:
        sum += chkPwd(pwd)

    return sum, pos


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    pwdLen = (M // 15) * (N // 6)
    checkedStr = [""] * pwdLen
    sIdx = 0
    res = 0

    inStr = [""] * N
    for row in range(N):
        inStr[row] = input()

    for row in range(N):
        endPos = M - 1
        while endPos > 13:
            while (inStr[row][endPos] == '0' and endPos > 12): endPos -= 1
            if endPos < 13:
                break

            sum, pos = getPwd(inStr[row], endPos)
            res += sum

            for x in range(row, N - 1):
                if inStr[x][endPos] == '0': break
                temp = inStr[x]
                inStr[x] = temp[0:pos] + '0' * (endPos - pos + 1) + temp[endPos + 1:]

    print("#%d %d" % (tc, res))