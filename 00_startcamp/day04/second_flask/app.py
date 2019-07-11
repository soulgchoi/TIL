import datetime

from art import *
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


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


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/artresult')
def artresult():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    artresult = text2art(input_text, font=font)
    return render_template('artresult.html', artresult=artresult)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive', methods=['POST'])
def receive():
    data = request.form.get('msg')

    token = 'pk_ab6974e61cb545d9b1a92dafe8947a10'
    stock = Stock(data, token=token).get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']

    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=latest_price
    )

if __name__ == '__main__':
    app.run(debug=True)
