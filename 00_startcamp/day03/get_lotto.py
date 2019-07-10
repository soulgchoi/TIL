# 현실 데이터 가져오기
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text

data = json.loads(response)


real_numbers = []
for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)
