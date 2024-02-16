# delivery_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/update_delivery_status', methods=['PUT'])
def update_delivery_status():
    data = request.json

    # Perform delivery status update logic here
    # For simplicity, let's assume status updated
    return jsonify({"message": "Delivery status updated successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5006)
