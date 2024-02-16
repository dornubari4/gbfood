# menu_service.py
from flask import Flask, jsonify

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Pizza", "price": 12.99},
    {"id": 2, "name": "Burger", "price": 8.99},
    {"id": 3, "name": "Salad", "price": 5.99},
]

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
