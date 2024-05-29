# Task 2: Implementing a Simple RESTful API for Product Management using Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data (for demonstration)
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 20.99},
]

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get a specific product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'}), 404

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201

if __name__ == '__main__':
    app.run(debug=True)
