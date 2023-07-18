from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') 
def hello_world():
    return 'hello world!'

@app.route('/products')
def products():
    return 'this is my products page'

if __name__=="__main__":
    app.run(debug=True)
