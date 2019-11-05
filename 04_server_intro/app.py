# Views 최고 중간 관리자
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # = domain 뒤에 아무 말이 없으면
def index():
    return render_template('index.html')


# static 에서는 불가능한 부분, 사용자 입력값을 받아 동적으로 처리
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number} 의 세제곱은 {number ** 3} 입니다.'


@app.route('/dictionary/<string:word>')
def my_dict(word):
    d = {'apple': '사과', 'peach': '복숭아'}
    # if word in d:
    #     return f'{word}은(는) {d[word]}!'
    # else:
    #     return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'

    result = d.get(word)

    return f'{word}은(는) {result}' if result else f'{word}은(는) 나만의 단어장에 없는 단어입니다!'

if __name__ == '__main__':
    app.run(debug=True)
