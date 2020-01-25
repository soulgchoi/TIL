from flask import Flask, render_template, request
from iexfinance.stocks import Stock
from decouple import config
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

    token = config('TOKEN')
    stock = Stock(data, token=token).get_quote()


if __name__ == '__main__':
    app.run(debug=True)
