from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Load data
def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

products_data = load_data('products.json')
carts_data = load_data('carts.json')
users_data = load_data('users.json')

# Helper functions
def get_product_by_id(id):
    for product in products_data['products']:
        if product['id'] == id:
            return product
    return None

def get_cart_by_id(id):
    for cart in carts_data['carts']:
        if cart['id'] == id:
            return cart
    return None

def get_user_by_id(id):
    for user in users_data['users']:
        if user['id'] == id:
            return user
    return None

# API Endpoints

@app.route('/api/products', methods=['GET'])
def api_products():
    return jsonify(products_data)

@app.route('/api/products/<int:id>', methods=['GET'])
def api_product_detail(id):
    product = get_product_by_id(id)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/api/products/search', methods=['GET'])
def api_product_search():
    query = request.args.get('q', '').lower()
    results = []
    for product in products_data['products']:
        if query in product['title'].lower() or \
           query in product['description'].lower() or \
           query in product['category'].lower():
            results.append(product)
    return jsonify({'products': results, 'total': len(results), 'skip': 0, 'limit': len(results)})

@app.route('/api/carts', methods=['GET'])
def api_carts():
    return jsonify(carts_data)

@app.route('/api/carts/<int:id>', methods=['GET'])
def api_cart_detail(id):
    cart = get_cart_by_id(id)
    if cart:
        return jsonify(cart)
    return jsonify({'error': 'Cart not found'}), 404

@app.route('/api/users', methods=['GET'])
def api_users():
    return jsonify(users_data)

@app.route('/api/users/<int:id>', methods=['GET'])
def api_user_detail(id):
    user = get_user_by_id(id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# UI Routes

@app.route('/')
def index():
    return redirect(url_for('products_list'))

@app.route('/products')
def products_list():
    return render_template('products.html', products=products_data['products'])

@app.route('/products/<int:id>')
def product_detail(id):
    product = get_product_by_id(id)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

@app.route('/carts')
def carts_list():
    return render_template('carts.html', carts=carts_data['carts'])

@app.route('/carts/<int:id>')
def cart_detail(id):
    cart = get_cart_by_id(id)
    if cart:
        # Enrich cart products with details if needed, but basic info is in cart
        return render_template('cart_detail.html', cart=cart)
    return "Cart not found", 404

@app.route('/users')
def users_list():
    return render_template('users.html', users=users_data['users'])

@app.route('/users/<int:id>')
def user_detail(id):
    user = get_user_by_id(id)
    if user:
        return render_template('user_detail.html', user=user)
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
