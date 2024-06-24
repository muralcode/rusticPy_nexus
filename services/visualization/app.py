from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Example: render a dashboard with processed data
    return render_template('dashboard.html', data=[1, 2, 3, 4, 5])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
