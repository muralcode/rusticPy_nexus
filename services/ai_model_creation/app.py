from flask import Flask, request, jsonify
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train_model():
    data = np.array(request.json.get('data'))
    target = np.array(request.json.get('target'))

    model = LogisticRegression()
    model.fit(data, target)

    predictions = model.predict(data)
    accuracy = accuracy_score(target, predictions)

    return jsonify({"accuracy": accuracy})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
