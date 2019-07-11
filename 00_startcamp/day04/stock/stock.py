from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/')
def index():
    return 'stock'


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive')
def receive():
    data = request.args.get('msg')

    token = 'pk_ab6974e61cb545d9b1a92dafe8947a10'
    stock = Stock(data, token=token).get_quote()


if __name__ == '__main__':
    app.run(debug=True)
