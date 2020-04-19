from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/<string:name>')
def greetings(name):
    return "Hello {}".format(name)


if __name__ == "__main__":
    app.run(debug=True)