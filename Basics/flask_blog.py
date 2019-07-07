from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
    return "<h1>Welcome to my Flask Blogging application with Jinja2</h1>"


@app.route('/about')
def about():
    return "My name is Shreyash"

if __name__ == '__main__':
    app.run(debug=True)
