from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['POST'])
def fetch_data():
    data_source = request.json.get('source')
    if data_source == 'api':
        response = requests.get("https://api.example.com/data")
        data = response.json()
    else:
        # Placeholder data
        data = [1, 2, 3, 4, 5]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
