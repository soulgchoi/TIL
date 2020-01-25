# 190711 startcamp day04

## 01. HTML과 포트폴리오

F12 눌러서 고쳐보고 코드 수정하는게 좋음

github에서 README.md > 자동으로 처음에 다 보여줌

username.github.io 쫌 특별한 리포

- 주소 치면 다 볼 수 있음
- 가장 쉽게 웹을 남에게 보여줄 수 있는 방법

- username.github.io = username.github.io/index.html
  - 왜 가능?; https의 특징 - index.html 이기 때문에 나오는것 다른건 안됨

- 정확하게 어디에 어디에 쳐야 나옴는 웹 스테틱웹 <-> 다이내믹웹

url = 어디에 있는가

[file:///C:/Users/student/](file:///C:/Users/student/) 주소창에 쳐서 볼 수 있음



## 02. Flask

### 2-1. url 입력

------

#### d-day 계산하기

```python
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    
    return f'SSAFY 2기 1학기 종료일까지 {left.days} 일 남았습니다.'

if __name__ == '__main__':
    app.run(debug=True)
```



flask 를 쓰기 위해서는

반드시!!!!!

`from flask import Flask, render_template` + flask 폴더 안에 templates 폴더 만들고 html 생성



##### html로 만들기

``````python
@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)
# 변수를 보내줘야함!
# py 에서 모든 연산을 끝내고 html에 보내줘야함
``````

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>D-day</title>
</head>
<body>
    <h1>SSAFY 1학기 종료 까지</h1>
    <h2>{{left_days}}일 남았습니다.</h2> <!--app.py에서 받은 변수 가져오는 flask 문법-->
