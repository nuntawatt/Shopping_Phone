from flask import Flask, render_template, jsonify, request, send_from_directory
import os
import json

app = Flask(__name__)

# Sample products data
products = [
    {
        "id": 1,
        "name": "iPhone 16 Pro Max",
        "category": "iphone",
        "price": 49900,
        "image": "/static/images/iPhone16pmax.jpeg",
        "description": "iPhone 16 Pro Max 256GB สีไทเทเนียมธรรมชาติ"
    },
    {
        "id": 2,
        "name": "iPhone 16 Pro",
        "category": "iphone",
        "price": 43900,
        "image": "/static/images/iPhone16Pro.jpg",
        "description": "iPhone 16 Pro 128GB สีไทเทเนียมขาว"
    },
    {
        "id": 3,
        "name": "iPhone 16",
        "category": "iphone",
        "price": 29900,
        "image": "/static/images/iphone16.jpeg",
        "description": "iPhone 16 128GB สีพิงค์"
    },
    {
        "id": 4,
        "name": "Samsung Galaxy S24 Ultra",
        "category": "samsung",
        "price": 44900,
        "image": "/static/images/S24_Ultra.jpeg",
        "description": "Samsung Galaxy S24 Ultra 256GB สีไทเทเนียมเทา"
    },
    {
        "id": 5,
        "name": "AirPods Pro (รุ่นที่ 2)",
        "category": "accessories",
        "price": 8990,
        "image": "/static/images/AirPods_pro.jpeg",
        "description": "AirPods Pro รุ่นใหม่ พร้อม Active Noise Cancellation"
    },
    {
        "id": 6,
        "name": "MagSafe Charger",
        "category": "accessories",
        "price": 1590,
        "image": "/static/images/MagSafe_Charger.jpeg",
        "description": "MagSafe Charger สำหรับ iPhone"
    },
    {
        "id": 7,
        "name": "iPhone 15 Pro Max",
        "category": "iphone",
        "price": 44900,
        "image": "/static/images/iPhone15pmax.jpeg",
        "description": "iPhone 15 Pro Max 256GB สีไทเทเนียมฟ้า"
    },
    {
        "id": 8,
        "name": "Samsung Galaxy S24+",
        "category": "samsung",
        "price": 32900,
        "image": "/static/images/S24.jpg",
        "description": "Samsung Galaxy S24+ 256GB สีม่วง"
    }
]

# Shopping cart (in real app, this would be in database or session)
cart = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    category = request.args.get('category')
    if category and category != 'all':
        filtered_products = [p for p in products if p['category'] == category]
        return jsonify(filtered_products)
    return jsonify(products)

@app.route('/api/products/<int:product_id>')
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify(cart)

@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    # Find product
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    # Check if item already in cart
    cart_item = next((item for item in cart if item['id'] == product_id), None)
    if cart_item:
        cart_item['quantity'] += quantity
    else:
        cart_item = {**product, 'quantity': quantity}
        cart.append(cart_item)
    
    return jsonify({'message': 'Item added to cart', 'cart': cart})

@app.route('/api/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    global cart
    cart = [item for item in cart if item['id'] != product_id]
    return jsonify({'message': 'Item removed from cart', 'cart': cart})

@app.route('/api/cart/<int:product_id>', methods=['PUT'])
def update_cart_item(product_id):
    global cart
    data = request.json
    quantity = data.get('quantity')
    
    cart_item = next((item for item in cart if item['id'] == product_id), None)
    if cart_item:
        if quantity <= 0:
            cart = [item for item in cart if item['id'] != product_id]
        else:
            cart_item['quantity'] = quantity
        return jsonify({'message': 'Cart updated', 'cart': cart})
    
    return jsonify({'error': 'Item not found in cart'}), 404

@app.route('/api/search')
def search_products():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify(products)
    
    filtered_products = [
        p for p in products 
        if query in p['name'].lower() or query in p['description'].lower()
    ]
    return jsonify(filtered_products)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    # In real app, you would save this to database or send email
    print(f"Contact form submission:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    
    return jsonify({'message': 'ขอบคุณสำหรับข้อความของคุณ! เราจะติดต่อกลับในเร็วๆ นี้'})

@app.route('/static/images/<filename>')
def serve_image(filename):
    # Serve placeholder images or real images
    return send_from_directory('static/images', filename)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)