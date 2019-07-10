# 190710 startcamp day03

어제 배운 것;

**<u>요청</u>**은 **<u>주소</u>**로 보내고 **<u>응답</u>**은 **<u>문서</u>**로 온다

우리가 배우는 명령어는 unix 계열

## 01. quiz.py

```python
name = input()  # 입력을 받는 함수, 액션을 취하지 않으면 끝나지 않는 함수
# 입력을 기다리고 입력하면 name에 저장한다 의 의미
print('hi, ' + name)
```

**= 는 오른쪽부터 읽고 왼쪽에 넣는다**

git bash 에서 $; 프롬프트, 쓰는 말을 받을 준비가 되었다는 의미

​							$가 뜨지 않는다는건 input 을 기다리며 계속 python을 있다는 것 > 이 터미널은 다른 일을 못해!! > ctrl + c 로 취소 가능

ctrl + d > exit

 ``````python
name = input('What is your name?: ')  # 질문 넣기 = 사용자 친화적으로
name = input('What\'s your name?: ')  # \'로 기호 넣기
print('hi, ' + name)
 ``````

UX/UI의 본질은 사용자에게 편리하도록 개선하는 것

------

### 문제 

``````python
words = input('입력 고고: ')

# words 의 첫 글자와 마지막 글자를 출력하라.
``````

``````python
numbers = [1, 2, 3, 4, 5]

# numbers의 첫 요소와 마지막 요소를 출력하라
``````

``````python
import random

length = random.choice(range(1, 100))
numbers= list(range(length))
# 처음과 마지막을 골라내는 코드

numbers[-1]  # 마지막은 무조건 -1 = numbers[length - 1]
``````

**<u>마지막은 무조건 -1</u>**

그러므로 첫 문제의 답;

``````python
words = input('입력 고고: ')

# words 의 첫 글자와 마지막 글자를 출력하라.
print(words[0], words[-1])
``````

------

### 박스 안에 든 것의 타입, 클래스가 뭐지?

``````python
words = input('입력 고고: ')
print(type(words))
``````

`print(words)`; words에 들어있는 게 뭐지?

`print(type(words))`; words에 들어있는 것의 타입이 뭐지?

문자열 = 일종의 list이기 때문에 0, -1 index 접근이 가능

``````python
words = input('입력 고고: ')

my_list = list(words)  # words를 리스트화(형변환), 여기서는 할 필요 없음
print(my_list)
print(my_list[0], my_list[-1])
``````

문자열은 list로 형변환 가능한 대표적 요소

------

### 형변환?

`````python
# n 을 입력받고, 1부터 n 까지 출력하라
n = input('자연수를 입력하세요: ')
`````

`input`값은 str 이기 때문에 숫자로 변환해야 한다.

``````python
n = input('자연수를 입력하세요: ')
n = int(n)  # str > list(str) / str > int(str)
``````

`int()`; 정수는 int로 변환 가능, 10진수에 한해 변환 가능

``````python
n = input('자연수를 입력하세요: ')
print(type(n))  # class 'str'
n = int(n)
print(type(n))  # class 'int'
``````

위아래의 class가 어떻게 다른지 비교

``````python
# n 을 입력받고, 1부터 n 까지 출력하라
n = input('자연수를 입력하세요: ')
n = int(n)

for i in range(n):  # 0 ~ n-1
    print(i + 1)
``````

print는 줄바꿈(\n)까지가 디폴트값이기 때문에, end = '' 붙여주면 줄바꿈 X

``````python
n = input('자연수를 입력하세요: ')
n = int(n)

for i in range(n):
    print(i + 1, end=' ')
``````

------

#### 코드 쪼개기/줄이기

``````python
string = input('숫자를 입력하세요: ')
number = int(string)
``````

``````python
number = int(input('숫자를 입력하세요: '))
``````

------

### 홀/짝 판별하기

``````python
number = int(input('숫자를 입력하세요: '))

# 짝수/홀수를 구분하자. 2 > 짝! 3 > 홀!

# 2로 나눴을때 나머지 0 일 때 짝! 1 일 때 홀!
if number % 2 == 0:  # 나눈 나머지를 구하는 연산자 %
    print('짝!')
else:
    print('홀!')
``````

​	들여쓰기 유의하기

​	파이썬에서 같다 '**==**'

​	if/elif/else 뒤에 **:** 빼먹지 말기

------

### fizz buzz

1 ~ number 까지 출력

그와중에 3 fizz / 5 buzz / 15 fizzbuzz

ex) 1 2 fizz 4 buzz ..

``````python
# 3배수 먼저 걸릴 때
for i in range(1, number + 1):  # range 설정 잘 하기
    if i % 3 == 0:
        if i % 5 == 0:
            print('fizzbuzz')
        else:
            print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
``````

``````python
# 15 부터 할 때
for i in range(1, number + 1):
if i % 15 == 0:
    print('fizzbuzz')
elif i % 5 == 0:
    print('buzz')
elif i % 3 == 0:
    print('fizz')
else:
    print(i)
``````

------

## 02. API

### pick lotto

로또 번호 고르기

------

### get lotto

#### 당첨 번호 가져오기

`requests`사용

``````python
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
print(response['bnusNo'])
``````

왜 안나올까?

``````python
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
print(type(response))
``````

위에서 딕셔너리처럼 결과가 나왔지만 사실 str 이었음

