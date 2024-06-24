from flask import Flask, request, jsonify
from rust_bindings import wrapper

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json.get('data')
    transformed_data = wrapper.transform(data)
    aggregated_data = wrapper.aggregate(transformed_data)
    analysis_result = wrapper.analyze(transformed_data)
    return jsonify({
        "transformed": transformed_data,
        "aggregated": aggregated_data,
        "analysis": analysis_result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
