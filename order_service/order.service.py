# order_service.py
from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/order', methods=['POST'])
def place_order():
    data = request.json

    if "item_id" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid request"}), 400

    item_id = data["item_id"]
    quantity = data["quantity"]

    # Here, you might want to call the Menu Service to get item details based on item_id.
    # For simplicity, we assume that the menu item exists.

    total_price = 0  # Calculate the total price based on the menu item's price.

    order = {
        "item_id": item_id,
        "quantity": quantity,
        "total_price": total_price
    }

    orders.append(order)

    return jsonify({"message": "Order placed successfully", "order": order})

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
