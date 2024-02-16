# user_service.py
from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "username": "john_doe", "email": "john@example.com"},
    {"id": 2, "username": "jane_smith", "email": "jane@example.com"},
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
