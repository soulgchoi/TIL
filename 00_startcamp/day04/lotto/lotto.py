import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

reponse = requests.get(url).text
data = json.loads(reponse)

real = []
for key, value in data.items():
    if 'drwtNo' in key:
        real.append(value)

bonus = data['bnusNo']
print(bonus)

print(real)
