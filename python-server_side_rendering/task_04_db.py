#!/usr/bin/python3
import csv
import json
import sqlite3
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


def read_sql():
    """Read products from SQLite database."""
    connection = sqlite3.connect('products.db')
    connection.row_factory = sqlite3.Row

    try:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT id, name, category, price FROM Products'
        )
        products = [dict(row) for row in cursor.fetchall()]
        return products
    finally:
        connection.close()


@app.route('/products')
def products():
    """Display products from JSON, CSV or SQLite."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    try:
        if source == 'json':
            product_list = read_json()
        elif source == 'csv':
            product_list = read_csv()
        else:
            product_list = read_sql()

        if product_id is not None:
            product_list = [
                product for product in product_list
                if str(product['id']) == product_id
            ]

            if not product_list:
                return render_template(
                    'product_display.html',
                    products=[],
                    error='Product not found'
                )

        return render_template(
            'product_display.html',
            products=product_list,
            error=None
        )

    except (sqlite3.Error, OSError, json.JSONDecodeError, csv.Error):
        return render_template(
            'product_display.html',
            products=[],
            error='Database error'
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
