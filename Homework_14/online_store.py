from dataclasses import dataclass

from flask import Flask, abort, session, request, redirect
from flask_session import Session
from sqlite3 import connect

DATABASE_FILE = 'sqlite.db'

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@dataclass
class Product:
    id: int
    name: str
    description: str
    category: str


def load_products() -> list[Product]:
    with connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT id, name, description, category FROM product')
        return [Product(*values) for values in execution_result.fetchall()]


def get_product(product_id: int) -> Product:
    with connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, name, description, category '
                                              'FROM product '
                                              'WHERE id = ?', (product_id,))
        rows = execution_result.fetchall()
        if len(rows) != 1:
            raise ValueError(f'Expected 1 object with id {product_id}, got {len(rows)}')
        return Product(*rows[0])


@app.route('/')
@app.route('/products')
def products_view():
    products = load_products()
    products_html = '\n'.join(
        f'<li><a href="/product/{product.id}">{product.name}</li>'
        for product in products)

    return f'''
    <html>
        <head>
            <title>Online Store</title>
        </head>
        <body>
            <h1>All Products</h1>
            <ul>
                {products_html}
            </ul>
        </body>
    </html>
    '''


@app.route('/product/<int:product_id>')
def product_view(product_id: int):
    try:
        product = get_product(product_id)
    except ValueError as e:
        abort(404, e)
    return f'''
    <html>
        <head>
            <title>Online Store</title>
        </head>
        <body>
            <a href="/products">Main page</a>
            <h1>{product.name}</h1>
            <h3>{product.category}</h3>
            <p>{product.description}</p>
            <form method="post" action="/product/favorites">
                <input type="hidden" name="product_id" value="{product.id}"/>
                <input type="submit" value="Add to favorites"/>
            </form>
        </body>
    </html>
    '''


@app.route('/product/favorites', methods=['POST'])
def add_to_favorites():
    product_id = int(request.form['product_id'])
    product = get_product(product_id)
    name = product.name
    added_favorites = session.setdefault('added_favorites', set())
    if product.id in added_favorites:
        name += '&#9733;'
        added_favorites.remove(product.id)
    return redirect(f'/product/{product.id}')


if __name__ == '__main__':
    app.run(port=8081, debug=True)