API 를 통해서 받아오는 정보도 거의 str

##### str > dict 변환하기

``````python
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
print(response)

data = json.loads(response)
print(type(data), data)
``````

##### 보너스번호 출력하기

``````python
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
print(response)

data = json.loads(response)
print(type(data), data)

print(data['bnusNo'])
``````

API를 이용하면 늘 같은 구조의 데이터를 가져올 수 있음

##### 당첨번호 출력하기

비효율적이지만 가능한 방법

```````python
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
data = json.loads(response)

real_numbers = (
    data['drwtNo1'],
    data['drwtNo2'],
    data['drwtNo3']
	)
print(real_numbers)
```````

※ f string

``````python
'나는 밥을 먹는다'
>>> import random
>>> meal = random.choice(['아침', '저심', '저녁'])
>>> string = '나는 {}을 먹는다'.format(meal)
>>> string = f'나는 {meal}을 먹는다.'
``````

**python에서 가능한 방법**

``````python
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
data = json.loads(response)

real_numbers = []
for key, value in data.items():  # .items()를 붙이면 key, value 같이
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)
``````

`.append`; 안에 쏙쏙 집어넣기(붙이기)

------

### check lotto

``````python
my = [1, 2, 3, 4, 5, 6]
real = [1, 2, 3, 4, 5, 7]
bonus = 6

# my 와 real 의 숫자가 모두(6개) 같으면 1등
# my 와 real 이 5개 같고 나머지 하나가 bonus 면 2등
# my 와 real 이 5개가 같으면 3등
# 4개가 같으면 4등
# 3개가 같으면 5등
# 나머지는 꽝
``````

------

## 03. app.py

### 내 프로그램을 서빙하자

``````python
import random

random.choice([1, 2, 3, 4, 5])

from random import choice  # random에서 choice라는 것을 찾겠다
choice([1, 2, 3, 4, 5])
``````

두 방법 차이

### Flask 이용하기

url 을 바꿔 웹에서 구동할 수 있음

컨텐츠를 입력, 전달하는 비즈니스 로직

``````python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'  # '/'뒤가 붙으면 return 일을 해라

if __name__ == "__main__":
    app.run(debug=True)
``````

``````python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():  # 변수 이름
    return 'Hello World!'

@app.route('/hi')
def hi():  # 변수 이름2
    return 'Hi'

if __name__ == "__main__":
    app.run(debug=True)
``````

``````python
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/hi')
def hi():
    return 'Hi'

@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)  # 비즈니스 로직


if __name__ == "__main__":
    app.run(debug=True)
``````

요청과 응답 사이의 로직

##### 사용자 입력 받기 #1

var routing

``````python
@app.route('/get_lotto/<int:num>')
# <int:num> 안을 비워두기 = variable routing 주소창 길 뚫어주기         # 대신 유연성이 생긴 길

@app.route('/hello/<name>')
def Hello(name):  # 위에서 <> 안에 들어간 것과 맞춰야함
    return f'hi, {name}'
``````

##### 사용자 입력 받기 #2

``````python
@app.route('/pick_luch/<count>')
def pick_lunch(count):
    return 1 + int(count)
``````

``````python
@app.route('/pick_luch/<int:count>')
def pick_lunch(count):
    return 1 + count
``````

int를 위에서 써도 ok

``````python
@app.route('/pick_luch/<int:count>')
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '깐풍기',
        '기스면'
    ]
    picks = random.sample(menus, count) # count 입력값만큼 고르기
    return str(picks)  # 리스트는 return 뒤에 올 수 없음
``````

##### 사용자 입력 받기 #3

``````python
@app.route('/cube/<int:num>')  # 입력한 숫자의 세제곱
def cube(num):
    result = num ** 3
    return str(result)
	
    return str(num ** 3)  # 이게 더 간단하다!
``````

------

### HTML 

##### html 문서작성법 개괄

``````html
<!DOCTYPE html> 
<html>
    <head>
        <!-- 정보 -->
        <meta charset="utf-8">
    </head>
    <body>
        <!-- 가시화된 정보 -->
        <h1>Today I Learned</h1>
        <h2>Learn Flask</h2>
        <ol>
            <!-- 순서가 있는 리스트 -->
            <li>pip install flask</li>
            <li>touch app.py</li>
            <li>python app.py</li>
        </ol>
        <h2>Learn HTML</h2>
        <ul>
            <!-- 순서가 없는 리스트 -->
            <li>doctype html</li>
            <li>head, body</li>
            <li>h1, h2, ol, ul, li</li>
        </ul>
    </body>
</html>
``````

- 내용은 body에 쓴다

- 태그가 있고, 태그 안에 쓴다

- html은 " "로 쓴다 (' ' 로도 나오긴 하지만 그래도...)

------

문서는 html로 만들고, 문서 서빙하는 코드를 만들자

`from <> improt <>, <>`; 일종의 종량제 봉투, 필요한 것만 꺼내쓰기

``````python
from flask import Flask, render_template  # Flask 함수 가져오기
import random

app = Flask(__name__)


@app.route('/')  # 길 설정
def index():  # 내보내기
    return render_template('/index.html')  # 무엇을? index.html을
    # Flask 자체가 파일을 templates 폴더에서 찾아오기 때문에 넣어야함


if __name__ == "__main__":
    app.run(debug=True)
``````

------

## 04. stock.py

제공하는 패키지를 가져다 쓰기