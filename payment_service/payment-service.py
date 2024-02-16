# payment_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json

    # Perform payment processing logic here
    # For simplicity, let's assume successful payment
    return jsonify({"message": "Payment processed successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5004)
