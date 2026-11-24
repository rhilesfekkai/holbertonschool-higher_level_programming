#!/usr/bin/python3
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read products from JSON."""
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Read products from CSV."""
    with open('products.csv', 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template(
            'product_display.html',
            error='Wrong source',
            products=[]
        )

    if source == 'json':
        product_list = read_json()
    else:
        product_list = read_csv()

    if product_id is not None:
        product_list = [
            product for product in product_list
            if str(product['id']) == product_id
        ]

        if not product_list:
            return render_template(
                'product_display.html',
                error='Product not found',
                products=[]
            )

    return render_template(
        'product_display.html',
        products=product_list,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
