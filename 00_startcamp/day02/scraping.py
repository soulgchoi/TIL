import requests
import bs4

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
text = bs4.BeautifulSoup(response, 'html.parser')
exchange_rate = text.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')

print(exchange_rate.text)
