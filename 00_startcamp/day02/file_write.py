lunches = {
    '양자강': '02-123-4567',
    '김밥카페': '02-123-5678',
    '순남시래기': '02-123-6789'
}
# 파이썬 딕셔너리 키-밸류 형태
with open('lunch.csv', 'w', encoding='utf-8') as f:
    f.write('식당이름, 전화번호\n')
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')
