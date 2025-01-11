from flask import Flask, render_template, request
from datetime import date
from pip._vendor import requests

app = Flask(__name__)
product_list = [
    {
        'id': '1',
        'title': 'Sprite',
        'price': '0.5',
        'description': "Some quick example text to build on the card title and make up the bulk of the card's content.",
        'image': 'sprite.jpg'
    },
    {
        'id': '2',
        'title': 'Drink',
        'price': '0.5',
        'description': "Some quick example text to build on the card title and make up the bulk of the card's content.",
        'image': 'sprite.jpg'
    }
]
current_product = []
bot_token = "7122074711:AAFcEsKdu_q4-ZpOAccuQRRbk7quHvJAbo"
chat_id = "@theara_st34"
bot_username = "t.me/theatre_st34"


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.get('/Product')
def product():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    product = response.json()
    product_list = product
    return render_template('Product.html', product_list=product_list)


@app.get('/Product_detail')
def product_detail():
    product_id = request.args.get('id')
    url = "https://fakestoreapi.com/products/{}".format(product_id)
    response = requests.get(url)
    current_product = []
    current_product = response.json()
    return render_template('Product_detail.html', current_product=current_product)


@app.get('/checkout')
def checkout():
    product_id = request.args.get('id')
    url = "https://fakestoreapi.com/products/{}".format(product_id)
    response = requests.get(url)

    current_product = response.json()
    return render_template('Checkout.html', current_product=current_product)


def open(param, param1):
    pass


@app.route('/ordered')
def ordered():
    product_id = request.args.get('id')
    url = "https://fakestoreapi.com/products/{}".format(product_id)
    response = requests.get(url)
    current_product = response.json()

    html = (
        "<strong>🧾 {inv_no}</strong>\n"
        "<code>📆 {date}</code>\n"
        "<code>============================</code>\n"
        "<code>ID\t\tQuality\t\tPrice\t\tAmount</code>\n"
    ).format(
        inv_no='INV0001',
        date=date.today(),
    )
    html += (
        f"<code>{current_product['id']}\t\t\t\t\t\t1\t\t\t\t\t{current_product['price']}\t\t\t\t{current_product['price']}</code>\n "
    )
    html += (
        "<code>-----------------------------</code>\n"
        "<code>Total: {total}$</code>\n"
        "<code>Grand Total: {grand_total}$</code>\n"
        # "<code>Discount: {discount}%</code>\n"
        # "<code>ប្រាក់ទទួល: {received_amount}$</code>\n"
        # "<code>💸ប្រាក់អាប់: {deposit_amount}$</code>\n"
    ).format(
        total=f'{current_product["price"]}',
        grand_total=f'{current_product["price"]}',
        # discount=f'{discount}',
        # received_amount=f'{received_amount}',
        # deposit_amount=f'{deposit_amount}'
    )

    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    files = {'photo': open(f'E:\image Card/images (2).jpg', 'rb')}
    data = {'chat_id': chat_id, 'caption': html, 'parse_mode': 'HTML'}
    response = requests.get(url, files=files, data=data)
    return render_template("ordered.html", current_product=current_product)


if __name__ == '__main__':
    app.run()


@app.get('/About')
def about():
    return render_template("About.html")


@app.get('/contact')
def contact():
    return render_template("contact.html")


@app.get('/jinja')
def jinja():
    now = date.now()
    return render_template("jinja.html", now=now)