</body>
</html>
```

------

#### 영화 top5

`{{ }}` ; 사용자에게 보여줄 때

`{% %}` ; 로직

``````python
@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 : 파 프롬 홈',
        '알라딘',
        '토이스토리 4',
        '기방도령',
        '라이온킹'
    ]
    return render_template('boxoffice.html', movies=top_5)
``````

``````html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Box office</title>
</head>
<body>
    <h1>box office</h1>
    <ol>
        {% for movie in movies %}
            <li>{{ movie }}</li>
        {% endfor %}  <!--끝내야함-->
    </ol>
</body>
</html>
``````

#### 링크 만들기

index.html 만들기

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/dday">dday</a></li>
            <li><a href="/boxoffice">boxoffice</a></li>
            <li><a href="#">ㅠㅠ</a></li>  <!--#; 모르겠다고-->
        </ul>
    </nav>
</body>
</html>
``````

------

### 2-2. send&receive

------

#### app.py & send.html

``````python
@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    return render_template('receive.html')
``````

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Send massage</title>
</head>
<body>
    <h1>Send message here</h1>
    <form>
        <input type="text" value="hi" placeholder="message here" autofocus>  <!--input은 클로징 태그 X--> 
        <input type="submit" value="보내기"> <!--value는 미리 값이 입력되는 것-->
    </form>
</body>
</html>
``````

input 값을 '보내기'누르면 app.py에 도달하도록 만들어야 함.

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Send massage</title>
</head>
<body>
    <h1>Send message here</h1>
    <form action="/receive">  <!--도달할 주소-->
        <input type="text" placeholder="message here" autofocus>
        <input type="submit" value="보내기">
    </form>
</body>
</html>
``````

일 시키는 트리거 = 주소!!!!!!

``````python
from flask import Flask, render_template, request  # request 추가
import datetime


@app.route('/send')
def send():
    print(request.headers)
    return render_template('send.html')


@app.route('/receive')
def receive():
    print(request)  # requests와 request 구분해서 사용
    return render_template('receive.html')
``````

``````python
@app.route('/receive')
def receive():
    print(request.args)  # request 다 보여주세요
    return render_template('receive.html')
``````

딕셔너리(키:밸류)로 돌려받음

ImmutableMultiDict([]); key 없이 value 만 보내서 나옴

``````html
<input type="text" name="msg">
``````

ImmutableMultiDict([('msg', 'This is my message')])

`name`을 만들어서 value 돌려받음

``````python
@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive')
def receive():
    data = request.args.get('msg')  # 데이터 담는 방법
    return render_template('receive.html', data=data)
	# 담은 데이터를 receive로 보낼거임
``````

#### receive.html

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>수신함</title>
</head>
<body>
    <h1>{{ data }}</h1>  <!--data 받아다가 출력-->
</body>
</html>
``````

보내기 누르면 새로운 창에서 받기 가능

------

참고; 

id 는 문서 하나에 같은거 하나

id가 필요한 이유? select 하기 위해서; 검색할 때 한방에 잡을 수 있음

class 주는 이유? 더 상세하게 설정할 수 있어서 그래도 p:nth child 이렇게 나옴

id는 선택자 selector

------

#### 데이터  더 받아보기

#### stock 가져오기

``````python
@app.route('/receive')
def receive():
    token = ''
    stock = Stock('TSLA', token=token).get_quote()

    data = request.args.get('msg') 
    return render_template('receive.html', stock=stock)
``````

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>수신함</title>
</head>
<body>
    <h1>{{ stock }}</h1>
</body>
</html>
``````

넘어온걸 처리해서 처리한 데이터를 내보내는 것이 핵심

##### 내가 입력한 데이터로 receive 에 가져오기

**#1 data의 위치를 바꾼다**

``````python
@app.route('/receive')
def receive():
    data = request.args.get('msg')

    token = 'pk_ab6974e61cb545d9b1a92dafe8947a10'
    stock = Stock(data, token=token).get_quote()

    return render_template('receive.html', stock=stock)
``````

**#2 key, value만 가져오기**

``````python
@app.route('/receive')
def receive():
    data = request.args.get('msg')

    token = 'pk_ab6974e61cb545d9b1a92dafe8947a10'
    stock = Stock(data, token=token).get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']

    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=latest_price
    )
``````

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>수신함</title>
</head>
<body>
    <h1>{{ c_name }}</h1>
    <p>$ {{ l_price }}</p>
</body>
</html>
``````

------

추가 과제; 환율을 가져와서 아마존 가격을 환율 계산해서 원화로 출력하기

추가추가 과제; 환율정보 api 또는 패키지 가져와서 계산하기

------

#### 숫자 두 개 입력받아서 결과 볼 수 있게 만들어보기

**#1 직접 한 것**

app.py

``````python
# 숫자 두 개 받아서 결과를 result
@app.route('/add')
def add():
    # pass # add.html => imput 두 개
    return render_template('add.html')


@app.route('/result')
def result():
    num1 = request.args.get('1num')
    num2 = request.args.get('2num')
    num = int(num1)+int(num2)
    # # pass # result.html => imput 두 개 합산
    return render_template('result.html', num=num)
``````

add.html

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add</title>
</head>
<body>
    <h1>Add</h1>
        <p>숫자를 입력하세요.</p>
    <form action='/result'>
        <input type="number" name="1num"><p>+</p>
        <input type="number" name="2num">
        <input type="submit" value=" = ? ">
    </form>
</body>
</html>
``````

result.html

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>답</title>
</head>
<body>
    <h1>답은</h1>
    <h1>{{ num }}</h1>
</body>
</html>
``````

**#2 텍스트를 입력했을 때 오류를 해결하기**

`type="number"`는 근본적 해결책은 아님ㅠㅠ

숫자가 아니면 다시 입력하게 만드는 방법은?

------

#### art & select

``````python
from art import *

@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/artresult')
def artresult():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    artresult = text2art(input_text, font=font)
    return render_template('artresult.html', artresult=artresult)
``````

art.html

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Make art</title>
</head>
<body>
    <h1>Put some text</h1>
    <form action="/artresult">
        <input type="text" name="input_text">
        <select name="font">
            <option value="random">랜덤</option>
            <option value="block">블록</option>
            <option value="white_bubble">동그라미</option>
        </select>
        <input type="submit">
    </form>
</body>
</html>
``````

왜 `<select>`를 써야할까? > 확정적으로 선택지를 줘야하는 경우

artresult.html

``````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>답</title>
</head>
<body>
    <h1>Result</h1>
    <pre>
        {{ artresult }}
    </pre>
</body>
</html>
``````

------

내일은..챗봇 Quest

Flask는 일종의 trigger

건드려졌을때 '어떤 행동을 한다' > 우리가 작성해야 하는 코드

server=요청을 들어주는 역할

------

#### 내 input 을 숨기고 싶다!

##### method

send.html

``````html
<body>
    <h1>Send message here</h1>
    <form action="/receive" method="POST">  <!--POST>보내줘!주소창에 남지 않음 중요하게 처리되어야 할 때-->
        <input type="text" autofocus name="msg">
        <input type="submit" value="보내기">
    </form>
</body>
``````

html에서 method를 바꾸면

``````python
@app.route('/receive', methods=['POST'])  # 명령한 method를 인지시킴
def receive():
    data = request.form.get('msg')  # args를 form으로 바꾸기
``````

`request`요청 자체`.args`url에 쓰기`.get`가져와!

​								`.form`포장하기

`GET`; url에 입력값이 보임, 디폴트값

`POST`; 주소창에서 가림, 대신 공유 불가, 중요한 요청(로그인 등) 보낼 때