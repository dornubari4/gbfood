# notification_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json

    # Perform notification sending logic here
    # For simplicity, let's assume notification sent
    return jsonify({"message": "Notification sent successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=5005)
