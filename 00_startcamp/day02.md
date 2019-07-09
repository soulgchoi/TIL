

# 190709 startcamp_day02

# Git

## what is git

git : **scm** (source code manager) / **vcs** (version control system)

git; 버전관리를 해주는 감시카메라

1. 폴더의 버전관리

   - `git init` > 폴더 관리 시작

   ![1562632906322](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562632906322.png)

   - (master) > 폴더가 관리되고 있음

   - `git add OO` > 감시카메라에 등록!

   - `git status` 로 등록 확인

     - 변경사항이 없을 때와 있을 때 차이

     빨간색 메세지가 뜬다 > 사진 찍을 준비가 안됐다! 

     이때 잠깐만! 의 의미가 **add** 

     add 하고 commit 가능

     - 윗줄은 add 한 상태, 아래는 안된 상태

     ​	![1562635621419](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562635621419.png)

     ​	이 때 commit 하면 위에만 남음

   - 메세지를 남겨놓으면 왜 버전을 나눴는지 알 수 있을 것임

     `git commit -m '~~~했음'`

     - git에서 user 등록 필요

       `git config --global use.email(/name)`

     사진찍기(버전 남기기)

   - 갤러리는 어디에 있나요?

     - `git log`

   - **순서대로 정리하기**

     `git init`

     `git add <filename>`

     `git commit -m '<message>'`

     변경사항 저장

     `git add <filename>`

     `git commit -m '<message>'`

     ...

     `git status`; 상태 물어보는 명령어

     `git log`; 사진(commit)들 로그를 보여줌

     

   * 상위폴더를 관리하면 하위폴더는 자동으로 관리된다.

   * `git add -A`=`git add .`; 통째로 관리하기

   

2. 다른 명령어

   - `cd (..)` > 한 단계 상위로 나가기
- `cd <name>` > 폴더 이동
   - `mkdir <name>` > OO폴더(==디렉토리) 만들기
- 대충 입력하다 탭탭 > 입력하다 탭 > 자동완성
   - `touch <filename>` > 생성
- `rm <filename` > 삭제
   - `ls` > 리스트
- <u>띄어쓰기로 구분</u>
  


3. 내가 어디에 있는지 늘 주의하자!



* github에 백업하기

`git remote add origin https://github.com/soulgchoi/practice_git.git`

`git push -u origin master`



* github/bitbucket/gitlab



------



## import web_browser

1. 여러개의 웹 브라우저를 한번에 열기

   ```python
   import webbrowser
   
   urls = [
       'www.github.com',
       'www.google.com',
       'www.mail.google.com',
       'http://edu.ssafy.com/edu/main/index.do',
       'https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA'
   ]
   
   for url in urls:
       webbrowser.open(url)
   ```

   

2. 정보 스크랩하기

   자주 확인하는 정보를 (자동)스크랩하기 ex) 코스피지수, 부동산가격 등



### **웹Web은 요청해야 응답한다**

어떻게? 뭘?

**요청request과 응답response**

브라우저는 요청을 **보내는** 대표 프로그램

​	**<u>주소</u>**url를 보낸다 = **<u>요청</u>**을 보낸다

​	**<u>문서</u>**(HTML, XML, Json)로 돌려준다 = **<u>응답</u>**한다

url 은 요청에 대한 상세이다

WYSIWYG



※ gitignore 밑에 두면 git이 보지 못함



#### 코스피지수 가져오기

requests 함수가 없다면 

`pip install <함수>`; 함수 다운로드

`requests.get ('주소')`; 요청했으니까 뱉어낼 것임

```python
import requests

response = requests.get('https://naver.com')
print(response)
```

``````python
import requests

response = requests.get('https://naver.com').text
print(response)
# url의 문서(html)를 가져옴
``````

`pip install bs4`; 파이썬에 맞게 만들어줌

ex) `text = bs4.BeautifulSoup(response)`; text를 넣었다 빼기

``````python
import requests
import bs4

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
text = bs4.BeautifulSoup(response)

print(text)
``````

``````python
import requests # requests 함수 가져옴
import bs4 # bs4 함수 가져옴

url = 'https://finance.naver.com/sise/' # url을 여기에서
response = requests.get(url).text # 요청을 보내서 response 박스에 넣음
text = bs4.BeautifulSoup(response, 'html.parser') # 받은 문서를 bs4에 넣었다 빼서 예쁘게 만듦
kospi = text.select_one('#KOSPI_now') # kospi는 여기 있다고 나타냄 (인터넷에서 가져오기)
										# 앞에서 bs4 썼기 때문에 select_one 가능해짐
print(kospi.text) # 가져온 kospi 중에 text만 골라냄
``````

+) 환율 가져오기

```python
import requests
import bs4

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
text = bs4.BeautifulSoup(response, 'html.parser')
exchange_rate = text.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')

print(exchange_rate.text)
```

------

#### 멜론 탑50 가져오기

``````python
import bs4
import requests

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': '0:)'}
# 대신 요청을 보낼 User-Agent Key Value를 만듦(딕셔너리)
response = requests.get(url, headers=headers).text

text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
# rows 안에는 한줄 한줄의 row가 있음
# 모든 row가 같은 구조를 가지고 있기 때문에 for문에 다 들어갈 수 있음
# text를 붙이지 않으면 span 웅앵 다 가져오게 됨
    print(rank, title, artist)
``````

------

#### 파일 가져오기

csv; comma separated value

##### lunch.csv 만들기

``````python
lunches = {
    '양자강': '02-123-4567',
    '김밥카페': '02-123-5678',
    '순남시래기': '02-123-6789'
}
# 파이썬 딕셔너리 키-밸류 형태
with open('lunch.csv', 'w', encording='utf-8') as f:
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')
``````

##### lunch.csv를 읽기

``````python
import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:  # 파일을 열고나서 f라고 부르겠다  # 열린 파일은 이 아래 블럭에서만 동작
    items = csv.reader(f)
    for item in items:
        print(item)
``````



##### 멜론 탑50

``````python
import bs4
import requests

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': '0:)'}
# 대신 요청을 보낼 User-Agent Key Value를 만듦(딕셔너리)
response = requests.get(url, headers=headers).text

text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')

with open('melon50.csv', 'w', encoding='utf-8') as f:
    f.write('순위, 제목, 가수\n')
    for row in rows:
        rank = row.select_one('td:nth-child(2) > div > span.rank').text
        title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
        artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
        f.write(f'{rank}, {title}, {artist}\n')
``````

``````python
import bs4
import requests

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': '0:)'}
# 대신 요청을 보낼 User-Agent Key Value를 만듦(딕셔너리)
response = requests.get(url, headers=headers).text

text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')

writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8'))
writer.writerow(['순위', '제목', '가수'])

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    f.write(f'{rank}, {title}, {artist}\n')
``````

``````python
import bs4
import requests
import csv

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': '0:)'}
# 대신 요청을 보낼 User-Agent Key Value를 만듦(딕셔너리)
response = requests.get(url, headers=headers).text

text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')


writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8', newline=''))
writer.writerow(['순위', '제목', '가수'])

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    writer.writerow([rank, title, artist])
``````



------

#### summary

웹은 요청을 보내면 응답한다

응답을 박스에 넣어서 for에서 돌릴 수 있다