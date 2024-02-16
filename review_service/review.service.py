# review_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

reviews = []

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.json

    # Perform review submission logic here
    reviews.append(data)
    return jsonify({"message": "Review submitted successfully"})

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True, port=5007)
