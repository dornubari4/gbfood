# inventory_service.py
from flask import Flask, jsonify

app = Flask(__name__)

inventory = {"Pizza": 20, "Burger": 15, "Salad": 30}

@app.route('/get_inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

if __name__ == '__main__':
    app.run(debug=True, port=5008)
