from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')  # 길 설정
def index():  # 내보내기
    return render_template('/index.html')  # 무엇을? index.html을
    # Flask 자체가 파일을 templates 폴더에서 찾아오기 때문에 넣어야함


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


@app.route('/hello/<name>')
def hello(name):  # 위에서 <> 안에 들어간 것과 맞춰야함
    return f'hi, {name}'


@app.route('/pick_lunch/<int:count>')
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '깐풍기',
        '기스면'
    ]
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:num>')  # 입력한 숫자의 세제곱
def cube(num):
    return str(num ** 3)


if __name__ == "__main__":
    app.run(debug=True)
