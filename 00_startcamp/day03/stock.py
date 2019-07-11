# 패키지 가져다 쓰기
from iexfinance.stocks import Stock

company = Stock('AAPL', token=)

print(company.get_quote())
