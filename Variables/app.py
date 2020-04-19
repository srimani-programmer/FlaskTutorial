from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    myVariable = "Hello!"
    return render_template('index.html', myVariable=myVariable)

@app.route('/bye')
def goodBye():
    myVariable = "Good Bye!"
    return render_template('index.html', myVariable=myVariable)


if __name__ == "__main__":
    app.run(debug=True)