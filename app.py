from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to ANN Traders!'


@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

    